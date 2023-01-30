#!/usr/bin/env python
# coding: utf-8

# In[1]:


#get & set methods
class Student:
    name="Random Name"
    __rollnumber=100
    def get_rollnumber(self):
        return self.__rollnumber
    def set_rollnumber(self,newvalue):
        self.__rollnumber=newvalue
obj=Student()
print(obj.name)
print(obj.get_rollnumber())


# In[4]:


#Multiple Inheritance
class A:
    def m1(self):
        print("In class A")
class B:
    def m1(self):
        print("In class B")
class Child(A,B):
    pass
ob=Child()
print(ob.m1())


# In[6]:


#task-1
n=int(input())
l=[]
for i in range(0,n):
    a=input("Username:")
    b=input("Password:")
    l.append({a:b})
print(l)


# In[9]:


#task-2
n=int(input())
l=[]
for i in range(0,n):
    a=input("Username:")
    b=input("Password:")
    l.append({a:b})
print(l)
x=input("Username:")
y=input("Password:")
f=False
for j in l:
    try:
        b=j[x]
        f=True
        if y==b:
            print("Valid Password")
        else:
            print("Invalid Password")
    except:
        pass
if f==False :
    print("User Not Found")


# In[12]:


#Stack
stack=[]
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
stack.append(5)
print(stack)
stack.pop(0)
print(stack)


# # Rock Paper Scissor Game (player vs computer)

# In[23]:


from random import randint
arr=['rock','paper','scissor']
user=input(f"Choose from {arr}").lower()
com=arr[randint(0,2)]
print("Computer chooses:",com)
if user==com :
    print("Draw Match")
elif user=='paper' and com=='rock':
    print("Player 1 wins")
elif user=='rock' and com=='scissor':
    print("Player 1 wins")
elif user=='scissor' and com=='paper':
    print("Player 1 wins")
else:
    print("Computer Wins")


# In[37]:


#Game with so many choices
from random import randint
arr=['rock','paper','scissor']
l=3
ps=0
cs=0
while True:
    user=input(f"Choose from {arr}").lower()
    com=arr[randint(0,2)]
    print("Computer chooses:",com)
    if user==com :
        print("Draw Match")
    elif user=='paper' and com=='rock':
        print("Player 1 wins")
        ps+=1
    elif user=='rock' and com=='scissor':
        print("Player 1 wins")
        ps+=1
    elif user=='scissor' and com=='paper':
        print("Player 1 wins")
        ps+=1
    else:
        print("Computer Wins")
        cs+=1
    if ps==l or cs==l:
        break
print(ps)
print(cs)
if ps>cs:
    print("Player 1 Wins the game")
else:
    print("Computer Wins the game")


# In[ ]:




