def highest_even(li):
    even_li = []
    for num in li:
        if num % 2 == 0:
            even_li.append(num)
    return max(even_li)
print(highest_even([10, 2, 3, 4, 8, 11]))