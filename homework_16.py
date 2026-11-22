# H-1

fruits = ['apple','banana','orenge','kiwi','grape']

print(fruits)

# H-2

numbers = [10,20,30,40,50]

print(numbers[0])
print(numbers[-1])
print(numbers[2])

# H-3

colors = ['red','green','blue','yellow']
colors[1] = 'black'
colors[-1] = 'white'

print(colors)

# H-4

students = ['Ali','Vali','Husan','Hasan','Olim']

print(len(students))

# H-5

numbers = [10,20,30,40,50,60,70,80]

print(numbers[2:5])

# H-6

letters = ['a','b','c','d','e','f']
letters.reverse()

print(letters)

# H-7

numbers = [1,2,3,4,5,6,7,8,9,10]

print(numbers[:-1:2])

# H-8

students = [
    ['Ali',90, 'English'],
    ['Vali',85, 'Match'],
    ['Hasan',95, "Python"]
]

print(students[0][0])
print(students[0][1])
print(students[0][-1])

# H-9

students = [
    ['Ali',90],
    ['Vali',85],
    ['Hasan',95]
]
students[0][-1] = 100

print(students)

# H-10

programming = [
    ['HTNL','CSS'],
    ['Python','JavaScript'],
    ['Java','C++']
]

print(programming[1][0])
print(programming[1][-1])

# H-11

numbers = [10,20,30,40,50,60,70,80,90,100]

print(numbers[1::3])

# H-12

numbers = [12,7,8,15,20,33,44,51,60]
numbers = numbers[::2]

print(numbers)

# H-14

numbers = [10,20,30,40,50,60,70,80]

print("1-list:",numbers[:4])
print("2-list:",numbers[4:])

# H-15

numbers = [10,20,30,40,50]
numbers[1],numbers[-2] = numbers[-2],numbers[1]

print(numbers)

# H-16

students = ['Ali','Vali','Husan','Hasan','Olim']
students[0],students[-1] = students[-1],students[0]

print(students)

# H-17

students = [
    ['Ali',85],
    ['Vali',90],
    ['Hasan',75],
    ['Husan',95]
]
students[0],students[2] = students[2],students[0]

print(students)

# H-20

fruits = ['apple','banana','orange']
fruits.append('mango')
fruits.insert(2,'strawberry')

print(fruits)

# H-21

cars = ['BMW','Mercedes','Audi','Tesla']
cars.remove('BMW')

print(cars)

# H-22

numbers = [10,20,30,40,50]

print("Ochirilgan element:",numbers.pop())
print("Qolgan list:",numbers)

# H-23

fruits = ['apple','banana','apple','orange','apple','kiwi']

print("Olma sani:",fruits.count('apple'))

# H-24

languages = ['Java','C++','Python','JavaScript','PHP']
languages = languages.index('Python')

print("Python indexsi:",languages)

# H-25

numbers = [45,12,89,3,21,67,10]
numbers.sort()

print(numbers)

