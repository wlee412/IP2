# primeio.py
# !/usr/bin/python
"""
It reads and writes a list of hundred prime numbers as csv file using csv module.
"""

"""
__author__ = "William Lee"
__license__ = "GPL"
__version__ = "0.1"
__email__ = "wjlee@valodsta.edu"
__status__ = "complete"
"""
import csv


def write_primes(l, file_name):
    """

       This method writes a list of hundred prime integer numbers to file_name.
       It takes a list of prime numbers and converts it to a csv file.
       Args:
       l(list): list of 100 prime integer numbers
       file_name(str): This input the file name.

       Returns:
       It doesn't have return value because this void method.

       Raises:
       IOError: IO Error.

       Examples:
       >>> write_primes(l, 'name.csv')

    """
    try:
        p_writer = open(file_name, 'w')
        write_csv = csv.writer(p_writer)
        write_csv.writerow([l])

    except BaseException:
        print("Please input correct variable name Ex)file_name or l")

    finally:
        p_writer.close()


def read_primes(file_name):
    '''
           This method reads a csv file_name, it saved the prime numbers in the cvs file as a list,
           convert to string using .join with comma, return the string of the list.


           Args:
           num (int): Input integer numbers.

           Returns:
           list: 100 prime numbers as an integer.

           Raises:
           IOError: IO Error.

           Examples:
           >>> list = read_primes('list.txt')

        '''
    try:
        p_open = open(file_name, 'r')
        p_string = ", "
        return p_string.join(p_open)

    except BaseException:
        print('No data available')
