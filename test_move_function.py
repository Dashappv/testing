from move_function import move 

# test checks if the mark is inserted at the specified position

def test_move_mark_inserted():
    board = 'xxo------xxo----xxx'
    position = 3
    mark = "o"

    updated_board = move(board, mark, position)

    assert updated_board == 'xxoo-----xxo----xxx'

# test checks that mark is not inserted if the position is already occupied

def test_move_position_occupied():
    board = 'o--o--o---x------x-'
    position = 0
    mark = "x"

    updated_board = move(board, mark, position)

    assert updated_board == 'o--o--o---x------x-'



""" 1.What is a Python module and how does it differ from a Python package?

    Python module can be observed as a separate file which contains code 
    that might be frequently used as a part of some bigger code. 
    It is created in order not to type the same part of the code multuple times.
    Package can contain multiple modules(=files) which are group in specific order depending on the project's needs.

2. What are side effects and give some examples.

    Side effect is something that can modify your result/outcome of the code without original intention for it. 
    This can be caused by wrong naming of variables, functions or, in case of testing, 
    executing the code when we only need to import it.

3. What are Exceptions and what to do if third-party code that we use throws them?

    Exceptions happen when an error or a wrong condition occurs in a code and it help us to overcome the it.
    There are some built-in exceptions in Python that prevent such logical errors like zero division and user can define 
    own exceptions that are checking for specific conditions or providing alternatives, if code throws an error. 

    To handle exceptions of a third-party, we can use the documentation that describes the exceptions (if such exists).
    Also, we can use try. Locationg a third-party code that throws an exception in try block, and using except to catch the error. 

4. Using which keywords can you create, throw and catch your new custom Exception?

    Custom exception can be craeted within a new class, where using methods we can describe what this exception should do.
    'Raise' will throw a custom exception after defining the condition for this exception.
    'Try' and 'except' blocks will catch our custom exceptions. In 'try' the code if executed and
    if the exception is caught 'except' block will print an error message.

5. Give examples of some benefits of testing?

    Providing a programm for clients which logic is based on rules of exernal party/company/regulator.
    Before releasing a version, test helps to check if all the changes were adopted correctly. Based on the 
    rules/requirements of this party, knowing how the outcome must look like, 
    we can test if the made changes are in line with them."""
