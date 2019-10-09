import random

with open("words.txt") as words_list:
    words = words_list.read().split()
    # print(type(words))
    # print(words)
answer = random.choice(words)
answer_letters = list(answer)
print(answer)
# print(type(answer))
# print(answer_letters)
# print(type(answer_letters))
print("This word has", len(answer), "letters!")

board = ('_ ' * len(answer))
board_squares = list(board)
print(board)
letter_guesses = []

# print(letter_and_index)
# print(type(board_squares))


def compare_letter(guess):
    frequency = answer_letters.count(guess)
    wrong_guesses = 0
    index = answer_letters.index(guess)
    # print(index)
    if guess in answer_letters:
        if frequency > 1:
            # board_squares.pop(letter_and_index[letter: value]
            print("byeeeeee")
        else:
            board_squares.pop(index*2)
            board_squares.insert((index*2), guess)
            # print(frequency)
            print("Nice! You found a letter.")
            # print(board)
            print("" .join(board_squares))
            guess = input("Guess a letter :) ")
            compare_letter(guess)
    else:
        print("Oops! Try a different letter.")
        wrong_guesses += 1
        print("You have", 8 - wrong_guesses, "guesses remaining!")


guess = input("Guess a letter :) ")
compare_letter(guess)
