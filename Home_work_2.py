import math

side_a = float(input("side a ="))
side_b = float(input("side b =")) 
side_c = float(input("side c ="))

p = (side_a + side_b + side_c ) / 2 
print("p =",p)

S = math.sqrt(p*(p-side_a) * (p-side_b) * (p-side_c))
print("S =",S)



