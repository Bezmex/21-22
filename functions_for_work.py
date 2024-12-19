#Функции ввода
import math
import random
from functools import lru_cache

def is_int(choice):
    """
    Алгоритм проверки на целочисленность введеного числа при выборе пунктов меню
    """
    try:
        if type(choice) is int:
            return True
        if choice is None:
            return False
        if not choice.isdecimal():
            return False
        int(choice)
        return True
    except (Exception, ValueError, TypeError):
        return False

#----------------------------------------------------------------------------------------------

#Ввод массива
def input_array():
    """
    Вводится массив чисел через пробел с клаваиатуры и возвращается
    """
    return [int(number) for number in input("Введите числа через пробел для массива: ").split()]

#Задание массива чисел рандомно
def random_array(length):
    """
    Рандомно вводится массив чисел и возвращается
    :param length: - длина массива, задаваемая пользователем
    """
    return [random.randint(1, 100) for _ in range(length)]

#------------------------------------------------------------------------------------------

#Задаем большое число и преобразуем его в массив
def input_large_number_for_arr():
    """
    Задается большое число пользователем и алгоритм возвращает массив из цифр
    """
    return [int(number) for number in input("Введите большое число: ")]

#Рандомно генерируем массив из длины числа
def generate_random_number_for_arr(length):
    """
    Рандомно задается большое число и алгоритм возвращает массив из цифр
    :param length: длина числа, задаваемая пользователем
    """
    return [random.randint(0, 9) for _ in range(length)]

#-----------------------------------------------------------------------------------------------

# Ввод массива точек от пользователя
def input_points():
    """
    Алгоритм ввода массива точек пользователем
    """
    num_points = int(input("Введите количество точек: "))
    points = []
    for i in range(num_points):
        point = tuple(map(int, input(f"Введите координаты точки через пробел {i+1} (x y): ").split()))
        points.append(point)
    return points

# Генерация случайных точек
def generate_random_points(num_points, max_value=100):
    """
    Алгоритм задания массива точек рандомно
    :param num_points: количество точек в массивах, задаваемое пользователем
    :param max_value: максимальное значение координаты (изначально установлено 100)
    """
    return [(random.randint(0, max_value), random.randint(0, max_value)) for _ in range(num_points)]

# Вычисление расстояния между двумя точками
@lru_cache(maxsize=None)
def distance(point1, point2):
    """
    Вычисляет расстояние между двумя точками
    :param point1: координаты точки 1
    :param point2: координаты точки 2
    """
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)