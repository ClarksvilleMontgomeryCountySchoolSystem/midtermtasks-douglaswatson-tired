
people = 4  # friends who went trick-or-treating
bg1 = 37
bg2 = 22
bg3 = 8
bg4 = 30

# Part 1: Combine the haul
candy_total=bg1+bg2+bg3+bg4
print(f"amount of candy you guys got during trick-or-treating {candy_total}")



# Part 2: Fair sharing (include yourself)
people=4+1
share=candy_total//people
leftover=2
print(f"Each person gets: {share}")
print(f"Leftover candy:{leftover}")



# Part 3: Include the sick friends
# Variable reassignment is fine - previous values were already printed
people=7
share=candy_total//people
leftover=6
print(f"Each person gets: {share}")
print(f"Leftover candy: {leftover}")
