#!/usr/bin/env python3
import random
import time

random.seed(hash('Testing Keys'))

lt_calls = 0
key_calls = 0
outer_key_calls = 0


def outer_key(item):
#    global outer_key_calls
#    outer_key_calls += 1
    return item.key()


class MyObject:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def __lt__(self, other):
        global lt_calls
        lt_calls += 1

        if self.value1 < other.value1:
            return True
        else:
            return self.value2 < other.value2

    def key(self):
        global key_calls
        key_calls += 1

        return self.value1, self.value2

    # def __lt__(self, other):
    #     global lt_calls
    #     lt_calls += 1

    #     return self.value1 < other.value1

    # def key(self):
    #     global key_calls
    #     key_calls += 1

    #     return self.value1


lt_list = [MyObject(value1, value1 - 50) for value1 in reversed(range(1000))]
random.shuffle(lt_list)

key_list = lt_list[:]
outer_key_list = lt_list[:]


print("Using a length: {} list".format(len(lt_list)))

s = time.time()
key_list.sort(key=MyObject.key)
ek = time.time() - s
print('key       %.6fs %6d calls' % (ek, key_calls))


s = time.time()
outer_key_list.sort(key=outer_key)
eok = time.time() - s
print('outer_key %.6fs %6d calls' % (eok, outer_key_calls))


s = time.time()
lt_list.sort()
elt = time.time() - s
print('lt        %.6fs %6d calls' % (elt, lt_calls))

print("time ratio:", elt / eok)

