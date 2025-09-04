from random import randint
import os

CRED = '\033[91m'
CYEL = '\033[43m'
CEND = '\033[0m'

X_SIZE = 10
Y_SIZE = 10

x_key = randint(0, X_SIZE)
y_key = randint(0, Y_SIZE)

x_player = 0
y_player = 0

player_found_key = False

moves = 0

array = [
    [' + ', ' + ', ' + ', ' + ', ' + ', ' + ', ' + ', ' + ', ' + ', ' + '],
    [' + ', ' + ', ' + ', ' + ', ' + ', ' + ', ' + ', ' + ', ' + ', ' + '],
    [' + ', ' + ', ' + ', ' + ', ' + ', ' + ', ' + ', ' + ', ' + ', ' + '],
    [' + ', ' + ', ' + ', ' + ', ' + ', ' + ', ' + ', ' + ', ' + ', ' + '],
    [' + ', ' + ', ' + ', ' + ', ' + ', ' + ', ' + ', ' + ', ' + ', ' + '],
    [' + ', ' + ', ' + ', ' + ', ' + ', ' + ', ' + ', ' + ', ' + ', ' + '],
    [' + ', ' + ', ' + ', ' + ', ' + ', ' + ', ' + ', ' + ', ' + ', ' + '],
    [' + ', ' + ', ' + ', ' + ', ' + ', ' + ', ' + ', ' + ', ' + ', ' + '],
    [' + ', ' + ', ' + ', ' + ', ' + ', ' + ', ' + ', ' + ', ' + ', ' + '],
    [' + ', ' + ', ' + ', ' + ', ' + ', ' + ', ' + ', ' + ', ' + ', ' + '],
]

while not player_found_key:
    os.system('cls')

    for i in range(0, X_SIZE):
        for j in range(0, Y_SIZE):
            
            player_position = f'{x_player}{y_player}'
            if i == x_player and j == y_player:
                print(CYEL + ' P ', end='' + CEND)
            elif i == x_key and j == y_key:
                print(CRED + ' K ', end='' + CEND)
            else:
                print(array[i][j], end='')
        print()

    print()
    print(f'        Moves: {moves}')
    print(f'x : {x_player}, y : {y_player}')
    print('You can go w/a/s/d')
    move = input('Where U ant to go ?')
    match move.lower():
        case 'w':
            x_player -= 1
            if x_player < 0:
                print('Wall hit!!!')
                x_player = 0
        case 's':
            x_player += 1
            if x_player > X_SIZE - 1:
                print('Wall hit!!!')
                x_player = X_SIZE - 1
        case 'a':
            y_player -= 1
            if y_player < 0:
                print('Wall hit!!!')
                y_player = 0
        case 'd':
            y_player += 1
            if y_player > Y_SIZE - 1:
                print('Wall hit!!!')
                y_player = Y_SIZE - 1
    
    if x_player == x_key and y_player == y_key:
        player_found_key = True
        os.system('cls')
        print(f'GAME END\nYou found the key!\n')

    moves += 1