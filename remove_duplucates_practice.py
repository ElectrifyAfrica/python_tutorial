numbers = [2, 2, 4, 6, 3, 4, 24, 21, 17, 14, 24, 6, 1]
uniques = []
for number in numbers:
    if number not in uniques: 
        uniques.append(number)
print(uniques)