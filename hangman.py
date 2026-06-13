import random

print("=" * 30)
print("🎮 HANGMAN GAME 🎮")
print("=" * 30)

words = ["apple", "tiger", "house", "beach", "robot"]

secret_word = random.choice(words)

guessed_letters = []
attempts = 6

while attempts > 0:

    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    if "_" not in display_word:
        print("\n🎉 Congratulations!")
        print("You guessed the word:", secret_word)
        break

    guess = input("Guess a letter: ").lower()

    # Check if only one letter is entered
    if len(guess) != 1:
        print("⚠ Please enter only one letter!")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print("⚠ You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("✅ Correct Guess!")
    else:
        attempts -= 1
        print("❌ Wrong Guess!")
        print("Attempts Left:", attempts)

if attempts == 0:
    print("\n💀 Game Over!")
    print("The word was:", secret_word)

print("\nThank you for playing Hangman!")