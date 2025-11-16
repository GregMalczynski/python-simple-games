from random import choice

GAME_RULES = {
    'paper': 'stone', # paper > stone
    'scissors': 'paper', # scissors > paper
    'stone': 'scissors' # stone > scissors
}

def get_player_choice():
    # get and validate player choice
    while True:
        choice = input('paper / scissors / stone : ').lower().strip()
        if choice in GAME_RULES:
            return choice
        print('Wrong choice, try again.')

def determine_winner(player, computer):
    # who win round
    if player == computer:
        return 'draw'
    return 'player' if GAME_RULES[player] == computer else 'computer'

def play_game(rounds=4):
    # main function
    scores = {'player': 0 , 'computer': 0}

    for round_num in range(1, rounds + 1):
        print(f'\n Round : {round_num}')

        player = get_player_choice()
        computer = choice(list(GAME_RULES.keys()))

        result = determine_winner(player, computer)

        print(f'Computer : {computer}, Player : {player}')

        if result == 'draw':
            print('Draw!')
        else:
            scores[result] += 1
            print(f'{'You winning' if result == 'player' else 'Computer winning'}')
    
    print(f'\n Summary : Player {scores['player']} , Computer {scores['computer']}')

if __name__ == '__main__':
    play_game()