"""
Run with python2
"""
import random
import string

WORDLIST_FILENAME = "palavras.txt"
NUMBER_OF_GUESSES = 8

def load_words():
    """
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # in_file: file
    in_file = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = in_file.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return random.choice(wordlist)


def is_word_guessed(secret_word, letters_guessed):

#    secretLetters = []
#    for letter in secret_word:
#        if letter in secretLetters:
#            secretLetters.append(letter)
#        else:
#            pass

    for letter in secret_word:
        if letter in letters_guessed:
            pass
        else:
            return False

    return True

# def get_guessed_word():
#     guessed = ''
#     return guessed

# def get_available_letters():
#     # import string
#     # 'abcdefghijklmnopqrstuvwxyz'
#     return string.ascii_lowercase


def hangman(secret_word):
    """
    Main function of the program
    """
    guesses = NUMBER_OF_GUESSES
    letters_guessed = []
    print 'Welcome to the game Hangman!'
    print 'I am thinking of a word that is', len(secret_word), ' letters long.'
    print '-------------'

    while is_word_guessed(secret_word, letters_guessed) is False and guesses > 0:
        print 'You have ', guesses, 'guesses left.'

        available = string.ascii_lowercase
        for letter in available:
            if letter in letters_guessed:
                available = available.replace(letter, '')
        print 'Available letters', available

        letter = raw_input('Please guess a letter: ')

        if letter in letters_guessed:
            print 'Oops! You have already guessed that letter: '

        elif letter in secret_word:
            letters_guessed.append(letter)
            print 'Good Guess: '

        else:
            guesses -= 1
            letters_guessed.append(letter)
            print 'Oops! That letter is not in my word: '

        guessed = ''
        for letter in secret_word:
            if letter in letters_guessed:
                guessed += letter
            else:
                guessed += '_ '
        print guessed
        print '------------'


    if is_word_guessed(secret_word, letters_guessed):
        print 'Congratulations, you won!'
    else:
        print 'Sorry, you ran out of guesses. The word was ', secret_word, '.'




SECRET_WORD = load_words().lower()
hangman(SECRET_WORD)
