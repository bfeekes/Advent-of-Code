input = open(r"C:\Users\bfeek\Pytest\Advent2022\Day3Input.txt","r")
total = 0

for line in input:
    half = int(len(line)/2)
    list1 = line[0:half]
    list2 = line[half:]
    for c in list1:
        if c in list2:
            print(c)
            if c.isupper():
                total += ord(c) - 38
            if c.islower():
                total += ord(c) - 96
            break

print(total)
