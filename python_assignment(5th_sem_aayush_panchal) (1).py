# -*- coding: utf-8 -*-
"""Python assignment(5th sem Aayush Panchal)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Poc7P_qXA16hwHRswkpS8K5ewlLQ9guG
"""

#1
n= float(input("Enter a float number:- "))
d= "{:.2f}".format(n)
print(d)

#2
a= int(input("Enter the intiger: "))
b= int(input("Enter another intiger: "))
print("Product= ",a*b)

#3
r= 10
pi= 3.14
vol= (4*pi*r*r*r)/3
print("Volume of sphere= ",vol)

#4
num1= int(input("Enter first number:- "))
num2= int(input("Enter second number:- "))
print("Product= ",num1*num2)

#5
a= int(input("Enter an intiger= "))
SOP= a + a*a + a*a*a
print(SOP)

#6
string= str(input("Enter a string:- "))
l= len(string)
print("Length of a given string is ",l)

#7
str_1= "120"
str_2= "120.5"
print("Parsed into INT= ",int(str_1))
print("Parsed into FLOAT= ",float(str_2))

#8
num1= int(input("Enter a number:- "))
num2= int(input("Enter another number:- "))
c= num1+num2
if(c>100):
  print("Since sum is greater 100 so the product will be",num1*num2)
else:
  print("Sum of two number is ",c)

#9
a= 10
b= 10
c= 20
if(a==b==c):
  print("Sum is:- ",a+b+c)
else:
  print("Sum is:- ",a+b+c)
  print("Product is:- ",a*b*c)

#10
price= 100
n= int(input("Enter a number of quantity you purchased:- "))
tot_price= n*100
dscnt= 0
if(tot_price>10000):
  dscnt= tot_price*0.5
  print("Your bill with 50% discount= ",dscnt)
else:
  print("Your total bill is:- ",tot_price,"\n          Discount:- ",dscnt)

#11
n= int(input("Enter a number:- "))
if(n%8==0 and n%12==0):
  print("Number is divisible by both 8 and 12...")
else:
  print("Number can be divisible by either 8 or 12 \nOR\nnot divisible by both")

#12
n= int(input("Enter a number:- "))
if(n%2==0):
  print("The number is even")
else:
  print("The number is odd")

#13
a= int(input("Enter the marks of PHYSICS:- "))
b= int(input("Enter the marks of CHEMISTRY:- "))
c= int(input("Enter the marks of BIOLOGY:- "))
d= int(input("Enter the marks of MATHEMATICS:- "))
e= int(input("Enter the marks of COMPUTER10:- "))
Tot_marks= (a+b+c+d+e)
prcntg= (Tot_marks*100)/500
print(10)
if(a>100 or b>100 or c>100 or d>100 or e>100):
  print("Marks are invalid...")
else:
  if(prcntg>= 90):
   print("\nGrade A")
  elif(prcntg>= 80):
   print("\nGrade B")
  elif(prcntg>= 70):
   print("\nGrade C")
  elif(prcntg>= 60):
   print("\nGrade D")
  elif(prcntg>= 40):
   print("\nGrade E")
  elif(prcntg< 40):
   print("\nGrade F")
  print("Total Percentage:- ",prcntg,"%")

#14
A= int(input("Enter the age of Aayush:- "))
Y= int(input("Enter the age of Yash:- "))
P= int(input("Enter the age of Pranay:- "))
if(A<Y and A<P):
  print("Aayush is youngest guy...")
elif(Y<P and Y<A):
  print("Yash is youngest guy...")
elif(P<A and P<Y):
  print("Pranay is youngest guy...")
else:
  print("All 3 are of same ages")

#15
units= int(input("Enter the number of units:- "))
if (units<= 50):
  charges= (0.5*units)+ 20/100
  print("Electricity Bill:- ",charges)
elif(units<= 100):
  charges= (0.75*units)+ 20/100
  print("Electricity Bill:- ",charges)
elif(units<= 250):
  charges= (1.20*units)+ 20/100
  print("Electricity Bill:- ",charges)
elif(units> 250):
  charges= (1.50*units)+ 20/100
  print("Electricity Bill:- ",charges)

