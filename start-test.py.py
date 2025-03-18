#1. Start

#2. Define a list of integers (input).
numbers = [1, 2, 3, 4, 5]
#3. Initialize variables:
sum_even = 0
product_odd = 1
#4. Loop through each number in the list:
for num in numbers:
    if num % 2 ==0: # Check if the number is even.
        sum_even += num
    else: # If the number is odd,
        product_odd *= num
#5. Calculate the difference:
difference = sum_even - product_odd
#6. Print sum_even, product_odd, and difference.
print("sum of even numbers:", sum_even)
print("product of odd numbers:", product_odd)
print("difference:", difference)
#7. End
