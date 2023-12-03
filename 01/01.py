def remove_alpha(s: str) -> str:
    return "".join([c for c in s if c.isnumeric()])

# with open("input.txt") as file:
#     input = file.readlines()
#
# digits = [remove_alpha(entry) for entry in input]
# calibrations = [int(item[0] + item[len(item)-1]) for item in digits]
#
# print(f"Answer 1: sum is {sum(calibrations)}")

with open("input.txt") as file:
    input = file.readlines()

calibrations = []

for item in input:
    for i, c in enumerate(item):
        if c.isnumeric():
            first = c
            break
        else:
            if item[i:].startswith("one"):
                first = "1"
                break
            elif item[i:].startswith("two"):
                first = "2"
                break
            elif item[i:].startswith("three"):
                first = "3"
                break
            elif item[i:].startswith("four"):
                first = "4"
                break
            elif item[i:].startswith("five"):
                first = "5"
                break
            elif item[i:].startswith("six"):
                first = "6"
                break
            elif item[i:].startswith("seven"):
                first = "7"
                break
            elif item[i:].startswith("eight"):
                first = "8"
                break
            elif item[i:].startswith("nine"):
                first = "9"
                break
    item = item[::-1]
    for i, c in enumerate(item):
        if c.isnumeric():
            last = c
            break
        else:
            if item[i:].startswith("one"[::-1]):
                last = "1"
                break
            elif item[i:].startswith("two"[::-1]):
                last = "2"
                break
            elif item[i:].startswith("three"[::-1]):
                last = "3"
                break
            elif item[i:].startswith("four"[::-1]):
                last = "4"
                break
            elif item[i:].startswith("five"[::-1]):
                last = "5"
                break
            elif item[i:].startswith("six"[::-1]):
                last = "6"
                break
            elif item[i:].startswith("seven"[::-1]):
                last = "7"
                break
            elif item[i:].startswith("eight"[::-1]):
                last = "8"
                break
            elif item[i:].startswith("nine"[::-1]):
                last = "9"
                break
    calibrations.append(first + last)

print(calibrations)

print(f"Answer 2: sum is {sum([int(x) for x in calibrations])}")