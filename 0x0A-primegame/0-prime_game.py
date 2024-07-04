#!/usr/bin/python3
"""Module that defines the isWinner function
"""


def isWinner(x, nums):
    """Checks for the winner between Ben and Maria"""
    if x < 1 or not nums:
        return None
    g_num = max(nums)

    m_map = [True for _ in range(max(g_num + 1, 2))]
    for i in range(2, int(pow(g_num, 0.5)) + 1):
        if not m_map[i]:
            continue
        for j in range(i * i, g_num + 1, i):
            m_map[j] = False

    m_map[0] = m_map[1] = False
    y = 0
    for i in range(len(m_map)):
        if m_map[i]:
            y += 1
        m_map[i] = y

    player1 = 0
    for x in nums:
        player1 += m_map[x] % 2 == 1
    if player1 * 2 == len(nums):
        return None
    if player1 * 2 > len(nums):
        return "Maria"
    return "Ben"
