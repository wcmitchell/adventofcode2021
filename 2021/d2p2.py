with open('./day2input.txt') as df:
    lines = df.readlines()
    loc = {"depth": 0, "distance": 0, "aim": 0}
    for line in lines:
        cmd, dist = line.split()
        dist = int(dist)
        if cmd == "up":
            loc["aim"] -= dist
        elif cmd == "down":
            loc["aim"] += dist
        elif cmd == "forward":
            loc["distance"] += dist
            loc["depth"] += dist*loc.get("aim")
        else:
            continue
    print(f'Position is: {loc}\nResult is: {loc.get("depth")*loc.get("distance")}')