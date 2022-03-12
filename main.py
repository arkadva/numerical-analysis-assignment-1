from math import fabs

eps = 1.0
while eps + 1 > 1:
    eps /= 2
eps *= 2
print("The machine epsilon is:", eps)

# mathematically incorrect output
print(fabs(3.0*(4.0/3.0-1)-1))

# mathematically correct outputs
print(fabs(3.0*(4.0/3.0-1)-1) - eps) # דרך ראשונה
print(fabs((3.0*4.0/3.0-3.0*1)-1)) # דרך שניה - פתיחת סוגריים מתמטית
