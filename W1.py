# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension
# В этом случае можно пропустить совсем тривиальные (т.е. задачу 1 или 2 тут точно решать не имеет смысла) - исходите из уровня группы и студента.

#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

lst = [2, 3, 5, 9, 3]
values_by_index = list(enumerate(lst))
val_maps = list(filter(lambda x: x[0]%2!=0, values_by_index))
result = sum(map(lambda x: x[1], val_maps))
print(result)