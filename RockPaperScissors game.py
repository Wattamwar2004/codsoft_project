import random

def get_user_choice():
    print("Choose an option:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    choice = input("Enter your choice (1/2/3): ")
    if choice in ['1', '2', '3']:
        return int(choice)
    else:
        print("Invalid choice. Please try again.")
        return get_user_choice()

def get_computer_choice():
    return random.randint(1, 3)

def determine_winner(user_choice, computer_choice):
    choices = {1: "Rock", 2: "Paper", 3: "Scissors"}
    print(f"You chose: {choices[user_choice]}")
    print(f"Computer chose: {choices[computer_choice]}")
    
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 1 and computer_choice == 3) or \
         (user_choice == 2 and computer_choice == 1) or \
         (user_choice == 3 and computer_choice == 2):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    print(result)

# Play the game
play_game()