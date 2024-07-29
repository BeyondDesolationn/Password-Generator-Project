import random
import string

def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters  # This part creates a string which includes all characters that could be selected for password creation
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    password = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(password) < min_length:
        new_char = random.choice(characters) # take a random char out of variable 'characters'
        password += new_char  # adds random character to password

        if new_char in digits:  # if the char is a digit
            has_number = True
        elif new_char in special:  # if the char is a special character
            has_special = True

        meets_criteria = True
        if numbers: # if the parameter 'numbers' is true
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special

    return password

min_length = int(input("Enter minimum length: "))
has_numbers = input("Do you want to have numbers? (y/n) ? ").lower() == "y"
has_special = input("Do you want to have special characters? (y/n) ? ").lower() == "y"
pwd = generate_password(min_length, has_numbers, has_special)
print("The generated password is: ", pwd)




