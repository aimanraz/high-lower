# Debug mode

##############################################################################
from replit import clear

# import the logo
from art import logo, vs
print(logo)

# import the data
from game_data import data

# generate value between the data size
import random 
def gen():
  ran_num = random.randint(0,len(data)-1)
  return ran_num

# data generator
def data_gen():
  return data[gen()]

# For starter, we will generate 2 random data to compare 
##  store the A from the data
var_A = data_gen()

## store the B from the data
var_B = data_gen()

# function to display the both val
def display():
  #print(f"Debugging, A:{var_A['follower_count']}, B:{var_B['follower_count']} ")
  print(f"Compare A: {var_A['name']}, a/an {var_A['description']}, from {var_A['country']}.")

  print(vs)

  print(f"Compare B: {var_B['name']}, a/an {var_B['description']}, from {var_B['country']}.")

# user score
SCORE = 0

# score checker 
win_lose = False
 

# while loop
while not win_lose:
  # call to display the first round random data
  display()

  # get the input from the user
  A_B = input("Who has more followers? Type 'A' or 'B': ").lower()

  # A or B comparator
  if A_B == 'a':
    if var_A['follower_count'] > var_B['follower_count']:
      before_score = SCORE
      SCORE += 1
      final_score = SCORE
      var_B = var_A
    else:
      before_score = SCORE
      final_score = before_score
  else:
    if var_B['follower_count'] > var_A['follower_count']:
      before_score = SCORE
      SCORE += 1
      final_score = SCORE
    else:
      before_score = SCORE
      final_score = before_score

  # display the result and generate new var_A
  clear()
  print(logo)

  if final_score > before_score:
    print(f"You're right! Current score: {final_score}")
    var_A = data_gen()
  else:
    print(f"Sorry, that's wrong. Final score: {final_score}")
    win_lose = True