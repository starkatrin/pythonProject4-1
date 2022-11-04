#задача 2 . Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
import random

def make_sequence():
    sequence = [random.randint(1, 10) for _ in range(random.randrange(1, 20))]
    return sequence
#Если необходимо вывести список без дубликатов:

def unique_elem(sequence):
    unique = []
    for elem in sequence:
        if elem not in unique:
            unique.append(elem)
    return unique

# Или с помощью множества:
# print(list(set(sequence)))

sequence = make_sequence()
unique_elem = unique_elem(sequence)


print(f'Последовательность: {sequence}\nУникальные элементы: {unique_elem}')

# Если нужно удалить все повторяющиеся елементы, тогда:
#un_seq = [elem for elem in sequence if sequence.count(elem) == 1]
#print(f'Уникальные элементы с помощью list comprehensions:'
#     f'{un_seq}')

