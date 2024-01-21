def move(board, mark, position):
    updated_board = board[:position] + mark + board[position + 1: ]
    return updated_board