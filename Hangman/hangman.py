from random import randint  # Do not delete this line


def displayIntro():
    filename = "hangman-ascii.txt"
    f1 = open(filename, "r")  # opening text file in read mode to get intro art and rules
    mylines = f1.readlines()  # reading all lines and storing them as elements of list named mylines
    for i in range(23):  # since first 23 lines is intro in the text file, we read first 23 lines
        print(mylines[i], end="")

def displayEnd(result):
    filename = "hangman-ascii.txt"
    f1 = open(filename, "r")  # opening text file in read mode to get end arts
    mylines = f1.readlines()
    if result:  # display winning art if result is True
        for i in range(190, 203):  # winning art is from lines 190 to 203 in text file
            print(mylines[i], end="")
    else:  # display losing art if result is false
        for i in range(99, 112):  # losing art is from lines 99 to 112 in text file
            print(mylines[i], end="")


def displayHangman(state):
    filename = "hangman-ascii.txt"
    f1 = open(filename, "r")  # opening text file in read mode to get hangman arts
    mylines = f1.readlines()
    n, m = 5, 5  # just declaring variables
    # in the following code, we assign n and m to numbers and that number range will be
    # used to read from text file and draw hangman according to the number of lives left
    if state == 5:
        n = 24
        m = 32
    elif state == 4:
        n = 37
        m = 45
    elif state == 3:
        n = 50
        m = 58
    elif state == 2:
        n = 63
        m = 71
    elif state == 1:
        n = 76
        m = 84
    elif state == 0:
        n = 89
        m = 97
    for i in range(n, m):
        print(mylines[i], end="")


def getWord():
    filename = "hangman-words.txt"
    f1 = open(filename, "r")  # opening words text file
    mylines = f1.readlines()  # reading all words and storing them as a list
    return mylines[randint(0, len(mylines) - 1)][:-1]  # return one element of the list but without \n


def valid(c):
    return True if c.isalpha() and c.islower() and len(c) == 1 else False
    # if the character satisfies 3 requirements, return True, else return False


def play():
    myword = getWord()  # storing random word in variable
    guessword = ""
    for i in range(len(myword)):  # creating underscores of the same length to display to the player
        guessword += "_"
    lives = 5
    while lives > 0:  # until lives run out, player will be able to play the game and input a character
        displayHangman(lives)
        print("Guess the word: ", end="")
        print(guessword)
        char = input("Enter the letter: ")
        while not valid(char):  # checking if inputted character is valid or not. if not, ask again
            char = input("Enter the letter: ")
        # checking if the player guessed correctly or not. if yes, replace appropriate underscore(s) with that character
        if char in myword:
            for j in range(len(myword)):
                if myword[j] == char:
                    guessword = guessword[:j] + char + guessword[j + 1:]
        else:
            lives -= 1  # if not, the player loses one life
        if myword == guessword:  # at the end of the loop checking if the player guessed all the characters
            print("Hidden word was: ", myword)  # reveal the hidden word anyways
            return True  # if yes, return true
    displayHangman(lives)  # if loop ends, it means no lives are left so the game is lost
    print("Hidden word was: ", myword)  # revealing the word
    return False  # and returning False


def hangman():
    while True:
        displayIntro()
        result = play()
        displayEnd(result)
        # after the game ends, ask the player if he/she wants to play again
        choice = input("Do you want to play again? (yes/no) ")
        # if no, we will break the loop and everything will end. if anything else(yes), loop will continue
        if choice == "no":
            break


if __name__ == "__main__":
    hangman()
