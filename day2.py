import numpy as np


def part1(data):
    instructions = data[:]
    instructions[1] = 12
    instructions[2] = 2
    return computer(instructions)


def computer(instructions):
    ugh = 0

    while True:

        op = instructions[int(ugh)]
        input1 = instructions[ instructions[int(ugh+1)] ]
        input2 = instructions[ instructions[int(ugh+2)] ]
        output = instructions[ugh+3]

        if op == 99:
            break
        elif op == 1:
            instructions[output] = input1 + input2

        elif op == 2:
            instructions[output] = input1 * input2
        ugh += 4

    return instructions[0]


def part2(data):
    results = []
    for x in range(100):
        for y in range(100):
            instructions = data[:]
            instructions[1], instructions[2] = x, y
            r = computer(instructions)
            results.append((100*x+y, r))
    ans = [z for z in results if z[1] == 19690720]
    return ans


if __name__ == "__main__":
    numbers = []
    for item in open("day2.csv").read().split(","):
        numbers.append(int(item))
    print(part1(numbers))
    print(part2(numbers))
