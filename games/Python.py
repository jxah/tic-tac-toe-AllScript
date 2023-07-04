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

print("Welcome to tic-tac-toe.  Here is the game map:")
print(gameMap)

gameState = ['   ']*9
gameState[0] = ' x '
print(gameboard.format(*tuple(gameState)))

while True:
    enterx = (input)
    entero = (input)
    if (done): break