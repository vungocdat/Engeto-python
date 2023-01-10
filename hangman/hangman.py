# imports
import os
from graphic import obesenec
from words import word_to_guess
from random import choice


def main():
    life = 7
    game_on = True
    game(game_on, life)


def game(game_on, life):
    word = choice(word_to_guess)
    result = create_playground(word)

    while game_on and life > 0:
        #os.system('clear')
        show_progress(result, life)
        guess = input('Guess a letter or a word: ')

        # if player guess right the word
        if guess == word:
            game_on = False
        elif guess in word and len(guess) == 1:
            guess_right(word, result, guess)
        else:
            print('You guessed wrong!')
            life -= 1

        if '_' not in result:
            game_on = False

    else:
        game_over(game_on, word)


def create_playground(word):
    return ['_'] * len(word)


def show_progress(progress, life):
    print(obesenec[7-life])
    print(f"Your progress: {' '.join(progress)}")
    print(f"Remaining lives: {life}")


def guess_right(word, result, guess):
    for index, letter in enumerate(word):
        if letter == guess:
            result[index] = guess
    print('You guessed right!')


def game_over(game_on, word):
    if not game_on:
        print('You won!')
    else:
        print(obesenec[7])
        print(f'You loose!\nThe word was: {word}')


main()
