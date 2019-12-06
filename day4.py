from re import finditer

def has_doubles(f):
    return len(set(str(f))) < len(str(f))

def has_exact_doubles(forever: str) -> bool:
    return any(len(match.group(0)) == 2 for match in finditer(r'(\d)\1+', forever))

def is_increasing(forever: str) -> bool:
    return ''.join(sorted(forever)) == forever

def part1(yikes):
    forever = []
    passwords = []
    
    for y in yikes:
        if has_doubles(y):
            forever.append(str(y))
    for f in forever:
        if is_increasing(f):
            passwords.append(f)
    print(len(passwords))
    



def part2(yikes):
    forever = []
    passwords = []
    
    for y in yikes:
        if is_increasing(str(y)) and has_exact_doubles(str(y)):
            passwords.append(y)
    print(len(passwords))






if __name__ == "__main__":
    potNums = list(range(382345,843167))
    part1(potNums)
    part2(potNums)