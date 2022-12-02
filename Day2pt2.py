input = open(r"C:\Users\bfeek\Pytest\Advent2022\Day2Input.txt","r")
score = 0
for line in input:
    elf, result = line.split(" ")
    result = result.replace("\n", "")
    #Winner Scenario
    if result == "Z":
        score += 6
        if elf == "A":
            score += 2
        elif elf == "B":
            score += 3
        else:
            score += 1
    #Draw Scenario
    elif result == "Y":
        score += 3
        if elf == "A":
            score += 1
        elif elf == "B":
            score += 2
        else:
            score += 3
    #Lose Scenario
    else:
        if elf == "A":
            score += 3
        elif elf == "B":
            score += 1
        else:
            score += 2

print(score)
