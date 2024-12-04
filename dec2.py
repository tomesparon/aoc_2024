def parse_input(input_path):
    with open(input_path, 'r') as file:
        return file.readlines()

def is_safe(report):
    increasing = True
    decreasing = True
    for i in range(len(report) - 1):
        current_num = report[i]
        next_num = report[i + 1]
        if not (1 <= abs(current_num - next_num ) <= 3):
            return False
        if current_num >= next_num:
            increasing = False
        if current_num <= next_num:
            decreasing = False
    return increasing or decreasing

def is_safe_with_dampener(report):
    if is_safe(report):
        return True
    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1 :]
        if is_safe(modified_report):
            return True
    return False

input_path = 'dec2.txt'
part1 = 0
safereports = 0
input_lines = parse_input(input_path)

for line in input_lines:
    string_report = line.split()
    report = [int(num) for num in string_report]
    if is_safe(report):
        part1 += 1  
    if is_safe_with_dampener(report):
        safereports += 1
print(f"Part 1 Number of safe reports: {part1}")
print(f"Part 2 Number of safe reports: {safereports}")
