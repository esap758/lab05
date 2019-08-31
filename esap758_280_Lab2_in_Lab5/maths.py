def add(first, second, third = None):
    if third == None:
        return first + second
    else:
        return convert_base(first + second, third)

def fibonacci(length):
    def internal(first, second, count):
        third = add(first, second)
        count -= 1
        if count == 1:
            return third
        else:
            return internal(second, third, count)

    return internal(0, 1, length)

HEX_CHARS = {
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F'
}

def factorial(number):
    factorial = 1
    if number == 0:
        return 1
    elif number > 0:
        for i in range(1, number+1):
            factorial = factorial * i
        return factorial

def convert_base(num, n):
    """Change a base 10 number to a base-n number. Supports up to base 16. """
    new_num_string = ''
    current = num
    while current != 0:
        remainder = current % n
        if remainder > 9:
            remainder_string = HEX_CHARS[remainder]
        elif remainder >= 36:
            remainder_string = '('+str(remainder)+')'
        else:
            remainder_string = str(remainder)
        new_num_string = remainder_string+new_num_string
        current = current//n
    return new_num_string
