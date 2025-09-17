import copy

class Sudoku:
    def __init__(self, grid):
        self.grid = grid

    def __str__(self):
        return self.as_pretty_string()

    def as_pretty_string(self):
        lines = []
        for r in range(9):
            if r % 3 == 0 and r != 0:
                lines.append("-"*21)
            row = []
            for c in range(9):
                if c % 3 == 0 and c != 0:
                    row.append("|")
                val = self.grid[r][c]
                row.append(str(val) if val != 0 else ".")
            lines.append(" ".join(row))
        return "\n".join(lines)

    def find_empty(self):
        for r in range(9):
            for c in range(9):
                if self.grid[r][c] == 0:
                    return r, c
        return None

    def is_valid(self, r, c, val):
        for i in range(9):
            if self.grid[r][i] == val and i != c:
                return False
            if self.grid[i][c] == val and i != r:
                return False
        br, bc = (r//3)*3, (c//3)*3
        for i in range(br, br+3):
            for j in range(bc, bc+3):
                if self.grid[i][j] == val and (i, j) != (r, c):
                    return False
        return True

    def is_complete_and_valid(self):
        for r in range(9):
            for c in range(9):
                val = self.grid[r][c]
                if val == 0 or not self.is_valid(r, c, val):
                    return False
        return True


def solve_backtracking(board: Sudoku):
    empty = board.find_empty()
    if not empty:
        return True
    r, c = empty
    for val in range(1, 10):
        if board.is_valid(r, c, val):
            board.grid[r][c] = val
            if solve_backtracking(board):
                return True
            board.grid[r][c] = 0
    return False


def main():
    print("Enter your Sudoku puzzle row by row.")
    print("Use 0 for empty cells. Example row: 530070000")

    grid = []
    for i in range(9):
        while True:
            row = input(f"Row {i+1}: ")
            if len(row) == 9 and row.isdigit():
                grid.append([int(ch) for ch in row])
                break
            else:
                print("Invalid input. Enter exactly 9 digits (0-9).")

    sudoku = Sudoku(grid)
    print("\n--- Your Sudoku ---")
    print(sudoku)

    # Check if current Sudoku is already solved and valid
    if sudoku.is_complete_and_valid():
        print("\n✅ The Sudoku is already correctly solved!")
        return

    # Check if the given numbers violate Sudoku rules
    for r in range(9):
        for c in range(9):
            val = sudoku.grid[r][c]
            if val != 0 and not sudoku.is_valid(r, c, val):
                print(f"\n❌ Invalid Sudoku! Error at row {r+1}, col {c+1} (value {val})")
                return

    # Try solving
    print("\nSolving your Sudoku...")
    solved = Sudoku(copy.deepcopy(sudoku.grid))
    if solve_backtracking(solved):
        print("\n✅ Solved Sudoku:")
        print(solved)
    else:
        print("\n❌ This Sudoku cannot be solved!")


if __name__ == "__main__":
    main()

