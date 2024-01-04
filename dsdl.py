
# 1.Prime or not
n=int(input())
c=0
for i in range(2,n):
  if(n%i==0):
    c=c+1
if(c==0):
  print("Prime")
else:
  print("Not Prime")

# 2. Replace vowel with *
n=input()
output=""
for char in n:
  if char in 'aeiouAEIOU':
     output+='*'
  else:
     output+=char
print(output)

# 3. Check Palindrome
n=input()
n1=n.upper()
n2=n1[::-1]
if(n1==n2):
  print("palindrome")
else:
  print("not palindrome")

# 4. Largest and smallest in list
n=input().split()
maximum=max(n)
minimum=min(n)
print(maximum)
print(minimum)

#4.largest and Smallest in tuple
t = tuple(map(int,input().split()))
maximum=max(t)
minimum=min(t)
print(maximum)
print(minimum)

# 5.# Dictionary to store student records
student_records = {
    1: {"admission_number": 1001, "roll_number": "44", "name": "John", "percentage": 85},
    2: {"admission_number": 1002, "roll_number": "55", "name": "Rohan", "percentage": 92.8},
    3: {"admission_number": 1003, "roll_number": "66", "name": "Ayush", "percentage": 95.3},
    4: {"admission_number": 1004, "roll_number": "77", "name": "Prachi", "percentage": 89.9},

}
n= int(input())
student = student_records.get(n)
if student:
    print("Student Details:")
    print("Admission Number:", student.get("admission_number"))
    print("Roll Number:", student.get("roll_number"))
    print("Name:", student.get("name"))
    print("Percentage:", student.get("percentage"))
else:
    print("Student with admission number",n, "not found.")

#6.square of a no.
n=int(input())
print(n*n)

# 6.log
import math
n=int(input())
result = math.log(n)
print(result)

#6.quad of a no.
n=int(input())
m= n**2
print(m)

#7.menu driven airthmetic operations
n1=int(input())
n2=int(input())
print("Press a for Addition")
print("Press s for Subtraction")
print("Press m for Multiplication")
print("Press d for Divison")
choice=(input())
if(choice=='a'):
  print(n1+n2)
elif(choice=='s'):
  print(n1-n2)
elif(choice=='m'):
  print(n1*n2)
elif(choice=='d'):
  print(n1/n2)
else:
  print("Not a right choice")

#8.fibo
n=int(input())
a=0
b=1
count=0
if n<=0:
    print("not applicable")
elif n==1:
    print(a)
else:
    while(count<n):
        print(a, end=" ")
        c=a+b
        a=b
        b=c
        count=count+1

#9.
def factorial(n):
    if((n==0) or (n==1)):
        return 1
    else:
        return n * factorial(n - 1)

def list_sum(numbers):
    return sum(numbers)

print("Enter 1 for factorial")
print("Enter 2 for sum for list elements")
choice=int(input())
if(choice==1):
  n=int(input())
  print(fact(n))
elif(choice==2):
  a=list(map(int,input().split()))
  print(list_sum(a))
else:
  print("wrong choice")

#10.
list=[2,1,3,4,5,6,7]
sum=0
for i in list:
  if i%2==0:
    sum+=(i*10)
print(sum)

#11.
l=["hiiiii","helloo","jaya","JAYA","RAM","END","AYUHEA"]
for i in l:
  if(i[-1]=="A"):
    print(i)

#12.read a text file line by line and display each word separated by #
file = open("python.txt", "r")

for line in file:
    words = line.split()
    new_line = '#'.join(words)
    print(new_line)

file.close()

#13 read a text file and display number of vowels
total_vowels = 0
total_constants = 0
total_uppercase = 0
total_lowercase = 0

file = open("python.txt", "r")

for line in file:
    words = line.split()
    for word in words:
        vowels = sum(1 for char in word if char.lower() in ['a', 'e', 'i', 'o', 'u'])
        uppercase = sum(1 for char in word if char.isupper())
        lowercase = sum(1 for char in word if char.islower())
        constants = sum(1 for char in word if not char.isalpha())

        total_vowels += vowels
        total_constants += constants
        total_uppercase += uppercase
        total_lowercase += lowercase

