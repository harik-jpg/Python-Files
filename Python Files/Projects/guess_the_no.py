import random

print("\nLet's play a game, shall we?")
print("I'm thinking of a number that is between 0 and 999. Try to figure out what number that is.")
print("I'll help you along the way by telling whether your guesses are higher or lower than my number.")


def guess_the_no():
    num = random.randint(0, 999)
    
    print("Difficulty rating: \n  Easy - 20 guesses (Enter e)\n  Normal - 15 guesses (Enter n)")
    print("  Hard - 10 guesses (Enter h)\n  Impossible - 5 guesses (Enter i)")
    print("Are you ready?\n")
    
    count = 0
    flag = 0
    guess = 0
    
    while True:
        mode = input("Enter difficulty rating:")
        if mode.lower() == 'e':
            mode = 20
            break
        elif mode.lower() == 'n':
            mode = 15
            break
        elif mode.lower() == 'h':
            mode = 10
            break
        elif mode.lower() == 'i':
            mode = 5
            spl_mode(5, num, 0, 0)
            count = 5 #to ignore the loop below
            guess = num # to ignore the below if statement
            break
        elif mode.lower() == 'hk': #easter egg
            print("A game by Hari Krishnan")
        else:
            print("Invalid input. Try again.")
            
    while flag == 0 and count != mode:
        try:
            guess = int(input("Guess the number:"))
            while True:
                    if guess == num:
                        print("\nCongratulations, you've won. The number is ",num)
                        count += 1
                        print("No. of guesses used: ", count)
                        flag = 1
                        break
                    elif guess > num:
                        print("The number is lower than that.")
                        count += 1
                        break
                    elif guess < num:
                        print("The number is higher than that.")
                        count += 1
                        break

        except:
             print("Invalid input. Enter a number.")
            
    if guess != num:
        print("\nOps! Sorry, you've used your",mode,"guesses.")
        print("The number is", num)            


def spl_mode(mode, num, flag, count):
    print('Bruh, you think you can win this? So cute')
    while flag == 0 and count != mode:
        try:
            spl_guess = int(input("Guess the number:"))
            while True:
                if spl_guess == num:
                    print("\nHow did you do that?!? It's supposed to be impossible.")
                    print("Anyways, congratulations. The number is ",num)
                    count += 1
                    print("No. of guesses used: ", count)
                    flag = 1
                    break
                
                elif spl_guess > num:
                    if (spl_guess - num > 0) and (spl_guess - num < 5):
                        print("The number is slightly lower than that.")
                        count += 1
                        break
                    elif (spl_guess - num > 5) and (spl_guess - num < 15):
                        print("Pretty close, but the number is lower than that.")
                        count += 1
                        break
                    elif (spl_guess - num > 15) and (spl_guess - num < 250):
                        print("The number is lower than that.")
                        count += 1
                        break
                    elif (spl_guess - num > 250):
                        print("The number is far lower than that.")
                        count += 1
                        break
                    
                elif spl_guess < num:
                    if (num - spl_guess > 0) and (num - spl_guess < 5):
                        print("The number is slightly higher than that.")
                        count += 1
                        break
                    elif (num - spl_guess > 5) and (num - spl_guess < 15):
                        print("Pretty close, but the number is higher than that.")
                        count += 1
                        break
                    elif (num - spl_guess > 15) and (num - spl_guess < 250):
                        print("The number is higher than that.")
                        count += 1
                        break
                    elif (num - spl_guess > 250):
                        print("The number is far higher than that.")
                        count += 1
                        break
        except:
            print("Invalid input. Enter a number.")
             
    if spl_guess != num:
        print("\nOps! Sorry, you've used your",mode,"guesses.")
        print("The number is", num)
           

guess_the_no()
while True:
    nxt_rnd = input("Do you wanna play again(y/n)?")
    if nxt_rnd.lower() == 'y':
        guess_the_no()
    elif nxt_rnd.lower() == 'n':
        break
    else:
        print("Invalid input, try again")
        
print("Thank you for playing our game!")
