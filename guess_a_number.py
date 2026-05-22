import random

GREEN = "\033[32m"
RED = "\033[31m"
BLUE = "\033[34m"
RESET = "\033[0m"

computer_number = random.randint(1, 100)
while True:
    player_input = input("Guess the number (1-100:) ")
    if not player_input.isdigit():
        print("Invalid input. Try again...")
        continue
    player_number = int(player_input)

    if player_number == computer_number:
        print(f"{GREEN}You guess it!{RESET}")
        break
    elif player_number > computer_number:
        print(f"{BLUE}Too High!{RESET}")
    else:
        print(f"{RED}Too Low!{RESET}")
