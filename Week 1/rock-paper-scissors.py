from random import choice


opt = ["Rock", "Paper", "Scissors"] # Game options to choose


print("This is a Rock, Paper, Scissors game. Below are the rules:\n1. Rock beats Scissors\n2. Scissors beats Paper\n3. Paper beats Rock" \
"\n4. If both parties outcome is the same it becomes a tie")


ready = input("Are you ready to play? (Yes/No) ").strip().lower() # gets user input

if ready != "yes":
    print("Maybe next time")
else:
    user_input = input(f"Select any of the following {opt} ").strip().capitalize()

    # Condition to check if the user option is in the list 'opt'
    if user_input not in opt:
        print(f"Incorrect input, pls select any of the following {opt}")
    else:
        comp_opt = choice(opt)
        print(f"Computer Choice: {comp_opt}")

        # Main game conditions
        if user_input == comp_opt:
            print("It's a Tie")
        elif (user_input == "Rock" and comp_opt == "Scissors") or \
            (user_input == "Scissors" and comp_opt == "Paper") or \
                (user_input == "Paper" and comp_opt == "Rock"):
            print("You Win")
        else:
            print("You Lose")
