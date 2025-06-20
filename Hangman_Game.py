import random

print("Guess Car Company Name:-")
# List of words to choose from
word_list = ["hyundai","suzuki","mahindra","tata","volkswagen","ford"]

# Randomly choose a word from the list
word = random.choice(word_list)
guessed_letters = []
tries = 6  # Number of allowed incorrect guesses

print("Welcome to Hangman!")
print("_ " * len(word))  # Show blank spaces

while tries > 0:
    guess = input("\nGuess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You've already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Good guess!")
    else:
        print("Wrong guess!")
        tries -= 1

    # Display the word with guessed letters
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print(display_word.strip())

    # Check if the word is completely guessed
    if all(letter in guessed_letters for letter in word):
        print("\nCongratulations! You guessed the word:", word)
        break
else:
    print("\nGame over! The word was:", word)
