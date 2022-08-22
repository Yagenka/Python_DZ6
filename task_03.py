# Найти сумму чисел списка стоящих на нечетной позиции


from functools import reduce

my_list = [2, 3, 5, 9, 3, 1, 1, 4, 3]
new_list = [my_list[i] for i in range(1, len(my_list), 2)]
summa = reduce(lambda x, y: x + y, new_list)
  
print(f'в списке {my_list} сумма чисел на нечетных позициях {summa}')




