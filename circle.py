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