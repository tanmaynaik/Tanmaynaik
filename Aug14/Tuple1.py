l = ("python",2021,"java","potato","12ka4","apple",3.14,9000,1200,"ip")

# Extract all list
print ("Extract all list",l)

# Extract index number 2 to 5
print ("Index number 2 to 5",l[2:5])

# Print list element reverse
print ("Reverse elements",l[::-1])

# Use append,insert add element 
y = list(l)
y.append("banana")
l = tuple(y)
print("Added an element",l)                 #Added element in tuple

y.remove("banana")
l = tuple(y)
print("Delete an element",l)                #Deleted element in tuple
