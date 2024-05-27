from collections import defaultdict
class Solution(object):
    def isValidSudoku(self, board):
        rows=defaultdict(set)
        colms=defaultdict(set)
        sqt=defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c]=='.':continue
                elif board[r][c] in rows[r] or board[r][c] in colms[c] or board[r][c] in sqt[(r//3,c//3)]:return False
                rows[r].add(board[r][c])
                colms[c].add(board[r][c])
                sqt[(r//3,c//3)].add(board[r][c])
        return True
