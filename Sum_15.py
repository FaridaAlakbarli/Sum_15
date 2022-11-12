full = list(map(int, input('Enter numbers: ').split()))
summ = sum(full)

if summ > 15 :
    dif = summ - 15
    sorted_full = sorted(full, reverse = True)
    for i in sorted_full:
        if i > dif:
            full[full.index(i)] = i - dif
            dif = 0
        elif i == dif:
            full[full.index(i)] = i - (dif-1)
            dif = 1
        elif i < dif:
            x = (dif - i) + 1
            full[full.index(i)] = i - (dif - x)
            dif = x
elif summ < 15:
    dif = 15 - summ
    sorted_full = sorted(full)
    for i in sorted_full:
        if 9 - i < dif:
            x = (dif - 9) + 1
            full[full.index(i)] = i + (dif - x)
            dif = x
        else:
            full[full.index(i)] = i + dif
            dif = 0
else:
    print('The sum is 15, no need to change! :)')
            
print(full)
