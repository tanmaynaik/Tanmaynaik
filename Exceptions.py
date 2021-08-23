# Name Error
# name = "Name Error"
# print(nam)

# Overflow Error
i=1
f = 3.0**i
for i in range(100):
    print (i, f)
    f = f ** 2

# Syntax Error
print(()

#Identation Error
    print("Identation error")

# Value Error
i="string"
print(int(i))

# Type Error
b = "String"
print("Type error",b)

# Unbound Local Error
x = 5
def local():
    print(x)
    x = 7
local()

#Zero Division Error
print(5/0)