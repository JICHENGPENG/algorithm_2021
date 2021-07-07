#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 18:36:54 2021

@author: apple

"""
#被围绕的区域
class Solution:
    def solve(self, board):
        if not board:
            return
        
        n, m = len(board), len(board[0])

        def dfs(x, y):
            if not 0 <= x < n or not 0 <= y < m or board[x][y] != 'O':
                return
            
            board[x][y] = "A"
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)
        
        for i in range(n):
            dfs(i, 0)
            dfs(i, m - 1)
        
        for i in range(m - 1):
            dfs(0, i)
            dfs(n - 1, i)
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == "A":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"

#课程表二
from collections import deque
class Solution2:
    def find_order(self, numCourses,prequisites):
        self.n = numCourses
        self.edge = [[] for each in range(numCourses)]
        self.inDeg = [0] * numCourses
        for pre in prequisites:
            ai,bi = pre[0],pre[1]
            self.addEdge(bi,ai)
        return self.topsort()
    def topsort(self):
        order = []
        q = deque()
        for i in range(self.n):
            if self.inDeg[i]==0:
                q.append(i)
        while len(q) > 0:
            x = q.popleft()
            order.append(x)
            for y in self.edge[x]:
                self.inDeg[y] -= 1
                if self.inDeg[y] == 0:
                    q.append(y)
        if len(order) == self.n:
            return order
        return[]
    def addEdge(self,u,v):
        self.edge[u].append(v)
        self.inDeg[v] += 1