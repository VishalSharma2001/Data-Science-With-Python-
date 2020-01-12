#!/usr/bin/env python
# coding: utf-8

# In[2]:


def Hello():
    print("Hello vishal")
#Hello()


# In[3]:


# no argument no return type
def sum():
    var1=int(input("Enter the first value:"))
    var2=int(input("Enter the second value"))
    var3=var1+var2
    print("Sum is:",var3)
sum()


# In[5]:


#with argument and no return
def sub(var1,var2):
    var3=var1-var2
    print("sub is:",var3)
sub(12,6)    


# In[18]:


# no argument with return type
def mul():
    var1=int(input("Enter the first value:"))
    var2=int(input("Enter the second value"))
    var3=var1*var2
    return var3
var4=mul()
print(var4)


# In[19]:


# with return type and argument
def dev(var1,var2):
    var3=var1/var2
    return var3
var4=dev(6,2)
print(var4)


# In[ ]:




