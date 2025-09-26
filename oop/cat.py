#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age
        


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('max', 5)
cat2 = Cat('milo', 2)
cat3 = Cat('tom', 4)


# 2 Create a function that finds the oldest cat

def checkAge():
    if cat1.age > cat2.age:
        if cat1.age > cat3.age:
            print(f'The oldest cat is {cat1.age} years old.')
        else:
            print(f'The oldest cat is {cat3.age} years old.')
    else:
        if cat2.age > cat3.age:
            print(f'The oldest cat is {cat2.age} years old.')
        else:
            print(f'The oldest cat is {cat3.age} years old.')

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
checkAge()

def oldest_cat(*args):
    return max(args)



print(f'Oldest Cat is {oldest_cat(cat1.age, cat2.age, cat3.age)} years old.')

