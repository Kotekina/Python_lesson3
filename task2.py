# 2. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def my_func (name, surname, yaer, city, email, mob):
    print(name, surname, yaer, city, email, mob)
my_func(name = "Svetlana", surname = 'Kot', yaer = '1985', city = 'Moscow', email = 'mail.com', mob = '89999999999')