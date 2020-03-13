# primemodule.py
# !/usr/bin/python

"""
This class finds 100 prime numbers using an algorithm and returns the found numbers.
"""

"""
__author__ = "William Lee"
__license__ = "GPL"
__version__ = "0.1"
__email__ = "wjlee@valodsta.edu"
__status__ = "complete"
"""


def isPrime(n):
    """
    I used the Eratosthenes sieve algorithm in the formula for determining prime numbers.
    To find primes less than N, we just delete the multiples of primes greater than or equal to 2 and less than root N.

    Args:
    is_prime(int):  integer numbers to n
    Returns: It doesn't return anything
    Boolean: It returns True, if the algorithm found the prime number.
    Raises:  IO Error.
    Examples:
    >>> if is_prime(6);

    """
    if n <= 1:
        return False

    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def getNPrime(num):
    '''
    This method uses the 'is_prime' method to determine the prime number, and stores and returns 100 filtered numbers
    in the list.

    Args:
    num (int): Input integer numbers.

    Returns:
    list: 100 prime numbers as an integer.

    Raises:
    IOError: IO Error.

    Examples:
    >>> list = read_primes('output.csv')

    '''

    p_list = []
    s_num = 2
    cnt = 0
    while cnt < num:
        if isPrime(s_num):
            p_list.append(s_num)
            cnt = cnt + 1
        s_num = s_num + 1
    return p_list
