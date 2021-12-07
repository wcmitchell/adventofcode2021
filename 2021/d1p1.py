last = None
inc = 0

with open('./day1input.txt') as df:
    sweeps = map(int, df.readlines())
    for curr in sweeps:
        if last:
            if curr > last:
                inc+=1
        last = curr
    print(f'Number of increments: {inc}')