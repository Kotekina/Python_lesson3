# 3. Реализовать функцию my_func(),
# которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(a,b,c):
    my_list = [a,b,c]
    max1 = max(my_list)
    my_list.remove(max1)
    max2 = max(my_list)
    total = max1+max2
    print(total)
my_func(a=100, b=5, c=10)
