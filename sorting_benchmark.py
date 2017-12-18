#!/usr/bin/env python

"""
Some timing code to test timing of various sorting approaches.

Inspired by a discussion on python-ideas about adding a:

__sort_key__ dunder method

The idea is that some custom classes might want to be sortable, but not impliment __lt__.

In addition, providing a key function can improve the performance of sorting, particulary for cases where __lt__ is not very cheap.

However, making it a dunder method that the sorting routines would look for would mean that ALL sorting calls would require an extra method lookup for every item in the iterable, which could be a substantial (wasted) performance impact if it isn't there.

This is particularly true for sequences of smple buildit types, like int and float, as they are very fast to compare. In fact, the reason adding a key function can improve sorting performance, is that it reduces the number of methods calls to O(n), and leaves what is often a very fast compare for basic types to O(n log(n)).

But when you have a basic type already, then adding a sort key adds O(n) function calls, while keeping the final O(n log(n)) compares the same.

Here are some benchmarks to see the impact of all of this:
"""

import timeit
import random

# A constant for how long lists we should work with:
N = 10000
NT = 1000 # number of timer runs to make

class MyTimer(timeit.Timer):

    long_list = [random.random() for i in range(10000)]

    def __init__(self, stmt):
        super().__init__(stmt=stmt,
                         globals=dict(self.__class__.__dict__),
                         )

    def time(self):
        for _ in range(3):
            num_calls, tot_time = self.autorange()
            print("time result is: {} seconds".format(tot_time / num_calls))

    @staticmethod
    def secs_formatter(secs):
        """
        converts seconds to milli, micro or nano seconds and
        returns a nice string
        """
        if secs < 1e-7:
            return "{:.3f} ns".format(secs * 1e9)
        elif secs < 1e-4:
            return "{:.3f} \u00B5s".format(secs * 1e6)
        elif secs < 1e-1:
            return "{:.3f} ms".format(secs * 1e3)
        else:
            return "{:.3f} s".format(secs)


# ## sorting lists of basic built in types:

# long_list = [random.random() for i in range(10000)]

# basic_sort_float = timeit.timeit('sorted(long_list)', globals=locals(), number=NT)

# key_sort_float = timeit.timeit('sorted(long_list)', globals=locals(), number=NT)

res = MyTimer('sorted(long_list)').time()



# print("basic sort: key sort", basic_sort_float, key_sort_float)




