import random  # Importing the random module for shuffling numbers

# Constants defining the number of digits in the secret number and max guesses allowed
NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    """Main function to handle game flow."""
    print('''
        I am thinking of a {}-digit number with no repeated digits.
        Try to guess what it is. Here are some clues:
        
        When I say:     That means:
          Pico              One digit is correct but in the wrong position.
          Fermi             One digit is correct and in the right position.
          Bagels            No digit is correct.

        For example, if the secret number was 248 and your guess was 843, the clues would be Fermi Pico.
        '''.format(NUM_DIGITS))
    
    while True:
        # Generate a random secret number
        secretNum = getSecretNum()
        print('I have thought up a number.')
        print('You have {} guesses to get it.'.format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            # Loop until user enters a valid guess
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}: '.format(numGuesses))
                guess = input('> ')

            # Get clues based on guess and secret number
            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break  # Correct guess, exit loop
            if numGuesses > MAX_GUESSES:
                print('You ran out of guesses.')
                print('The answer was {}.'.format(secretNum))

        # Ask the player if they want to play again
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')

def getSecretNum():
    """Generates a random secret number with unique digits."""
    numbers = list('0123456789')  # List of possible digits
    random.shuffle(numbers)  # Shuffle the digits

    secretNum = ''  # Initialize secret number
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])  # Select the first NUM_DIGITS shuffled digits
    return secretNum

def getClues(guess, secretNum):
    """Returns clues based on the user's guess compared to the secret number."""
    if guess == secretNum:
        return 'You got it!'  # Perfect match, player wins
    
    clues = []  # List to store clues

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')  # Correct digit in correct position
        elif guess[i] in secretNum:
            clues.append('Pico')  # Correct digit in wrong position
    
    if len(clues) == 0:
        return 'Bagels'  # No correct digits
    else:
        clues.sort()  # Sort clues alphabetically for consistency
        return ' '.join(clues)  # Return clues as a space-separated string
    
if __name__ == '__main__':
    main()  # Run the main function when script is executed