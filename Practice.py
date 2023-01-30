#!/usr/bin/env python
# coding: utf-8

# In[1]:


n=int(input())
for i in range(n):
    for j in range(i+1):
        print(j+1,end="")
    print("\n")


# In[2]:


n=int(input())
i=1
while(i<=n):
    j=1
    while(j<=n):
        if j<i:
            print(' ',end=' ')
        else:
            print('@',end=' ')
        j=j+1
    i=i+1
    print()
    


# In[11]:


n=int(input("Enter no. of rows:"))
i=1
while i<n:
    j=n
    while j>i:
        print(' ',end=' ')
        j-=1
    print('*',end=' ')
    k=1
    while k<2*(i-1):
        print(' ',end=' ')
        k+=1
    if i==1:
        print()
    else:
        print('*')
    i+=1
i=n-1
while i>=1:
    j=n
    while j>i:
        print(' ',end=' ')
        j-=1
    print('*',end=' ')
    k=1
    while k<2*(i-1):
        print(' ',end=' ')
        k+=1
    if i==1:
        print()
    else:
        print('*')
    i-=1


# In[12]:


word="India"
x=""
for i in word:
    x+=i
    print(x)


# In[9]:


rows=5
k=2*rows-2
for i in range(0,rows):
    for j in range(0,k):
        print(end=" ")
    k=k-1
    for j in range(0,i+1):
        print("* ",end="")
    print("")
k=rows-2
for i in range(rows,-1,-1):
    for j in range(k,0,-1):
        print(end=" ")
    k=k+1
    for j in range(0,i+1):
        print("* ",end="")
    print("")


# In[21]:


a=int(input('a:'))
r=int(input('r:'))
for i in range(0,r):
    for j in range(0,i+1):
        ch=chr(a)
        print(ch,end=' ')
        a+=1
    print(" ")


# In[26]:


a = 65
r = 5
m = (2*a) -2
for i in range(0, r):
    for j in range(0, m):
        print(end=" ")
    m = m - 1
    for j in range(0, i+1):
        ch = chr(a)
        print(ch, end=' ')
        a+=1
    print(" ")


# In[27]:


rows = 10
for i in range(1, rows+1):
    for j in range(1, i+1):
        print(i*j, end=" ")
    print()


# In[31]:


#function syntax
'''
def username(arg1,arg2,......,n):
----------
----------
return
'''
def diff(a, b):
    return a-b
x = 20
y = 10
operation = diff
print(operation(x,y))


# In[33]:


#program to display a string n number of times
def fun():
    for i in range(5):
        print("Hi! Welcome")
fun()


# In[34]:


def diff(a, b):
    result = a-b
    print("Difference of a&b is:", result)
a=20
b=10
diff(a,b)


# In[2]:


m=int(input())
n=int(input())
if(m<1 or n<1 or m>n):
    print("Provide valid input")
