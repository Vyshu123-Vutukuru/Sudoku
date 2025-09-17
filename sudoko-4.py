
import tkinter as tk

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

def on_validate(entry, r, c):
    """Validate input when user types a number."""
    val = entry.get()
    if not val.isdigit() or not (1 <= int(val) <= 9):
        entry.config(bg="red")
        return False

    grid[r][c] = int(val)
    if is_valid(grid, r, c, int(val)):
        # restore alternating 3x3 block background
        if (r//3 + c//3) % 2 == 0:
            entry.config(bg="white")
        else:
            entry.config(bg="#d0e7f9")
        return True
    else:
        entry.config(bg="red")
        return False

def draw_sudoku(window, puzzle):
    """Draw Sudoku grid with Entry boxes for empty cells."""
    for r in range(9):
        for c in range(9):
            val = puzzle[r][c]

            # Alternate colors for 3x3 blocks
            if (r//3 + c//3) % 2 == 0:
                bg = "white"
            else:
                bg = "#d0e7f9"

            if val != 0:
                # Pre-filled (locked)
                cell = tk.Label(
                    window, text=str(val), width=4, height=2,
                    font=("Arial", 18, "bold"),
                    relief="solid", borderwidth=1,
                    bg=bg
                )
                cell.grid(row=r, column=c, padx=1, pady=1, sticky="nsew")
            else:
                # Editable Entry
                entry = tk.Entry(
                    window, width=4, font=("Arial", 18, "bold"),
                    justify="center", relief="solid", borderwidth=1, bg=bg
                )
                entry.grid(row=r, column=c, padx=1, pady=1, sticky="nsew")
                entry.bind(
                    "<KeyRelease>",
                    lambda e, ent=entry, rr=r, cc=c: on_validate(ent, rr, cc)
                )

# keep a working grid
grid = [row[:] for row in puzzle]

# Create window
root = tk.Tk()
root.title("Interactive Sudoku")

draw_sudoku(root, puzzle)

# Resizable grid
for i in range(9):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
