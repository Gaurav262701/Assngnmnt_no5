#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Assignement no 5
#proram to find LCM
#Answer no.1
def compute_Lcm(x,y):
    if x > y:
        greater = x
    else:
        greater = y
        
    while(True):
        if ((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
    return lcm
num1 = 50
num2 = 40
print("The L.C.M is ",compute_Lcm(num1,num2))


# In[3]:


#Answer no.2
def compute_Hcf(x,y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1,smaller+1):
        if ((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf
num1 = 50
num2 = 40
print("The H.C.F is",compute_Hcf(num1,num2))


# In[4]:


#Answer no.3
#python program to convert decimal to octal,binary and hexadecimal

decimal = 344
print("The decimal value of " , decimal, "is:")
print(bin(decimal),"in binary")
print(oct(decimal),"in octal")
print(hex(decimal),"in hexadecimal")


# In[6]:


#Answer no.4
#program to find ASCII value in character
a = 'p'
print("The ASCII value of'" + a + "' is ", ord(a))


# In[ ]:


#Answer no.5
#program for simple calculator
def add(x , y):
    return x + y
def subtract(x , y):
    return x - y
def multiply(x , y):
    return x * y
def devide(x , y):
    return x / y
print("Select operation")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.devide")

while True:
    choice = input("Enter choice(1/2/3/4):")
    if choice in ('1', '2', '3' , '4'):
        num1 = float(input("Enter the first number:"))
        num2 = float(input("Enter the second number"))
        
        if choice == '1':
            print(num1 , "+" , num2, "=" , add(num1,num2))
            
        elif choice == '2':
            print(num1, "-" , num2, "=" ,subtract(num1,num2))
            
        elif choice == '3':
            print(num1 , "*" , num2, "=", multiply(num1,num2))
            
        elif choice == '4':
            print(num1 , "/" , num2 , "=" , devide(um1,num2))
        
        next_calculatio = input("Lets do next calculation? (yes/no):")
        if next_calculation == "no":
            break
            
    else:
        print("Invalid input")


# In[ ]:




