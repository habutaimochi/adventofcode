count = 0
total = 0
currentTotal = 0

file = open("input1.txt")
for line in file:
    if line.isspace():
        currentTotal = 0
        continue
    else:
        currentTotal += int(line)
    if currentTotal > total:
        total = currentTotal
print(total)
