# Simple Game *** FIND KEY ***

# Imports
from random import randint
from math import sqrt

# Declare game data

GAME_WIDTH = 10
GAME_HEIGHT = 10

key_x = randint(0, GAME_WIDTH)
key_y = randint(0, GAME_HEIGHT)

player_x = 0
player_y = 0

player_found_key = False

moves = 0
distance_before_move = sqrt((key_x - player_x) ** 2 + (key_y - player_y) ** 2 )

while not player_found_key:
    moves += 1
    print()
    print('You can go w/a/s/d')

    move = input('Where U ant to go ?')

    match move.lower():
        case 'w':
            player_x += 1
            if player_x > GAME_HEIGHT:
                print('Wall hit!!!')
                player_x = GAME_HEIGHT
        case 's':
            player_x -= 1
            if player_x < 0:
                print('Wall hit!!!')
                player_x = 0
        case 'a':
            player_y -= 1
            if player_y < 0:
                print('Wall hit!!!')
                player_y = 0
        case 'd':
            player_y += 1
            if player_y > GAME_WIDTH:
                print('Wall hit!!!')
                player_y = GAME_WIDTH
        case 'q':
            print('Quit game')
            quit()
        case '_':
            print('I dont know where U want to go')
            continue

    if player_x == key_x and player_y == key_y:
        print(f'Congratulations, U found key in {moves} times!')
        quit()

    distance_after_move = sqrt((key_x - player_x) ** 2 + (key_y - player_y) ** 2 )
    if distance_before_move > distance_after_move:
        print('You are nearer')
    else:
        print('You are moving away')

    distance_before_move = distance_after_move

    print(f'Your current position is x : {player_x} , y : {player_y}')