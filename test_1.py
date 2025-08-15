'''Done
Q1. Sum of Digits
Take a number and return the sum of its digits.
Example: Input: 1234 → Output: 10
'''
# class solution:
#     def sum_of_digit(self, num:int):
#         # total = 0
#         if num == 0:
#             return 0
#         while num > 0:
#             digit = num % 10
#             num = num // 10
#             total += digit
#         return total
# total = solution()
# print(total.sum_of_digit(1234))  # Expected output: 6

'''Done
Q2. Reverse the integer
Take a number and return the number reversed.
Example: Input: 1234 → Output: 4321
'''
# class solution:
#     def integer_rev(self, num:int):
#         rev_num = 0
#         while num > 0:
#             digit = num % 10
#             num = num // 10
#             rev_num = rev_num * 10 + digit
#         return rev_num
# rev_num = solution()
# print(rev_num.integer_rev(4321))     

'''Done
Q3. Count the Digits
Count how many digits are in the given number.
Example: Input: 786 → Output: 3
'''
# class solution:
#     def count_digit(self, num:int):
#         count = 0
#         if num == 0:
#             return 1
#         while num > 0:
#             num = num // 10
#             count += 1
#         return count
# count = solution()
# print(count.count_digit(1234))

'''Done
Q4. Check for Palindrome Number
Check if the number reads the same forward and backward.
Example: Input: 121 → Output: True, Input: 123 → Output: False
'''
# class solution:
#     def palindrome(self, num:int):
#         original_num = num  # Store the original number
#         reversed_num = 0
#         if num == 0:
#             return True
#         while num > 0:
#             digit = num % 10
#             num = num // 10
#             reversed_num = reversed_num * 10 + digit
#         return original_num == reversed_num
# check = solution()
# print(check.palindrome(121))
# print(check.palindrome(123))

'''Done
Q5. Find the Largest Digit
Return the largest digit in a number.
Example: Input: 4723 → Output: 7
'''
# class solution:
#     def largest(self, num:int):
#         digit = 0
#         largest = 0
#         if num == 0:
#             return 0
#         while num > 0:
#             digit = num % 10
#             num = num // 10
#             if digit > largest:
#                 largest = digit
#         return largest
# check = solution()
# print(check.largest(334569))

'''Done
Q6. Sum of Even Digits
Take a number and return the sum of only the even digits.
Example: Input: 123456 → Output: 2 + 4 + 6 = 12
'''
# class solution:
#     def sum_of_even(self, num:int):
#         total = 0
#         digit = 0
#         if num == 0:
#             return 0
#         while num > 0:
#             digit = num % 10
#             num = num // 10
#             if digit % 2 == 0:
#                 total += digit
#             else:
#                 pass
#         return total
# check = solution()
# print(check.sum_of_even(332))

'''Done
Q7. Check if Number is Armstrong
Check if a 3-digit number is an Armstrong number.¶
(Armstrong = sum of cubes of digits equals the number)
Example: Input: 153 → Output: True (1³ + 5³ + 3³ = 153)
'''
# class solution:
#     def armstrong(self, num:int):
#         original_num = num
#         cubic_sum_num = 0
#         if num == 0:
#             return 0
#         while num > 0:
#             digit = num % 10
#             num = num // 10
#             cubic_sum_num += digit ** 3 
#         return original_num == cubic_sum_num
# check = solution()
# print(check.armstrong(153))

'''Done
Q8. Count Occurrences of a Digit
Count how many times a digit (say 5) appears in a number.
Example: Input: 15525, Digit: 5 → Output: 3
'''
# class solution:
#     def count_num(self, num:int):
#         count = 0
#         if num == 0:
#             return 1
#         while num > 0:
#             digit = num % 10
#             num = num // 10
#             if digit == digit:
#                 count += 1
#             return count
# check = solution()
# print(check.count_num(552))

