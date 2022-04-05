from datetime import datetime

print('name')
ten = input()
print('tuoi')
tuoi =  input()
nam = datetime.date(datetime.now()).year
nam100tuoi = 100 - int(tuoi) + nam
print('nam ban 100 tuoi la:',nam100tuoi)
