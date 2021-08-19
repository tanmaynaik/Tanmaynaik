# Write Programm to calculate GST i.e. 18% on base price 34900/-
a = 34900

# Calculating GST
gst = (18 * a) / 100
print ("GST amount is: ",gst)



# Write programm to calculate monthly simple intrest and compound intrest(5%/Month) on amount - 161258/-
p = 161258
r = 5
n = 1

# Calculating Simple Interest
si = (p * r * n) / 100
print ("Simple Interest: ",si)

# Calculating compound interest
amount = p * (pow((1 + r / 100),n))
ci = amount - p
print ("Compound Interest: ",ci)
