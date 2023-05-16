import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors", "lizard", "spock"]

while True:
    user_input = input("Type Rock/Paper/Scissors/Lizard/Spock or Q to quit.").lower()
    if user_input == "q":
      break
    
    if user_input not in options:
      continue
    
    random_number = random.randint(0, 4)

    computer_guess = options[random_number]
    print("Computer picked", computer_guess + ".")
    
    if user_input == "rock" and computer_guess == "scissors":
      print("Rock crushes scissors!")
      user_wins += 1
      continue
    
    elif user_input == "rock" and computer_guess == "lizard":
      print("Rock crushes lizard!")
      user_wins += 1
    
    elif user_input == "scissors" and computer_guess == "paper":
      print("Scissors cuts paper!")
      user_wins += 1
      
    elif user_input == "scissors" and computer_guess == "lizard":
      print("Scissors decapitates lizard!")
      user_wins += 1
    
    elif user_input == "paper" and computer_guess == "rock":
      print("Paper covers rock!")
      user_wins += 1
      
    elif user_input == "paper" and computer_guess == "spock":
      print("Paper disproves Spock!")
      user_wins += 1
    
    elif user_input == "lizard" and computer_guess == "spock":
      print("Lizard poisons Spock!")
      user_wins += 1
    
    elif user_input == "lizard" and computer_guess == "paper":
      print("Lizard eats paper!")
      user_wins += 1
    
    elif user_input == "spock" and computer_guess == "scissors":
      print("Spock smashes scissors!")
      user_wins += 1
      
    elif user_input == "spock" and computer_guess == "rock":
      print("Spock vaporizes rock!")
      user_wins += 1
    
    elif user_input == computer_guess:
      print("It's a draw!")
    
    else:
      print("Try again!")
      computer_wins += 1 

print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Bye!")  
