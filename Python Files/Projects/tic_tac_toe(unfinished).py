print("\n       TIC TAC TOE            ")
pos = [i for i in range(0, 9)]
demo = f"""
        {pos[0]} | {pos[1]} | {pos[2]}
        {pos[3]} | {pos[4]} | {pos[5]}
        {pos[6]} | {pos[7]} | {pos[8]}
       """
print(demo)

def player():
        user = int(input("Enter the position no where you want to mark the 'X':"))
        global pos
        pos = [" " for i in range(0, 9)]
        pos[user] = 'X'
        print(pos)
        demo = f"""
                | {pos[0]} | {pos[1]} | {pos[2]} |
                | {pos[3]} | {pos[4]} | {pos[5]} |
                | {pos[6]} | {pos[7]} | {pos[8]} |
                """
        print(demo)


player()
print(pos)
