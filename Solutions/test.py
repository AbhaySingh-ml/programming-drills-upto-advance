# class solution:
#     def sum_of_digit(self, num: int) ->int:
#         total = 0
#         while num > 0 :
#             total += num % 10
#             num //= 10
#         return total

'''
Q2. Reverse the integer
Take a number and return the number reversed.
Example: Input: 1234 → Output: 4321
'''
# class solution:
#     def reverse_the_integer(self, num: int):
#         reverse_num = 0
#         while num > 0:
#             digit = num % 10
#             reverse_num = reverse_num * 10 + digit
#             num = num // 10
#             return reverse_num

        
    

# class solution:
#     def reverse_digit(self, num: int) ->int
#     for i in range(num):
#         reverse = num % 10
#         return reverse

        # class solution:
#     def sum_of_digit(self, num: int) ->int:
#         total = 0
#         while num > 0 :
#             total += num % 10
#             num //= 10
#         return total



# class solution:
#     def reverse_digit(self, num: int) ->int
#     for i in range(num):
#         reverse = num % 10
#         return reverse

# class solution:
#     def count_digit(self, num: int):
#         for i in range(num):
#             count = num // 10

# class solution:
#     def count_digit(self, num: int):
#         while num > 0:
#             count = num // 10
#             count +1

# class solution:
#     def count_digit(self, num: int):
#         count = 0
#         if num == 0:
#             return 1
        
#     while num > 0:
#         num = num // 10
#         count +=1
#     return count    

# for 

# class solution:
#     def sum_of_digit(self, num: int):
#         sum = 0 
#         while num > 0:
#             num = num // 10
#             sum += 1
#         return sum


'''Q4. Check for Palindrome Number
Check if the number reads the same forward and backward.
Example: Input: 121 → Output: True, Input: 123 → Output: False
'''
# class solution:
#     def palindrome(self, num: int):
#         # edge case
#         if num == 0:
#         #   if the input is 0 this will treat not a plaindrome
#           return False 
#         while num > 0:
#            last_digit = 0
#            last_digit = num % 10
           
"""
Q5. Find the Largest Digit
Return the largest digit in a number.
Example: Input: 4723 → Output: 7
"""          
# class solution:
#     def largest_digit(self, num: int):
#         if num == 0:
#             return 0
#         while num > 0:
#             # extract every digit from the number 
#             # and then campare then in this while loop
#             digit = num % 10

'''
Q6. Sum of Even Digits
Take a number and return the sum of only the even digits.
Example: Input: 123456 → Output: 2 + 4 + 6 = 12
'''
# class solution:
#     def sum_of_even_digit(self, num: int):
#         # take out the single digit from the number 
#         # check the divisiblity by 2 
#         # if the remainder is 0 and add them
#         while num > 0:
#             single_digit = num % 10
#             check_even = single_digit / 2
#             if check_even == 0:
#                 # add all the digit with reminder 0 
#                 # but i dont know how to code it
#             else:
#                 # this is the case of odd digit in the number leave this number
#                 # do nothing here
#                 # break
#                 return check_even
            
'''
Q7. Check if Number is Armstrong
Check if a 3-digit number is an Armstrong number.¶
(Armstrong = sum of cubes of digits equals the number)
Example: Input: 153 → Output: True (1³ + 5³ + 3³ = 153)
'''
# class solution:
#     def armstrong(self, num: int):
#         while num > 0:
#             digit = num % 10
#             Square = digit * digit 
#             new_num += Square
#         return num == new_num
    
    # tell me the correction and accuracy with this code and tell me the correct solution 

'''
Q8. Count Occurrences of a Digit
Count how many times a digit (say 5) appears in a number.
Example: Input: 15525, Digit: 5 → Output: 3
'''
# class solution:
#     def count(self, num: int):
#         while num > 0:
#             digit = num % 10
#             num = num // 10 
#             if digit == digit:
#                 return num
#             else:
                


    # tell me the correction and accuracy with this code and tell me the correct solution 


