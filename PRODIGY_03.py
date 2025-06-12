grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
def print_grid(arr):
    for row in arr:
        print(row)
def find_empty_location(arr):
    for i in range(9):
        for j in range(9):
            if arr[i][j] == 0:
                return (i, j)
    return None
def is_safe(arr, row, col, num):
    for x in range(9):
        if arr[row][x] == num:
            return False
    for x in range(9):
        if arr[x][col] == num:
            return False
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if arr[start_row + i][start_col + j] == num:
                return False
    return True
def solve_sudoku(arr):
    empty = find_empty_location(arr)
    if not empty:
        return True  # No empty location, Sudoku solved

    row, col = empty
    for num in range(1, 10):  # Try numbers 1 to 9
        if is_safe(arr, row, col, num):
            arr[row][col] = num  # Place num
            if solve_sudoku(arr):  # Recur with next empty cell
                return True
            arr[row][col] = 0  # Backtrack if needed
    return False  # Trigger backtracking
if solve_sudoku(grid):
    print_grid(grid)
else:
    print("No solution exists")
