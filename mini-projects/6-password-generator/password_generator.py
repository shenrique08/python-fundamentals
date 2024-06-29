import random
import string

print()
message = " Welcome to the ultimate password generator "
print(message.center(75, '='))

while True:
    amount_letters = int(input("\nHow many [letters] would you like in your password? x > 0 "))
    amount_symbols = int(input("How many [symbols] would you like? x > 0 "))
    amount_numbers = int(input("How many [numbers] would you like? x > 0 "))
    if amount_letters > 0 and amount_symbols > 0 and amount_numbers > 0:
        break
    else:
        print("\nERROR! Try again!")

random_letters = ''
for char in range(1, amount_letters + 1):
    random_letter = random.choice(string.ascii_letters)
    random_letters += random_letter

random_symbols = ''
for char in range(1, amount_symbols + 1):
    random_symbol = random.choice(string.punctuation)
    random_symbols += random_symbol

random_numbers = ''
for char in range(1, amount_numbers + 1):
    random_number = random.choice(string.digits)
    random_numbers += random_number

# this is one way to concatenate strings in python
password = random_letters + random_numbers + random_symbols


# function to shuffle the password created
def shuffle_string(s):
    char_list = list(s)
    random.shuffle(char_list)
    return ''.join(char_list)


password = shuffle_string(password)

print(f"The password created was [[[  {password}   ]]]")
