import random
from art import header

wordList = ['aardvark', 'baboon', 'camel']
chosenWord = random.choice(wordList)
lives = len(chosenWord)

print(f'''{header}
The random word is: {chosenWord}.
You have {lives} lives.
''')

placeholder = ''
for position in range(len(chosenWord)):
    placeholder += '_ '
print(placeholder)

gameOver = False
correct_letters = []
while not gameOver:
    guess = input('guess a letter: ').lower()
    display = ''
    if guess in correct_letters:
        print(f"You've already guessed letter '{guess}'.")
    for letter in chosenWord:
        if letter == guess:
            display += letter + ' '
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter + ' '
        else:
            display += '_ '
    print(display)

    if guess not in chosenWord:
        lives -= 1
        print(f'You have {lives} left.')
        if lives == 0:
            gameOver = True
            print('You lose!')
    else:
        print(f'You have {lives} left.')

    if '_' not in display:
        gameOver = True
        print('You win!')