file.close()

print("Number of vowels: ", total_vowels)
print("Number of constants: ", total_constants)
print("Number of uppercase letters: ", total_uppercase)
print("Number of lowercase letters: ", total_lowercase)

#14 remove all the lines that contains the character 'a' in a file and write it to another file and show all copied data
with open("python.txt", "r") as file:
    lines = file.readlines()

with open("newfile.txt", "w") as newfile:
    for line in lines:
        if 'a' not in line:
            newfile.write(line)

with open("newfile.txt", "r") as newfile:
    lines = newfile.readlines()
    for line in lines:
        print(line.strip())

#15. WAP to count the words "to" and "the" present in the file
count = {'to': 0, 'the': 0}
words = ['to', 'the']

with open("python.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    words1 = line.lower().split()
    for word in words:
        count[word] += words1.count(word)

print(f"to appears {count['to']} times.")
print(f"the appears {count['the']} times.")

#17 WAP to count occurence of each word in a given file
file_name = 'python.txt'
count = {}

with open(file_name, 'r') as file:
    words = file.read().split()

for word in words:
    word = word.lower()
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

print(count)

#18.WAP to count number of words in a given file
file_name = 'python.txt'

with open(file_name, 'r') as file:
    words = file.read().split()

count = len(words)

print(f'total no. of words are: {count}')

#24 random no. generator
import random
result = random.randint(1,6)
print(result)

"""Pdf Questions

"""

#1 WAP to convert long seconds in hour....
n=int(input())
hours=n//3600
minutes=(n//60)%60
seconds=n%60
print("{} Hours {} Minutes {} Seconds".format(hours,minutes,seconds))

#2 "Autulya".....
str=input()
print(str[0])
print(str[1:3])
print(str[4:])

#4 domination of a no....
amount = int(input())
denominations = [2000, 500, 200, 100, 50, 10, 5, 2, 1]

for denom in denominations:
    count = 0
    while amount >= denom:
        count += 1
        amount -= denom
    if count != 0:
        print(denom, "-", count)

#5 functions of list
l=input("enter the list:elements seprated by ,").split(',')
print("Display list:",l)
l.sort()
print("sort the list:",l)
l.append("new")
print("add element to the list:",l)
l.remove("new")
print("delete an element from the list",l)
print("length of list",len(l))
l.clear()
print("clear the list:",l)

#6 character is alphabet digit....
ch=(input())
if(ch.isalpha()):
    print("It is an Alphabet")
elif(ch.isdigit()):
    print("It is a Digit")
else:
    print("It is a Special Character")

#7 create dictinary...
keys = [10, 20, 30]
values = ['Ten', 'Twenty', 'Thirty']
dictionary = dict(zip(keys, values))
print(dictionary)

#9 random no. generator...
import random
r = random.randint(1,6)
print(r)

#10 calculate electricity bill
def Functionbill(units):
    surcharge = 0
    if units <= 50:
        amt = units * 2.60
        surcharge = 25
    elif units <= 100:
        amt = 130 + ((units - 50) * 3.25)
        surcharge = 35
    elif units <= 200:
        amt = 130 + 162.50 + ((units - 100) * 5.25)
        surcharge = 45
    else:
        amt = 130 + 162.50 + 526 + ((units - 200) * 8.45)
        surcharge = 75

    final_bill = amt + surcharge
    return final_bill

units_consumed = int(input("Enter the units consumed: "))
bill_amount = Functionbill(units_consumed)
print(bill_amount)

#11 strong password
def check(password):
    if len(password) < 8:
        return False
    if not any(char.isupper() for char in password):
        return False
    if '_' not in password:
        return False
    if not any(char.isdigit() for char in password):
        return False
    return True


user_password = input("Enter your password: ")

if check(user_password):
        print("Password is strong.")
else:
        print("Password is not strong.")