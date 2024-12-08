"""
BFS: TC: O(m*n) and SC: O(m*n)

Todo: DFS
"""

from collections import deque
from typing import List


class Solution_without_extra_space:
    def bfs(self, board, click):
        x = click[0]
        y = click[1]
        if board[x][y] == 'M':
            board[x][y] = 'X'
            return board
        dir = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)]
        q = deque()
        q.append(click)
        board[x][y] = 'B'
        print(board)
        while q:
            # pop the from queue
            curr = q.popleft()
            flag = False
            num_mines = 0
            x = curr[0]
            y = curr[1]
            for d in dir:
                newx = d[0] + curr[0]
                newy = d[1] + curr[1]
                if newx >= 0 and newx < len(board) and newy >= 0 and newy < len(board[0]):
                    if board[newx][newy] == "M":
                        num_mines += 1
                        flag = True

            if flag:
                board[x][y] = str(num_mines)

            else:
                for d in dir:
                    newx = d[0] + curr[0]
                    newy = d[1] + curr[1]
                    if newx >= 0 and newx < len(board) and newy >= 0 and newy < len(board[0]):
                        if board[newx][newy] == 'E':
                            board[newx][newy] = 'B'
                            q.append((newx, newy))

        return board

    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        visited = set()
        return self.bfs(board, (click[0], click[1]))


class Solution_with_extra_space:
    def bfs(self, board, click, visited):
        x = click[0]
        y = click[1]
        # check if the users have clicked on the mine, if yes update value and return board
        if board[x][y] == 'M':
            board[x][y] = 'X'
            return board

        # traverse in all 8 directions
        dir = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)]
        q = deque()
        q.append(click)

        while q:
            # pop the form queue
            curr = q.popleft()
            if curr not in visited:
                x = curr[0]
                y = curr[1]
                visited.add(curr)
                num_mines = 0
                flag = False
                # check if any of the neighbors is mine
                for d in dir:
                    newx = d[0] + curr[0]
                    newy = d[1] + curr[1]
                    if newx >=0 and newx <len(board) and newy >=0 and newy < len(board[0]):
                        if board[newx][newy] == "M":
                            num_mines += 1
                            flag = True
                # if any of the neighbor is not mine then add the neighbors to the queue
                if not flag:
                    for d in dir:
                        newx = d[0] + curr[0]
                        newy = d[1] + curr[1]
                        if newx >=0 and newx <len(board) and newy >=0 and newy < len(board[0]):
                            q.append((newx, newy))
            # upadate the value of baord
            if flag:
                board[x][y] = str(num_mines)
            else:
                board[x][y] = 'B'

        return board

    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        visited = set()
        return self.bfs(board, (click[0], click[1]), visited)

obj = Solution()
ans = obj.updateBoard(
    [["B", "1", "E", "1", "B"], ["B", "1", "M", "1", "B"], ["B", "1", "1", "1", "B"], ["B", "B", "B", "B", "B"]],
    [1, 2])
print(ans)
