from random import choice

print("H A N G M A N")

def user_choice():

    while True:
        selection = input('Type "play" to play the game, "exit" to quit: ')
        if selection == "play":
            return True
        elif selection == "exit":
            return False
        else:
            continue

def is_valid_input(guess):
    if len(guess) != 1:
        print("You should input a single letter")
        return False
    elif guess not in "abcdefghijklmnopqrstuvwxyz":
        print("It is not an ASCII lowercase letter")
        return False
    return True

while user_choice():
    word_list = ['python', 'java', 'kotlin', 'javascript']
    word = choice(word_list)
    display_list = list("-" * len(word))
    lives = 8
    used = ""

    while lives > 0:
        display = "".join(l for l in display_list)
        print(f"\n{display}")
        if display == word:
            print("You guessed the word!\nYou survived!\n")
            break

        guess = input("Input a letter: ")

        if is_valid_input(guess):
            if guess in used:
                print("You already typed this letter")
                continue

            used += guess

            if guess in set(word):
                for c in range(len(word)):
                    if guess == word[c]:
                        display_list[c] = guess
            else:
                print("No such letter in the word")
                lives -= 1

    if lives == 0:
        print("You are hanged!\n")


