def month_of_season(a):
    if a == 1 or a== 2 or a== 12:
        return 'qish'
    elif a == 3 or a == 4 or a == 5:
        return 'bahor'
    elif a == 6 or a== 7 or a == 8:
        return 'yoz'
    elif a == 9 or a == 10 or a == 11:
        return 'kuz'

print(month_of_season(7))
print(month_of_season(1))
print(month_of_season(4))
print(month_of_season(9))