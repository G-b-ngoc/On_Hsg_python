'''
    Viết ct giải phương trình bậc nhất: Ax + B = 0 | 0- b %a = x
'''

# a, b = map(float, input("hệ số a, b = ").split(","))
a = float(input("Hệ số A: "))
b = float(input("Hệ số B: "))

#Đk pt có 1ngh a != 0 
if (a == 0 and b == 0 ):
    print("Pt vô số nghiệm")
 
elif (a == 0 and b != 0):
    print("Pt vn")
    
else:
    x = (- b) / a
    print(f"pt có 1 nghiệm X =1", x)
    
    