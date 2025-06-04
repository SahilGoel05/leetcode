class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        sqs = [set() for _ in range(9)]

        for row_num, row_vals in enumerate(board):
            for col_num, val in enumerate(row_vals):
                if val == '.':
                    continue
                sq_num = row_num // 3 * 3 + col_num // 3
                if val in rows[row_num] or val in cols[col_num] or val in sqs[sq_num]:
                    return False
                rows[row_num].add(val)
                cols[col_num].add(val)
                sqs[sq_num].add(val)
        
        return True

'''
TC: O(n^2)
SC: O(n^2)

Optimal Solution (bitmaskx):

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        squares = [0] * 9

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                val = int(board[r][c]) - 1
                if (1 << val) & rows[r]:
                    return False
                if (1 << val) & cols[c]:
                    return False
                if (1 << val) & squares[(r // 3) * 3 + (c // 3)]:
                    return False
                    
                rows[r] |= (1 << val)
                cols[c] |= (1 << val)
                squares[(r // 3) * 3 + (c // 3)] |= (1 << val)

        return True

TC: O(n^2)
SC: O(n)
'''

