# Exercise 1

number = input()
12345

first_num = (number % 10) + ((number % 1000) // 100) + (number // 10000)
second_num = ((number % 100) // 10) + ((number % 10000) // 1000)

print (f"Number {number} becomes {first_num}{second_num}")