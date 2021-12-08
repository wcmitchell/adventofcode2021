from collections import Counter

def rec_list(list, index):
    curr = Counter([entry[index] for entry in list])
    if curr.get('0') == curr.get('1'):
        return '1'
    else: 
        return curr.most_common(1)[0][0]

with open('./day3input.txt') as df:
    lines = df.readlines()
    lines = [x.strip() for x in lines]
    lines.sort()

    o2_vals = co2_vals = lines

    for idx in range(len(lines[0])):
        if len(o2_vals) > 1:
            o2_check = rec_list(o2_vals, idx)
            o2_vals = [line for line in o2_vals if line[idx] == o2_check]
        else:
            continue
        if len(co2_vals) > 1:
            co2_check = rec_list(co2_vals, idx)
            co2_vals = [line for line in co2_vals if not line[idx] == co2_check]
        else:
            continue

    print(f' O2 Value: {int(o2_vals[0], 2)}\nCO2 Value: {int(co2_vals[0], 2)}\nResult: {int(o2_vals[0], 2) * int(co2_vals[0], 2)}')
