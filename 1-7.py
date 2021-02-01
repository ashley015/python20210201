#1-7
q=int(input('輸入英文成績:'))
w=int(input('輸入數學成績:'))
if q >=90 and w >=90:
    print('有獎勵')
elif q <60 and w <60:
    print('有處罰')
elif q <60 or w <60:
    print('再加油')