input = open(r"C:\Users\bfeek\Pytest\Advent2022\Day1Input.txt","r")
count = 0
first = 0
second = 0
third = 0
for line in input:
    if line == "\n":
        if count > first: 
            third = second
            second = first
            first = count
        elif count > second:
            third = second
            second = count
        elif count > third:
            third = count
        count = 0
    elif line != "\n":
        count += int(line)

print("Top 3 is", first, second, third)
print("Count from Top 3 is", first + second + third)

