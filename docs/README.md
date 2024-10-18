# How to use calculator:
1. Run `python calculate.py`
2. Enter the figure name. Available are Circle, Square.
3. Enter the function: Area or Perimeter.
4. Enter figure sizes. Radius for circle, one side for square.
5. Get the answer!

# Math formulas
## Area
- Circle: `S = πR²`
- Rectangle: `S = ab`
- Square: `S = a²`
- Triangle: `S = sqrt(p * (p-a) * (p-b) * (p-c))` where p is semiperimeter

## Perimeter
- Circle: `P = 2πR`
- Rectangle: `P = 2a + 2b`
- Square: `P = 4a`
- Triangle: `P = a + b + c`

# Функций и Math formulas

## Общее описание
- Данные функции вычисляют площадь и периметр для представленых выше фигур
- Для каждой фигуры свой файл,где содержатся функции вычисляющие
их площадь и периметр

### circle.py
``` python 
import math


def area(r):
    '''
        Принимает целое число r - радиус окружности
        Возвращает значение площади с плавающей точкой
        r(7) = pi * 7 * 7 = 153,938
    '''
    return math.pi * r * r

def perimeter(r):
    '''
        Принимает целое r - радиус окружности
        Возвращает значение периметра с плавающей точкой
        r(7) = 2 * pi * 7 = 43,982
    '''
    return 2 * math.pi * r
```
### rectangle.py
``` python
def area(a, b):
    '''
        Принимает целые числа: a и b - стороны прямоугольника
        Возвращает значение площади - целое число
        a(7) b(2) = a * b = 14
    '''
    return a * b
def perimeter(a, b):
    '''
        Принимает целые числа: a и b - стороны прямоугольника
        Возвращает значение периметра - целое число
        a(7) b(10) = 2*(a+b) = 34
    '''
    return 2 * (a + b)
```
### square.py
``` python
def area(a):
    '''
        Принимает целое число a  -  сторона квадрата
        Возвращает значение площади - целое число
        a (7) = a * a = 49
    '''
    return a * a
    
def perimeter(a):
    '''
        Принимает целое число a  -  сторона квадрата
        Возвращает значение периметра - целое число
        a(7)= a * 4 = 28
    '''
    return 4 * a
```
### triangle.py
``` python
def area(a, h):
    '''
        Принимает целые числа: a и h - сторона и высота проведённая к этой стороне
        Возвращает значение площади целое число
        a(2) h(3) = a * h / 2 = 3
    '''
    return a * h / 2
    
def perimeter(a, b, c):
    '''
        Принимает целые числа: a и b и c - стороны треугольника
        Возвращает значение периметра целое число
        a(10) b(10) c(10) = a+b+c = 30
    '''
    return a + b + c
```
### calculate.py
``` python
import circle
import square

'''Импортирем модули "circle" и "square"'''

figs = ['circle', 'square']
funcs = ['perimeter', 'area']

'''Объявляем списки доступных фигур и функций'''

sizes = {}

'''Создаем словарь для хранения размеров фигур'''


def calc(fig, func, size):
    '''Создаём функцию для вычисления периметра или площади'''
    assert fig in figs
    '''Проверяем, что фигура допустима'''
    assert func in funcs
    '''Проверяем, что функция допустима'''

    '''Вычисляем результат с помощью динамического вызова метода'''
    result = eval(f'{fig}.{func}(*{size})')
    print(f'{func} of {fig} is {result}')
    '''Выводим результат'''


if __name__ == "__main__":
    '''Проверяем, запущен ли скрипт напрямую'''
    func = ''
    fig = ''
    size = list()
'''Запрашиваем фигуру до тех пор, пока не введем допустимую'''
while fig not in figs:
    fig = input(f"Enter figure name, avaliable are {figs}:\n")
'''Запрашиваем функцию до тех пор, пока не введем допустимую'''
while func not in funcs:
    func = input(f"Enter function name, avaliable are {funcs}:\n")
'''Запрашиваем размеры до тех пор, пока их количество не совпадет с необходимым'''
while len(size) != sizes.get(f"{func}-{fig}", 1):
    size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))

calc(fig, func, size)
'''Вызываем функцию для расчета'''
```
### Added rectangle.py and description of the rectangle functions

> Commit hash: 4032c81c9c80e8d33a3823c37d9137da71c67079

### Added description of the circle functions

> Commit hash: d560a4190439693fa02f9d5d4720b8b7659f8cb8

### Added description of the rectangle functions

> Commit hash: c098a49adf68412340d839c5b795d0b199eb06f8

### Added description of the square functions

> Commit hash: e8789df349191afe6dba7fe45f5215f62df6a166

### Added description of the calculate functions

> Commit hash: 279625d78e9e1cbdf7ff6333639761a58d01a5b9