# class solution:
#     def reverse(self, num: int):
#         digit = num % 10
#         reverse_digit = digit * 10 + digit
#         num = num // 10
#         return reverse_digit
#     sol = solution()
#     print(sol.reverse_digit(1234))  # Output: 4321

# class solution:
#     def sum_of_even_digit(self, num: int):
#         even_digit = 0
#         while num > 0:
#             digit = num % 10
#             num = num // 10
#             if digit % 2 == 0:
#                 even_digit = even_digit + digit
#             else:
#                 # do nothing i dont know how to code this condition
#             return even_digit
        
# num = [1,2,3,4] 
# for i in range(num):
#     print(i)

'''
Q51. Count Digits Greater Than a Given Number
Count how many digits in the number are greater than k.
Example: Input: 548723, k=5 → Output: 3 (8, 7, 6)'''
# class solution:
#     def count_digit(self, num: int, k: int):
#         list_of_digit = []
#         while num > 0:
#             digit = num % 10
#             if digit > k:
#                 list_of_digit.append()
#         return list_of_digit

'''
Q8. Count Occurrences of a Digit
Count how many times a digit (say 5) appears in a number.
Example: Input: 15525, Digit: 5 → Output: 3
'''
# class solution:
#     def count_occurrences(self, num: int, digit: int):
#         total = 0
#         while num >0:
#             count = num % 10
            
#             if count == digit:
#                 total += 1
#             num = num // 10
#         return total
                

'''
Q52. Remove Repeated Digits
Remove all repeated digits from a number, keeping only the first occurrence.¶
Example: Input: 12233441 → Output: 1234
'''
# class solution:
#     def repeated_digit(self, num: int):
#         while num > 0:
#             digit = num % 10 #last digit of the num
#             check_digit = 0 # num variable to make sure it is same or not
#             num = num // 10
#             if digit != check_digit:
#                 return check_digit == digit
            
# Q:
# Remove all repeated digits from a number, keeping only the first occurrence.
# Input: 9876677892
# Expected Output: 
# class solution:
#     def repeated_digit(self, num: int):
#         seen = ()
#         digit = num % 10
        

'''10. Product of Digits
Multiply all digits in a number.
Example: Input: 1234 → Output: 1 × 2 × 3 × 4 = 24'''    
# class solution:
#    def multiply(self, num: int):
#       while num > 0:
#         total_multiply = 0
#         digit = num % 10
#         total_multiply = digit * total_multiply
#         num = num // 10
#         return total_multiply

# class solution:
#    def duplicate(self, num: int):
#       seen = set()
#       while num > 0:
#          digit = num % 10
#          if digit in seen:
#             return False
#          seen.add(digit)
#          num = num // 10
#             return True
# class Solution:
#     def duplicate(self, num: int) -> bool:
#         seen = set()
#         while num > 0:
#             digit = num % 10
#             if digit in seen:         # Check first if digit already seen
#                 return False          # Duplicate found
#             seen.add(digit)           # Otherwise, add digit to the set
#             num = num // 10
#         return True                   # All digits are unique


'''
Q55. Find Difference Between Sum of Even and Odd Digits
Return the difference between the sum of even and odd digits.
Example: Input: 12345 → Output: (2+4) - (1+3+5) = 6 - 9 = -3
'''
# class solution:
#     def difference(self, num: int):
#         even_digit = []
#         odd_digit = []
#         while num > 0:
#             digit = num % 10
#             num = num // 10
#             if digit % 2 ==0:
#                 even_digit.append(digit)
#             else:
#                 odd_digit.append(digit)
#             return 
'''
Q56. Count Continuous Digit Pairs (like 11, 22)
Count how many consecutive digits are the same.
Example: Input: 112233445 → Output: 4
'''
# class solution:
#     def continuous_digit(self, num: int):
#         count = 0
#         while num > 0:
#             digit = num % 10
#             num = num // 10
#             if digit == digit:
#                 count += 1
#             else:
#                 count += 0
#             return count

