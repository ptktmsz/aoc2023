with open("input.txt") as file:
    input = file.readlines()

def calcScore(winning: list, yours: list) -> int:
    matches = 0
    for n in yours:
        if n in winning:
            matches += 1
    if matches == 0:
        return 0
    else:
        return pow(2, matches - 1)

def calcMatches(winning: list, yours: list) -> int:
    matches = 0
    for n in yours:
        if n in winning:
            matches += 1
    return matches

def scratchCard(winning: list, yours: list, id: int) -> list:
    matches = calcMatches(winning, yours)
    return [id + i + 1 for i in range(matches)]


scores = []

for line in input:
    yours = list(filter(None, line.split("|")[1].strip().split(" ")))
    winning = list(filter(None, line.split("|")[0].split(":")[1].strip().split(" ")))
    scores.append(calcScore(winning, yours))

print(f"Answer 1 is {sum(scores)}.")

scratchcards = {}

for i, line in enumerate(input):
    scratchcards[i+1] = 1

for i, line in enumerate(input):
    yours = list(filter(None, line.split("|")[1].strip().split(" ")))
    winning = list(filter(None, line.split("|")[0].split(":")[1].strip().split(" ")))
    for _ in range(scratchcards[i+1]):
        wonScratchcards = scratchCard(winning, yours, i + 1)
        for scratchcard in wonScratchcards:
            scratchcards[scratchcard] += 1

print(f"Answer 2 is {sum(scratchcards.values())}.")
