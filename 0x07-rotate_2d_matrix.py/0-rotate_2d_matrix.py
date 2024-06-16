#!/usr/bin/python3
"""
This module provides a function to rotate a 2D matrix.

The function defined in this module rotates a given n x n matrix
90 degrees clockwise. The matrix is assumed to be 2D and non-empty.
"""


def rotate_2d_matrix(matrix) -> None:
    """Rotates the given n x n matrix 90 degrees clockwise in-place.

    Args:
        matrix (list of list of int): A 2D list representing an n x n matrix.
    """
    N = len(matrix)
    for row in range(int(N / 2)):
        for col in range(row, N - row - 1):
            temp = matrix[row][col]

            matrix[row][col] = matrix[N-1-col][row]

            matrix[N-1-col][row] = matrix[N-1-row][N-1-col]

            matrix[N-1-row][N-1-col] = matrix[col][N-1-row]

            matrix[col][N-1-row] = temp
