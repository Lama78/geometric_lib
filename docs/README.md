# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab 
- Square: S = a² 

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

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
### Add rectangle.py

> Commit hash: 305a3a94809db44dd5619cee6ce643ec3f23986b

### Added a description of the circle functions

> Commit hash: 40b344f0e72c562320e51e32077149c24f939801

### Added a description of the rectangle functions

> Commit hash: 9c2b15c7991db79057150f4a703c48e022e2a8cb

### Added a description of the square functions

> Commit hash: 4d5cc2c0fe6d1b4bc2901e4af3d4e49b9ff36acf