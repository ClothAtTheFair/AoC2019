def elements(yikes):
    print(yikes)


if __name__ == "__main__":
    ele = []
    for item in open("day6.txt").read().split("\n"):
        ele.append(str(item))
        elements(ele)