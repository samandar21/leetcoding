def solve_sudoku(board):
    def is_valid(row, col, num):
        for i in range(9):
            if board[row][i] == num or board[i][col] == num or board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == num:
                return False
        return True

    def solve():
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for num in '123456789':
                        if is_valid(i, j, num):
                            board[i][j] = num
                            if solve():
                                return True
                            board[i][j] = '.'
                    return False
        return True

    solve()


board = [
    ["9",".","5","4","8",".",".",".","3"],
    ["2","1",".",".",".","9","6","5","8"],
    [".",".",".",".","2","5",".",".","4"],
    [".","9","7",".","6",".",".",".","5"],
    [".",".","8",".",".",".","3",".","."],
    ["5",".",".",".","4",".","7","8","."],
    ["8",".",".","6","1",".",".",".","."],
    ["7","5","6","2",".",".",".","1","9"],
    ["1",".",".",".","9","8","4",".","7"]
]

solve_sudoku(board)

for row in board:
    print(row)
