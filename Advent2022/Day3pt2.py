import re

input = open(r"C:\Users\bfeek\Pytest\Advent2022\Day3Input.txt","r")
total = 0

list = re.findall(r"(.+\n.+\n.+\n)",input.read())
for element in list:
    line1, line2, line3, line4 = element.split("\n")
    for c in line1: 
        if c in line2: 
            if c in line3:
                if c.isupper():
                  total += ord(c) - 38
                if c.islower():
                  total += ord(c) - 96
                break

print(total)