import numpy
import time
print(time.time)
print(numpy.arange(10))
for i in range(10):
    print(i)

while True:
    print("hello")
    time.sleep(1)


def dynamicProgramming(n):
    """
    A function that calculates the n-th Fibonacci number using dynamic programming.

    Parameters:
    n (int): The index of the Fibonacci sequence.

    Returns:
    int: The n-th Fibonacci number.
    """
    if n == 0:  # Base case: Fibonacci(0) = 0
        return 0
    elif n == 1:  # Base case: Fibonacci(1) = 1
        return 1
    else:  # Recursive case: Fibonacci(n) = Fibonacci(n-1) + Fibonacci(n-2)
        return dynamicProgramming(n - 1) + dynamicProgramming(n - 2)


def n_queen(n):
    """
    A function that solves the n-queens problem using backtracking.

    Parameters:
    n (int): The size of the chessboard.

    Returns:
    list: A list of lists representing the solutions to the n-queens problem.
    """
    board = [[0] * n for _ in range(n)]
