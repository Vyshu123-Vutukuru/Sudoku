def print_sudoku(grid):
    """Print Sudoku in a visual box layout."""
    print("\n+-------+-------+-------+")
    for i in range(9):
        row = "| "
        for j in range(9):
            val = grid[i][j]
            row += str(val) if val != 0 else "."
            row += " "
            if (j + 1) % 3 == 0:
                row += "| "
        print(row)
        if (i + 1) % 3 == 0:
            print("+-------+-------+-------+")


def is_valid(grid, r, c, val):
    """Check if placing val at (r,c) is valid."""
    for i in range(9):
        if grid[r][i] == val and i != c:
            return False
        if grid[i][c] == val and i != r:
            return False
    br, bc = (r // 3) * 3, (c // 3) * 3
    for i in range(br, br + 3):
        for j in range(bc, bc + 3):
            if grid[i][j] == val and (i, j) != (r, c):
                return False
    return True


def check_sudoku(grid):
    """Check if Sudoku is completely valid."""
    for r in range(9):
        for c in range(9):
            val = grid[r][c]
            if val == 0 or not is_valid(grid, r, c, val):
                return False
    return True


def main():
    # Pre-filled puzzle (0 = empty)
    puzzle = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]

    print("🟦 Welcome to Sudoku! Fill in the missing numbers (1-9).")
    print("   Use 0 to keep empty.")
    print_sudoku(puzzle)

    # Ask user to fill missing values
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == 0:
                while True:
                    try:
                        val = int(input(f"Enter value for row {r+1}, col {c+1} (0-9): "))
                        if 0 <= val <= 9:
                            puzzle[r][c] = val
                            print_sudoku(puzzle)
                            break
                        else:
                            print("❌ Enter a number between 0 and 9.")
                    except ValueError:
                        print("❌ Invalid input, enter a number.")

    print("\nFinal Sudoku:")
    print_sudoku(puzzle)

    if check_sudoku(puzzle):
        print("✅ Congratulations! You filled the Sudoku correctly.")
    else:
        print("❌ The Sudoku has mistakes. Please check again.")


if __name__ == "__main__":
    main()
