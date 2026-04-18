# "123" => "1", "2", "3"
def sum_digits(number):
    s = 0
    for digit in str(number):
        raqam = int(digit)
        s+=raqam
    
    return s
print(sum_digits(123))