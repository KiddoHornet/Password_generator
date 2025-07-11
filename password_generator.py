import random
import string

def generate_password(length, include_uppercase=True, include_lowercase=True, include_numbers=True, include_special_chars=True):
    characters = ''
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_numbers:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    if not characters:
        return "Error: No character types selected."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    print("--- Password Generator ---")

    while True:
        try:
            password_length = int(input("Enter the desired password length: "))
            if password_length <= 0:
                print("Password length must be a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer for the length.")

    include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    include_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    include_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

    generated_password = generate_password(password_length, include_uppercase, include_lowercase, include_numbers, include_special_chars)

    print(f"\nYour generated password is: {generated_password}")  