def show_menu():
    """
    Вызов меню для работы
    """
    print("Меню"
          "\n1. Выбор задачи"
          "\n2. Ввод данных"
          "\n3. Выполнение алгоритма по выбранному заданию"
          "\n4. Вывод результата алгоритма"
          "\n5. Завершение работы"
          )
    return True

def show_tasks():
    """
    Вызов списка заданий для выбора
    """
    print("\n\nДоступные задачи для решения:"
          "\n1. Входные данные: 2 массива с цифрами, каждый представляет собой большое число. Нужно произвести сумму или разность массивов. "
          "\n2. Входные данные: 2 массива с числами. Требуется проверить, сколько у массивов общих чисел. "
          "Также, число будет считаться общим, если оно входит в один массив, а в другом массиве находится его перевернутая версия."
          "\n3. Входные данные: 2 массива с точками и число. Требуется вывести точки из первого и второго массивов, расстояния между которыми больше заданного числа. "
          "Расстояния считаются только для соответствующих чисел.")