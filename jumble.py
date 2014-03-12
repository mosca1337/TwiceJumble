#!/usr/bin/python

# Creates a hash table of characters as the key to a list of words
def createLookupTable():
    # Obtain a list of all english words
    words = open('corncob_lowercase.txt').read().splitlines()

    # Create a lookup table of characters to words
    lookupTable = {}
    for word in words:
        characters = sorted(word) # Sort the characters
        characters = ''.join(characters) # Merge list of characters to string
        if characters in lookupTable:
            lookupTable[characters].append(word)
        else:
            lookupTable[characters] = [word]

    return lookupTable

# Get all possible search keys for the given characters.
# Ex. listOfKeys('abc') will return ['abc', 'ab', 'ac', 'a', 'bc', 'b', 'c']
def listOfKeys(key):
    keys = recursiveListOfKeys('',key)
    return keys[:len(keys) - 1] # Avoid returning the base case of ''

def recursiveListOfKeys(left, right):
    # Base case
    if right == '':
        return [left + right]
    
    keys = recursiveListOfKeys(left + right[0:1], right[1:]) + recursiveListOfKeys(left, right[1:])
    return keys

def main():
    
    # Create a lookup table of characters to english words
    lookupTable = createLookupTable()

    while True:
        # Grab a word/characters from the user and clean it up
        word = raw_input("Enter a word or characters: ")
        word = word.lower().strip()
        characters = sorted(word) # Sort by characters
        characters = ''.join(characters) # Merge list of characters to string

        # Find all possible keys that can be derived from these characters
        keys = listOfKeys(characters)
        possibleWords = []
        for key in keys:
            # Are there any possible english words made up of these characters?
            if key in lookupTable:
                possibleWords = possibleWords + lookupTable[key]
        
        # Print the results
        if len(possibleWords) > 1:
            # Print out all possible words
            print('Possible words:')
            for possibleWord in possibleWords:
                # Do not print out the word to be scrambled
                if possibleWord != word:
                    print(possibleWord)
        else:
            print('No possible words.')

main()
