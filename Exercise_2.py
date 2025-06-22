# S30 Problem #75 Word Search
#LeetCode #79 https://leetcode.com/problems/word-search/description/

# Author : Akaash Trivedi
# Time Complexity : O(m * n * 3^l) 3 -> directions to explore (exclude the direction we came from)
# Space Complexity : O(l) l -> length of the word in recursive stack
# Did this code successfully run on Leetcode :  Yes #
# Any problem you faced while coding this : No

# search the board for the 1st char in word, call dfs
# recursive call dfs on 4 directions and check if it matches next char in word
# if matches make as visited by replacing the char on the board with #
# after reaching the end of the word return true
# backtrack to restore original char and explore other paths to find rest of the word

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # direction array right, bottom, left, top
        direction = [(1,0),(0,-1),(-1,0),(0,1)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.dfs(board, word, 0, i, j, direction):
                        return True

        return False        

    # idx to track position of word
    def dfs(self, board, word, idx, r, c, direction) -> bool:
        #base
        # check if word is traversed
        if idx == len(word):
            return True
        if r < 0 or r == len(board) or c < 0 or c == len(board[0]) or board[r][c] == "#":
            return
        
        #logic
        if board[r][c] == word[idx]:
            # action
            # mark the word as visitied
            board[r][c] = "#"
            
            #recurse
            for dr in direction:
                nr = dr[0] + r
                nc = dr[1] + c
                # recurse
                if self.dfs(board, word, idx+1, nr, nc, direction):
                    return True

            # backtrack
            board[r][c] = word[idx]

        return False