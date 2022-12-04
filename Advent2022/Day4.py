input = open(r"C:\Users\bfeek\Pytest\Advent2022\Day4Input.txt","r")
pairs = 0

for line in input: 
    pair1, pair2 = line.split(",")
    pair2 = pair2.replace("\n", "")
    pair1_1, pair1_2 = pair1.split("-")
    pair2_1, pair2_2 = pair2.split("-")
    pair1_1 = int(pair1_1)
    pair1_2 = int(pair1_2)
    pair2_1 = int(pair2_1)
    pair2_2 = int(pair2_2)
    if pair1_1 <= pair2_1 and pair1_2 >= pair2_2:
        pairs += 1
    elif pair2_1 <= pair1_1 and pair2_2 >= pair1_2:
        pairs += 1

print("Solution is: ", pairs)