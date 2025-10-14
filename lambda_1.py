my_list = [5, 4, 3]

print(list(map(lambda item: pow(item, 2), my_list)))


a = [(0, 2), (4, 3), (9, 9), (10, -1)]

# List Sorting
a = [(0, 2), (4, 3), (9, 9), (10, -2)]

a.sort(key=lambda x: x[1])
print(a)