else:
    while(m<=n):
        if(m==2):
            print(m,end=" ")
        elif(m==1):
            m+=1
            continue
        else:
            flag=0
            for i in range(2,m//2+1):
                if m%i==0:
                    flag=1
                    break
            if flag==0:
                print(m,end=" ")
        m+=1


# In[3]:


#x-pattern
n=int(input("Enter the size:"))
val=n*2-1
for i in range (1,val+1):
    for j in range(1,val+1):
        if i==j or j==val-i+1:
            print('*',end='')
        else:
            print(' ',end='')
    print()


# In[ ]:


#plus-pattern
size=int(input("Enter the size:"))
for i in range(1,2*size):
    for j in range(1,2*size):
        if i==size or j==size:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()


# In[1]:


#writing a function to understood a mismatch parameters
def fun(i):
    print("Orange",i)
fun(5+2*4)


# In[2]:


#program to demo key args
def display(str,int_x,float_y):
    print("The String is:",str)
    print("The Integer is:",int_x)
    print("The Float is:",float_y)
display(float_y=5678.9998,str="hi",int_x=1234)


# In[3]:


#lambda function
addition=lambda x,y,z:x+y+z
print("Sum=",addition(10,20,30))


# In[4]:


1.lambda fun have no names
2.It can take n no.of attributes
3.It can only return 1 value
4.lambda fun cannot access global variable
5.cannot access var other than their parameters list
6.cannot contain multi parameters
7.does not have explicit return statements


# In[7]:


#program to find smaller number by lambda
def small(a,b):
    if(a<b):
        return a
    else:
        return b
add=lambda x,y:x+y
diff=lambda x,y:x-y
print("Smaller of two no.:",small(add(-3,-2),diff(-1,2)))


# In[10]:


#program to increment a number by lambda
def increment(y):
    return(lambda x:x+1)(y)
a=100
print("a=",a)
print("a after incrementing")
b=increment(a)
print(b)


# In[11]:


#program to pass a lambda fun as an function org
def fun(f,n):
    print(f(n))
twice= lambda x:x*2
triple=lambda x:x*3
fun(twice,4)
fun(triple,3)


# In[12]:


x=lambda:sum(range(1,11))
print(x())


# In[13]:


#swap using functions 
def shifth(a,b):
    a,b=b,a
    print("After swap")
    print("A=",a)
    print("B=",b)
a=int(input("A="))
b=int(input("B="))
print("Before Swap")
print("A=",a)
print("B=",b)
shifth(a,b)


# In[14]:


#write a program to return the full name of a person where 1st variable passed is first name , 2nd variable passed is last name
def name(fn,ln):
    s=' '
    n=fn+s+ln
    return n
print(name("G","Vaishnavi"))


# In[19]:


#write a program to calculate SI. Suppose the customer is a senior citizen.He is being offered 12% ROI;for all other customers, 
#the ROI is 10%
def fun(age):
    if age>60:
         
    else:
        
age=int(input("Enter age:"))
p=200
r=3
fun(age)
si = p*r*ROI/100
print(si)


# In[20]:


#factorial 
def fact(n):
    if(n==1 or n==0):
        return 1
    else:
        return n*fact(n-1)
n= int(input())
print(fact(n))


# In[22]:


#program to find the exp(x,y) using recursion function
def expo(x,y):
    if y==0:
        return 1
    else:
        return(x*expo(x,y-1))
n=int(input())
m=int(input())
print("Result=",expo(n,m))


# In[1]:


#program to find the fibonacci series
def fib(n):
    if n<2:
        return 1
    return(fib(n-1)+fib(n-2))
n=int(input())
for i in range(n):
    print("Fibonacci(",i,")=",fib(i))


# In[4]:


def fun(n,s,d,a):
    if n==1:
        print("Move disk 1 from Source",s,"to Destination",d)
        return
    fun(n-1,s,a,d)
    print("Move disk",n,"from source",s,"to destination",d)
    fun(n-1,a,s,d)
    
n=int(input("Enter no.of disks:"))
fun(n,'A','B','C')


# In[6]:


#tower of hanoi iteration process
def hanoi(n,A,B,C):
    if n>0:
        hanoi(n-1,A,C,B)
        if A:
            C.append(A.pop())
        hanoi(n-1,B,A,C)
A=[1,2,3,4]
B=[]
C=[]
print(A,B,C)
hanoi(len(A),A,B,C)
print(A,B,C)


# In[8]:


#check if two strings match where one string contains wildcard characters
def solve(a,b):
    n,m=len(a),len(b)
    if n==0 and m==0:
        return True
    if n>1 and a[0]=='+'and m==0:
        return False
    if(n>1 and a[0]=='?')or(n!=0 and m!=0 and a[0]==b[0]):
        return solve(a[1:],b[1:])
    if n!=0 and a[0]=='*':
        return solve(a[1:],b)or solve(a,b[1:])
    return False
x=str(input("Enter the string with char:"))
y=str(input("Enter the string for match:"))
print("With Wild characters:",x)
print("Without wild characters:",y)
print(solve(x,y))


# In[17]:


n=int(input())
list=[]
for i in range(1,n+1):
    if i<=0:
        print("Invalid Input")
    elif(i%2):
        list.append(i)
    #if(i//(2n-1)):
        #list.append(b)
print(list)

