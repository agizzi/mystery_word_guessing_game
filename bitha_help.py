import random


def play_game():
    permission = input('Would you like to guess a word:')
    if permission == 'y':
        guess_word()
    else:
        print('See you next time')


def difficulty():
    guess_difficulty = input(
        'Press e for Easy mode, n for normal mode, or h for hard mode').lower()
    if guess_difficulty == 'e':
        word_range = range(4, 7)
        print("Welcome to easy mode")
    if guess_difficulty == 'n':
        word_range = range(6, 9)
        print("You've entered normal mode")
    if guess_difficulty == 'h':
        word_range = range(8, 30)
        print("Prepare for hard mode")


def guess_word():
    with open('words.txt') as file:
        text = file.read()
        words = text.split()
        word = random.choice(words)
        print(word)

        word_length = len(word)
        print(word_length)


play_game()
difficulty()
