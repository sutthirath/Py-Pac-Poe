#### Py Pac Poe ###


## Variables

A1 = ""
A2 = ""
A3 = ""
B1 = ""
B2 = ""
B3 = ""
C1 = ""
C2 = ""
C3 = ""

# # welcome message at start
print("-------------------------- \n  Let's play Py-Pac-Poe!\n--------------------------")

# # Show board before making first move
print("""
         A   B   C 

     1)    |   |   
        -----------
     2)    |   |  
        -----------
     3)    |   |  
                    """)

## Functions

# Gameboard
def gameplay():
    print(f"     A    B    C \n\n 1)  {A1}  | {A2}  | {A3} \n    -------------\n 2)  {B1}  | {B2}  | {B3} \n    -------------\n 3)  {C1}  | {C2}  | {C3}")

# Player X's move
def x_turn():
    x_move = input("Player X's please make a move: ")
    if x_move == "A1":
        global A1
        A1 = "X"
        gameplay()
        return A1
    elif x_move == "A2":
        global A2
        A2 = "X"
        gameplay()
        return A2
    elif x_move == "A3":
        global A3
        A3 = "X"
        gameplay()
        return A3
    elif x_move == "B1":
        global B1
        B1 = "X"
        gameplay()
        return B1
    elif x_move == "B2":
        global B2
        B2 = "X"
        gameplay()
        return B2
    elif x_move == "B3":
        global B3
        B3 = "X"
        gameplay()
        return B3
    elif x_move == "C1":
        global C1
        C1 = "X"
        gameplay()
        return C1
    elif x_move == "C2":
        global C2
        C2 = "X"
        gameplay()
        return C2
    elif x_move == "C3":
        global C3
        C3 = "X"
        gameplay()
        return C3
    else:
        print("Please enter a valid coordinate")

# Player O's move
def o_turn():
    o_move = input("Player Y's please make a move: ")
    if o_move == "A1":
        global A1
        A1 = "O"
        gameplay()
        return A1
    elif o_move == "A2":
        global A2
        A2 = "O"
        gameplay()
        return A2
    elif o_move == "A3":
        global A3
        A3 = "O"
        gameplay()
        return A3
    elif o_move == "B1":
        global B1
        B1 = "O"
        gameplay()
        return B1
    elif o_move == "B2":
        global B2
        B2 = "O"
        gameplay()
        return B2
    elif o_move == "B3":
        global B3
        B3 = "O"
        gameplay()
        return B3
    elif o_move == "C1":
        global C1
        C1 = "O"
        gameplay()
        return C1
    elif o_move == "C2":
        global C2
        C2 = "O"
        gameplay()
        return C2
    elif o_move == "C3":
        global C3
        C3 = "O"
        gameplay()
        return C3
    else:
        print("Please enter a valid coordinate")

# Game loop
while A1 == "" or A2 == "" or A3 == "" or B1 == "" or B2 == "" or B3 == "" or C1 == "" or C2 == "" or C3 == "":
    x = 0
    y = 0
    if (x_turn):
        x += 1
    elif (o_turn):
        y -= 1
    else:
        break
    x_turn
    o_turn



# # Check for win
# def check():
#     if     



# print([[row [i] for row in game] for i in range(3)])

# for i1, inner_game in enumerate(game):
#     for i2, item in enumerate(inner_game):
#         print i1, i2, item, game[i1][i2]



