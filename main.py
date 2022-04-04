ten,tuoi,nghenghiep = "thanh",22,"technician"

print(type(ten))
print(type(tuoi))
print(type(nghenghiep))

#bai 6: kiểu số trong PYTHON
# lấy toàn bộ thư viện decimal
# từ thư viện decimal-> import vào mọi thứ(*) vào
from decimal import*
# lấy 3 số thập phân Decimal và phần nguyên
getcontext().prec = 3
print(Decimal(10)/3)
d = Decimal(10)/3
print(d)
