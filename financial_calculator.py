#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math


print("Investment  - to calculate the amount of interest you will earn on interest")  
print("Bond        - to calculate the amount you will have to pay on a home loan\n")   
print("Choose between 'investment' or 'bond' from the menu below to proceed\n")
selection = str(input())



if selection.lower() == "investment":
    print("Enter the amount you want to deposit: ")
    inv = int(input())
    print("Enter the interest rate(%): ")
    interest_Rate = int(input())
    print("Enter the number of years you are planning to invest:")
    intYears= int(input()) 
    print("Do you want to calculate in simple or compound interest(enter 's' for simple and 'c' for compound interest)")
    interest = input()


    if(interest == "s"):
        simple_int = inv*(interest_Rate/100)*intYears
        simple_total = inv + simple_int
        print("R",simple_total)
    if(interest == "c"):
        compound_int = inv * math.pow((1+interest_Rate),intYears)
        print("R", compound_int )
        
        
elif selection.lower() =="bond":
    print("Enter the present value of the house:")
    house_val = input()
    print("Enter the interest rate:")
    int_rate = input()
    print("Enter the number of months they plan to take to repay the bond:")
    num_Months_repay = input()
    calculation=(((float(int_rate)/100)/12) *float(house_val)) / (1-math.pow((1+ ((float(int_rate) /100) /12)), -(float(num_Months_repay))))
    print("The amount of money you would need to repay is: R"+ str(round(calculation, 2)))

    
elif selection !="bond":
    print("Input Error! Run program again")
    


# # 

# In[1]:





# In[ ]:




