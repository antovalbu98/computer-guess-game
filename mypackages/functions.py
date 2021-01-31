def linear_congruence(x0):
    """
    Function that uses the linear congruences method to generate either a 0 or a 1
    randomly. It returns either a 0 or a 1 and a new random number.
    """
    a = 22695477
    b = 1
    m = 2**32
    xi_plus_1 = (a*x0+b)%m
    if xi_plus_1 <= m/2:
        compu_choice = 0
    else:
        compu_choice = 1
    return compu_choice, xi_plus_1


def algoritmo(previous_choice, throw00, throw10, throw01, throw11, seed):
    """
    Function that determines the choice of the computer between 0 and 1 depending
    on the previous actions of the human player.
    """
    if previous_choice == 0:
        if throw10 > throw00:
            computer_choice = 1
        elif throw10 < throw00:
            computer_choice = 0
        else:
            computer_choice = linear_congruence(seed)[0]
            seed = linear_congruence(seed)[1]

    elif previous_choice == 1:
        if throw11 > throw01:
            computer_choice = 1
        elif throw11 < throw01:
            computer_choice = 0
        else:
            computer_choice = linear_congruence(seed)[0]
            seed = linear_congruence(seed)[1]
    else:
        computer_choice = linear_congruence(seed)[0]
        seed = linear_congruence(seed)[1]

    return computer_choice, seed


def intro_numero(ronda):
    intro = input(f"Player move {ronda + 1}: ")
    while intro not in ["1", "0"]:
        print("Invalid input. Intoduce a 0 or a 1")
        intro = input(f"Player move {ronda + 1}: ")
    numero = int(intro)
    return numero


def intro_diff():
    intro = input("Please choose the type of game (1: Easy, 2: Difficult): ")
    while intro not in ["1", "2"]:
        print("Invalid input. Intoduce a 1 for Easy gameplay or a 2 for Difficult gameplay.")
        intro = input("Please choose the type of game (1: Easy, 2: Difficult): ")
    diff = int(intro)
    return diff


def intro_nmoves():
    intro = input("Enter number of moves: ")
    try:
        nmoves = int(intro)
        return nmoves
    except:
        print("Invalid input. Introduce an integer.")
        intro_nmoves()


def intro_seed():
    intro = input("Enter a seed: ")
    try:
        seed = int(intro)
        if seed < 1 or seed > 2 ** 31:
            print("Invalid input. Introduce an integer between 1 and 2^31.")
            intro_diff()
        return seed
    except:
        print("Invalid input. Introduce an integer between 1 and 2^31.")
        intro_diff()


def intro_new_game():
    intro = input("Do you want to start a new game? Yes (Y) No (N): ")

    while intro not in ["Y", "N", "y", "n"]:
        print("Invalid input. Intoduce Y if you want to start a new game or N if you want to exit")
        intro = input("Do you want to start a new game? Yes (Y) No (N): ")
    new = intro.upper()
    return new
