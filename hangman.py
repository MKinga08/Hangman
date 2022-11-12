import os
word = "babo"


def hangman_print():
    print("""
      o         o                                                                               
     <|>       <|>                                                                              
     < >       < >                                                                              
      |         |      o__ __o/  \o__ __o     o__ __o/  \o__ __o__ __o      o__ __o/  \o__ __o  
      o__/_ _\__o     /v     |    |     |>   /v     |    |     |     |>    /v     |    |     |> 
      |         |    />     / \  / \   / \  />     / \  / \   / \   / \   />     / \  / \   / \ 
               \      \o/  \o/   \o/  \      \o/  \o/   \o/   \o/   \      \o/  \o/   \o/ 
      |         |     o      |    |     |    o      |    |     |     |     o      |    |     |  
     / \       / \    <\__  / \  / \   / \   <\__  < >  / \   / \   / \    <\__  / \  / \   / \ 
                                                    |                                           
                                            o__     o                                           
                                            <\__ __/>                                           """)


def path():
    list_of_underscores = len(word) * "_ "
    list_of_words = [i for i in word]
    print(list_of_underscores)
    return list_of_words


def get_users_input():
    while True:
        guess = input("Guess a letter:").lower()
        if guess == "quit":
            quit()
        if guess.isalpha():
            if len(guess) > 1:
                print("You have to guess a letter")
            elif guess in correct:
                print("You have guessed this letter before")
            else:
                return guess
        else:
            print("You have to enter a letter")


def game(list_of_words, guess):
    for i in range(len(list_of_words)):
        if list_of_words[i] == guess:
            correct.append(guess)
    if len(correct) == len(word):
        print("You guessed the word!")
        play_again()


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
        print("You lost the game :(")
        play_again()


def screen_cleaner():
    os.system('cls')


def play_again():
    again = input("Do you want to play again?")
    if again == "yes" or again == "y":
        print("You sure?")
    else:
        quit()


def information(list_of_words, guess):
    print(''.join(c if c in correct else '_ ' for c in word))
    lives(list_of_words, guess)
    print(f"Already guessed letters:{already_guessed}")


correct = []
already_guessed = []
life = 5


def main():
    hangman_print()
    wordlist = path()
    while True:
        guessing = get_users_input()
        game(wordlist, guessing)
        screen_cleaner()
        information(wordlist, guessing)
        if life == 0 or len(correct) == len(word):
            play_again()


if __name__ == "__main__":
    main()
