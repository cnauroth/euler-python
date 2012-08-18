#!/usr/bin/python

import operator
import os.path
import re
import sys

def __print_usage():
    '''prints usage information'''
    print """Project Euler - Problem 1

http://projecteuler.net/

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get
3, 5, 6 and 9. The sum of these multiples is 23.  Find the sum of all the
multiples of 3 or 5 below 1000.

Answer: 233168

Usage:
    %(file)s [max_exclusive [factor*]]

    max_exclusive - maximum number to include in the sum, exclusive, default
        1000
    factor* - any number of factors for which multiples will be included in the
        sum, default 3 5

    The command accepts any number of positive integer arguments.  The first, if
    provided, is interpreted as maxExclusive.  All others, if provided, are
    interpreted as factors.

Examples:
    %(file)s
    233168

    %(file)s 1000
    233168

    %(file)s 1000 3 5
    233168

    %(file)s 10 3 5
    23""" % { 'file': os.path.basename(__file__) }

FACTORS_DEFAULT = [3, 5]
MAX_EXCLUSIVE_DEFAULT = 1000

invalid_args = filter(lambda arg: not re.match('^\d+$', arg), sys.argv[1:])

if invalid_args:
    __print_usage()
    sys.exit()

int_args = map(lambda arg: int(arg, 10), sys.argv[1:])
max_exclusive = int_args[0] if len(int_args) > 0 else MAX_EXCLUSIVE_DEFAULT
factors = int_args[1:] if len(int_args) > 1 else FACTORS_DEFAULT

ranges = map(lambda factor: range(factor, max_exclusive, factor), factors)
factor_set = set()

for range in ranges:
    factor_set.update(range)

sum = reduce(operator.add, factor_set)
print sum