# class Solution:
#     def count_digit_occurrence(self, num: int, target_digit: int) -> int:
#         count = 0
#         while num > 0:
#             digit = num % 10
#             if digit == target_digit:
#                 count += 1
#             num = num // 10
#         return count
'''Done
Q9. Print All Digits (One Per Line)
Print each digit of the number on a separate line.
Example: Input: 123 → Output:
1
2
3
'''
# class solution:
#     def element(self, num: int):
#         for digit in str(num):
#             print(digit)
# check = solution()
# print(check.element(552))
'''Done
Q10. Product of Digits
Multiply all digits in a number.
Example: Input: 1234 → Output: 1 × 2 × 3 × 4 = 24
'''
# class solution:
#     def multiplication(self, num: int):
#         # digit = 0
#         multi = 1
#         if num == 0:
#             return 0
#         while num > 0:
#             digit = num % 10
#             num = num // 10
#             multi *= digit
#         return multi
# check = solution()
# print(check.multiplication(12)) 

'''Done
Q11. Count Even and Odd Digits
Count how many even and odd digits are in the given number.
Example: Input: 12345 → Output: Even=2, Odd=3.
'''
# class solution:
#     def count(self, num:int):
#         even_digit = 0
#         odd_digit = 0
#         if num == 0:
#             return 0
#         while num > 0:
#             digit = num % 10
            
#             if digit % 2 == 0:
#                 even_digit += 1
#             else:
#                 odd_digit += 1
#             num = num // 10
#         return even_digit, odd_digit

# check = solution()
# print(check.count(123)) 

'''Done
Q12. Check if Number is Prime
Check if the given number is a prime number.
Example: Input: 13 → Output: True , Input: 12 → Output: False
'''
# class solution:
#     def prime_num(self, num:int):
#         if num <= 1:
#             return False
#         if num == 0:
#             return False
#         if num == 2:
#             return True
#         i = 3
#         while i * i <= num:
#             if num % i == 0:
#                 return False
#             i += 2
#         return True
# check = solution()
# print(check.prime_num(12))

'''Done
Q13. Find GCD of Two Numbers
Find the Greatest Common Divisor (GCD) of two numbers.
Example: Input: 12, 18 → Output: 6
'''


# '''
# Q14. Find LCM of Two Numbers
# Find the Least Common Multiple (LCM) of two numbers.
# Example: Input: 4, 5 → Output: 20
# '''
# class solution:
#     def gcd(self, a: int, b: int):
#         while b != 0:
#             a, b = b , a % b
#         return a
#     def lcm(self, a: int, b:int):
#         gcd = self.gcd(a, b)
#         return (a *b)// gcd

'''Done
Q15. Check if Number is Perfect
Check if the number is a perfect number (sum of proper divisors equals the number).
Example: Input: 28 → Output: True (1+2+4+7+14=28)
'''
# class solution:
#     def perfect_num(self, num:int):
#         sum_divisor = 1
#         if num == 0:
#             return 0
#         while num >0:
#             if num % sum_divisor == 0:
#                 sum_divisor +=1
#         return sum_divisor
# class solution:
#     def perfect_num(self, num: int):
#         if num <= 1:  # 0 and 1 are not perfect numbers
#             return False

#         sum_divisor = 0
#         for i in range(1, num):  # check all numbers less than num
#             if num % i == 0:
#                 sum_divisor += i

#         return sum_divisor == num  # True if sum equals the number

# # Example usage:
# total = solution()
# print(total.perfect_num(28))  # Expected output: True

'''Done
Q16. Count Total Factors of a Number
Count how many factors (including 1 and itself) the number has.
Example: Input: 6 → Output: 4 (1, 2, 3, 6)
'''
# class solution:
#     def factor(self, num: int):
#         count = 1
#         if num < 0:
#             return 0
#         for i in range(count, num):
#             if num % count == 0:
#                 count +=1
#         return count
# check = solution()
# print(check.factor(6))
# def count_factors(n: int) -> int:
#     count = 0  # To count total number of factors

#     for i in range(1, n + 1):  # Check all numbers from 1 to n
#         if n % i == 0:         # If i divides n with no remainder
#             count += 1         # Then i is a factor, increment count

#     return count

# # Example
# num = 6
# print("Total number of factors:", count_factors(num))  # Output: 4

