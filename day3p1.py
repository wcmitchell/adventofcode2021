from typing_extensions import Concatenate


with open('./day3input.txt') as df:
    lines = df.readlines()
    counts = [0] * len(lines[0].strip())
    res = ''
    for line in lines:
        for idx, val in enumerate(line.strip()):
            counts[idx] += int(val)
    for count in counts:
        if count < len(lines)/2:
            res+='0'
        else:
            res+='1'
    flip = ''.join('1' if x == '0' else '0' for x in res)
    bres = int(res,2)
    bflip = int(flip,2)
    print(res,flip)
    print(bres, bflip, bres*bflip)