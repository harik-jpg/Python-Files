import random


#p > r, r > s, s > p
def play():
    game = 0
    player = 0
    comp = 0
    
    while game != 10:
        
        p1 = input("\nRock, Paper, or Scissor? ")
        p2 = random.choice(["rock", "paper", "scissor"])
        user = p1.lower()
        opponent = p2.lower()
        
    
        if user=='rock' or user=='paper' or user=='scissor':
            if (user=='rock' and opponent=='scissor') or (user=='paper' and opponent=='rock') or (user=='scissor' and opponent=='paper'):
                print("Computer chooses", opponent)
                print(user, "beats" , opponent,"\nYou take a point\n")
                player += 1
                game += 1

            elif (user == opponent):
                print("Computer chooses", opponent)
                print(user, "vs" , opponent,"\nIt's a tie\n")
                game += 1

            else:
                print("Computer chooses", opponent)
                print(opponent, "beats" , user,"\nComputer takes a point\n")
                comp += 1
                game += 1
                            
        else:
            print("Invalid input")
            
    
    if player > comp:
        print("\nYour score:", player, "\nComputer's score: ", comp)
        print("You won the match")
        
    elif player == comp:
        print("\nYour score:", player, "\nComputer's score: ", comp)
        print("The match is a tie")
        
    else:
        print("\nYour score:", player, "\nComputer's score: ", comp)
        print("You lost the match")
    



play()
while True:
    nxt_rnd = input("\nDo you wanna play again(y/n)?")
    if nxt_rnd.lower() == 'y':
        play()
    elif nxt_rnd.lower() == 'n':
        break
    else:
        print("Invalid input, try again")
        
print("Thank you for playing our game!")
