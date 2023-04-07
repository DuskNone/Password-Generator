import random
import string

def generate_password(length, numbers=True, special_chars=True):
    # define the possible characters for the password
    
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
  
    # generate a password with the specified length
    # password = ''.join(random.choice(characters) for i in range(length))

    characters = letters
    if numbers: characters += digits
    if special_chars: characters += special
    
    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < length:
        new_char = random.choice(characters)
        pwd+= new_char
        
        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True
            
        meets_criteria=True
        if numbers:
            meets_criteria= has_number
        if special_chars:
            meets_criteria= meets_criteria and has_special 

    return pwd

# test the password generator by generating a password with a length of 12 characters
# password = generate_password(12,special_chars=False,numbers=False)

password = generate_password(12)
print(password)