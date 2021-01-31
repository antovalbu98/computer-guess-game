from time import sleep
from mypackages.functions import *

t00 = 0
t10 = 0
t01 = 0
t11 = 0
CWINS = 0
PWINS = 0
prev_choice = None
new_game = None

# GAME is played inside while loop as long as the user rejects (new_game == N) playing a new game
# after the current game ends

while new_game != "N":
    print("Welcome to Human Behavior Prediction by Antonio Valbuena")

    # GAME CONDITIONS: number of moves, difficulty and seed for random play
    # in an if else block because the seed is only defined in the first game, then (new_game == "Y"), game takes
    # the last seed and doesn't ask the user for a new one at the beginning of the second game and further

    if new_game != "Y":
        print("First, you have to introduce a seed so the computer can generate random numbers when it is pertinent.")
        seed = intro_seed()
        print("Now, introduce the number of rounds you would like the game to last.")
        nmoves = intro_nmoves()
        print("Finally, choose the difficulty.")
        dificultad = intro_diff()
    else:
        print(f"As you have already introduced a seed, we won't ask you for a new one: Your last seed was {seed}.")
        print("Introduce the number of rounds you would like this new game to last.")
        nmoves = intro_nmoves()
        print("Finally, choose the difficulty.")
        dificultad = intro_diff()

    # GAME DIFFICULTY: depending on wheather (dificultad == 1 or == 2), the game runs

    if dificultad == 1:
        print(f"You have chosen the EASY difficulty. The game will have {nmoves} rounds... Let's start!")
        # EASY GAME, each iteration is a round
        for i in range(nmoves):
            print("-" * 30, "\n")
            print(f"ROUND {i + 1}")
            print(f"Current seed is: {seed}")
            print()
            # computer "chooses" number between 0 and 1 acc to linear congruence method
            computer_choice = linear_congruence(seed)[0]
            # seed for linear congruence method is updated with xi+1 seed
            seed = linear_congruence(seed)[1]
            # user chooses number between 0 and 1
            player_choice = intro_numero(i)
            sleep(1)
            print(f"Computer move {i + 1}: {computer_choice}")
            sleep(1)
            # POINTS ASSIGNMENT: Computer earns a point if it "guesses" the player's move,
            # if it doesn't, the player earns a point
            if player_choice == computer_choice:
                print("The computer gueesed your move and wins this round!")
                CWINS += 1
            else:
                print("The computer couldn't guess your move, you win this round!")
                PWINS += 1
            sleep(1)
            print("PLAYER WINS:  ", PWINS * "*")
            print("COMPUTER WINS:", CWINS * "*")
            sleep(1)

    elif dificultad == 2:
        print(f"You have chosen the DIFFICULT difficulty. The game will have {nmoves} rounds... Let's start!")
        # DIFFICULT GAME, each iteration is a round
        for i in range(nmoves):
            print("-" * 30, "\n")
            print(f"ROUND {i + 1}")
            print(f"Current seed is: {seed}")
            print()
            # computer chooses number between 0 and 1 acc to ML algorithm
            computer_choice = algoritmo(prev_choice, t00, t10, t01, t11, seed)[0]
            seed = algoritmo(prev_choice, t00, t10, t01, t11, seed)[1]
            # user chooses number between 0 and 1
            player_choice = intro_numero(i)
            sleep(1)
            print(f"Computer move {i + 1}: {computer_choice} ")
            sleep(1)
            # POINTS ASSIGNMENT: Computer earns a point if it "guesses" the player's move,
            # if it doesn't, the player earns a point
            if player_choice == computer_choice:
                print("The computer gueesed your move and wins this round!")
                CWINS += 1
            else:
                print("The computer couldn't guess your move, you win this round!")
                PWINS += 1
            sleep(2)
            print("PLAYER WINS:  ", PWINS * "*")
            print("COMPUTER WINS:", CWINS * "*")
            sleep(1)

            # Update of algorithm's 4 conditional inputs

            if (player_choice == 0) and (prev_choice == 0):
                t00 += 1

            elif (player_choice == 1) and (prev_choice == 0):
                t10 += 1

            elif (player_choice == 0) and (prev_choice == 1):
                t01 += 1

            elif (player_choice == 1) and (prev_choice == 1):
                t11 += 1
            else:
                pass

            # update of choice: as round is over, the choice made in this round becomes the previous choice for
            # next round
            prev_choice = player_choice

    print(f"The {nmoves} rounds have been played and the game has concluded")
    sleep(1)

    # once we exit either of the for loops where game takes place, we are out of rounds and game is done
    # check who won in the end (or if there was a draw) and inform the player

    if CWINS > PWINS:
        print("\n", "_" * 30, "\n")
        print("Oh no! The computer wins!")
        print("PLAYER WINS:  ", PWINS * "*")
        print("COMPUTER WINS:", CWINS * "*")

    elif CWINS < PWINS:
        print("\n", "_" * 30, "\n")
        print("Congratulations, you win")
        print("PLAYER WINS:  ", PWINS * "*")
        print("COMPUTER WINS:", CWINS * "*")

    else:
        print("\n", "_" * 30, "\n")
        print("It's a draw")
        print("PLAYER WINS:  ", PWINS * "*")
        print("COMPUTER WINS:", CWINS * "*")

    # As the game is done, we reset the count of the rounds won by each player, in case the player wants to
    # play again

    CWINS = 0
    PWINS = 0
    sleep(1)
    new_game_proxy = intro_new_game()
    sleep(1)
    if new_game_proxy == "N":
        print("Shame to see you leave :(")
        new_game = new_game_proxy
    else:
        new_game = new_game_proxy
        print("Great! Let's play another game!")
        sleep(1)