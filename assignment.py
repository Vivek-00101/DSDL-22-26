# -*- coding: utf-8 -*-
"""assignment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MopaasFegF3AolZeED9LhbOzfYQwrCLX
"""

#prime number or not
prime=0
number=int(input("Enter the number: "))
for i in range(2,number):
  if number%i==0:
    prime=1
    break
if (prime==1):
  print("Number is not prime")
else:
  print("Number is prime")

#conversion of vowel in *
def convo(str):
  vowel=['a','e','i','o','u','A',"E",'I','O','U']
  for i in str:
    if i in vowel:
      str=str.replace(i,"*")
  print(str)
str=input()
convo(str)

#palindrome string
str=input()
str1=str[::-1]
if str1==str:
  print("String is palindrome ")
else:
  print("String is not palindrome ")

#MAXIMUM AND MINIMUM NUMBER IN LIST
list1=[1,2,3 ,4 ,5,6]
min=list1[0]
max=list1[0]
for i in list1:
  if i>max:
    max= i
  if i<min:
    min=i
print(max,min)

#square of a no.
n=int(input())
print("square of a number",n*n)

#log
import math
result = math.log(n)
print("log of a number",result)

#quad of a no.
m= n**4
print("quad of a number",m)

#menu driven airthmetic operations
n2=int(input())
n1=int(input())
print("Press + for Addition")
print("Press - for Subtraction")
print("Press * for Multiplication")
print("Press / for Divison")
choice=(input())
if(choice=="+"):
  print(n2+n1)
elif(choice=="-"):
  print(n2-n1)
elif(choice=="*"):
  print(n2*n1)
elif(choice=="/"):
  print(n2/n1)
else:
  print("Not a right choice")

#fibonaaci series
n=int(input())
def fib(n):
  if(n==0 or n==1):
    return n
  else:
    return (fib(n-1)+fib(n-2))
for i in range(0,n):
   print(fib(i))

#factorial
choice=int(input("enter choice 1:factorial choice 2:sum of list"))
n=(input())

def sumlist(n):
  list=n.split()
  sum=0
  for i in list:
    sum=sum+int(i)
  return sum
def fact(n):
  if n == 0 or n == 1:
    return n
  else:
    return n * fact(n - 1)
if choice==1:
  print(fact(int(n)))

if choice==2:
  print(sumlist(list))

#TenTimesEven
n=input()
list=n.split()
def TenTimesEven(list):
  sum=0
  for i in list:
    if(int(i)%2==0):
      sum=sum+int(i)
  return sum*10
print(TenTimesEven(list))

#EndingANames
names=input()
list=names.split()
def EndingA(names):
  for i in list:
    if i[len(i)-1]=="a" or i[len(i)-1]=="A":
      print(i)
EndingA(names)

#number of to and the
file=open("poem.txt","r")
data=file.read()
to=0
the=0
list1=data.split()
for i in list1:
  if i=="to":
    to+=1
  if i=="the":
    the+=1
print(to,the)

#number of letter
file=open("text.txt","r")
data=file.read()
vowel=0
consonant=0
uppercase=0
lowercase=0
vowels=['a','e','i','o','u','A',"I",'E','O','U']
consonants="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
for i in data:
    if i in vowels:
        vowel=vowel+1
    if i in consonants:
        consonant=consonant+1
for i in data:
    if i.isupper():
        uppercase=uppercase+1
    if i.islower():
        lowercase=lowercase+1
print("vowels=",vowel)
print("consonant=",consonant)
print("uppercase",uppercase)
print("lowercase",lowercase)
file.close()

#trasnferin data
f1=open("f1.txt","r+")
f2=open("f2.txt","w+")
data=f1.readlines()
for i in data:
  list=i.split()
  if "a" in list:
    f2.write(i)
    data.remove(i)
f1.close()
f1=open("f1.txt","w")
for i in data:
  f1.write(i)
f2.seek(0)
data1=f2.read()
print(data1)

#count number of words
file=open("text.txt","r")
data=file.read()
list1=data.split()
print(len(list1))

#dice
import random
print(random.randint(1,6))
