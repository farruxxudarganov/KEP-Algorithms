
def reverse_number(number):
    string_number = str(number)
    return int(string_number[::-1])
count = 0
for num in reverse_number:
    if num == 0:
        count + 1
    else:
        break
print(count)