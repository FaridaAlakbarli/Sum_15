def change_to_15(lis):
    summ = sum(lis)
    if summ > 15 :
        dif = summ - 15
        sorted_list = sorted(lis, reverse = True)
        for i in sorted_list:
            if i > dif:
                lis[lis.index(i)] = i - dif
                dif = 0
            elif i == dif:
                lis[lis.index(i)] = i - (dif-1)
                dif = 1
            elif i < dif:
                x = (dif - i) + 1
                lis[lis.index(i)] = i - (dif - x)
                dif = x
    elif summ < 15:
        dif = 15 - summ
        sorted_list = sorted(lis)
        for i in sorted_list:
            if 9 - i < dif:
                x = (dif - 9) + 1
                lis[lis.index(i)] = i + (dif - x)
                dif = x
            else:
                lis[lis.index(i)] = i + dif
                dif = 0
    else:
        print('The sum is 15, no need to change! :)')
    
    print(lis)            

n = list(map(int, input('Enter 3 numbers: ').split()))
change_to_15(n)
