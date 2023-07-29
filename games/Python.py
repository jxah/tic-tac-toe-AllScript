# print the game board

gameboard ='''  
{0}|{1}|{2}
---|---|---
{3}|{4}|{5} 
---|---|---
{6}|{7}|{8}
'''

gameMap = """  
 0 | 1 | 2 
---|---|---
 3 | 4 | 5 
---|---|---
 6 | 7 | 8 
"""

print("Welcome to tic-tac-toe.  Here is the placment game map:")
print(gameMap)

gameState = ['   ']*9
#print(gameState)
#gameState[0] = ' x '
print(gameboard.format(*tuple(gameState)))

while True: #game play loop
    invalid = 1
    while invalid == 1: #check input loop
        enterx = input("Enter space number for player X:")
        enterx = int(enterx)
        print(enterx," entered")
        if (gameState[enterx] == " X ") or (gameState[enterx] == " O ") : invalid = 1
        else : invalid = 0
    gameState[enterx] = " X "
    print(gameboard.format(*tuple(gameState)))
    invalid = 1
    while invalid == 1: #check input loop
        entero = input("enter space number for player O:")
        entero = int(entero)
        if gameState[entero] != "   " : invalid = 1
        else : invalid = 0
    gameState[entero] = " O "
    print(gameboard.format(*tuple(gameState)))
(done) = 0 