'''
Q17. Generate Fibonacci Series (n terms)
Print the first n terms of the Fibonacci series.
Example: Input: 5 → Output: 0 1 1 2 3
'''

            

'''
Q18. Check if Number is Strong
Check if the number is a strong number (sum of factorial of digits equals the number).
Example: Input: 145 → Output: True (1! + 4! + 5! = 145)
'''

'''Done
Q19. Sum of Digits Until Single Digit
Keep summing the digits until a single digit is left.
Example: Input: 9875 → 9+8+7+5=29 → 2+9=11 → 1+1=2 → Output: 2
'''
# class solution:
#     def unit_digit_sum(self, num: int):
#         while num >= 10:
#             total = 0
#             while num > 0:
#                 digit = num % 10
#                 total += digit
#                 num = num // 10
#             num = total
#         return num
                

'''Done
Q20. Swap Two Numbers (Without Third Variable)
Swap two numbers without using a third variable.
Example: Input: 4, 5 → Output: 5, 4
'''
# class solution:
#     def reverse(self, a:int, b:int):
#         a,b = b, a
#         return a, b
# class Solution:
#     def swap(self, a: int, b: int):
#         a = a + b  # Step 1: Add both numbers
#         b = a - b  # Step 2: Subtract new b from a (which is a + b) → gives original a
#         a = a - b  # Step 3: Subtract new b (original a) from a (a + b) → gives original b
#         return a, b

'''Done
Q21. Check if Number is Harshad
Check if the number is divisible by the sum of its digits.
Example: Input: 18 → Output: True (18 % (1+8) == 0)
'''
# class solution:
#     def sum_of_digit(self, num: int):
#         total = 0
#         while num > 0:
#             digit = num % 10
#             num = num // 10
#             total += digit
#             if num % total == 0:
#                 return True
#             else:
#                 return False
# check = solution()
# print(check.sum_of_digit(18))
# class solution:
#     def is_harshad(self, num: int):
#         if num == 0:  # Edge case
#             return False

#         total = 0
#         temp = num
#         while temp > 0:
#             digit = temp % 10
#             temp = temp // 10
#             total += digit

#         return num % total == 0  # Check divisibility after sum is computed
# # Example usage
# check = solution()
# print(check.is_harshad(18))  # Expected output: True

             
'''
Q22. Check if Number is Automorphic
Check if the square of the number ends with the number itself.
Example: Input: 76 → 76² = 5776 → Output: True
'''
# class solution:
#     def automorphic(self, num:int):
#         square = num * num 
#         return(str(num).endswith(str(square)))

'''Done
Q23. Find First Digit of a Number
Return the first digit of the number.
Example: Input: 9321 → Output: 9
'''
# class solution:
#     def frist_digit(self, num:int):
#         while num >=10:
#             num = num // 10

'''Done
Q24. Find Last Digit of a Number
Return the last digit of the number.
Example: Input: 9321 → Output: 1
'''
# class solution:
#     def last_digit(self, num:int):
#         return num % 10

'''Done
Q25. Reverse Only the Digits of a Number (Keep sign)
Reverse the digits of the number but preserve its sign.
Example: Input: -123 → Output: -321
'''
# class solution:
#     def reverse(self, num:int):
#         sgin = -1 if num < 0 else 1
#         num = abs(num)
#         reversed_num = 0
#         while num > 0:
#             digit = num % 10
#             num = num // 10
#             reversed_num = reversed_num * 10 + digit
#         return reversed_num * sgin

'''Done
Q26. Count Zeros in a Number
Count how many zeros are present in the number.
Example: Input: 10500 → Output: 3
'''
# class Solution:
#     def count_zeros(self, num: int) -> int:
#         count = 0
        
#         if num == 0:
#             return 1  # Special case: 0 has one zero

#         while num > 0:
#             digit = num % 10           # Extract the last digit
#             if digit == 0:
#                 count += 1             # If the digit is zero, increase the count
#             num = num // 10            # Remove the last digit

#         return count
'''
Q27. Print Number in Words
Print each digit of the number in words.
Example: Input: 123 → Output: One Two Three
'''
class solution:
    def num_in_words(self, num:int):
        if num == 0:
            print ("Zero")
        while num > 0:
            

