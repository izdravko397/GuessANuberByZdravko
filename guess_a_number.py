import random

computer_number = random.randint(1 , 100)

while True:
    player_input_number = input("Guess the number (1-100): ")

    if not player_input_number.isdigit():
        print("Invalid number. Try again...")
        continue

    player_number = int(player_input_number)

    if player_number == computer_number:
        print("You guess it!")
        break
    elif player_number > computer_number:
        print("Too High!")
    else:
        print("Too Low")