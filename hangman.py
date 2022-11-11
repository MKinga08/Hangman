import os
word = "babo"


def path():
    list_of_underscores = len(word) * "_"
    list_of_words = [i for i in word]
    print(list_of_underscores)
    return list_of_words


def get_users_input():
    while True:
        guess = input("Guess a letter:").lower()
        if guess == "quit":
            quit()
        if guess.isalpha():
            if guess in correct:
                print("You have guessed this letter before")
            else:
                return guess
        else:
            print("You have to enter a letter")


def game(list_of_words, guess):
    for i in range(len(list_of_words)):
        if list_of_words[i] == guess:
            correct.append(guess)
    print(''.join(c if c in correct else '_' for c in word))
    if len(correct) == len(word):
        print("You guessed the word!")
        quit()


def lives(list_of_words, guess):
    global life
    if guess not in list_of_words:
        if guess not in already_guessed:
            life -= 1
            already_guessed.append(guess)
            if 5 >= life > 1:
                print(f"You have {life} lives left")
            elif life == 1:
                print(f"You have {life} life left")
        else:
            print("You have guessed this letter before")
    if life == 0:
        print("You lost the game")
        quit()


def screen_cleaner():
    os.system('cls')


correct = []
already_guessed = []
life = 5


def main():
    wordlist = path()
    while True:
        guessing = get_users_input()
        game(wordlist, guessing)
        lives(wordlist, guessing)
        screen_cleaner()
        print(''.join(c if c in correct else '_' for c in word))

if __name__ == "__main__":
    main()
