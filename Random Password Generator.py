import random # Import the random module
import string # Import the string module
import secrets # Import the secrets module
import pyperclip # Import the pyperclip module


def generate_password(length, include_letters=True, include_numbers=True, include_symbols=True): # Default values are True
    characters = '' # Empty string
    if include_letters: # If include_letters is True
        characters += string.ascii_letters # Add all the letters to the characters string
    if include_numbers: # If include_numbers is True
        characters += string.digits # Add all the digits to the characters string
    if include_symbols: # If include_symbols is True
        characters += string.punctuation # Add all the punctuation to the characters string

    password = ''.join(random.choice(characters) for _ in range(length)) # Join the random characters from the characters string for the length of the password
    return password # Return the password

def main(): # Main function
    length = int(input("Enter the length of the password: ")) # Ask the user for the length of the password
    include_letters = input("Include letters? (y/n): ").lower() == 'y' # Ask the user if they want to include letters
    include_numbers = input("Include numbers? (y/n): ").lower() == 'y' # Ask the user if they want to include numbers
    include_symbols = input("Include symbols? (y/n): ").lower() == 'y' # Ask the user if they want to include symbols

    password = generate_password(length, include_letters, include_numbers, include_symbols) # Generate the password
    print("Generated password:", password) # Print the generated password

    if input("Copy to clipboard? (y/n): ").lower() == 'y': # Ask the user if they want to copy the password to the clipboard
        pyperclip.copy(password) # Copy the generated password to the clipboard

if __name__ == '__main__': # If the script is being run directly
    main() # Run the main function  