#16
tc= int(input("Total number of working days:- "))
c= int(input("total no of days worked:- "))
percentage= (c*100)/tc
if(percentage<80):
  print("Not eligible for exam...")
else:
  print("eligible for exam...")

#18
n= int(input("Enter a number: "))
sum= 0
while n>0:
  r= n%10
  sum= sum+ r
  n= n//10
print(sum)

#19
n= int(input("Enter a number:- "))
p= 1
while n>0:
  r= n%10
  p= p*r
  n= n//10
print(p)

#20
n=int(input("Enter the range of number:"))
temp= 3
sum= 0
for i in range(1,n+1):
    sum += temp
    temp=(temp*10)+3
print("The sum of the series = ",sum)

#21
n= int(input("Enter a number of rows: "))
for i in range(n):
  for j in range(0, i+1):
    print("*",end= ' ')
  print(" ")
for i in range(n+1,0,-1):
  for j in range(0,i-2):
    print("*",end= ' ')
  print(" ")

#22
n= int(input("Enter a number to reverse:- "))
rev= 0
while(n>0):
  r= n%10
  rev= rev*10 + r
  n= n//10
print(rev)

#23
n= int(input("Enter a number to reverse:- "))
x= n
rev= 0
while(n>0):
  r= n%10
  rev= rev*10 + r
  n= n//10
print(rev)
if (x==rev):
  print(x,"is Palindrome")
else:
  print(x,"is not Palindrome")

#24 
sum= 0
n= int(input("Enter a number:- "))
num= n
while(n!=0):
  r= num%10
  sum= sum + r**3
  num= num//10
if num==sum:
  print(num,"is amstrong number...")
else:
  print(num,"is not amstrong number...")

#25
num= int(input("Enter a number to find factorial:- "))
f= 1
for i in range(1,num+1):
  f= f*i
print("Factorial of",num,"is",f)

#26
n= int(input("Enter a number: "))
temp= n
sum= 0
while n>0:
  i= 1
  fact= 1
  digit= n%10
  for j in range(digit+1):
    fact= fact*j
    j+= 1
  sum= sum+ fact
  n= n//10
if sum==temp:
  print(n,"is a strong number")
else:
  print(n,"is not a strong number")

#30
n= int(input("Enter the number of rows: "))
for i in range(n+1,0,-1):
  for j in range(0,i-1):
    print("*",end=' ')
  print(" ")

#34
string= str(input("Enter the string: "))
print("The length of a given string: ",len(string))

#35
str1= input("Enter the first string: ")
str2= input("Enter the second string: ")
lst_1= list(str1)
lst_2= list(str2)
s= lst_1[0]
lst_1[0]= lst_2[0]
lst_2[0]= s
print("Swaping after first charachter of both the strings:- \n",''.join(lst_1),"and",''.join(lst_2))

#36
suffix= "polis"
str1= input("Enter the string: ")
n= len(str1)
if (n>3):
  print(str1)
elif (n>=3):
  print(str1+suffix)

#37
word= input("Enter the string: ")  # say "google.com"
lst= list(word)
D_word= {}
for i in lst:
  key= i
  value= lst.count(i)
  D_word.update({key:value})
print(D_word)

#38
def change(string):
      return string[-1:] + string[1:-1] + string[:1]
string= input("Enter string:")
print("Modified string:")
print(change(string))

#39
a= input("Enter a string:- ")
print("Orignal string:- ",a)
b= list(a)
n= len(b)
for i in range(0, n+1, 2):
  b.pop(i)
print(b)

#40
s= input("Enter a string:- ")
print("Orignal string:- ",s)
s1= s.lower()
print("Input string in lower case ->",s1)
s2= s.upper()
print("Input string in upper case ->",s2)

#41
s= "Protect yourself against COVID-19 and stay safe and secure"
print("count of substring AND =",s.count("and"))

#42
s= input("Enter a string:- ")
n= int(input("Enter a number of charachters to be lowercased (from starting):- "))
print(s[:n].lower()+ s[n:])

#43
s= input("Enter a string:- ")
print(s.strip())

#44
def moveSpaces(str1): 
    no_spaces = [char for char in str1 if char!=' ']   
    space= len(str1) - len(no_spaces)
    result = ' '*space    
    return result + ''.join(no_spaces)
