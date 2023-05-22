import random
range_guess_number = 100
tries = 10
levels = 1

print("Hello let's play Guess a Number game!")
print("When guess the number in range of tries you win the round and your level upping!")
print("When your level up, your tries to guess are lowing and your range to guess are upping!")

while True:
    computer_number = random.randint(1, range_guess_number)
    hint_lower_limit = computer_number - random.randint(1, 10)
    hint_upper_limit = computer_number + random.randint(1, 10)

    play_again_flag = False
    print(f"Les's play on level {levels}")
    print(f"You have {tries} tries to guess it...")

    for _try in range(1, tries + 1):
        if _try == tries:
            while True:
                inp = input("You are on last try, do you want a hint? Enter [yes] or [no]")
                if inp.lower() == "yes":
                    print(f"The correct number is in range ({hint_lower_limit} - {hint_upper_limit})")
                    break
                elif inp.lower() == "no":
                    break
                else:
                    print("Invalid input. Try again...")
                    continue

        player_input_number = input(f"Guess the number (1-{range_guess_number}): ")

        if not player_input_number.isdigit():
            print("Invalid number. Try again...")
            continue

        player_number = int(player_input_number)

        if player_number == computer_number:
            print(f"You guess it in {_try} tries! Let's level up...")
            if levels == 10:
                raise SystemExit("You WIN the game!!!")
            break
        elif player_number > computer_number:
            print("Too High!")
        else:
            print("Too Low")
    else:
        play_again = ""
        print("You lose!")
        while True:
            play_again = input("If you want try again in same level enter [yes] or enter [no] for exit ot game...")

            if play_again.lower() == "yes":
                play_again_flag = True
                break
            elif play_again.lower() == "no":
                raise SystemExit("Thanks for playing!")
            else:
                print("Invalid input. Please try again...")
                continue

    if play_again_flag:
        continue

    levels += 1
    tries -= 1
    range_guess_number += 100
