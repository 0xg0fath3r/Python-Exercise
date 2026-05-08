#1. How to calculate the hypothenus of a triangle.

adjacent_a = int(input("Enter the adjacent side: "))
obtuse_b = int(input("Enter the obtuse side: "))

hypothenus_c = (adjacent_a**2 + obtuse_b**2)**0.5 # multiplied by 0.5 since root of a number can also be that number multiplied by 0.5

print(hypothenus_c)

#2. Currency exchange: multiply the currency by the current exchange price in dollar

CO = int(input("What do you ahve left in pesos? ")) * 0.00027
PE = int(input("What do you ahve left in soles? ")) * 0.29
BR = int(input("What do you ahve left in reais? ")) * 0.20

total_in_usd = CO + PE + BR

print(total_in_usd)


#3. Shows how to concatenate a string

butterflies = 10
beetles = 12
ladybugs = 20

total = butterflies + beetles + ladybugs

print('I caught ' + str(butterflies) + ' 🦋 butterflies!')
print('I caught ' + str(beetles) + ' 🪲 beetles!')
print('I caught ' + str(ladybugs) + ' 🐞 ladybugs!')

print('I caught ' + str(total) + ' total bugs!')

