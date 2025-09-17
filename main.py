import random
import copy

class Sudoku:
    def __init__(self, grid=None):
        if grid:
            self.grid = [row[:] for row in grid]
        else:
            self.grid = [[0]*9 for _ in range(9)]

    def copy(self):
        return Sudoku(self.grid)

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
            if self.grid[r][i] == val:
                return False
            if self.grid[i][c] == val:
                return False
        br = (r//3)*3
        bc = (c//3)*3
        for i in range(br, br+3):
            for j in range(bc, bc+3):
                if self.grid[i][j] == val:
                    return False
        return True


def solve_backtracking(board: Sudoku, limit_solutions=None):
    solutions = []

    def backtrack():
        if limit_solutions is not None and len(solutions) >= limit_solutions:
            return
        empty = board.find_empty()
        if not empty:
            solutions.append(copy.deepcopy(board.grid))
            return
        r, c = empty
        for val in range(1, 10):
            if board.is_valid(r, c, val):
                board.grid[r][c] = val
                backtrack()
                board.grid[r][c] = 0
                if limit_solutions is not None and len(solutions) >= limit_solutions:
                    return

    backtrack()
    if not solutions:
        return 0, None
    else:
        return len(solutions), Sudoku(solutions[0])


def generate_full_solution():
    board = Sudoku()
    numbers = list(range(1,10))

    def fill_cell(idx=0):
        if idx == 81:
            return True
        r, c = divmod(idx, 9)
        if board.grid[r][c] != 0:
            return fill_cell(idx+1)
        random.shuffle(numbers)
        for n in numbers:
            if board.is_valid(r, c, n):
                board.grid[r][c] = n
                if fill_cell(idx+1):
                    return True
                board.grid[r][c] = 0
        return False

    fill_cell(0)
    return board


def generate_puzzle(clues=30, max_tries=5000):
    full = generate_full_solution()
    puzzle = full.copy()

    positions = [(r, c) for r in range(9) for c in range(9)]
    random.shuffle(positions)

    removals = 81 - clues
    tries = 0
    for (r, c) in positions:
        if removals <= 0:
            break
        tries += 1
        if tries > max_tries:
            break
        backup = puzzle.grid[r][c]
        puzzle.grid[r][c] = 0

        count, _ = solve_backtracking(puzzle.copy(), limit_solutions=2)
        if count != 1:
            puzzle.grid[r][c] = backup
        else:
            removals -= 1

    return puzzle, full


def demo():
    print("Generating a Sudoku puzzle...")
    puzzle, solution = generate_puzzle(clues=30)
    print("\n--- Puzzle ---")
    print(puzzle)
    print("\n--- Solution ---")
    print(solution)


if __name__ == "__main__":
    demo()
