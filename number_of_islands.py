'''
Problem 2 — Number of Islands
Medium
Graphs / Grid Traversal
30 minutes

Problem statement
You are given an m x n grid containing "1" (land) and "0" (water).

An island is a group of land cells connected horizontally or vertically. Diagonal connections do not count.

Your task is to return the number of distinct islands.

Constraints
- 1 <= m, n <= 300
- grid[r][c] is either "0" or "1".
- Islands connect horizontally and vertically, never diagonally.
'''


def num_islands(grid: list[list[str]]) -> int:
    rows = len(grid)
    columns = len(grid[0]) if rows > 0 else 0
    island_count = 0
    visited = set()

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= columns:
            return
        if grid[r][c] == "0" or (r, c) in visited:
            return
        
        visited.add((r, c))

        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)

    for row in range(rows):
        for cell in range(columns):
            if grid[row][cell] == "1" and (row, cell) not in visited:
                island_count += 1
                dfs(row, cell)
    return island_count


# Test 1: Single island
grid1 = [
    ["1", "1", "0"],
    ["1", "0", "0"],
    ["0", "0", "0"]
]
# Expected: 1

# Test 2: Multiple islands
grid2 = [
    ["1", "0", "1"],
    ["0", "0", "0"],
    ["1", "0", "1"]
]
# Expected: 4

# Test 3: All water
grid3 = [
    ["0", "0"],
    ["0", "0"]
]
# Expected: 0

# Test 4: One cell
grid4 = [["1"]]
# Expected: 1

print(num_islands(grid1))
print(num_islands(grid2))
print(num_islands(grid3))
print(num_islands(grid4))
