# Hangman

## About the project and it's functions:

- basic hangman game with english words
  - words are selected randomly from a txt file
- Letter guessing function is validated:
  - You can't guess a number or multiple letters (but lives are not taken from you if you do)
  - You can't guess a letter you did before (lives are not taken from you here either)
  - If you guess a wrong letter, you will lose a life, and you will add a "body part" to the man hanging
  - If you guess the right letter(s) the program will change the right blank underscore to the letter
- Screen cleaner function
  - Note: it only works if you open the file in CLI, PyCharm doesn't want to accept this feature :(
  - With this function you will only see the following information:
    - the word you are trying to guess with underscores replacing the letters, and only previously guessed letters are visible 
    - Your remaining lives
    - The current state of the hangman drawing (depending on your lives)
    - Already guessed wrong letters
    - And of course the instruction: "Guess a letter:"
- Winning and losing: 
  - either you win or lose, the word you were trying to guess will appear on the screen with a question whether you want to play again or not
- Play again function:
  - The game will restart if you type "yes" or "y" and will quit in any other cases
- A little extra:
  - It has a big "Hangman" title, written in a funny form, check it out if you are curious how it looks like ;)

## If you are not familiar with the game:
You can find the instruction manual and all other useful information about the game here: [Hangman](https://en.wikipedia.org/wiki/Hangman_(game))