#store the contents of list.txt into an array of arrays,
# where each array contains each line until a blank line is reached.

elves = []
with open("list.txt") as f:
    #create a new array for each blank line
    elves.append([])
    for line in f:
        if line.strip() == "":
            elves.append([])
        else:
            elves[-1].append(int(line.strip()))
elf_carrying_most = 0
for elf in elves:
    total_calories = 0
    for ingredient in elf:
        total_calories += ingredient
    max_calories = 0
    #find the index of the elf with the most calories
    if total_calories > max_calories:
        max_calories = total_calories
        elf_carrying_most = elf
print(elf_carrying_most)
print(max_calories)