def bubble_sort(a: list) -> list:
    """
    Функция реализует оптимизированную пузырьковую сортировку.
    Она принимает на вход список, сортирует его по неубыванию и возвращает
    отсортированный список.

    :param a: list - список, который необходимо отсортировать.
    :return: list - отсортированный по неубыванию список.
    """
    n = len(a)

    # основной цикл отвечает за количество проходов по списку, оно равно длине списка - 1, поскольку
    # в конце каждого прохода "всплывает" (встает в конец списка) наибольший элемент списка
    for i in range(n - 1):

        # переменная swap является флажком, принимает значение истина, если за проход по списку происходит
        # хотя бы один обмен элементов списка
        swap = False

        # внутренний цикл отвечает за индексы левых элементов в паре для сравнения
        # с каждым проходом будем исключать из сравнения по одному элементу списка с правого конца,
        # поскольку он уже будет стоять на своем месте
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swap = True

        # если за проход по списку не произошло ни одного обмена элементов, список отсортирован
        # и можно завершить сортировку раньше
        if not swap:
            break

    return a
