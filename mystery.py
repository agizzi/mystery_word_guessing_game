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

board = ['_ ' * len(answer)]
print(board[0])


def compare_letter(guess):
    wrong_guesses = 0
    if guess in answer_letters:
        print("Nice! You found a letter.")
        # guesses.append(guess)
    else:
        print("Oops! Try a different letter.")
        wrong_guesses += 1
        print("You have", 8 - wrong_guesses, "guesses remaining!")


guess = input("Guess a letter :) ")
compare_letter(guess)
