"""
BFS: since we have to find the minimum number of neighbours.
Since we have to traverse the matrix, any easy way would be flattening the matrix in 1D array.
Since the number on board starts with 1, add one extra 0 at the start of array for simplicity.
TC:O(n*n) all cells once, if snake bites we might go back but that would be constant number of times. SC: O(n*n)
Todo: without using 1D array
"""

from collections import deque


class Solution:
    def bfs(self, newboard, rows, cols):
        directions = [1, 2, 3, 4, 5, 6]
        q = deque()
        # add the index into the queue
        q.append(1)
        # mark it visited
        newboard[1] = -2
        while q:
            # get size of queue
            size = len(q)
            # for that given level
            for _ in range(size):
                # get the idx
                currIdx = q.popleft()
                # we can get 6 different values
                for d in directions:
                    # get newidx
                    newIdx = currIdx + d
                    # if we reach the last cell or the current cell has last cell index
                    if newIdx == rows * cols or newboard[newIdx] == rows * cols:
                        self.ans += 1
                        return
                    # check if it visited
                    if newboard[newIdx] != -2:
                        # check it value
                        if newboard[newIdx] == -1:
                            q.append(newIdx)
                        else:
                            q.append(newboard[newIdx])
                        # should be marked visited after appending to the queue
                        # since what if there is ladder on the visted cell
                        newboard[newIdx] = -2

            # increment moves once you finish the level
            self.ans += 1

        self.ans = -1

    def snakesAndLadders(self, board: List[List[int]]) -> int:
        newboard = []
        newboard.append(0)
        rows = len(board)
        cols = len(board[0])

        r = rows - 1
        c = 0
        flag = True
        # the board starts from the end
        while len(newboard) <= (rows * cols):
            if flag:
                newboard.append(board[r][c])
                c += 1

            if not flag:
                newboard.append(board[r][c])
                c -= 1

            if c >= cols:
                flag = False
                r -= 1
                c = cols - 1

            if c <= -1:
                flag = True
                r -= 1
                c = 0

        self.ans = 0
        self.bfs(newboard, rows, cols)
        return self.ans


