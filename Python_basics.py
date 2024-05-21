# Data types in python 
# 1. int
# 2. float
# 3. complex
# 4. bool
# 5. str
# 6. list
# 7. tuple
# 8. set
# 9. dict
# 10. None
# 11. bytes
# 12. bytearray
# 13. memoryview
a=["saima","dleep","nouman"]
b=["saima","dleep","nouman"]
# print(type(a))
type(b)

# if condition in python:
# x=34
# y=45

# if x>y:
#     print("x is greater than y")
# else:
#     print("y is greater than x")
# user input in python:
# f_name=input("enter your name: ")
# s_name=input("enter your name: ")
# f_age=input("enter your age f_name: ")
# s_age=input("enter your age s_name: ")
# if f_age >s_age:
#     print(f_name,"is older than",s_name)
# else:
#     print(s_name,"is younger than",f_name)
# print("my name is",f_name ,", or sunao")
# Data structure in python:
# 1. list
# 2. tuple
# 3. set
# 4. dict
# 5. string
# 6. bytes
# 7. bytearray
# 8. memoryview
# food=["dahi bhallay","daal","smoosy","shamy","biryani","palak paneer"]
# print(food)
# print(food[3])
# food[1]="chicken pulao"
# print(food)
# 2.tuple
coordiantes=(23,3.4)
# print(coordiantes)
# print(coordiantes[0])
# # 3.set 
# st={"dahi bhallay","daal","smoosy","shamy","biryani","palak paneer"}
# print(st)
# st.add('pakoora')
# print(st)
# # 4.dict
# dic={'brand':'Ford','model':'Mustang','year':1967}
# print(dic)
# dic['year']=2012
# print(dic)
# print(dic['year'])
# Control flow statements in python:
# 1. if
# 2. elif
# 3. else
# 4. for
# 5. while
# 6. break
# 7. continue
# 8. pass
# 9. try
# conditional statements:
# 1. <
# 2. >
# 3. <=
# 4. >=
# 5. ==
# 6. !=
# 7. and
# 8. or
# 9. not
# 10. in
# 11. not in
# 12. is
# 13. is not
# x=-34

# if x>0:
#     print("positive")
# elif x<0:
#     print("negative")
# else:
#     print("zero")
# 

# For loops in python:
menu=["dahi bhallay","daal","smoosy","shamy","biryani","palak paneer"]
for food in menu:
    # print(food)

# While loops in python:
# i=1
# while i<6:
#     print(i)
#     i+=1

# for letters in "python":
#     if letters=='h':
#         break
#     print(letters)

# for letters in "python":
#     if letters=='h':
#         continue
#     print(letters)

# for letters in "python":
#     if letters=='h':
#         pass
#     print(letters)

# for letters in "python":
#     if letters=='h':
#         break
#     print(letters)

# Nested loop in python:
# 1. nested for
# 2. nested while
# colors=["red","green ","blue"]
# items=["book","pen","copy"]
# for color in colors:
#     for item in items:
#         print(color,item)

# nested while loop:
# i=1
# while i<6:
#     j=1
#     while j<6:
#         print(i,j)
#         j+=1
#     i+=1 

# i=1
# while i<6:
#     for j in range(3):
#         print(i,j)
#     i+=1

# d=1
# while d<6:
#     for i in range(4):
#         print(d,i)
#     d+=1

# function in python:
# 1. def
# 2. return
# 3. lambda
# def greet_user():
    print("hello, user")

# greet_user()

def Aoa():
    print("Assalam o Alikum ")
# Aoa()

def aoa(name,age):
    print("my name is",name,"and my age is",age)

# aoa("nouman",19)

def aoa(name="khuda kay banday "):
    print("my name is",name)

# aoa("malik nouman ")

# Return values 
def square(number):
    return number**2

# print(square(5))
# print(square(10))

# Recursion function in python:
# 1. factorial
# 2. fibonacci
# 3. prime number
# 4. prime number range

def factorial (n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
# print(factorial(6))

def factorial(b):
    if b==2:
        return 2
    else:
        return b*factorial(b-1)
# print(factorial(3))

# Lambda function in python:
x=lambda a:a+10
# print(x(5))

x=lambda a,b:a*b
# print(x(5,6))

x=lambda a,b,c:a*b+c
# print(x(5,7,2))
# /////////////////////////////////////////////////////////////////////
i=1
while i<=6:
    for j in range(4):
        print(i,j)
    i+=1

j=1
for j in range(8):
    while i<=8:
        print(j,i)
        i+=1

def num(a,b):
    print(f"this is my birth place {a},! and this is my home land {b}")

num("lahore","karachi")

def num1(name,fathername,age,gender):
    print(f"my name is  {name},! my father name is {fathername},! my age is {age},! nad  i am a {gender}")

num1("nouman","malik nouman",19,"male")

def factorial(a):
    return a/5

print(factorial(5))

def factorial(b):
    return b**34

print(factorial(12))

def factorial(c):
    return c+90

print(factorial(23))

x=lambda a:a+12

print(x(5))

c=lambda a,b:a//b

print(c(5,2))

i=1
while i <9:
    for j in range(4):
        print(i,j)

        i+=1

def gender(input):
    if input=="male":
        return "his"
    else:
        return "her"

print(gender("male"))

def factorial(m):
    return m/7

print(factorial(7))

z=lambda x:x+34

print(z(34))