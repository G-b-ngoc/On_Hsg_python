'''
    Viết ct tính giá trị biểu thức F(x): 2x^3 + 3x^2 + 5x - 1
    
    cách viết:  2x^3 = 2*x**3
                3x^2 = 3*x**2
                5x = 5*x
'''

x =float(input("cho X:"))

f = (2*x**3 + 3*x**2 + 5*x - 1)
print(round( f , 2))