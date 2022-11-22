# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

import random

random_list = [random.randint(1, 20) for i in range(random.randint(10, 30))]
print(random_list)
print(list(set(random_list)))
uniq_list = [i for i in set(random_list) if random_list.count(i) == 1]
print(uniq_list)