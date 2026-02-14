import random

letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '+', '=', '(', ')' ]

print("Welcome to the PyPassword Generator!")
nr_letter = int(input("How many letters? "))
nr_numbers = int(input("How many numbers? "))
nr_symbols = int(input("How many sumbols? "))

random_letters = random.sample(letters, nr_letter)
random_numbers = random.sample(numbers, nr_numbers)
random_symbols = random.sample(symbols, nr_symbols)

password = random_letters + random_numbers + random_symbols
rand_password = random.sample(password, len(password))
print(f'Your password is: {''.join(rand_password)}')
