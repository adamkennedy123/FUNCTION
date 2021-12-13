import math
 
b = lambda x : x**2
print(b(5))
a = lambda x, y : x**2 + y**2
print(a(10, 2))
c = lambda *args : sum(args)/len(args)
print(c(4))
d = lambda s : "".join(set(s))
print(d(5))