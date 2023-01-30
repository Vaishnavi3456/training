#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Program to access a class var using a class, object

class abc:
    var=22
obj=abc()
print(obj.var)


# In[2]:


#Program to access a class member using class obj

class abc:
    var=22
    def display(self):
        print("This is Class Method")
obj=abc()
print(obj.var)
obj.display()


# In[3]:


#program to illustrate the constructor
#__init__()............method

class abc:
    def __init__(self , val):
        print("In Class Method")
        self.val=val
        print("The Value is:",val)
obj=abc(10)


# In[5]:


#Program to differentiate bteween class and obj variable
class abc():
    class_var=0   #class variable
    def __init__(self,var):
        abc.class_var+=1
        self.var=var    #obj variable
        print("The Obj variable is:",var)
        print("The Class value of c-=var:",abc.class_var)
obj1=abc(10)
obj2=abc(20)
obj3=abc(30)


# In[8]:


#Program for illustrating a modification on numerics
class Number:
    even=0   #default val
    def check(self,num):
        if num%2==0:
            self.even=1
    def even_odd(self,num):
        self.check(num)
        if self.even==1:
            print(num,"is even")
        else:
            print(num,"is odd")
obj=Number()
obj=
obj


# In[10]:


#Program for illustrating a modification on numerics
class Number:
    evens=[]
    odds=[]
    def __init__(self,num):
        self.num=num
        if num%2==0:
            Number.evens.append(num)
        else:
            Number.odds.append(num)
n1=Number(21)
n2=Number(32)
n3=Number(43)
n4=Number(54)
n5=Number(65)
print("Even Numbers are:",Number.evens)
print("Odd Numbers are:",Number.odds)


# In[22]:


#delete method---C++/Java analogus to destructor
#general syntax: __del__
class abc():
    class_var=0
    def __init__(self,var):
        abc.class_var+=1
        self.var=var
        print("The obj value is:",var)
        print("The class value:",abc.class_var)
    def __del__(self):
        abc.class_var-=1
        print("Object with value %d is going out of scope",self.var)
obj1=abc(11)
obj2=abc(22)
obj3=abc(33)
del obj1
del obj2
del obj3


# In[ ]:


(1)__repr__-----syntax report of the object
(2)__cmp__-----compares two class object
(3)__len__-----len(object)
(4)__call__-----It acts like a func to call its instances
(5)__it__,__le__,__eq__,__ne__,__gt__,__ge__,__cmp__-----compares two  objects
(6)__iter__-----iteration over an object
(7)__getitem__-----used for indexing
gs: def __getitem_(self,var/key)
(8)__setitem__----- assign an item to the indexed value


# In[26]:


#program to demonstrate get and set items in a list
class numbers:
    def __init__(self,mylist):
        self.mylist=mylist
    def __getitem__(self,index):
        return self.mylist[index]
    def __setitem__(self,index,val):
        self.mylist[index]=val
numlist=numbers([1,2,3,4,5,6,7,8,9])
print(numlist[3])
print(numlist.mylist)
numlist[3]=10
print(numlist.mylist)
print(numlist[3])


# In[32]:


class ABC:
    def __init__(self,name,var):
        self.name=name
        self.var=var
    def __repr__(self):
        return repr(self.var)
    def __len__(self):
        return len(self.name)
    def __cmp__(self,obj):
        return self.var-obj.var
obj=ABC("abcdef",10)
print("The value stored in obj is:",repr(obj))
print("The length of the name stored in obj:",len(obj))
obj1=ABC("ghijkl",1)
val=obj.__cmp__(obj1)
if val==0:
    print("Both values are equal")
elif val==-1:
    print("1st value is less than 2nd")
else:
    print("2nd value is less than 1st")


# In[41]:


#is for illustrating use of a private method
class abc():
    def __init__(self,var):
        self._var=var
    def __display(self):
        print("This from class method,var=",self._var)
obj = abc(10)
obj._abc__display()


# In[42]:


#program to show how a class method calls a function which defined in the global name space
def scale_10(x):
    return x*10
class abc():
    def __init__(self,var):
        self.var=var
    def display(self):
        print("Var is =",self.var)
    def modify(self):
        self.var=scale_10(self.var)
obj=abc(10)
obj.display()
obj.modify()
obj.display()


# In[ ]:


#built-in attributes
#for get set and delete
1..hasattr(obj,name)-checks obj possesses the attributes values or not
2..getattr(obj,name[,default])
3..setattr(obj,name,value)--which is used to set an attribute of the obj
4..delattr(obj,name)


# In[ ]:


built-in class attributes
1. .__dict__
2. .__doc__
3. .__name__
4. .__bases__ #we use it mostly for inheritance


# In[44]:


import gc
print("Garbage collection threeshold:",gc.get_threshold())


# In[46]:


m=int(input())
n=int(input())
Numcount=0
for i in range(m,n+1):
    if (i%7==0) and (i%5==0):
        Numcount=Numcount+1
print(Numcount)


# In[ ]:




