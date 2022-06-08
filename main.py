# ====> Formatted Strings <====
# firstname = "Mohd"
# lastname = "Rizwan"

# fullname = f'{firstname} {lastname}'
# print(fullname)


# String Methods =>  Manipulating Strings <======================================================

# str = "Hello, I am Mohd Rizwan"
#1 String length
# print(len(str)) <===
# ============= 
#2 String to uppercase
# print(str.upper()) <===
# ============= 
#3 String to lowercase
# print(str.lower()) <===
# ============= 
#4 capitalize
# print(str.capitalize()) <===
# ============= 
#5 ends with
# print(str.endswith("Rizwan")) <===
# ============= 
#6 replace
# print(str.replace('Mohd Rizwan', "Arafat Ali")) <===
# =============
#7 in interator <======================================================
# print("Rizwan" in str)


# Arithmatic Operaotrs
# Following are the arithmatic operators
# +, -, *, /, %, +=, -=, **, // etc.

# print(20 // 6)  returns an interger instead of a float number, it will return 3
# print(10 ** 2) returns the expnent of the first operand, here it will return 100 = 10 * 10
# Most operator similar to js operators


# Math Functions

# to use math functions we need to import math from math library in python

# import math
# x = 2.9
# print(math.ceil(x)) rounds up
# print(math.floor(x)) rounds down

# IF STATEMENT

# is_hot = False
# is_cold = False

# if is_hot:
#     print("It's a hot day")
#     print('Drink plenty of water')
# elif is_cold:
#     print("It's a cold day")
#     print('Wear warm cloths')
# else:
#     print("It's a lovely day")
#     print('Enjoy your day')

# Give a Down Payment Discount on a good credit score <===
# price = 1000000
# is_credit_good = False
# if is_credit_good:
#     down_payment = 0.1 * price
# else:
#     down_payment = 0.2 * price

# print(f"Down payment: ${down_payment}")

# Logical Operators <======================================================
 #1. and
 #2. not
 #3. or 

# name = input('Your name: ')
# income = int(input('Your income: '))

# if income >= 50000 and income <= 100000:
#     print(f"Congratulations, {name}! You are eligible for this loan")
#     amount = int(input("Please enter the amount you want to borrow: "))
#     if amount <= 100000:
#         print(f"Dear {name}, you have successfully requested {amount} loan, the money will be credited in your account within 24 hours")
#     else:
#         print(f"Dear {name}, we cannot lend you more than 100000")
# elif income < 50000:
#     print(f"Sorry, {name}! You aren't eligible for this loan, please try after 6 months")
# else:
#     print(f"Dear {name}, you have enough money, you don't need to borrow any money")
# print('Have a great day! Thanks')

# Weight Converter <======================================================

# weight = int(input('Weight: '))

# pound_or_killograms = input('LBS (Pound) or KG (Killograms): ')

# if pound_or_killograms.lower() == 'k':
#     print(f"{weight * 0.453592}")
# elif  pound_or_killograms.lower() == 'l':
#     print(f"{weight / 0.453592}")
# else:
#     print('Please enter L or K')
# print('Great!')

# LOOPS
# While Loop

# num = 1
# while num < 5:
#     print(num)
#     num = num + 1
# print('Done')

# Guess Game <======================================================

# guess_count = 0
# guess_limit = 3
# secret_number = 9
# while guess_count < guess_limit:
#     guess = int(input('Guess: '))
#     guess_count += 1
#     if guess == secret_number:
#         print("You won!")
#         break
# else:
#     print('Sorry, You failed!')

# Card Game <======================================================


# command = ""

# while command != 'quit':
#     command = input(">").lower()
#     if command == "start":
#         print("The car started")
#     elif command == "stop":
#         print('The car stopped')
#     elif command == 'help':
#         print("""
#             Start - To start the car
#             Stop - To stop the car
#             Quit - to quit
#         """)
#     elif command == "quit":
#         break
#     else:
#         print("Sorry! I don't understand that")
# else:
#     print("Sorry! I don't undestand that")


# For Loop <======================================================

# prices = [20,30,25,36,24,15,50,100,125]

# total = 0

# for price in prices:
#     total = total + price
# print(f"The total cost of your cart is: {total}")

# numbers = [6,2,6,2,2]
# for x in numbers:
#     count = ''
#     for count_x in range(x):
#         count += "X"
#     print(count)
    
#### Lists <=======================================================

# names = ["Rashid", "Sajid", "Rizwan", "Saddam", "Gulsher", "Arafat"]

# print(names[:])

# find the lar,gest number is a list
# numbers = [25,26,28,46,45,178,102,125,158]
# max = numbers[0]

# for number in numbers:
#     if number > max:
#         max = number
# print(max)

## 2D Lists <======

# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# for row in matrix:
#     for item in row:
#         print(item)
#     print(row)

# List Methods <=====

# 1. Append - Used to append the item into the 
# => numbers.append(20)
# 2. Insert - Used to insert the item at the specific index of list: Take to parameters 1 - index, 2 - Item
# => numbers.insert(2, 25)
# print(numbers)
# 3. Remove - Used to remove an item from the list
# => numbers.remove(2)
# print(numbers)
# 4. Clear  - Used to remove all the items from the list
# => numbers.clear()
# print(numbers)
# 5. Pop    - Used to remove the last item from the list
# => numbers.pop()
# print(numbers)
# 6. Index  - Used to check if an item is exist in the list - Returns the index
# print(numbers.index(5))
# 7. Count -  Used to return the numbers of same items found in the list
# print(numbers.count(1))
# 8. Sort  - Used to reverse the list in ascending order
# numbers.sort()
# print(f"Ascending order: {numbers}")
# 9. Reverse - Used to sort the list in descending order
# numbers.reverse()
# print(f"Descending order: {numbers}")

numbers = [1, 5, 2, 3, 2, 4, 5, 9, 2, 1, 6, 9,1,1]
uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
