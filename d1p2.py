from itertools import tee

def window(iterable, size):
    iters = tee(iterable, size)
    for i in range(1, size):
        for each in iters[i:]:
            next(each, None)
    return zip(*iters)

with open('./day1input.txt') as df:
    last = None
    inc = 0
    entries = map(int, df)
    winders = window(entries, 3)
    for curr in winders:
        if last:
            if sum(curr) > sum(last):
                inc += 1
        last = curr
    print(f'Window increases: {inc}')