word = "thisishard" #19


def game():
    field = len(word)*"_"
    print(field)
    list_of_words = [i for i in word]
    return list_of_words


def get_users_input(list_of_words):
    c = 0
    while True:
        guess = input("Guess a letter:").lower()
        for i in range(len(list_of_words)):
            if list_of_words[i] == guess:
                c += 1
        if c == len(word):
            print("You guessed the word!")
            break


def main():
    wordlist = game()
    get_users_input(wordlist)


if __name__ == "__main__":
    main()