'''
Q28. Find Power Without Using ** or pow()
Calculate the power of a number without using ** or pow().
Example: Input: 2, 3 → Output: 8
''' 

'''
Q29. Print All Prime Numbers Up to N
Print all prime numbers up to a given number N.
Example: Input: 10 → Output: 2, 3, 5, 7
'''

'''
Q30. Check if Digits Are in Increasing Order
Check if the digits of the number are in strictly increasing order.
Example: Input: 1234 → Output: True; Input: 1324 → Output: False
'''
'''
Q31. Find Product of Digits
Return the product of all digits in a number.
Example: Input: 1234 → Output: 24 (123*4)
'''
'''
Q32. Count Frequency of Each Digit
Count how many times each digit appears in the number.
Example: Input: 112232 → Output: 1=2, 2=3, 3=1
'''
'''
Q33. Check if Number is Armstrong
Check if a number is equal to the sum of the cubes of its digits.
Example: Input: 153 → Output: True (1³ + 5³ + 3³ = 153)
'''
'''
Q34. Rotate Digits of a Number (Right Rotation by 2)
Rotate the digits of a number to the right by 2 places.
Example: Input: 12345 → Output: 45123
'''
'''
Q35. Convert Binary to Decimal
Convert a binary number (as integer input) to its decimal form.
Example: Input: 1010 → Output: 10
'''
'''
Q36. Convert Decimal to Binary
Convert a decimal number to binary (without using bin()).
Example: Input: 10 → Output: 1010
'''
'''
Q37. Reverse Binary Representation
Reverse the binary digits of a number.
Example: Input: 6 (110) → Output: 011 → 3
'''
'''
Q38. Find Second Largest Digit in a Number
Return the second largest digit from the number.
Example: Input: 4723 → Output: 4
'''
'''
Q39. Sum of All Prime Digits
Add only the prime digits in the number.
Example: Input: 2379 → Output: 2+3+7 = 12
'''
'''
Q40. Check if Number is Duck Number
Check if a number contains at least one zero but does not begin with zero.
Example: Input: 1023 → Output: True; Input: 0123 → Output: False
'''
'''
Q41. Check if Number is Magic Number
Magic number = recursively add digits until you get 1.
Example: Input: 199 → 1+9+9=19 → 1+9=10 → 1+0=1 → Output: True
'''
'''
Q42. Print All Divisors of a Number in Sorted Order
List all divisors of the given number.
Example: Input: 12 → Output: 1 2 3 4 6 12
'''
'''
Q43. Find the Sum of Factorials of Even Digits Only
Only add factorials of even digits.
Example: Input: 2483 → Output: 2! + 4! + 8! = 2 + 24 + 40320 = 40346
'''
'''
Q44. Reverse a Number Without Converting to String
Reverse the digits using only math operations.
Example: Input: 1234 → Output: 4321
'''
'''
Q45. Replace All Zeros with Fives
Convert every 0 in a number to 5.
Example: Input: 1020 → Output: 1525
'''
'''
Q46. Find the Smallest Prime Factor
Return the smallest prime factor of the number.
Example: Input: 91 → Output: 7
'''
'''
Q47. Sum of Digits at Even and Odd Positions Separately
Return separate sums for digits at even and odd indices (0-based).
Example: Input: 123456 → Output: EvenPosSum=1+3+5=9, OddPosSum=2+4+6=12
'''

'''
Q48. Calculate HCF and LCM Together
Return both HCF and LCM of two numbers.
Example: Input: 12, 18 → Output: HCF=6, LCM=36'''

'''
Q49. Count Palindromic Numbers in a Range
Given a range from a to b, count how many palindromes exist.
Example: Input: 10, 100 → Output: 9 (11, 22, ..., 99)
'''
'''
Q50. Add Digits in Alternating Fashion (Odd - Even + Odd - Even...)
Alternate between adding and subtracting digits from left to right.
Example: Input: 12345 → Output: 1-2+3-4+5 = 3
'''