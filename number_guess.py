import sys, random

def pick_number():
    return random.randint(1, 20)

# Initialize
player_name = input("Hello! What's your name? ")
print(f"Hi {player_name}!")
print("I'm going to pick a number between 1 and 20. \n" \
"Try to guess the number. You'll have up to 6 tries. \n" \
"If you guess within 6 tries, you'll win. If you don't guess within 6 tries, I'll win. \n" 
"Let's get started.")
try_count = 0
number_to_guess = pick_number()
game_on = True

## Play
print(f"The number to guess is {number_to_guess}\n")

while game_on:
    for tries in range(0,6):
        guess = int(input("I'm thinking of a number between 1 and 20. Take a guess. \n"))
        if guess > number_to_guess:
            try_count += 1
            print(f"Try number {try_count}. Too high! \n > ")
        elif guess < number_to_guess:
            try_count += 1
            print(f"Try number {try_count}. Too low! \n > ")
        elif guess == number_to_guess:
            try_count += 1
            print(f"That's it! The number is {number_to_guess}. You got it in {try_count} tries.")
            break
    game_on = False
    if try_count >= 6:
        print(f"Sorry! The number I was thinking of was {number_to_guess}.")
