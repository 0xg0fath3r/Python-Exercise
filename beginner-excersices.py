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

print('I caught ' + str(butterflies) + ' butterflies!')
print('I caught ' + str(beetles) + ' beetles!')
print('I caught ' + str(ladybugs) + ' ladybugs!')

print('I caught ' + str(total) + ' total bugs!')


#4. Calculate interest rate from balance

balance = int(input("Enter your balance: "))
rate = int(input("Enter interest rate: "))

new_balance = balance + (balance * rate)

print(new_balance)


#5. To calculate the ph_level:

ph = int(input("Enter a value between 0 and 14: "))

if ph > 7:
  print("Basic")
elif ph < 7:
  print("Acidic")
else:
  print("Neutral")



# Magic 8 ball:

# Write code below 💖
import random

question = input("Question: ")

random_number = random.randint(1, 9)

if random_number == 1:
  print("Yes - definitely.")
elif random_number == 2:
  print("It is decidedly so.")
elif random_number == 3:
  print("Without a doubt.")
elif random_number == 4:
  print("Reply hazy, try again.")
elif random_number == 5:
  print("Ask again later.")
elif random_number == 6:
  print("Better not tell you now.")
elif random_number == 7:
  print("My sources say no.")
elif random_number == 8:
  print("Outlook not so good.")
else:
  print("Very doubtful.")


