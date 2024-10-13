import math

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = [int(math.fabs(len(i) - len(j))) for i, j in zip(first, second) if len(i) != len(j)]
second_result = [True if len(first[i]) == len(second[i]) else False for i in range(0, len(first))]

print(list(first_result))
print(list(second_result))
