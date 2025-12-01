def fib(number):
    i = 0
    first = 0
    second = 1
    fib_list = []
    fib_list.append(first)
    fib_list.append(second)

    while i < number - 1:
        num = first + second
        fib_list.append(num)
        first = second
        second = num
        i +=1
    return fib_list
        
print(fib(5))
