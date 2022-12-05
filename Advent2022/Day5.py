import re
input = open(r"C:\Users\bfeek\Pytest\Advent2022\Day5Input.txt","r")
inputList = input.readlines()

boxes = inputList[:8]
moves = inputList[10:]

for row in range(len(boxes)):
    boxes[row] = boxes[row].replace("\n", "").replace("[","").replace("]","").replace("  "," ")
print(boxes)

stacks = [""] * 9

for row in range(len(boxes)):
    if boxes[row][0] != " ":
        stacks[0] = stacks[0] + boxes[row][0]
    if boxes[row][2] != " ":   
        stacks[1] = stacks[1] + boxes[row][2]
    if boxes[row][4] != " ":
        stacks[2] = stacks[2] + boxes[row][4]
    if boxes[row][6] != " ":
        stacks[3] = stacks[3] + boxes[row][6]
    if boxes[row][8] != " ":   
        stacks[4] = stacks[4] + boxes[row][8]
    if boxes[row][10] != " ":
        stacks[5] = stacks[5] + boxes[row][10]
    if boxes[row][12] != " ":
        stacks[6] = stacks[6] + boxes[row][12]
    if boxes[row][14] != " ":   
        stacks[7] = stacks[7] + boxes[row][14]
    if boxes[row][16] != " ":
        stacks[8] = stacks[8] + boxes[row][16]
    
print(stacks)

for move in moves:
    n,start,stop = re.findall(r"\d\d?", move)
    print(n,start,stop)

    n = int(n)
    stop = int(stop) - 1
    start = int(start) - 1 
    for i in range(n):
        grabby = stacks[start][0]
        stacks[start] = stacks[start][1:]
        stacks[stop] = grabby + stacks[stop]

    #grabby = stacks[start][:n]
    #stacks[start] = stacks[start][n:]
    #stacks[stop] = grabby + stacks[stop]

    print(stacks)

