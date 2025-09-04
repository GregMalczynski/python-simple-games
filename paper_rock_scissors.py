from random import randint

GAME_DATA = ['paper', 'scissors', 'stone']
GAME_COUNTS = 4
COUNT_NUMBER = 0
PLAYER_WINS = 0
COMPUTER_WINS = 0

while COUNT_NUMBER < GAME_COUNTS:
    COUNT_NUMBER += 1

    computer_choice = randint(0, 2)
    
    print()
    player_choice = input('paper / scissors / stone ')

    match player_choice.lower():
        case 'paper':
            if computer_choice == 0:
                print('remis')
            elif computer_choice == 1:
                print(f'Computer wins! , Computer : {GAME_DATA[computer_choice]} , Player : {player_choice.lower()}')
                COMPUTER_WINS += 1
            elif computer_choice == 2:
                print(f'Player wins! , Computer : {GAME_DATA[computer_choice]} , Player : {player_choice.lower()}')
                PLAYER_WINS += 1
        case 'scissors':
            if computer_choice == 0:
                print(f'Player wins! , Computer : {GAME_DATA[computer_choice]} , Player : {player_choice.lower()}')
                PLAYER_WINS += 1
            elif computer_choice == 1:
                print('remis')
            elif computer_choice == 2:
                print(f'Computer wins! , Computer : {GAME_DATA[computer_choice]} , Player : {player_choice.lower()}')
                COMPUTER_WINS += 1
        case 'stone':
            if computer_choice == 0:
                print(f'Computer wins! , Computer : {GAME_DATA[computer_choice]} , Player : {player_choice.lower()}')
                COMPUTER_WINS += 1
            elif computer_choice == 1:
                print(f'Player wins! , Computer : {GAME_DATA[computer_choice]} , Player : {player_choice.lower()}')
                PLAYER_WINS += 1
            elif computer_choice == 2:
                print('remis')

print()
print(f'SUMMERY - Player Wins : {PLAYER_WINS} , Computer Wins : {COMPUTER_WINS} in {GAME_COUNTS} rounds')