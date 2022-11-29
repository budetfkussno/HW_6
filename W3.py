# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

string = 'Текст текабвст, из которого которогоабв надо удаабвлить удалить'
lst = string.split(' ')

print(lst)
tmp = list(filter(lambda x: 'абв' not in x, lst))
result = ' '.join(tmp)
print(result)