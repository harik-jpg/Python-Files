import random


wait = 0
guess = 0

print("\nThink of any number. I'll try to guess it.")

while True:
    query = input("Have you figured out the number (y/n)?")
    
    if query.lower() == 'y':
        
        print("Tell me the range of your number (like 0 to 200). Make it challenging for me.")
        start=int(input("Enter start value: "))
        end=int(input("Enter end value: "))
        
        num = random.randint(start, end)
        start0, end0 = start, end
        
        
        
        while True:
            try:
                hint = input(f"Is {num} too high (enter h), too low (enter l), or correct (enter c)?")
                guess += 1
                
                if hint.lower() == 'c':
                    print("Oohoo! I found it.")
                    break
                elif hint.lower() == 'l':
                    start = num + 1
                    num = random.randint(start, end)
                elif hint.lower() == 'h':
                    end = num - 1
                    num = random.randint(start, end)
                else:
                    guess -= 1
            except:
                print("\nAre you messing with me here? Let's start from the beginning.")
                print("This time, think of a number before playing.\n")
                start, end = start0, end0
                guess = 0       
        break

    elif query.lower() == 'n':
        if wait < 2:
            print("I'm waiting.")
            wait += 1
        else:
            print("I'm still waiting.")
            

if guess <= 5:
    print(f"Number of guesses:{guess}")
    print("Either you made it so easy for me or I'm a pro at this.")
elif guess > 5 and guess < 15:
    print(f"Number of guesses:{guess}")
    print("That's not so bad. Patting myself on the back.")
elif guess > 15 and guess < 25:
    print(f"Number of guesses:{guess}")
    print("I did good right...right?")
else:
    print(f"Number of guesses:{guess}")
    print("Either you made it so challenging for me or I'm just a dumb machine.")