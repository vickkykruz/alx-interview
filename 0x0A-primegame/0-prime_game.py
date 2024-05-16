#!/usr/bin/python3
"""
Maria and Ben are playing a game. Given a set of consecutive integers starting
from 1 up to and including n, they take turns choosing a prime number from the
set and removing that number and its multiples from the set.
The player that cannot make a move loses the game.
"""


def is_prime(num):
    """ This is a function that return True if number is prime otherwise
        false
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def isWinner(x, nums):
    """ This function return the winner """
    def find_next_prime(remaining):
        """ This function return the prime number otherwise None """
        for num in remaining:
            if is_prime(num):
                return num
        return None

    def remove_multiples(prime, remaining):
        """ This function return the list of number if is not divisable
            by the prime number
        """
        return [num for num in remaining if num % prime != 0]

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        remaining_numbers = list(range(1, n + 1))
        maria_turn = True

        while True:
            next_prime = find_next_prime(remaining_numbers)
            if next_prime is None:
                break

            remaining_numbers = remove_multiples(next_prime, remaining_numbers)
            maria_turn = not maria_turn

        if maria_turn:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
