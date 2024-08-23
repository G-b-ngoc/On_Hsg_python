'''
    Viết ct ktr năm nhuận
'''

y = int(input("Nhập năm cần ktr: "))

if (y < 1582) :
    print(f"{y} Không tính theo lịch Gregorius")

elif ( y % 400 ==0 or (y % 4 ==0 and y % 100 !=0)):
    print(f"{y} Là năm nhuận")

else:
    print(f"{y} Không phải năm nhuận")

