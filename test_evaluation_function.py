from evaluation_function import evaluate

# test 1 checking if x won

def test_evaluation_x_win():
    board = 'xxo------xxo----xxx'
    assert evaluate(board) == 'x won'

# test 2 checking if o won
    
def test_evaluation_o_win():
    board = 'o--o--o---x------x-'
    assert evaluate(board) == 'o won'

# test 3 checking if the game ends up with draw
    
def test_evaluation_draw():
    board = 'ooxoxxoxooxxoxooxxo'
    assert evaluate(board) == '!'

# test 4 checking if the game goes on
    
def test_evaluation_keep_playing():
    board = 'o--o--o---x------x-'
    assert evaluate(board) == '-'

# test 5 checking if lenght of the board is 20 
    
def test_evaluation_keep_playing():
    board = 'o--o--o---x----x-'
    assert len(board) == 20