import random
import string
def generate_password(length):
    # Define character sets for different complexity levels
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine character sets based on desired complexity
    character_sets = [lowercase_letters, uppercase_letters, digits, special_characters]

    # Ensure that the password length is at least 8 characters
    if length < 8:
        length = 8

    # Initialize the password with a random character from each character set
    password = [random.choice(charset) for charset in character_sets]

    # Fill the rest of the password with random characters
    while len(password) < length:
        charset = random.choice(character_sets)
        password.append(random.choice(charset))

    # Shuffle the characters to make the password more random
    random.shuffle(password)

    # Convert the list of characters to a string
    password = ''.join(password)

    return password

def main():
    print("Welcome to the Password Generator!")
    length = int(input("Enter the desired length of the password: "))

    password = generate_password(length)
    print("Your generated password is:", password)

if __name__ == "__main__":
    main()
