import random
letter_guesses = []


def end_game():
    with open("words.txt") as words_list:
        words = words_list.read().split()
    answer = random.choice(words).lower()
    print(answer)
    print("This word has", len(answer), "letters!")
    board = ['_'] * len(answer)
    game_over = False
    print(" ".join(board))

    def compare_letter(word, board, guess):
        start = 0
        if len(letter_guesses) >= 8:
            game_over = True
            print(
                "Well, this is awkward... You lost! Press the up arrow and hit enter to play again.")
            print(game_over)
            return
        else:
            if word.find(guess, start) == -1:
                letter_guesses.append(guess)
                print("Oops, try another letter or word.")
                print("Incorrect guesses:", ", ".join(letter_guesses))
                print("You have", 8-len(letter_guesses), "guesses remaining.")
                # print(game_over)
            else:
                while word.find(guess, start) != -1:
                    index = word.index(guess, start)
                    start = index + 1
                    board[index] = guess
                    print("Incorrect guesses:", ", ".join(letter_guesses))
                    print("You have", 8-len(letter_guesses), "remaining.")
                    return board

    def compare_word(word, board, guess):
        if guess == answer:
            print("Wow! You win! Press the up arrow and hit enter to play again. :) ")
            board = guess
            game_over == True
            return
        else:
            print("Oops, that's not a valid guess. :/ Try again. ")
            guess = input("Guess a letter or word :)  ")

    while (game_over == False):
        if len(letter_guesses) >= 8:
            print("GAME OVER LOSERRRR")
            return
        else:
            guess = input("Guess a letter or word FUCKKKKK:)  ")
            if len(guess) == 1 and guess.isalpha():
                compare_letter(answer, board, guess)
                print(" ".join(board))
                # guess = input("Guess a letter or word :)  ")
            elif len(guess) == len(answer) and guess.isalpha():
                compare_word(answer, board, guess)
            else:
                print("Oops, that's not a valid guess. :/ Try again. ")
                # guess = input("Guess a letter or word :)  ")


end_game()
