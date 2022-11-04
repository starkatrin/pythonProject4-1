#задача 1. Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.

def factor(n):
    factors = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            n //= i
            factors.append(i)
        i += 1
    if n > 1:
        factors.append(n)
    return factors


try:
    n = int(input('Введите натуральное число:'))
except ValueError:
    n = int(input('Необходимо ввести натуральное число:'))

print(factor(n))