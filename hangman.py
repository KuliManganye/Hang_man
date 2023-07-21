import random
import os

# import the words from hangmanwords to be used in this file
from hangmanwords import word_list

# using random to choose a word from the word_list and assigning it to a variable chosen_word
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# We will use a while loop to allow the user to go again till they finish guessing the letters. The loop will only stop once the user has guess all the letters in the chosen_word and 'display'
# has no more blanks ("_"). Then we can tell the user they've won
end_game = False

# create a variable called lives. This is to assign lives to the user. That of every wrong guess they get the ;ives are depleted till they lose
lives = 6

# Import the logo from hangmanart and print it at the start of the game
from hangmanart import logo
print(logo)

# Testing the code
print(chosen_word)

# Our game needs a list as the display for each letter in chosen_word should "_". To start the process let us create an empty list then assign the display of "_" to the length of each "chosen_word"
display = []
for _ in chosen_word:
    display += "_"

while not end_game:
# Ask the user to guess a ltter and assign their answer to a variable called guess. the .lower() is to ensure the computer ignores the case by automatically lowering the letters
    guess = input("Guess A Letter!: ").lower()
    
    # clear the screen after prompting the user to make a guess
    os.system("cls")
            
# If the user has entered a letter they've alraedy guess before, print the letter and let them know
    if guess in display:
        print(f"You've already guessed {guess}")
    
        
# Loop through each letter in the chosen_word. If the letter matches the guess, then reveal the letter at it's correct position
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guess letter: {guess}")
        if letter == guess:
            display[position] = letter
    
# Everytime the user gets a guess wrong for the letter in the chosen_word, reduce the lives by 1
# If lives goes down to 0 then the game should stop and it should let the user know they lost
    if guess not in chosen_word:
        # if the letter guessed is incorrect, print the letter and let the user know it's incorrect
        print(f"You guess {guess}, that's not in the word, you lose a life")
        lives -= 1
        if lives == 0:
            end_game = True
            print("You Lose!")

    # Join all the elemts in the list and turn it into a string
    print(f"{' '.join(display)}")

    # check if the user got all the letters correct.
    if "_" not in display:
        end_game = True
        print("You Win!")

# Print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining
    from hangmanart import stages
    print(stages[lives])