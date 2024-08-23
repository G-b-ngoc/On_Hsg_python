'''
    chuyển đổ hệ 24 giờ sang 12 pm
'''

h = int(input("Giờ: "))
m = int(input("Phút: "))

chuyen_doi = (h - 12 )

if (h >= 24):
    print("Giờ Không hợp lệ")
elif (m >= 60):
    print("Phút không hợp lệ")
elif (chuyen_doi <= 11):
    print(f"{chuyen_doi}:{m} pm")
elif (chuyen_doi > 11 and chuyen_doi <= 12):
    print(f"{chuyen_doi}:{m} am")
    
