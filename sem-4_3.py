#задача 3. Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
#*Пример:*
#- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

def write_file(polynomial):
    with open('polynomial.txt', 'w') as data:
        data.write(polynomial)

def make_koef(k):
    list_of_koef = [randint(0, 10) for _ in range(0, k+1)]
    if list_of_koef[-1] == 0:
        list_of_koef[-1] = randint(1, 10)
    return list_of_koef


def make_polynomial(list_of_koef):
    polynomial = []
    for i in range(len(list_of_koef)):
        if list_of_koef[i] != 0:
            a = f'{list_of_koef[i]}*x^{i}'
            polynomial.append(a)
        else:
            polynomial += ''
    polynomial = polynomial[::-1]
    return '+'.join(polynomial).replace('x^1', 'x').replace('*x^0', '').replace('1*x', 'x')+'=0'

try:
    k = int(input('Введите натуральную степень:'))
except ValueError:
    k = int(input('Необходимо ввести натуральное число:'))

list_of_koef = make_koef(k)
polynomial = make_polynomial(list_of_koef)
write_file(polynomial)

print(list_of_koef)
print(polynomial)
