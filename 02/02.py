import re

with open("input.txt") as file:
    input = file.readlines()

rTot = 12
gTot = 13
bTot = 14

valid = []
powers = []

for line in input:
    line = line.strip()
    id = int(re.findall("Game (\d+)", line)[0])
    rMax = max([int(item.split(" ")[0]) for item in re.findall("\d+ red", line)])
    gMax = max([int(item.split(" ")[0]) for item in re.findall("\d+ green", line)])
    bMax = max([int(item.split(" ")[0]) for item in re.findall("\d+ blue", line)])
    if (rMax <= rTot) and (gMax <= gTot) and (bMax <= bTot):
        valid.append(id)
    power = rMax * gMax * bMax
    powers.append(power)

print(f"Answer 1 is {sum(valid)}.")

print(f"Answer 2 is {sum(powers)}.")