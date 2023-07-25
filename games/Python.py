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

while True:
    enterx = (input)
    entero = (input)
    if enterx == 1 : gameState[1] = " X "
(done) = 0 