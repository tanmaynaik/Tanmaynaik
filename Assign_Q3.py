# In a small company, the average salary of three employees is Rs1000 per week. 
# If one employee earns Rs1100 and other earns Rs500, how much will the third employee earn?

average = 1000
e1 = 1100
e2 = 500

e3 = (average - (e1 + e2)/3)*3                  #Calculating salary of 3rd employee


print("Salary of Third employee is: ", e3)