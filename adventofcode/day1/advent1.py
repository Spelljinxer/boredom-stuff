
elves = []
with open("./adventofcode/day1/list.txt") as f:
    elves.append([])
    for line in f:
        if line.strip() == "":
            elves.append([])
        else:
            elves[-1].append(int(line.strip()))
elf_carrying_most = 0
print(elves)
for elf in elves:
    total_calories = 0
    for ingredient in elf:
        total_calories += ingredient
    if total_calories > elf_carrying_most:
        elf_carrying_most = total_calories
print(elf_carrying_most)
