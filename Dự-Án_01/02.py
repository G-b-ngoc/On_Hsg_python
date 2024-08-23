numbers = input("nhập các số nguyên cách nhau bằng dấu cách: ").split()
numbers = [int(num) for num in numbers]

numbers.sort()
print("Danh sách số nguyên đã sắp xếp:", numbers)