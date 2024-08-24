import random

def get_user_choice():
    while True:
        print("Please choose: ")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        choice = input("Enter your choice (1/2/3): ")
        
        if choice in ['1', '2', '3']:
            return int(choice)
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def choice_to_string(choice):
    if choice == 1:
        return "Rock"
    elif choice == 2:
        return "Paper"
    elif choice == 3:
        return "Scissors"

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 0
    elif (user_choice == 1 and computer_choice == 3) or \
         (user_choice == 2 and computer_choice == 1) or \
         (user_choice == 3 and computer_choice == 2):
        return 1
    else:
        return -1
def display_result(user_choice, computer_choice, result):
    print(f"You chose: {choice_to_string(user_choice)}")
    print(f"Computer chose: {choice_to_string(computer_choice)}")
    if result == 0:
        print("It's a tie!")
    elif result == 1:
        print("You win!")
    elif result == -1:
        print("Computer wins!")
def play_game():
    user_score = 0
    computer_score = 0
    while True:
        user_choice = get_user_choice()
        computer_choice = random.randint(1, 3) 
        result = determine_winner(user_choice, computer_choice)
        display_result(user_choice, computer_choice, result)
        
        
        if result == 1:
            user_score += 1
        elif result == -1:
            computer_score += 1
        
        print(f"Score - You: {user_score}, Computer: {computer_score}")
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

def main():
    print("Welcome to Rock, Paper, Scissors!")
    play_game()
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
