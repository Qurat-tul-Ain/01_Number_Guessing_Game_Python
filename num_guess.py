# Guess My Number
# I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high
# Enter a new number: 25 Your guess is too low
# Enter a new number: 40 Your guess is too low
# Enter a new number: 45 Your guess is too low
# Enter a new number: 48 Congrats! The number was: 48

#-----------------------------------------------------------------------------------------------------------------------

import random

random_generated_num = random.randint(1, 9)

allowed_attempts = 5
user_attempts = 0

# 2. while: condition with break statement
print("Start The Game!")
while user_attempts < allowed_attempts:
    print(f"Attempts Left: {allowed_attempts - user_attempts}")
  
    # 3. Get user input
    try:
        user_input = int(input("Enter a Number: "))
    except ValueError:
        print("Please enter a valid integer!")
        continue  # Skip the rest of the loop iteration if invalid input is given
    
    user_attempts += 1

    # 4. if statement:
    if user_input == random_generated_num:
        print("Congrats you guessed right:", random_generated_num)
        break
    elif user_input < random_generated_num:
        print("Too Low")
    elif user_input > random_generated_num:
        print("Too High")  
    else:
        print("Invalid input!")

# End Game Message after 5 attempts (if the user hasn't guessed correctly)
if user_attempts == allowed_attempts and user_input != random_generated_num:
    print(f"Game Over!\nThe correct number was {random_generated_num}.\nBetter luck next time!")

  
# hints
# Error handling



