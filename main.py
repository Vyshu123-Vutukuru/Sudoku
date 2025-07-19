from sudoku_solver import solve_sudoku
from sudoku_generator import generate_sudoku, print_board

def main():
    board = generate_sudoku()
    print("Generated Sudoku:")
    print_board(board)

    print("\nSolved Sudoku:")
    solve_sudoku(board)
    print_board(board)

if __name__ == "__main__":
    main()
