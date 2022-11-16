# 1)написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
# - перший записує в список нову справу
# - другий повертає всі записи
# 2) протипізувати перше завдання

# def notebook():
#     todo_list:list[str] = []
#
#     def add_todo(todo:str) -> None:
#         nonlocal todo_list
#         todo_list.append(todo)
#
#     def get_all() -> list[str]:
#         nonlocal todo_list
#         return  todo_list
#
#     return add_todo,get_all
#
#
# add_todo,get_all = notebook()

# 3) створити функцію котра буде повертати сумму розрядів числа у вигляді строки (також використовуемо типізацію)
#
# Приклад:
#
# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'

# def expanded_form(num:int) -> str:
#         lenght = len(str(num))
#         nums = ' + '.join(l + '0' * (lenght-i-1) for i,l in enumerate(str(num)) if l != '0')
#         return nums


# 4) створити декоратор котрий буде підраховувати скільки разів була запущена функція продекорована цим декоратором,
# та буде виводити це значення після виконання функцій

def decor(func):
    count = 0
    def res(*args,**kwargs):
        print('--------')
        nonlocal count
        count += 1
        func(*args,**kwargs)
        print('count:' + f'{count}')
        print('--------')
    return res

@decor
def func1():
    print('func1')

@decor
def func2():
    print('func2')

