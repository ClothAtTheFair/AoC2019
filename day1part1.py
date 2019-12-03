import numpy as np
import math
import sys

new = []


def mass(fuel):
    for f in fuel:
        temp = (math.floor(f / 3)) - 2
        new.append(temp)
    print(np.sum(new))


if __name__ == "__main__":
    file1 = open("day1.txt", "r")
    numbers = np.loadtxt(file1)
    mass(numbers)

