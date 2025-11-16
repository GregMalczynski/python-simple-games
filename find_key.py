from random import randint
import os

# Constans
COLORS = {
    'RED': '\033[91m',
    'YELLOW': '\033[43m',
    'END': '\033[0m'
}
BOARD_SIZE = (10, 10)
MOVES = {'w': (-1, 0), 's': (1, 0), 'a': (0, -1), 'd': (0, 1)}

# Pure functions
def create_game_state():
    # Initial game state
    return {
        'player_pos': (0, 0),
        'key_pos': (randint(0, BOARD_SIZE[0]-1), randint(0, BOARD_SIZE[1]-1)),
        'moves': 0,
        'wall_hit': False,
        'found_key': False
    }

def move_player(pos, direction, board_size):
    # Immutable move - return new position and state
    if direction not in MOVES:
        return pos, False, True  # pos, hit_wall, invalid_input
    
    dx, dy = MOVES[direction]
    new_x = max(0, min(pos[0] + dx, board_size[0] - 1))
    new_y = max(0, min(pos[1] + dy, board_size[1] - 1))
    hit_wall = (new_x, new_y) != (pos[0] + dx, pos[1] + dy)
    
    return (new_x, new_y), hit_wall, False

def render_board(state, board_size):
    # Board render
    lines = []
    for i in range(board_size[0]):
        row = ''
        for j in range(board_size[1]):
            if (i, j) == state['player_pos']:
                row += f"{COLORS['YELLOW']} P {COLORS['END']}"
            elif (i, j) == state['key_pos']:
                row += f"{COLORS['RED']} K {COLORS['END']}"
            else:
                row += ' + '
        lines.append(row)
    return '\n'.join(lines)

def render_ui(state):
    # Render UI
    output = [f"\n        Moves: {state['moves']}"]
    output.append(f"x: {state['player_pos'][0]}, y: {state['player_pos'][1]}")
    
    if state['wall_hit']:
        output.append('Wall Hit !!!')
    
    output.append('You can go w/a/s/d or q to quit')
    return '\n'.join(output)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Game Loop
def game_loop():
    state = create_game_state()
    
    while not state['found_key']:
        clear_screen()
        print(render_board(state, BOARD_SIZE))
        print(render_ui(state))
        
        move = input('\nWhere U want to go? ').lower()
        
        if move == 'q':
            print("Game quit!")
            return
        
        new_pos, hit_wall, invalid = move_player(
            state['player_pos'], move, BOARD_SIZE
        )
        
        if not invalid:
            state['player_pos'] = new_pos
            state['wall_hit'] = hit_wall
            state['moves'] += 1
            state['found_key'] = (new_pos == state['key_pos'])
    
    clear_screen()
    print(f"GAME END\nYou found the key in {state['moves']} moves!\n")

if __name__ == '__main__':
    game_loop()