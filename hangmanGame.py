# Hangman game
#
#Joseph Barkate
# -----------------------------------


import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    #need a number count
    wordNum = 0
    
    for letter in secretWord:
        if letter in lettersGuessed:
            wordNum += 1
    # see if words in list match length of secret word
    if wordNum == len(secretWord):
        return True
    else:
        return False
        



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    #Create list of hangman guess as well as an index for stepping
    status = ['_ ']*len(secretWord)
    i = 0

    #Step through secret word and compare to list
    for letter in secretWord:       
        if letter in lettersGuessed:
            status[i]=letter
            
        i += 1
    #Join list together and return
    result =''
    return result.join(status)



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    #Create alphabet variable
    import string
    alphabet = string.ascii_lowercase
    notGuessed = ''
    
    for letter in alphabet:
        if letter not in lettersGuessed:
            notGuessed += letter
    
    return notGuessed
    
    

def hangman():
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    #Load Words
    loadWords()
    
    #Declare variables
    lettersGuessed = []
    mistakesMade = 0
    numGuess = 8
    
    #Define vraibles
    secretWord = chooseWord(wordlist)
    availableLetters = getAvailableLetters(lettersGuessed)
    
    #Start up sequence
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.')
    print('-------------')
    
    #Loop that is the main game
    while mistakesMade < numGuess:
        
        print('You have ' + str(numGuess - mistakesMade) + ' guesses left.')
        print('Available letters: '+ availableLetters)
        guess = input('Please guess a letter: ')
        
        #compare if that letter has been guessed before 
        if guess.lower() in lettersGuessed:
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
        
        #if  the guess was correct
        elif guess in secretWord:
            lettersGuessed += guess.lower()
            print('Good Guess: ' + getGuessedWord(secretWord, lettersGuessed))
            
        #if the guess was incorrect
        elif guess not in secretWord:
            lettersGuessed += guess.lower()
            mistakesMade += 1
            print('Oops! that letter is not in my word: ' + getGuessedWord(secretWord, lettersGuessed))
            
        #Update before next iteration of the loop    
        availableLetters = getAvailableLetters(lettersGuessed)
        print('------------')   
        
        #if the entire word is guessed
        if isWordGuessed(secretWord, lettersGuessed) :
            break 

       
    if mistakesMade < numGuess:
        print('Congratulations, you won!')
        
    else:
        print('Sorry, you ran out of guesses. The word was ' + secretWord)
        

#-----------------------------------------------------
#Test code to test the game
print(""""Welcome!  Type "hangman()" to play""")
#hangman()
