import random, string
from words import pool_of_words
from visual_hangman import lives_visual_dict
from colorama import init, Fore
init(autoreset = True)

def hangman():
    def get_valid_word():
        words = random.choice(pool_of_words)
        while True:
            if words.isalpha() == True and len(words) == 6:
                break
            else:
                words = random.choice(pool_of_words)
        return words

    word = get_valid_word().upper()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    print("\n\nLet's play a game of hangman, shall we? Figure out the 6-letter-word given below.")
    print("You have only 12 moves. Win the game to save the hangman.\n")

    move = 12
    i, j = 0, 0
    while len(word_letters) != 0 and move != 0:        
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Moves left:", move)
        print("The letters used: ", " ".join(used_letters))
        print( "\nCurrent word:", "".join(word_list))

        
        while i % 2 == 0:                   #to make hangman lose his body parts for every 2 moves
            if j == 6:
                break
            print(lives_visual_dict[j])
            j += 1
            break

        user_letter = input("Enter any letter that you think might be in the word:").upper()
        print("\n")
        
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            move -= 1
            i += 1
            if user_letter in word_letters:
                word_letters.remove(user_letter)
        elif user_letter in used_letters:
            print(Fore.RED + "\nYou've already used this letter. Try again.\n")
            move -= 1
            i += 1
        else:
            print(Fore.RED + "\nInvalid character. Try again.\n")
            i = (2*i) + 1
            
            
    if len(word_letters) == 0:        
        print(f"Congratulations, the word is {word}. The hangman is saved.")
        print(lives_visual_dict['w'])
    else:
        print("Moves left: 0")
        print("Sorry, you failed to save the hangman. The word was", word)
        print(lives_visual_dict['l'])

    
hangman()
while True:
    nxt_rnd = input("\nDo you wanna play again(y/n)?")
    if nxt_rnd.lower() == 'y':
        hangman()
    elif nxt_rnd.lower() == 'n':
        break
    else:
        print("Invalid input, try again")
        
print("Thank you for playing our game!")