word = "babo"


def path():
    list_of_underscores = len(word) * "_"
    list_of_words = [i for i in word]
    print(list_of_underscores)
    return list_of_words, list_of_underscores


def get_users_input():
    guess = input("Guess a letter:").lower()
    return guess


def validate_users_input(list_of_words):
    already_guessed = []
    life = 5
    while True:
        guess = get_users_input()
        for i in range(len(list_of_words)):
            if list_of_words[i] == guess:
                already_guessed.append(guess)
        print(f"Already guessed letter(s):{already_guessed}")
        print(''.join(c if c in already_guessed else '_' for c in word))
        if len(already_guessed) == len(word):
            print("You guessed the word!")
            break
        if life > 0:
            if guess not in list_of_words:
                life -= 1
                if 5 >= life > 1:
                    print(f"You have {life} lives left")
                elif life == 1:
                    print(f"You have {life} life left")
        if life == 0:
            print("You lost the game")
            quit()



def main():
    wordlist, fieldlist = path()
    validate_users_input(wordlist)


if __name__ == "__main__":
    main()
