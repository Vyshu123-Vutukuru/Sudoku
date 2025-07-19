import random
from sudoku_solver import solve_sudoku, is_valid

def generate_sudoku(empty_cells=40):
    board = [[0 for _ in range(9)] for _ in range(9)]
    for _ in range(17):
        row, col = random.randint(0, 8), random.randint(0, 8)
        num = random.randint(1, 9)
        if board[row][col] == 0 and is_valid(board, row, col, num):
            board[row][col] = num
    solve_sudoku(board)
    cells = [(i, j) for i in range(9) for j in range(9)]
    random.shuffle(cells)
    for i in range(empty_cells):
        row, col = cells[i]
        board[row][col] = 0
    return board

def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))
