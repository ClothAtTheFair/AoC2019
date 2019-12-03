import numpy as np
import math
import sys

new = []


def mass(fuel):
    for f in fuel:
        temp = f
        while f > 0:
            f = (math.floor(f / 3)) - 2
            if f >= 0:
                new.append(f)
    print(np.sum(new))


if __name__ == "__main__":
    file1 = open("day1.txt", "r")
    numbers = np.loadtxt(file1)
    mass(numbers)
