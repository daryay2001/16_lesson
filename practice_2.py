# Упаковка данных

# def func(*args, num=11):
#     print(args)
#     new_list = list(args)
#     print(new_list)
#     print(num)
#
#
# func(1, 3, 5, "Word")

# def func_2(num=1, **kwargs):
#     print(kwargs)
#     print(num)
#
# func_2(numb = 23, numb_2 = 33, word = "Parrot")

# def test_func(*args, **kwargs):
#     print(f"args: {args}")
#     print(f"kwargs: {kwargs}")
# test_func("Kotik", "Sobaka", 22, number=23, number_2=17)

# Распаковка данных

# def func(a: str, b, c, d):
#     print(a, b, c, d)
#
#
# my_list = ("Hello", 12, 57, 68)
# func(*my_list)

# def func(name, age, town):
#     print(f"Name: {name}, age: {age}, town: {town}")
#
#
# residents = {
#     "name": "Maks",
#     "age": 33,
#     "town": "New York"
# }
#
# func(**residents)

# def func(pet, name, age):
#     print(f"Hello, pet: {pet}, name: {name}, age: {age}")
#
#
# pet_info = ("Cat", "Mursik", 5)
#
# pets = {
#     1: ("Cat", "Mursik", 5),
#     2: ("Dog", "Sharik", 7),
#     3: ("Rat", "Busya", 2)
# }
#
# for key in pets:
#     func(*pets[key])

# users = {
#     "son": ("Kolya", 12, "Football"),
#     "mother": ("Katya", 33, "Painting"),
#     "father": ("Maksim", 35, "Swimming")
# }
#
#
# def show_family(son, mother, father):
#     def func(name, age, hobby):
#         print(f"Hello, {name}. Your age is {age} and your hobby is {hobby}")
#
#     print(f"Son info: {son}")
#     print(f"Mother info: {mother}")
#     print(f"Father info: {father}")
#
#     func(*son)
#     func(*mother)
#     func(*father)
#
#
# show_family(**users)

#######
# Замыкание
#
# def outer():
#     num = 1
#
#     def inner():
#         nonlocal num
#         num += 1
#         print(num)
#
#     return inner
#
#
# my_func = outer()
#
# my_func()
# my_func()
# my_func()

# def add_nums(num1): return lambda num2: num1 + num2
#
#
# n1 = 5
# my_func = add_nums(n1)
#
# for i in range(1, 10):
#     print(f"{n1} + {i} = {my_func(i)}")


# def hello_curried(greeting):
#     def symbol_sepatator(separator):
#         def string_end(end_symbol):
#             def hello(name):
#                 print(f"{greeting}{separator} {name}{end_symbol}")
#
#             return hello
#
#         return string_end
#
#     return symbol_sepatator
#
#
# my_func = hello_curried("Hello")(",")("!")
#
# my_func("Nastya")
# my_func("Kolya")
#
# my_func = hello_curried("Salut")(",")("!!!")
#
# my_func("Isabella")

# names = ["Miroslava", "Katya", "Pasha"]
#
#
# def hello_curried(greeting):
#     def hello(name):
#         print(f"{greeting}, {name}! Nice to meet you!")
#
#     return hello
#
#
# my_func = hello_curried("Hello")
#
# for name in names:
#     my_func(name)

# def decoration_for_function(function_for_decoration):
#     def modified_hello():
#         print("First important logic")
#         function_for_decoration()
#         print("More important logic")
#     return modified_hello
#
# @decoration_for_function
# def hello():
#     print("Hello, everyone!")
#
# hello()

# def check_permission(input_function):
#     def check(access_level):
#         match access_level:
#             case "elf":
#                 print("May the star light be with you, brother!")
#                 input_function(access_level)
#             case _:
#                 print("Only elves can see this information, stranger. ")
#                 print()
#
#     return check
#
#
# @check_permission
# def secret_elf_information(access_level):
#     print(f"You should drink dew to be stronger, {access_level}.")
#
#
# secret_elf_information("man")
# secret_elf_information("elf")

# def validate(input_function):
#     def validate_function(username, user_age):
#         if len(username) < 2:
#             username = "no name"
#         if user_age <= 0 or user_age > 150:
#             user_age = 1
#         input_function(username, user_age)
#
#     return validate_function
#
#
# def greeting(user_info):
#     def hello(name, age):
#         print("Hello, your info:")
#         user_info(name, age)
#
#     return hello
#
#
# # Порядок декораторов имеет значение!
# @validate
# @greeting
# def show_user(name, age):
#     print(f"Name: {name}, age: {age}")
#
#
# show_user("", -23)
# show_user("Masha", 14)
