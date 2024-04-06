import random
def initial_display(word):
    return '_'*len(word)
def select_word():
    return random.choice(["computer","mouse","keyboard","cpu"])
def check_letter(letter,word):
    return letter in word
def update_display(word,display,letter):
    new_display=""
    for i in range(len(word)):
        if word[i]==letter:
            new_display+=letter
        else:
            new_display+=display[i]
    return new_display
def check_win(display):
    return "_" not in display
def check_lose():
    return incorrect_attempts==6
def display_hangman(incorrect_attempts):
    stages=[
        """
                  --------
                  |      |
                  |      O
                  |     \\|/
                  |      |
                  |     / \\
               """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     /
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |
        """,
        """
           --------
           |      |
           |      O
           |
           |
           |
        """,
        """
           --------
           |      |
           |
           |
           |
           |
        """
    ]
    return stages[incorrect_attempts]
print("lets play hangman game ")
word = select_word()
display = initial_display(word)
print("World:",display)
incorrect_attempts = 0
guessed_letters = []
while True:
    guess=input("Enter a single letter: ").lower()
    if guess in guessed_letters:
        print("Already guessed")
    guessed_letters.append(guess)
    if check_letter(guess,word):
        display=update_display(word,display,guess)
        print("Correct guess")
        print("The word is:",display)
        if check_win(display):
            print("Congratulations! You win the game.The word was:",display)
            break
    else:
        print("Incorrect letter")
        incorrect_attempts+=1
        print(display_hangman(incorrect_attempts))
        if check_lose():
            print("You lost")
            print(display_hangman(incorrect_attempts))
            break
