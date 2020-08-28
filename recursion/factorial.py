
def factorial(num):
    result = num
    for i in range(1, num):
        result *= i
    return result


def resursion1(num):
    if num == 1:
        return 1
    else:
        return resursion1(num - 1) * num


print(factorial(5000))
