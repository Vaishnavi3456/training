#!/usr/bin/env python
# coding: utf-8

# In[5]:


n=int(input())
m=str(input())
max=0
count=0
flag=0
arr=list(m)
for i in range(0,n):
    if(arr[i]=='1'):
        count=count+1;
        flag=1
    elif(arr[i]=='0' and flag==--1):
        count=0
        flag=0
    if count>max:
        max=count
print(max)


# In[10]:


v=int(input())
w=int(input())
if(2<=w and w%2==0 and v<w):
    a=((4*v)-w)//2
    b=v-a
    print("TW=",a,"FW=",b)
else:
    print("Invalid Input")


# In[ ]:


#Binary trees
class bt:
    def __init__(self,data):
        self.data=data
        self.lc=None
        self.rc=None
def insert(root,newvalue):
    if root is None:
        root=bt(newvalue)
        return root
    if newvalue<root.data:
        root.lc=insert(root.lc,newvalue)
    else:
        root.rc=insert(root.rc,newvalue)
    return root
def inorder(root):
    if root=None:
        return 
    inorder(root.lc)
    print
    inorder(root.rc)
root=insert(None,15)
insert(root,10)
insert(root,24)
insert(root,5)
insert(root,14)
insert(root,22)
insert(root,55)
print("Inorder Traversal of a bat")

