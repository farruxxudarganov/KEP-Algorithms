# Stringni kesib olish va teskarisiga o'girish
# txt = 'abcd'
# print(txt[1:3]) #bc
# print(txt[0:len(txt)]) #abcd
# print(txt[0::])
# print(txt[::-1])

def reverse_number(number):
    str(number)
    string_number = str(number)
    return int(string_number[::-1])
for num in range(1000,10000):
    reverse_num = reverse_number(num)
    if reverse_num == 4*num:
        print(num)