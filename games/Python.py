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
playerX = input("What is playerX's name? (optional)")
playerO = input("What is playerO's name? (optional)")
print("Welcome to tic-tac-toe", playerX,".  Here is the placment game map:")
print(gameMap)
done = 0

gameState = ['   ']*9
#gameState[0] = ' x '
print(gameboard.format(*tuple(gameState)))

while done == 0: #game play loop
    invalid = 0
    enterx = int(input("Enter space number for " + playerX + ":"))
    print(enterx," entered")
    if (gameState[enterx] == " X ") or (gameState[enterx] == " O ") : invalid = 1
    else : invalid = 0
    while invalid == 1: 
        print('Sorry, that space is already taken')
        enterx = int(input("Enter space number for " + playerX + ":"))
        print(enterx," entered")
        if (gameState[enterx] == " X ") or (gameState[enterx] == " O ") : invalid = 1
        else : invalid = 0
    gameState[enterx] = " X "
    print(gameboard.format(*tuple(gameState)))
    entero = int(input("Enter space number for " + playerO + ":"))
    if gameState[entero] != "   " : invalid = 1
    else : invalid = 0
    while invalid == 1: 
        print('Sorry, that space is already taken')
        entero = int(input("Enter space number for " + playerO + ":"))
        if gameState[entero] != "   " : invalid = 1
        else : invalid = 0
    gameState[entero] = " O "
    print(gameboard.format(*tuple(gameState)))
    #print(gameState)
done = 0 

while True:
    #if gameState : ['X'],['X'],['X'],['X' or 'O']*6 or ['X' or 'O']*3,['X'],['X'],['X'],['X' or 'O']*3 or ['X' or 'O']*6,['X'],['X'],['X']:
    if done == 1:
        print("X wins")
    if done == 2:
        print("O WINS")