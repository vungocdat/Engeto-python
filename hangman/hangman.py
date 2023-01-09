# imports
from graphic import obesenec
from words import word_to_guess
from random import choice

# variables
life = 7
game_on = True
word = choice(word_to_guess)
result = ['_'] * len(word)

while game_on and life > 0:
    #show result
    print(f"Your progress: {' '.join(result)}")
    print(f"Remaining lives: {life}")

    # TODO input
    guess = input('Guess a letter or a word: ')

    # if player guess right the word
    if guess == word:
        game_on = False

    # if player guess right the letter
    elif guess in word and len(guess) == 1:
        for index, letter in enumerate(word):
            if letter == guess:
                result[index] = guess
        print('You guessed right!')

        # if all letter are guessed right 1 by 1
        if '_' not in result:
            game_on = False

    # if the letter is not in word
    else:
        print('You guessed wrong!')
        life -= 1
else:
    if not game_on:
        print('You won!')
    else:
        print(f'You loose!\nThe word was: {word}')
