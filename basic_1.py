#print("twinkle twinkle little star\n\thow i wonder what you are!\n\t\tup above the word so high\nlike a diamond in the sky")
#show version and version info
'''import sys
print("system version info\n")
print(sys.version_info)
print("system version\n")
print(sys.version)
'''
#show current date and time
'''import datetime
now=datetime.datetime.now()
print("current date and time is")
print (now.strftime("%d-%m-%Y %H:%M:%S"))
'''
#radius input out put area

'''a=float(input("enter the radius of the circle"))
area=3.141*a*a
print(area)
'''
#input 1st and last name of user
'''
firstname=input("enter your first name\n")
lastname=input("enter your last name\n")
print(lastname+" "+ firstname)
'''
#tuple and list input
'''values=input("enter comma seperated numbers")
list=values.split(",")
tuple=tuple( list)
print('list :',list)
print('tuple :',tuple)
'''
#print extension of file name
'''
filename=input("enter file name")
f=filename.split(".")
print(f[1])
'''
#print 1st and last colors of the list
'''
colors=input("enter colors name:\n")
list=colors.split(",")
print(list[0])
print(list[-1])
'''
#print exam date
'''
date=(10,12,2021)
print("exam date is: %i/ %i/ %i"%date)
'''
#print a number in format  a+aa+aaa
'''
number=int(input("enter a number\n"))
n1=int("%s"%number)
n2=int("%s%s"%(number,number))
n3=int("%s%s%s"%(number,number,number))
sum=n1+n2+n3
print(sum)
'''
#python docstring
'''
print(abs.__doc__)
print(print.__doc__)
'''
#print calendar
'''
import calendar
i=0
while 1:
    if(i==2):
        break
    i=i+1 
    x=int(input("enter month:\n"))
    y=int(input("enter year:\n"))
    print(calendar.month(y,x))
'''
#print a format string
'''
print('''
'''
a string that you "don't" have to escape
This
is a ....... multi-line
#heredoc string --------> example'''


#no. of days between 2 given dates 
'''
from datetime import date
ldate=date(2021,3,31)
fdate=date(1999,3,31)
noday=ldate-fdate
print(noday)
'''
#volume of sphere
'''
pi=3.14
r=6
volume=4.0/3.0*pi*r**3
print("volume of sphere is : ",volume)
'''
#absolute difference
'''
n=int(input("enter a number: \n"))
gn=17
if(n>gn):
    print(abs(2*(n-gn)))
else:
    print(abs(n-gn))
'''
#test whether a number is within 100 of 1000 or 2000
'''
def near_thousand(n):
    return (abs(1000-n)<=100 or abs(2000-n)<=100)
print(near_thousand(100))
print(near_thousand(800))
'''
#calculate the sum of three given numbers, if the values are equal then return three times of their sum
'''
a=int(input("enter a number:\n"))
b=int(input("enter a number:\n"))
c=int(input("enter a number:\n"))
def sumthrice(a,b,c):
    sum=a+b+c
    if a==b==c:
        sum=sum*3
    
    return sum

print(sumthrice(a,b,c))
'''
#to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string
'''
string=input("enter a string\n")
def returnstr(str):
    if len(string)>=2 and string[:2]=="is" :
        return string
    return "is"+string
print(returnstr(string))
'''
# get a string which is n (non-negative integer) copies of a given string.
'''
def ncopiesstring(str,n):
    for i in range (n):
        print(str)
string=input("enter a string\n")
n=int(input("enter a number \n"))
print(ncopiesstring(string,n))
'''
#numbers of 4 in a given list
'''
def countfour(lists):
    count=0
    for x in lists:
        if x==4:
            count=count+1
    return count
lists=[1,2,4,5,5,4,6,4,7]
print(countfour(lists))
'''
#to get the n (non-negative integer) copies of the first 2 characters of a given string.
'''
def character2(str,n):
    string=" "
    x=str[:2]
    for i in range(n):
        string=string+x
str=input("enter a string\n")
n=int(input("enter a number\n"))
print(character2(str,n))
'''

















