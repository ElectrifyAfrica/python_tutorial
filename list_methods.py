numbers = [5, 2, 1, 7, 4]
numbers.append(20)
print(numbers)

numbers = [7, 4, 2, 8, 6]
numbers.insert(0, 10)
print(numbers)

numbers = [7, 4, 2, 8, 6]
numbers.remove(4)
print(numbers)

numbers = [7, 4, 2, 8, 6]
numbers.clear()
print(numbers)

numbers = [7, 4, 2, 8, 6]
numbers.pop()
print(numbers)

numbers = [7, 4, 2, 8, 6]
print(numbers.index(8))

numbers = [7, 4, 2, 8, 6]
print(4 in numbers)

numbers = [7, 4, 2, 8, 6]
print(50 in numbers)

numbers = [7, 4, 2, 8, 6, 7, 24, 17]
print(numbers.count(5))

numbers = [7, 4, 2, 8, 6, 7, 24, 17]
print(numbers.count(7))

numbers = [7, 4, 2, 8, 6, 7, 24, 17]
numbers.sort()
print(numbers)

numbers = [7, 4, 2, 8, 6, 7, 24, 17]
numbers.sort()
numbers.reverse()
print(numbers)

numbers = [7, 4, 2, 8, 6, 7, 24, 17]
numbers2 = numbers.copy()
numbers.append(10)
print(numbers)
print(numbers2)