#Hello, Master
"""This is a simple Python script that prints a greeting message to the console.
This is not a Comment.(Doc String)
"""

# Adi = "Hello, Master"
# print(Adi)

# n = int(input("Which Table you want to print :"))

# for i in range(1, 11):
#     print(f"{n} * {i} = {n*i}")

# n = int(input("Upto which n no. :"))
# sum = 0
# for i in range (1, n+1):
#     sum += i
# print(sum)

# n = int (input("Which no. fact you want to find :"))
# fact = 1
# for i in range (1, n+1):
#     fact = fact * i
    
# print(f"Your Factorial is : {fact}")

# n=(int(input("Tell me your number :")))
# even = 0 
# odd = 0

# for i in range (1, n+1):
#     if i%2==0:
#         even = even + i
#     else :
#         odd = odd + i
# print(f"Your Even and Odd sum are : {even} , {odd}")

# n = int(input("Tell me Your Number :"))

# for i in range (1, n+1):
#     if n%i == 0 :
#         print(f"{i} is a factor of {n}")


# n=(int(input("Tell me your number :")))
# sum =0
# for i in range (1, n): 
#     if n%i == 0:
#       sum = sum + i
# if sum == n :
#         print (f"{n} is a perfect number")
# else :
#         print (f"{n} is not a perfect number")

 
# n=(int(input("Check Your number is prime or not :")))
# count = 0
# for i in range(1, n+1):
#     if n%i == 0 :
#         count = count + 1
# if count == 2 : 
#     print (f"{n} is a prime number")
# else :
#     print (f"{n} is not a prime number")
 
# a = "SNAKE"
# b= ""
# for i in range(len(a)-1,-1,-1):
#     b = b + a[i]
# print(b)

# a = "NAMAN"
# b= ""
# for i in range(len(a)-1,-1,-1):
#     b = b + a[i]
# if b == a:
#     print(f"{a} is a palindrome")
# else :
#     print(f"{a} is not a palindrome")


# a = "dgrrjtfdj12354!#%^@!"

# dig = 0
# char = 0
# spchr = 0

# for i in a :
#     if i.isdigit():
#         dig = dig +1
#     elif i.isalpha():
#         char = char +1
#     else :
#         spchr = spchr +1

# print(f"You have {dig} digits, {char} characters and {spchr} special characters in your string")

# def sum (a,b): # Parameters
#     print(f"The sum of two number is : {a+b}")
# sum(12,12) # Arguments
# sum(866,253) # Arguments


# def demo (a,b):
#     print (f"My Name is {a} & My Age is {b}")

# demo (b = 20 , a ="Aditya")

# wheather = input("tell me the wheather : ")


# if wheather == "rainy":
#     print("Take an Umbrella")
# else:
#     print("No need to take an Umbrella")

# def max_num (num1,num2,num3):
#     if num1>=num2 and num1>=num3:
#         return num1
#     elif num2>=num1 and num2>=num3:
#         return num2
#     else:
#         return num3

# print(max_num(245,174,85))

# data1 = float(input("Enter your first number :"))
# opt = input("Choose your operator (+,-,*,/) :")
# data2 = float(input("Enter your second number :"))

# if opt == "+" :
#     print("The sum of two number is : ", data1 + data2)
# elif opt == "-" :
#     print("The difference of two number is : ", data1 - data2)
# elif opt == "*" :
#     print("The product of two number is : ", data1 * data2)
# elif opt == "/" :
#     print("The quotient of two number is : ", data1 / data2)
# else :
#     print("Enter a valid operator")

# Dictionary 
# ----------
# monthConversion = {
#     "jan" : "january",
#     "feb" : "february",
#     "mar" : "march",
#     "apr" : "april",
#     "may" : "may",
#     "jun" : "june",
#     "jul" : "july",
#     "aug" : "august",
#     "sep" : "september",
#     "oct" : "october",
#     "nov" : "november",
#     "dec" : "december"
# }
# # print(monthConversion["apr"])
# print(monthConversion.get("dec"))

# i= 1

# while i<=10:
#     print(i)
#     i += 1
# print("Done with loop.")

# Guessing Game
# -------------

# secret_word = "Aditya"
# guess = ""
# guess_count = 0
# guess_limit = 3
# out_of_guesses = False

# while guess != secret_word and not(out_of_guesses):
#     if guess_count < guess_limit:
#         guess = input("Enter your guess : ")
#         guess_count += 1
#     else:
#         out_of_guesses = True
# if out_of_guesses:
#     print("Out of Guesses.")
# else:  
#     print("You win!")
# -----------------------------------------------------------
# 2**3 is used for power
# def raise_to_power(base_num, pow_num):
#     result = 1
#     for i in range(pow_num):
#         result = result * base_num
#     return result

# print(raise_to_power(2,3))
# ------------------------------------------------------------

# number_grid = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [0]
# ]

# print(number_grid[0][1])

# for row in number_grid:
#     for col in row:
#         print(col)

# --------------------------------------------------------------

# def translate(phrase):
#     transalation = ""
#     for letter in phrase:
#         if letter in "AEIOUaeiou":
#             transalation = transalation + "g"
#         else:
#             transalation = transalation + letter
#     return transalation

# print(translate(input("Enter you phrase :")))

# ----------------------------------------------------------------

# try :
#     answer = 10/0
#     number = int(input("Enter any number :"))
#     print(number)
# # except ZeroDivisionError:
# #     print("Divided by Zero")
# except ZeroDivisionError as err:
#     print(err)
# except ValueError:
#     print("Invalid input")

# ---------------------------------------------------------------

