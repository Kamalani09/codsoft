import random
import string

def generate_password(length):
    # Define possible characters: uppercase, lowercase, digits, symbols
    characters = string.ascii_letters + string.digits + string.punctuation

    # Randomly choose characters to form the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("=== Password Generator ===")
    while True:
        try:
            length = int(input("Enter desired password length: "))
            if length <= 0:
                print("Please enter a positive number.")
                continue
            password = generate_password(length)
            print(f"\nGenerated Password: {password}")
        except ValueError:
            print("Invalid input. Please enter an integer.")

        # Ask user if they want another password
        again = input("\nGenerate another password? (y/n): ").lower()
        if again != 'y':
            print("Goodbye! Stay secure.")
            break
        print("--------------------------")

# Run the program
main()

