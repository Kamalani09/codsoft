import random

def get_user_choice():
    while True:
        choice = input("Choose rock, paper, or scissors: ").lower()
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        print("Invalid choice. Please enter rock, paper, or scissors.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return "user"
    else:
        return "computer"

def get_contact_info():
    print("=== Welcome to Rock-Paper-Scissors Game ===")
    name = input("Enter your name: ")
    phone = input("Enter your phone number: ")
    email = input("Enter your email: ")
    address = input("Enter your address: ")
    print(f"\nHello {name}! Let's start the game.\n")
    return {"name": name, "phone": phone, "email": email, "address": address}

def main():
    contact_info = get_contact_info()
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        winner = determine_winner(user_choice, computer_choice)

        if winner == "tie":
            print("It's a tie!")
        elif winner == "user":
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"\nScoreboard -> {contact_info['name']}: {user_score} | Computer: {computer_score}")

        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print(f"\nThanks for playing, {contact_info['name']}! Final score -> You: {user_score}, Computer: {computer_score}")
            print(f"Contact Info stored: {contact_info}")
            break
        print("\n-------------------------------")

# Run the game
main()

