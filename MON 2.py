#!/usr/bin/env python
# coding: utf-8

# In[5]:


n=int(input())
m=list(map(int,input().strip().split()))
a=[]
b=[]
for i in m:
    if i%2==0:
        a.append(i)
    else:
        b.append(i)
c=a+b
print(*c,sep=" ")


# In[14]:


x=int(input())
l=[10,98,3,33,12,22,21,11]
l1=[]
l2=[]
for i in l:
    if i%2==0:
        l1.append(i)
    else:
        l2.append(i)
m=l1+l2
print(m,end=" ")


# In[ ]:


'''
Input:
Keys=['NAME','AGE','BRANCH']
Values=['ABC','100','AERONAUTICAL']
'''


# In[13]:


keys=['NAME','AGE','BRANCH']
values=["ABC",100,"AERONAUTICAL"]
details=zip(keys,values)
Dict=dict(details)
print(Dict)


# In[19]:


#WRITE A PROGRAM TO STORE A SPARSE MATRIX IN TO A DICTIONARY
#EXAMPLE:[[0,0,0,1,0],[2,0,0,0,3],[0,0,0,4,0]]
m=[[0,0,0,1,0],
   [2,0,0,0,3],
   [0,0,0,4,0]]
dic={}
for i in range(len(m)):
    print("\n")
    for j in range(len(m[i])):
        print(m[i][j],end=" ")
        if m[i][j]!= 0:
            dic[i,j]=m[i][j]
print(dic)


# In[23]:


#PRINT A NON-REPEATED CHARACTER IN A STRING
#EXAMPLE: I/P:1.'LEVEL'
#         O/P:2. V
S="level"
for i in S:
    c=0
    for j in S:
        if i==j:
            c+=1
        if c>1:
            break
    if c==1:
        print(i)


# In[31]:


#Write a program to insert,delete a node in a single-linked list
#ex:1 3 5 8
class Node:
    def __init__(self,num):
        self.num=num
        self.next=None
class llist:
    def __init__(self):
        self.head=None
    def push(self,newnum):
        newnode=Node(newnum)
        newnode.next=self.head
        self.head=newnode
    def insertnext(self,prenode,newnode):
        if prenode is None:
            print("The Previous Node")
            return
        newnode=Node(newnum)
        newnode.next=prenode.next
        prenode.next=newnode
    def append(self,newnum):
        newnode=Node(newnum)
        if self.head is None:
            self.head=newnode
            return
        last=self.head
        while(last.next):
            last=last.next
        last.next=newnode
    def printnum(self):
        t=self.head
        while(t):
            print(t.data)
            t=temp.next
if __name__=='__main__':
    l1=llist()
    l1.append(1)
    l1.append(3)
    l1.append(5)
    l1.append(8)
print(printnum)


# In[32]:


s1=input()
s2=input()
if(sorted(s1)==sorted(s2)):
    print("Yes")
else:
    print("No")


# In[ ]:




