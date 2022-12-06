input = open(r"C:\Users\bfeek\Pytest\Advent2022\Day6Input.txt","r")
s = input.read()

for i,p in enumerate(s):
    if i >= 3:
        list = [s[i-3],s[i-2],s[i-1]]
        count = 0
        if p not in list:
            for j,c in enumerate(list):
                list[j]= 0
                if c in list:
                    count +=1
                list[j] = c
            if count == 0:
                print(f"Solution is {i+1}")
                break
    

