import numpy as np
import functools

def coords(directions):
    wires = []
    uhh = []
    x = 0
    y = 0
    result = None    
    length = 0
    for i in directions:
        oldpos = (x,y)
        temp = i[0]
        dist = int(i[1:])
    
        if temp == "R":
            x += dist
    
        elif temp == "L":
            x -= dist
    
        elif temp == "U":
            y += dist
        
        elif temp == "D":
            y -= dist

        man = abs(x) + abs(y)
        if result is None or result > man:
            result = man
        wires.append((oldpos, (x,y), man))
        length += dist
        uhh.append(man)

    
    print(man)
    return wires

    

def part1():
   print()

if __name__ == "__main__":
    directions = []
    for item in open("day31.txt").read().split(","):
        directions.append(str(item))
    coords(directions)

   
   
    #print(part1(directions))
    #print(part2(directions))
