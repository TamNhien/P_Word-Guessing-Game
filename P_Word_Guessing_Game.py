import random

name = input("What is your name? ")

print("Good luck !", name)

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

# Function will choose one random
# word from this list of words
word = random.choice(words)

print("Guess the characters")

guesses = ''

# any number of turns can be used here
turns = 12

while turns > 0:
    # counts the number of times a user fails
    failed = 0
    # all characters from the input
    # word taking one at a time.
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_")
            failed +=1
            
    if failed == 0:
        print("You win")
        print("The word is : ", word)
        break
    # if user has input the wrong alphabet then
    # it will ask user to enter another alphabet
    print()
    guess = input("guess a character : ")
    
    guesses += guess
    
    if guess not in word:
        turns -= 1
        print("Wrong")
        print("You have", + turns, "more guesses")
        
        if turns == 0:
            print("You lose")
        
    