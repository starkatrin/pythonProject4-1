#задача 4 необязательная. НА ВХОДЕ ИМЕННО СТРОКА!
# Найдите корни квадратного уравнения, уравнение вводит через строку пользователь.
# например, 6*x^2+5*x+6=0 . Само собой, уравнение может и не иметь решения.
# Предусмотреть все варианты, сделать обработку исключений.


import math

def make_koef(polynom):
    koef = polynom.replace('x^2', ' ').replace('x2', ' ').replace('x', ' ').\
            replace('+', '').replace('x**2', ' ').replace('*', ' ').replace('=0', '')
    koef = koef.split(' ')
    for elem in koef:
        if not elem.lstrip('+-').isdigit():
            koef.remove(elem)
    return koef

polynom = input('Введите квадратное уравнение')
koef = make_koef(polynom)

a, b, c = map(int, koef)
print(f'Коэффициенты:\na = {a}\nb = {b}\nc = {c}')
discr = b ** 2 - 4 * a * c
print('Дискриминант D = %.2f' % discr)


try:
    if discr == 0:
        x = -b / (2 * a)
        print('x = %.2f' % x)
    else:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        print('x1 = %.2f \nx2 = %.2f' % (x1, x2))
except ValueError as ve:
        print('Корней нет')

