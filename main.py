# упаковка данных для функции
# в кортеж
# def func(*args, num=10):
#     print(args)
#     info = list(args)
#     print(info)
#     print(num)
#
#
# func()
# func(1, 4, 2, "Hello")


# def func(num, **kwargs):
#     print(kwargs)
#     print(num)
#
#
# func(num=10)
# func(num=22, num2=33, num1=10)


# def test_func(*args, **kwargs):
#     print(f"args: {args}")
#     print(f"kwargs: {kwargs}")
#
#
# test_func("one", "two", "three", first="Vasya", second="Petya", age=123)

###
# распаковка данных для функций
# кортеж
# def func(a: int, b, c, d):
#     print(a, b, c, d)
#
#
# nums = (2, 1, 5, 2)
# func(*nums)
#
#
# # словарь
# def func(name, age, hobby):
#     print(f"Name: {name} age: {age} hobby: {hobby}")
#
#
# users = {
#     "name": "Vasya",
#     "age": 33,
#     "hobby": "test"
# }
#
# func(**users)

########
###
# def func(name, age, hobby):
#     print(f"Hello, {name} your age: {age} and hobby: {hobby}")
#
#
# user_info = ("Vasya", 33, "swimming")
#
# users = {
#     1: ("Vasya", 33, "swimming"),
#     2: ("Petya", 44, "swimming"),
#     3: ("Ivan", 55, "swimming")
# }
# # передаем список с кол-вом значений эквивалентным количеству параметров функции
# for key in users:
#     # func(users[key][0], users[key][1], users[key][2])
#     func(*users[key])

# func(user_info[0], user_info[1], user_info[2])
# func(*user_info)

###
# users = {
#     "admin": ("Vasya", 33, "swimming"),
#     "moderator": ("Petya", 44, "swimming"),
#     "user": ("Ivan", 55, "swimming")
# }
#
#
# def show_roles_and_users(admin, moderator, user):
#     def func(name, age, hobby):
#         print(f"Hello, {name} your age: {age} and hobby: {hobby}")
#
#     print(f"Admin info: {admin}")
#     print(f"Moderator info: {moderator}")
#     print(f"User info: {user}")
#
#     func(*admin)
#     func(*moderator)
#     func(*user)
#
#
# show_roles_and_users(**users)

##########
# def outer():
#     number = 1
#
#     def inner():
#         nonlocal number
#         number += 1
#         print(number)
#
#     return inner
#
#
# my_func = outer()
# my_func()
# my_func()

#########
# def add(num1): return lambda num2: num1 + num2
#
#
# n1 = 3
# test_add_func = add(n1)
#
# for i in range(2, 10):
#     print(f"{n1} + {i} = {test_add_func(i)}")

####
# Карринг — это преобразование функции от многих аргументов в набор функций,
# каждая из которых является функцией от одного аргумента.
# Мы можем передать часть аргументов в функцию и получить обратно функцию, ожидающую остальные аргументы.
names = ["Vasya", "Petya", "Anton", "Petro"]


# без карринга
# def hello(greeting, name):
#     print(f"{greeting}, {name}")
#
#
# hello("Hello", "Vasya")
# hello("Hello", "Petya")
# hello("Hello", "Anton")
# hello("Hello", "Petro")


# с каррингом
# def hello_curried(greeting):
#     def hello(name):
#         print(f"{greeting}, {name}")
#
#     return hello
#
#
# my_greeting = hello_curried("Hello")
#
# for name in names:
#     my_greeting(name)
#
# my_greeting = hello_curried("Goodbye")
#
# for name in names:
#     my_greeting(name)

# my_greeting("Vasya")
# my_greeting("Petya")
# my_greeting("Anton")
# my_greeting("Petro")

#####
# def hello_curried_v2(greeting):
#
#     def symbol_separator(separator):
#
#         def end(string_end):
#
#             def hello(name):
#                 print(greeting + separator + name + string_end)
#
#             return hello
#
#         return end
#
#     return symbol_separator

# my_greeting = hello_curried_v2("Hello")(", ")(".")
# my_greeting("Vasya")
# my_greeting("Petya")
#
# my_greeting = hello_curried_v2("Goodbye")(": ")("!")
# my_greeting("Vasya")
# my_greeting("Petya")

############
# def decoration_function(function_for_decoration):
#     def modified_hello():
#         print("Some important logic")
#         function_for_decoration()
#         print("more important logic")
#     return modified_hello
#
#
# @decoration_function
# def hello():
#     print("Hello world")
#
#
# hello()

####
# def a(func1):
#     return func1
#
#
# @a
# def func():
#     print('Hello')
#
#
# func()

#########
# def check_permission(input_function):
#     def check(access_level):
#         match access_level:
#             case "admin":
#                 print("Access granted!")
#                 input_function(access_level)
#             case _:
#                 print("Access denied!")
#     return check
#
#
# @check_permission
# def super_secret_function(access_level):
#     print(f"Super secret function information for {access_level}")
#
#
# super_secret_function("user")
# super_secret_function("admin")

##########
# def validate(input_function):
#     def validated_function(username, user_age):
#         if len(username) < 2:
#             username = "noname"
#         if user_age <= 0 or user_age > 150:
#             user_age = 1
#         input_function(username, user_age)
#
#     return validated_function
#
#
# def greeting(user_info):
#     def hello(name, age):
#         print(f"Hello, your info: ")
#         user_info(name, age)
#
#     return hello
#
#
# @validate
# @greeting
# def show_user(name, age):
#     print(f"Name: {name} Age: {age}")
#
#
# show_user("", -10)
# show_user("Vasya", 30)

