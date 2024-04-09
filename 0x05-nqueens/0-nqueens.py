#!/usr/bin/python3
""" This is a module that solves N queens puzzel """


import sys


def is_safe(board, row, col, N):
    """ This return True if condition are meet """
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_util(board, col, N, solutions):
    """ Base case: If all queens are placed then return true """

    if col >= N:
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return True

    # Consider this column and try placing this queen in all rows one by one
    for i in range(N):
        if is_safe(board, i, col, N):
            # Place this queen in board[i][col]
            board[i][col] = 1

            # Recur to place rest of the queens
            solve_nqueens_util(board, col + 1, N, solutions)

            # If placing queen in board[i][col] doesn't lead to a solution then
            # remove queen from board[i][col]
            board[i][col] = 0


def solve_nqueens(N):
    """ This function the resolve sultion """

    board = [[0] * N for _ in range(N)]
    solutions = []
    solve_nqueens_util(board, 0, N, solutions)
    return solutions


if __name__ == "__main__":
    # Check if the number of arguments is correct
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Check if N is a number
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is at least 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve N queens problem
    solutions = solve_nqueens(N)

    # Print solutions
    for solution in solutions:
        print(solution)
