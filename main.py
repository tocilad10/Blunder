import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    print('''Blunder, a deductive logic game.
            I am thinking of a {}-digit number with no repeated digits. 
            Try to guess what it is. Here are some clues:
            When I say:
                Misplaced - One digit is correct but in the wrong position.
                Spot-on - One digit is correct and in the right position.
                Blunder - No digit is correct.
                '''.format(NUM_DIGITS))
    
    while True:
        #store the secret number that player needs to guess
        #secretNum = getSecretNum()
        print("I'm thinking of a {}-digit number.".format(NUM_DIGITS))
        print('You have {} guesses to get it.'.format(MAX_GUESSES))
        return False


def getSecretNum():
    #returns a string made up of NUM_DIGITS unique random digits
    
    numbers = list('0123456789') #creates a list of digits 0-9
    random.shuffle(numbers) #shuffle numbers 
    
    #get the first NUM_DIGITS digits in the list for the secret number
    secretNum = ''
    
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum