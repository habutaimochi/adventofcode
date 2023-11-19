topThree = [0,0,0]
currentTotal = 0 
totals = []

file = open("input1.txt")
for line in file:
    if line == "\n":
        totals.append(currentTotal)
        currentTotal = 0
        continue
    else:
        currentTotal += int(line)

topThree = sorted(totals, reverse=True)[:3]
print(topThree)
sumOfTopThree = sum(topThree)
print(sumOfTopThree)
