numbers =  input("Nhập các số nguyên: ").split()
numbers = [int(num) for  num in numbers]
numbers.sort()
print("Danh sach so nguyen:", numbers) 