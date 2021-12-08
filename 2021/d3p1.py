with open('./day3input.txt') as df:
    lines = df.readlines()
    counts = [0] * len(lines[0].strip())
    res = ''
    flip = ''
    for line in lines:
        for idx, val in enumerate(line.strip()):
            counts[idx] += int(val)
    for count in counts:
        if count < len(lines)/2:
            res+='0'
            flip+='1'
        else:
            res+='1'
            flip+='0'
    bres = int(res,2)
    bflip = int(flip,2)
    print(res,flip)
    print(bres, bflip, bres*bflip)