# Import the random module
import random
# Create count_rock, count_paper and count_scissors variables 
count_rock=0
count_paper=0
count_scissors=0

# Create the update_counts() function.
def update_counts(user_input):
  global count_rock,count_paper,count_scissors
  if user_input==0:
    count_rock=count_rock+1
  elif user_input==1:
    count_paper=count_paper+1
  elif user_input==2:
    count_scissors=count_scissors

    # Create the predict() function.
def predict():

  if count_rock > count_paper and count_rock > count_scissors:
    pred = 0
  elif count_paper > count_rock and count_paper > count_scissors:
    pred = 1
  elif count_scissors > count_rock and count_scissors > count_paper:
    pred = 2
  else:
    pred = random.randint(0, 2)

  return pred

# Create the player_score and comp_score variables.
player_score=0
comp_score=0

# Create the update_scores() function.
def update_scores(user_input):
  global player_score, comp_score
  # Rock wins over scissors, scissors win over paper and paper wins over rock.
  pred = predict()

  # Situation 1, 2 and 3.
  if user_input == 0:
    if pred == 0:
      print("\nYou played ROCK, computer played ROCK.")
      print("\nComputer Score: ", comp_score, "\nYour Score: ", player_score)
    elif pred == 1:
      print("\nYou played ROCK, computer played PAPER.")
      comp_score += 1
      print("\nComputer Score: ", comp_score, "\nYour Score: ", player_score)
    else:
      print("\nYou played ROCK, computer played SCISSORS.")
      player_score += 1
      print("\nComputer Score: ", comp_score, "\nYour Score: ", player_score)
  
  # Situation 4, 5 and 6.
  elif user_input == 1:
    if pred == 1:
      print("\nYou played PAPER, computer played PAPER.")
      print("\nComputer Score: ", comp_score, "\nYour Score: ", player_score)
    elif pred == 0:
      print("\nYou played PAPER, computer played ROCK.")
      player_score += 1
      print("\nComputer Score: ", comp_score, "\nYour Score: ", player_score)
    else:
      print("\nYou played PAPER, computer played SCISSORS.")
      comp_score += 1
      print("\nComputer Score: ", comp_score, "\nYour Score: ", player_score)

  else:
    # Situation 7,8 and 9.
    if pred==2:
      print("\nYou played SCISSORS, computer played SCISSORS.")
      print("\nComputer Score: ", comp_score, "\nYour Score: ", player_score)
    elif pred==0:
      print("\nYou played SCISSORS, computer played ROCK.")
      comp_score +=1
      print("\nComputer Score: ", comp_score, "\nYour Score: ", player_score)
    else:
      print("\nYou played SCISSORS, computer played PAPER.")
      player_score += 1
      print("\nComputer Score: ", comp_score, "\nYour Score: ", player_score)

# Create a list and store it
valid_entries = ['0', '1', '2']

# Create an infinite while loop.
while True:
  user_input = input("Enter 0 for ROCK, 1 for PAPER and 2 for SCISSORS: ")
  # Another while loop to check whether the input provided by a player exists in the valid_entries list or not.
  while user_input not in valid_entries:
    # If the input provided by a player does not exist in the valid_entries list, then Invalid Input! is printed
    print("\nInvalid Input!")
    user_input = input("Enter 0 for ROCK, 1 for PAPER and 2 for SCISSORS: ")

  # Convert the user_input value to an integer value
  user_input = int(user_input)
  # Call the update_scores() function with the user_input
  update_scores(user_input)
  # Call the update_counts() function with the user_input 
  update_counts(user_input)
  # Check if the score is 10 for any of the players
  if comp_score==10:
    print("Computer Won!")
    break
  # Else if the player_score == 10, print winning message
  elif player_score==10:00
  print("You Won!")
  break