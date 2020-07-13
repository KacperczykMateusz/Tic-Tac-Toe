cells = list(' ' * 9)


def field():
    print('-' * 9)
    print('|', ' '.join(cells[:3]), '|')
    print('|', ' '.join(cells[3:6]), '|')
    print('|', ' '.join(cells[6:]), '|')
    print('-' * 9)


while ' ' in cells:
    turn = 'X'
    field()
    x, y = input('Enter the coordinates: > ').split()
    if not (x.isdigit() or y.isdigit()):
        print('You should enter numbers!')
    elif not (1 <= int(x) <= 3 and 1 <= int(y) <= 3):
        print('Coordinates should be from 1 to 3!')
    elif cells[3 - (int(y)) * 3 + (int(x)) - 1] != ' ':
        print('This cell is occupied! Choose another one!')
    else:
        if turn == 'X':
            cells[(int(x)) - 1 + abs(int(y) - 3) * 3] = 'X'
            turn = 'O'
        elif turn == 'O':
            cells[(int(x)) - 1 + abs(int(y) - 3) * 3] = 'O'
            turn = 'X'
        # all possible ways to win
        lines = [cells[:3], cells[3:6], cells[6:], cells[0:9:3],
                 cells[1:9:3], cells[2:9:3], cells[0:9:4], cells[2:7:2]]
        if ['O', 'O', 'O'] in lines:
            print('O wins')
        elif ['X', 'X', 'X'] in lines:
            print('X wins')
        elif ' ' not in cells:
            print('Draw')
