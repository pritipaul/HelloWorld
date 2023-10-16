'''
Number Of Enclaves Problem
You are given an n x m binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.
A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.
Find the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.
Example:
Input:
grid[][] = {{0, 0, 0, 0},
            {1, 0, 1, 0},
            {0, 1, 1, 0},
            {0, 0, 0, 0}}
Output:
3
Explanation:
0 0 0 0
1 0 1 0
0 1 1 0
0 0 0 0
The highlighted cells represents the land cells.
'''
from typing import List

class Solution:    
    def numberOfEnclaves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        count = 0
        v = 0
        value = []
        for i in range(1,n-1):
            for j in range(1,m-1):
                if grid[i][j] == 1:
                    count += 1
                    v += 1
            value.append(v)
            v = 0

        for i in range(len(value)):
            if value[i]>1:
                return count
                break
        else:
            return 0
if _name_ == "_main_":
    for _ in range(int(input())):
        n, m = map(int,input().strip().split())
        grid = []
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])

        obj=Solution()
        print(obj.numberOfEnclaves(grid))
