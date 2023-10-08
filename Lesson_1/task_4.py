# Задача: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input("Введите один размер шоколадки в дольках: "))
m = int(input("Введите другой размер шоколадки в дольках: "))
k = int(input("Введите количество долек, которое хотите отломить: "))
if k < m * n and (k % m == 0 or k % n == 0):
    print('Да')
else:
    print('Нет')