# H-1

fruits = ['apple','banana','orange','kiwi']
for fruit in fruits:
    print(fruit)


# H-2 

names = ['ali','vali','hasan','husan']
for name in names:
    print(name.upper())

# H-3

cars = ['bmw','mers','nexia','malibu','cobalt']
for car in cars:
    print(car[0])

# H-4

countries = ['UZBEKISTAN','RUSSIA','TURKEY','USA']
for country in countries:
    print(country.lower())

# H-5

names = ['ali','sardor','abdulloh','aziz']
for name in names:
    print(name,len(name),"ta harif")

# H-6

animals = ['cat','dog','lion','tiger']
for i in range(len(animals)):
    animals[i] = animals[i].upper()

print(animals)

# H-7

names = ['ali','vali','sardor','aziz']
for i in range(len(names)): 
    names[i] = names[i].upper()

print(names)

# H-8

names = ['ali','hasan','husan','sardor']
for i in range(len(names)): 
    names[i] = names[i].capitalize()

print(names)

# H-10

animals = ['tiger','lion','elephant','rabbit']
for animal in animals:
    print(animal[0],"-",animal[-1])

# H-12

cars = ['bmw','nexia','malibu','cobalt','damas']
for i in range(len(cars)):
    cars[i] = cars[i].upper()

print(cars)

# H-13

name = input("ismingizni kiriting: ")
takrorlash = int(input("Necha marta chiqarilsin? "))
for i in range(takrorlash):
    print(name)

# H-14

miyweler = []
san = int(input("Necha meva kiritmoqchisiz? "))
for i in range(san):
    miywesi = input(f"{i + 1}-mevani kiriting: ")
    miyweler.append(miywesi)
print("mevalar",miyweler)

# H-15
renler = []
san = int(input("Necha rang kiritmoqchisiz? "))
for i in range(san):
    sani = input(f"{i + 1}-rangni kiriting: ")
    renler.append(sani)

print("Siznin sevimli raanglaringiz:",renler)