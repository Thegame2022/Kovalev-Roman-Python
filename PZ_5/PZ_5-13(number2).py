#Описать функцию ShiftRight3(A, B, C), выполняющую правый циклический сдвиг:
#значение A переходит в B, значение B — в C, значение C — в A (A, B, C —
#вещественные параметры, являющиеся одновременно входными и выходными). С
#помощью этой функции выполнить правый циклический сдвиг для двух данных
#наборов из трех чисел: (A1, B1, C1) и (A2, B2, C2).
def ShiftRight3(A, B, C):
    # Проверка, что все параметры являются вещественными числами
    if not all(isinstance(x, (int, float)) for x in (A, B, C)):
        raise ValueError("Все параметры должны быть вещественными числами.")
    # Выполнение правого циклического сдвига
    return C, A, B  # Возвращаем новые значения в порядке C, A, B
# Основная часть программы
try:
    # Набор 1
    A1, B1, C1 = 1.0, 2.0, 3.0
    A1, B1, C1 = ShiftRight3(A1, B1, C1)
    print("После сдвига (A1, B1, C1):", A1, B1, C1)
    # Набор 2
    A2, B2, C2 = 4.0, 5.0, 6.0
    A2, B2, C2 = ShiftRight3(A2, B2, C2)
    print("После сдвига (A2, B2, C2):", A2, B2, C2)
except ValueError as e:
    print("Ошибка:", e)