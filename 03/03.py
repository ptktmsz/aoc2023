import numpy as np

with open("input.txt") as file:
    input = file.readlines()

adjacents = set()
parts = []

for i, line in enumerate(input):
    for j, c in enumerate(line.strip()):
        if not c.isalnum() and c != ".":
            adjacents.add((i - 1, j - 1))
            adjacents.add((i - 1, j))
            adjacents.add((i - 1, j + 1))
            adjacents.add((i, j - 1))
            adjacents.add((i, j + 1))
            adjacents.add((i + 1, j - 1))
            adjacents.add((i + 1, j))
            adjacents.add((i + 1, j + 1))

parts = []
partsEnd = []

for i, line in enumerate(input):
    for j, c in enumerate(line.strip()):
        if c.isnumeric():
            k = j
            partStart = (i, k)
            try:
                while line[k+1].isdigit():
                    k = k + 1
            except IndexError:
                partEnd = (i, k)
            partEnd = (i, k)
            if partEnd not in partsEnd:
                parts.append((partStart, partEnd))
                partsEnd.append(partEnd)

parts_dicts = []

for part in parts:
    partCors = []
    partCors.append(part[0])
    x_value = part[0][0]
    y_values = range(part[0][1]+1, part[1][1])
    missingCors = [(x_value, y) for y in y_values]
    for missingCor in missingCors:
        partCors.append(missingCor)
    partCors.append(part[1])
    id = ""
    if part[0] == part[1]:
        id = input[partCors[0][0]][partCors[0][1]]
    else:
        for partCor in partCors:
            id += input[partCor[0]][partCor[1]]
    part_dict = {}
    part_dict["id"] = id
    part_dict["cors"] = partCors
    parts_dicts.append(part_dict)

sum = 0

for item in parts_dicts:
    for cor in item["cors"]:
        if cor in adjacents:
            sum += int(item["id"])
            break

print(f"Answer 1 is {sum}.")

ratios = []

for i, line in enumerate(input):
    for j, c in enumerate(line.strip()):
        if c == "*":
            starAdjacents = []
            starAdjacents.append((i - 1, j - 1))
            starAdjacents.append((i - 1, j))
            starAdjacents.append((i - 1, j + 1))
            starAdjacents.append((i, j - 1))
            starAdjacents.append((i, j + 1))
            starAdjacents.append((i + 1, j - 1))
            starAdjacents.append((i + 1, j))
            starAdjacents.append((i + 1, j + 1))
            matches = set()
            for adjacent in starAdjacents:
                for part_dict in parts_dicts:
                    if adjacent in part_dict["cors"]:
                        matches.add(int(part_dict["id"]))
            matches = list(matches)
            if len(matches) == 2:
                ratios.append(np.prod(matches))
            matches = set()

print(f"Answer 2 is {np.sum(ratios)}.")
