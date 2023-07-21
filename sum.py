#Program to find the sum of numbers using the keyboard inputs 
numbers = []
while True:
    num = int(input("Enter a number (enter 0 to calculate sum): "))
    if num == 0:
        break
    numbers.append(num)

sum_of_numbers = sum(numbers)
print("Sum of the numbers entered:", sum_of_numbers)