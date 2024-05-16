#!/usr/bin/python3
"""
Maria and Ben are playing a game. Given a set of consecutive integers starting
from 1 up to and including n, they take turns choosing a prime number from the
set and removing that number and its multiples from the set.
The player that cannot make a move loses the game.
"""


def isWinner(x, nums):
    """This Prime Game returns the winner """
    if not nums or x < 1:
        return None
    n = max(nums)
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    sieve = [i for i, prime in enumerate(sieve) if prime]
    c = 0
    for n in nums:
        for i in range(len(sieve)):
            if sieve[i] > n:
                break
            c += 1
        if c % 2 == 0:
            return "Ben"
        else:
            return "Maria"