str1 = input("Enter string:- ")
print("Original String:\n",str1)
print("\nAfter moving all spaces to the front:")
print(moveSpaces(str1))

#45
from collections import Counter
string= input("Enter the string:- ")
result= Counter(string)
result= max(result, key= result.get)
print("Most frequent character: ",result)

#46
s= input("Enter a number:- ")
print(s[0:1].upper()+s[1:5]+s[-1:].upper())

#47
def sum(ss):
  k= 0
  for i in ss:
    if i.isdigit()==True:
      a= int(i)
      k= k+a
  print("SUM of digits:- ",k)
s= input("Enter a string:- ")
sum(s)

#48
lst= []
n= int(input("Enter a number of words:- "))
for i in range(n):
  l= len(i)
  lst.append(input(i))

#49
def x(N):
  xN= N**2 +1
  print("Result= ",xN)
n= 4
x(n)

# 55
def fact(num):
  n= 1
  for i in range(1,num+1):
    n= n*i
  print("Factorial of",num,"is-> ",n)
num= int(input("Enter the number to find factorial:- "))
fact(num)

#56
def hello(a,b):
  for i in range(a,b+1):
    if i%7==0 and i%9==0:
      print(i)
a= 100
b= 500
print("Multiples of 7 and 9 are:- ")
hello(a,b)

#57
num = int(input("Enter a number:- "))
p = 0
for i in range(2, num):
    if num%i==0:
        p = 1
        break
if p==0:
    print("\nIt is a Prime Number")
else:
    print("\nIt is not a Prime Number")

#58
num = int(input("Enter a number: "))
sum = 0
n = num
while n > 0:
  digit = n % 10
  sum += digit ** 3
  n //= 10
if num == sum:
  print(num,"is an Armstrong number")
else:
  print(num,"is not an Armstrong number")

#59
def ap():
  print("Aayush from method ap...")
def ap1():
  print("Aayush from method ap1...")
  return ap()
returned_function= ap1()
print(returned_function)

#62
lst= []
n= int(input("Enter a number of elements: "))
for i in range(n):
    lst.append(int(input("-> ")))
print(lst)
print(sum(lst))

#63
lst= []
n= int(input("Enter a number of elements: "))
for i in range(n):
  lst.append(float(input("-> ")))
print(lst)
pos= int(input("Enter a position number:- "))
element= float(input("Enter an element to insert: "))
lst.insert(pos, element)
print("List after inserting new element:- \n",lst)

#64
lst= []
n= int(input("Enter a number of elements:- "))
for i in range(n):
  lst.append(int(input("-> ")))
print(lst)
print("Highest element:- ",max(lst))
print("Lowest element:- ",min(lst))

#65
lst= []
n= int(input("Enter a number of elements:- "))
for i in range(n):
  lst.append(int(input("-> ")))
print(lst)
print("Highest element:- ",max(lst))
print("Lowest element:- ",min(lst))

#66
lst= []
n= int(input("Enter the elements: "))
for i in range(n):
  lst.append(float(input("->")))
print(lst)
i= int(input("Enter a index number: "))
lst.pop(i)
print("List after deletion of element: ",lst)

# 67
lst= []
n= int(input("Enter a number of elements:- "))
for i in range(n):
    lst.append(int(input("-> ")))
lst.pop(1)
lst.pop(2)
lst.pop(5)
print(lst)

# 68
def SubList(l):
  lst1= [[]]
  for i in range(len(l)+1):
    for j in range(i):
      lst1.append(l[j:i])
  return lst1
  
lst= []
n= int(input("Enter a number of elements: "))
for i in range(n):
  lst.append(str(input("-> ")))
print(SubList(lst))

# 69
num= int(input("Enter a number:- "))
n= int(input("Enter a number of elements:- "))
lst= []
for i in range(n):
  lst.append(int(input("-> ")))
print(lst)
l= []
for i in lst:
  if i>num:
    l.append(i)
print(l)

# 70
lst= []
n= int(input("Enter a number of elements:- "))
print("Create a list of",n,"integers")
for i in range(n):
  lst.append(int(input("-> ")))
print(lst)
even_lst= []
for j in lst:
  if j%2==0:
    even_lst.append(j)
print(even_lst)