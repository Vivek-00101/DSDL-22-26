# -*- coding: utf-8 -*-
"""dsdlassignment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GouNE759bOLt2-KfvtMm-JKHpCywLhuG
"""

#prime or not
num=int(input("enter the num"))
flag=0
for i in range(2,num):
  if(num%i==0):
    flag=1
    break
if( flag==1):
  print(" not prime")
else:
  print("prime")

#conversion of vowels into"*" using function
word=input("enter the string")
vowels=['a','e','i','o','u','A','E','O','U']
def convert(word):
  for i in word:
    if i in vowels:
      word=word.replace(i,"*")
  return word
print(convert(word))

word=input()
word1=word[::-1]
if(word==word1):
  print("palindrome")
else:
  print("not palindrome")

#max and min in list
list1=[1,2,3 ,4 ,5,6]
min=list1[0]
max=list1[0]
for i in list1:
  if i>max:
    max= i
  if i<min:
    min=i
print(max,min)

#max and min in tuple
list1=(1,2,3 ,4 ,5,6)
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
print(n*n)

#log
import math
n=int(input())
result = math.log10(n)
print(result)

#quad
n=int(input())
m= n**4
print(m)

#airthmetic operations
a=int(input())
b=int(input())
print("Press + for Addition")
print("Press - for Subtraction")
print("Press * for Multiplication")
print("Press / for Divison")
choice=(input())
if(choice=="+"):
  print(a+b)
elif(choice=="-"):
  print(a-b)
elif(choice=="*"):
  print(a*b)
elif(choice=="/"):
  print(a/b)
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

#10 times even
n=input()
list=n.split()
def TenTimesEven(list):
  sum=0
  for i in list:
    if(int(i)%2==0):
      sum=sum+int(i)
  return sum*10
print(TenTimesEven(list))

#function for ending A names
names=input()
list=names.split()
def EndingA(names):
  for i in list:
    if i[len(i)-1]=="a" or i[len(i)-1]=="A":
      print(i)
EndingA(names)

#reading file
file=open("text.txt","r")
string=file.readlines()

for i in string:
    list=i.split()
    str="#".join(list)
    print(str)

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
file.close()





#count number of words
file=open("text.txt","r")
data=file.read()
list1=data.split()
print(len(list1))













#dice
import random
print(random.randint(1,6))

global max=5
global stack[]
choice=int(input("1:push 2:pop 3:display 0:exit"))
global top =(-1)
def push(n):
  if top==max-1
  stack.append(n)
  print("element is pushed")
def pop(n)