board = str('-' * 20)

def evaluate(board):
    if 'xxx' in board:
        return 'x won'
    elif 'ooo' in board:
        return 'o won'
    elif '-' not in board:
        return '!'
    else:
        return '-'