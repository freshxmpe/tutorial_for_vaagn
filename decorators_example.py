# Это комментарий, интерпретатор игнорирует его

# используя ключевое слово def, мы определяем функцию
def my_func():
    pass # pass говорит что функция еще не реализована

my_func() # Это вызов функции. Не чего не произойдет


def add(operand1, operand2):  # объявляем обязательные аргументы функции
    return operand1 + operand2 # возвращаем результат их сложения

# концепция полиморфизма
add(1, 2) # вернет 3
add('I love', ' python') # вернет I love python
add([1, 2], [3, 4]) # вернет новый массив [1, 2, 3, 4]


# паттерн декоратор
def decorator(func):
    def wrapper():
        print('i am advanced')
        return func()
    
    return wrapper

# можем вызвать функцию вручную 
def func():
    print('hello world')

newFunc = decorator(func)
newFunc() # выведет i am advanced затем hello world

# или использовать синтаксический сахар
# тоже самое что и wrap_awesome = decorator(awesome)
@decorator
def awesome():
    return True

print(awesome()) # выведет сначала i am advanced затем True


