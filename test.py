'''
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

'''
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


'''
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

'''
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



'''
Q5. Find the Largest Digit
Return the largest digit in a number.
Example: Input: 4723 → Output: 7
'''
class solution:
    def largest(self, num:int):
        digit = 0
        largest = 0
        if num == 0:
            return 0
        while num > 0:
            digit = num % 10
            num = num // 10
            if digit > largest:
                largest = digit
        return largest
check = solution()
print(check.largest(334569))



'''
Q6. Sum of Even Digits
Take a number and return the sum of only the even digits.
Example: Input: 123456 → Output: 2 + 4 + 6 = 12
'''

'''
Q7. Check if Number is Armstrong
Check if a 3-digit number is an Armstrong number.¶
(Armstrong = sum of cubes of digits equals the number)
Example: Input: 153 → Output: True (1³ + 5³ + 3³ = 153)
'''
'''
Q8. Count Occurrences of a Digit
Count how many times a digit (say 5) appears in a number.
Example: Input: 15525, Digit: 5 → Output: 3
'''
'''
Q9. Print All Digits (One Per Line)
Print each digit of the number on a separate line.
Example: Input: 123 → Output:
1
2
3
'''

'''
Q10. Product of Digits
Multiply all digits in a number.
Example: Input: 1234 → Output: 1 × 2 × 3 × 4 = 24
'''