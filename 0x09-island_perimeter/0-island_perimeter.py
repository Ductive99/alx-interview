#!/usr/bin/python3
"""
Module that defines the island_perimeter function
"""
def check_val(n):
    """Checks if a number is equal to 0
    """
    return 1 if n == 0 else 0

def island_perimeter(grid):
    """Island Perimeter function
    """

    row = len(grid)
    col = len(grid[0])
    assert (1 <= row and col <= 100), "grid length i between 1 and 100"

    x = 0
    for i in range(row):
        for j in range(col):
            assert (grid[i][j] == 0) or (grid[i][j] == 1),\
                                        "grid values must be either 0 or 1"
            if grid[i][j] == 1:
                if i-1 < 0:
                    x += 1
                else:
                    x += check_val(grid[i-1][j])
                if j-1 < 0:
                    x += 1
                else:
                    x += check_val(grid[i][j-1])

                try:
                    x += check_val(grid[i+1][j])
                except IndexError:
                    x += 1
                try:
                    x += check_val(grid[i][j+1])
                except IndexError:
                    x += 1

    return x
