input = open(r"C:\Users\bfeek\Pytest\Advent2022\Day2Input.txt","r")
score = 0
for line in input:
    elf, mine = line.split(" ")
    mine = mine.replace("\n", "")
    if mine == "X":
        score += 1
        if elf == "A":
            score += 3
        elif elf == "C":
            score += 6
    elif mine == "Y":
        score +=2
        if elf == "B":
            score += 3
        elif elf == "A":
            score += 6
    elif mine == "Z":
        score +=3
        if elf == "C":
            score += 3
        elif elf == "B":
            score += 6
    

print(score)