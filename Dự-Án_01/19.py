'''
    Viết ct giải phương trình bậc hai: ax^2 + bx + c = 0 (a != 0)
'''

#nhập tự bàn phím
a = float(input("Hệ số a: "))
b = float(input("Hệ số b: "))
c = float(input("Hệ số c: "))

x = (b**2 - 4 * a *c)
xk = (-b / 2* a)
x1 = (-b + x**(1/2))/ 2* a
x2 = (-b - x**(1/2))/ 2* a
#đk
if (a == 0 ):
    print("pt không hợp lệ")
elif (x == 0):
    print(f"pt có nghiệm kép x1 = x2 = {xk}")
elif ( x < 0):
    print("pt vô nghiệm")
else:
    print(f"Có hai nghiệm: x1= {x1}, x2 = {x2}")
    


