def flip_number(num):
    if num // 10 == 0:
        return num
    last = num % 10
    rest = flip_number(num // 10)
    return last * pow(10, len(str(rest))) + rest
print("flip number 133", flip_number(133))
print("flip number 456", flip_number(456))

n = int(input("Enter a number"))

print("flip number" + str(n) ,"=",flip_number(n))