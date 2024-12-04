
with open("dec3.txt", "r") as file:
  input_data = file.read()
    
import re
matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", input_data)
count : int = 0
for match in matches:  
    var1 = int(match[0])
    var2 = int(match[1])
    answer = var1 * var2
    count += answer

print(count)
count = 0

matches = re.findall(r"(don't\(\)|do\(\)|mul\((\d{1,3}),(\d{1,3})\))", input_data)
doRead = True
for match in matches:
    if match[0] == "don't()":
        doRead = False
        continue
    elif match[0] == "do()":
        doRead = True
        continue
    else:   
        if doRead:
            try:
                answer = int(match[1]) * int(match[2])
            except:
                ValueError() # ignore non numbers for now
            count += answer
print(count)