# '''
# Q58. Find Average of Digits
# Return average value of all digits (as float).
# Example: Input: 1234 → Output: 2.5
# '''
# class solution:
#     def avg(self, num:int):
#         total_sum = 0
#         while num > 0:
#             digit = num % 10
#             total_sum += digit #this code is adding the digit 
#             total_avg = total_sum / 2
#         return total_avg




# # this is the question with my own code solution tell me where i did wrong and give me the 
# # solution of this problem without any in-built function of python

# class solution:
#     def star_append(self, num: int):
#         num_str = str(num)
#         result = num_str[0]

#         for i in range(i, len(num_str)):
#             result += '*' + num_str[i]
#         return result
# sol = Solution()
# print(sol.insert_stars(1234))    # Output: '1*2*3*4'
# print(sol.insert_stars(89))      # Output: '8*9'
# print(sol.insert_stars(7))       # Output: '7'
# print(sol.insert_stars(101))     # Output: '1*0*1'
'''
Q12. Check if Number is Prime
Check if the given number is a prime number.
Example: Input: 13 → Output: True , Input: 12 → Output: False
class solution:'''
# class solution:
#     def prime(self, num:int):
#         if num <= 1:
#             return False
#         if num == 2:
#             return True
#         if num % 2 == 0:
#             return False
#         # while i, (num ** 0.5)
#         # for i in range(i<=3,num **0.5)
#         for i in range(3, int(num ** 0.5) + 1, 2):
#             if num % i==0:
#                 return False
#             #But return True only after the loop has finished and no divisors were found.
#             return True
'''
Q59. Replace Every Digit with Sum of Previous and Next Digits
Treat number as array; replace each digit with sum of neighbors. First and last remain same.
Example: Input: 12345 → Output: 1 3 5 7 5'''
     
# class solution:
#     def sum_of_digit(self, num:int):

'''
Q60. Multiply Alternate Digits (odd-indexed digits only)
Multiply only the digits at odd indices.
Example: Input: 1234 → Odd Indices = 2, 4 → Output: 8
'''
# class solution:
#     def odd_product(self, num: int):
#         for i, d in enumerate(str(num)):
#             if i % 2 == 0:
#                 pass
#             else:
#                 product = 

    # i is the index (0, 1, 2, ...)
    # d is the digit (as a string — convert to int if needed)
'''
Q61. Count How Many Digits Are Perfect Squares
Return count of digits which are perfect squares (0,1,4,9).
Example: Input: 14932 → Output: 3 (1, 4, 9)
'''
class solution:
    def perfect_num(self, nums:int):
        while nums > 0:
            digit = nums % 10
            nums = nums // 10
            perfect_square = digit * digit
            for num in nums:
                if num == perfect_square:
                    return num
                


'''
Q62. Count Digits Smaller Than Average Digit
Return how many digits are smaller than the average of all digits.
Example: Input: 1236 → Avg = 3 → Digits < 3: 1, 2 → Output: 2
'''
# class solution:
#     def digit_avg(self, num:int):
#         while num >0:
#             digit = num % 10
#             num = num // 10
#             sum_of_digit += digit #adding the digit 
#             for i in num:
#                 digit % i

class solution:
    def digit_ang(self, num:int):
        digit= []
        temp = num
        while temp >1:
            digit.append(temp % 10)
            temp = temp // 10





'''
Q63. Remove All Even Digits
Remove even digits from the number.
Example: Input: 123456 → Output: 135
'''

'''
Q64. Check if All Digits Form a Geometric Sequence
Check if digits follow a geometric progression.
Example: Input: 248 → 2×2=4, 4×2=8 → Output: True
'''

'''
Q65. Count Digits Between Two Given Digits
Count digits that lie between two given digits a and b (exclusive).
Example: Input: 283519, a=2, b=9 → Count digits between 2 and 9 → Output: 4 (3, 5, 1, 8)
'''
