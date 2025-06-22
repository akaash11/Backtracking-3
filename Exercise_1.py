# S30 Problem #74 N Queens
#LeetCode #51 https://leetcode.com/problems/n-queens/description/

# Author : Akaash Trivedi
# Time Complexity : O(N!) N factorial
# Space Complexity : O(N^2)
# Did this code successfully run on Leetcode :  Yes #
# Any problem you faced while coding this : No

# for loop based recursion with backtracking
# check if its safe to put the queen at [row][col] on board
# checking columns up, diagonally left, diagonally right till in-bound of the board
# construct the board with string builder patter and create a list of position of Q
# backtrack to unmarking the q and explore other positions on in that row

class Solution:
    def __init__(self):
        self.result = []

    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [[False for _ in range(n)] for _ in range(n)]
        self.helper(board,0)
        return self.result

    def helper(self, board, row):
        #base
        if row == len(board):
            # process board and create list
            li = []
            for i in range(len(board)):
                # building string in loop using string builder pattern
                # as string are immutable, creating repeated memory allocation
                rowBuilder = []
                for j in range(len(board)):
                    if board[i][j]:
                        rowBuilder.append("Q")
                    else:
                        rowBuilder.append(".")
                st = "".join(rowBuilder)
                li.append(st)
            self.result.append(li)
            return

        #logic
        # iterate over all children of curr row
        for col in range(len(board)):
            # check if its safe to put the queen
            if self.isSafe(board, row, col):
                # action - mark for queens position
                board[row][col] = True

                # recurse for next row
                self.helper(board, row+1)

                # backtrack - unmark the last row to explore other options
                board[row][col] = False

    # check if its safe to put queen at position [row][col]
    def isSafe(self, board, row, col) -> bool:
        # Check up column i -1
        for i in range(row):
            # check all the column in that row
            if board[i][col]:
                return False
        # check up diagonal left i-1, j-1
        i = row
        j = col
        while i >= 0 and j >=0:
            #if queen present return false
            if board[i][j]:
                return False
            i -=1
            j -=1

        # check up diagonal right i-1, j+1
        i = row
        j = col
        while i >= 0 and j < len(board):
            #if queen present return false
            if board[i][j]:
                return False
            i -=1
            j +=1
        return True