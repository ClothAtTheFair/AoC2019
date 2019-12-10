def process(instruc):
    curr = [0,0]
    for i in instruc.split(','):
        for _ in range(int(i[1:])):
            curr[0 if i[0] in ('L', 'R') else 1] += -1 if i[0] in ('L', 'D') else 1
            yield tuple(curr)
with open('day3.txt', 'r') as f:
    wires = [list(process(line)) for line in f.readlines()]
intersections = set(wires[0]) & set(wires[1])
print(min(abs(x) + abs(y) for (x,y) in intersections))
print(2+ min(sum(wire.index(intersect) for wire in wires) for intersect in intersections))