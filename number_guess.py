import sys, random

def pick_number():
    return random.randint(1, 20)

# Initialize
player_name = input("Hello! What's your name? ")
print(f"Hi {player_name}!")
print("This game is pretty simple. I'm going to pick a number between 1 and 20." \
"Your job is to guess the number. You have up to 6 tries." \
"If you guess within 6 tries, you win. If you don't get it within 6 tries, I win." 
"Let's get started.")
try_count = 0
number_to_guess = pick_number()

## Play
print(f"The number to guess is {number_to_guess}")
while True:
    try:
        guess = int(input("I'm thinking of a number between 1 and 20. Take a guess. \n"))
        break
    except ValueError:
        print("You need to enter a valid integer. Try again.")

if guess > number_to_guess:
    try_count = +1
    print(f"Try number {try_count}. Too high! \n > ")
elif guess < number_to_guess:
    try_count = +1
    print(f"Try number {try_count}. Too low! \n > ")
else:
    print(f"That's it! The number is {number_to_guess}. You got it in {try_count} tries.")

    



