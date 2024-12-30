import random



print("Welcome to the number guessing Game")

attempts = 0

is_game_over = False

actual_answer = random.randint(1,100)

print("I am thinking of a number between 1 and 100")

# print(f"For reference correct answer is {actual_answer}")



difficulty = input("Choose a difficulty. Type 'easy' or 'hard: ")



if difficulty == "easy":

  attempts = 10

  print(f"You have {attempts} attempts remaining to guess the number")

  while is_game_over == False and attempts > 0:

    guess = int(input("Make a guess "))    

    if guess == actual_answer:

      is_game_over = True

      

      print(f"You got it! The answer was {actual_answer}.")

    if guess < actual_answer:

      attempts -= 1

      print("Too low")

      print(f"You have {attempts} attempts remaining to guess the number")

    if guess > actual_answer:

      attempts -= 1

      print("Too high")

      print(f"You have {attempts} attempts remaining to guess the number")

  if attempts == 0:

    print("You have lost")

    print(f"Actual answer is {actual_answer}")

elif difficulty == "hard":

  attempts = 5

  print(f"You have {attempts} attempts to guess the number")

  while is_game_over == False and attempts > 0:

    guess = int(input("Make a guess "))

    if guess == actual_answer:

      is_game_over = True

      print(f"You got it! The answer was {actual_answer}.")

    if guess < actual_answer:

      attempts -= 1

      print("Too low")

      print(f"You have {attempts} attempts remaining to guess the number")

    if guess > actual_answer:

      attempts -= 1

      print("Too high")

      print(f"You have {attempts} attempts remaining to guess the number")

  if attempts == 0:

    print("You have lost")

    print(f"Actual answer is {actual_answer}")