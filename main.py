print("Hello Mahi")

name = "Mahi"
age = 26

print(name)
print(age)


age = 18

if age > 18:
    print("Eligible")
else:
    print("Not Eligible")

for i in range(5):
    print(i)


def add(a,b):
    return a+b

print(add(5,5))



#name = input("Enter your name: ")
#age = int(input("Enter your age: "))
#city = input("Enter your city: ")
#print(f"My name is {name}, I am {age} years old, from {city}")


a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

print(a+b)
print(a-b)
print(a*b)
print(a/b)





basic = int(input("Enter Basic Salary: "))
hra =  basic * 20/100
da = basic * 15/100
total = basic + hra + da

print(f"Total = {total}")
print(f"HRA = {hra}")
print(f"DA = {da}")





num = int(input("Enter Number : "))

if num % 2 ==0:
    print("Even Number")
else:
    print("Odd Number")


num = int(input("Enter Number : "))

for i in range(1,11):
    print(f"{num} x {i} = {num * i}")


a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

if b==0:
    print("Cannot divide by zero")
else:
    c=a/b
    print(f"Divide value {c}")



def is_even(a):
    if a % 2 ==0:
        return True
    else:
        return False
num = int(input("Enter a number : "))
print(is_even(num))


nums = [10,45,3,99,27]
biggest = nums[0]

for i in nums:
    if i > biggest:
        biggest = i

print(f"Biggest Number is : {biggest}")


mydetails = {
    "name" : "Mahi",
    "age"  : 26,
    "city" : "Kumbakonam",
    "experience" : 3.5
}

for key, value in mydetails.items():
    print(key,value)


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def show(self):
        print(f"{self.name} has {self.marks} marks")

stud1 = Student("Mahi", 80)
stud2 = Student("Ammu", 85)

stud1.show()
stud2.show()


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def show(self):
        print(f"{self.name} has {self.marks} marks")
    def is_pass(self):
        if self.marks >= 40:
            return True
        else:
            return False

stud1 = Student("Mahi", 40)
stud2 = Student("Ammu", 35)

stud1.show()
stud2.show()

print(stud1.is_pass())
print(stud2.is_pass())



class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount 

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount                        

acc = BankAccount(1000)
acc.deposit(200)
acc.withdraw(1200)
print(acc.balance)
acc.withdraw(5000)





try:
    num = int(input("Enter a Integer : "))
    print(25/num)
except ValueError:
    print("Give only numbers")
except ZeroDivisionError:
    print("Cannot divide by Zero")



with open("students.txt", "w") as f:
    f.write("Mahi\n")
    f.write("Keerthi\n")
    f.write("Dhivii\n")    

with open("students.txt", "r") as f:
    for line in f:
        print(line.strip())

with open("students.txt", "a") as f:
    f.write("Ammu\n")
print("----------------------")
with open("students.txt", "r") as f:
    for line in f:
        print(line.strip())


import json

mydetails = {
    "name": "Mahi",
    "age": 26,
    "city": "Kumbakonam",
    "experience": 3.5
}

with open("details.json", "w") as f:
    json.dump(mydetails, f, indent=4)

with open("details.json", "r") as f:
    data = json.load(f)

print(f"Name : {data["name"]} , City : {data["city"]}")


import json

student = {"name": "Mahi", "age": 26, "skills": ["C#", "SQL"]}

# dict -> JSON string
text = json.dumps(student)
print(text)

# JSON string -> dict
data = json.loads(text)
print(data["name"])

# JSON file la write
with open("student.json", "w") as f:
    json.dump(student, f, indent=4)

# JSON file la irundhu read
with open("student.json", "r") as f:
    data = json.load(f)
print(data["skills"])

import os
print(os.getcwd())


result = [n for n in range(1, 21) if n % 3 ==0]
print (result)

names = ["mahi", "ravi", "arun"]
upper_names = [n.upper() for n in names]
print(upper_names)



def multiply_all(*args):
    total = 1
    for num in args:
        total *=num
    return total

print(multiply_all())




def print_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

print_profile(name="Ravi", age=30, city="Chennai", role="Developer")



import helpers

print(helpers.add(2,3))
print(helpers.is_even(5))



import requests
r = requests.get("https://api.github.com")
print(r.status_code)


import math

r = int(input("Enter radius : "))

print (math.pi*r*r)



import requests

r = requests.get("https://api.github.com")
print(r.status_code)


nums = [1, 2, 3, 4, 5]
result = [n * 2 for n in nums if n > 2]
print(result)


def wrap(func):
    print("func is:", func)
    def wrapper():
        print("Wrapping start")
        func()
        print("Wrapping end")
    return wrapper

def hello():
    print("Hello")

print("hello is:", hello)
new_hello = wrap(hello)
print("---- ippo new_hello call ----")
new_hello()


def shout(func):
    def wrapper(*args, **kwargs):
        print("Start")
        func(*args, **kwargs)
        print("End")
    return wrapper

@shout
def greet(name):
    print(f"Hi {name}")

greet("Mahi")


def shout(func):
    def wrapper(*args, **kwargs):
        print("Start")
        result = func(*args, **kwargs)
        print("End")
        return result
    return wrapper

@shout
def add(a, b):
    return a + b

print(add(2, 3))



def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args} ")
        result = func(*args,**kwargs)
        return result
    return wrapper

@log_call
def add(a, b):
    return a + b

print(add(12, 3))



def count_up(n):
    for i in range(1, n + 1):                
        yield i

n = int(input("Enter value : "))
gen = count_up(n)
for x in count_up(n):
    print(x)



def evens(n):
    for i in range(1, n + 1):                
        if i % 2 ==0:
            yield i

n = int(input("Enter value : "))
for x in evens(n):
    print(x)



import sys

a = [n for n in range(1000000)]
b = (n for n in range(1000000))

print(sys.getsizeof(a))
print(sys.getsizeof(b))