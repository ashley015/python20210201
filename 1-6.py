#1-6
q=int(input('請輸入成績:'))
if q >100:
    print('輸入錯誤')
elif q<0:
     print('輸入錯誤')
elif q>=90:
    print('A')
elif q>=80:
    print('B')
elif q>=70:
    print('c')
elif q>=60:
    print('D')
else:
    print('E')
    