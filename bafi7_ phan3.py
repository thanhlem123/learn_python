# kiểu toán tự %
a = 'thanh nam nay %s %s tuoi' %('2','2')
print(a)
b = 'thanh nam nay %s tuoi'
print(b %('22'))
c =  '%d'%(10/3) # chỉ lấy phần nguyêb
print(c)
d = '%.0f' %(3.5312391) # lấy 3 số ở phần thực. làm tròn lên khi phần thực lên đến .5
print(d)
tên = 'thanh' # tác dụng của f trong Python là thay thế
tuoi = '22'
result =  f'hc sinh:{tên}\nage{tuoi}
print(result)
# căn lề cho chuỗi giữa ^, trái<, phải>
q = '{:^45}'.format('toi la thanh')
print(q)