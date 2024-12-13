#Дан список размера N и целое число K (1 < K < N). Осуществить сдвиг элементов
#списка влево на K позиций (при этом AN перейдет в AN-K, AN-1 — в AN-K-1, ..AK+1 — в
#A1, а исходное значение K первых элементов будет потеряно). Последние K
#элементов полученного списка положить равными 0.
def shift_list_left(A, K):
    try:
        #Проверка на допустимость значения K
        if not (1 < K < len(A)):
            raise ValueError("Значение K должно быть больше 1 и меньше длины списка.")

        #Создание новой копии списка для сохранения оригинала
        shifted_A = A.copy()

        #Выполнение сдвига элементов влево на K позиций
        shifted_A = shifted_A[K:] + [0] * K

        #Вывод исходного и результирующего списков
        print(f"Исходный список: {A}")
        print(f"Сдвинутый список: {shifted_A}")

    except ValueError as e:
        print(f"Произошла ошибка: {e}")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")

if __name__ == "__main__":
    try:
        #Запрашиваем у пользователя ввод списка A
        A = list(map(int, input("Введите элементы списка A через пробел: ").split()))
        #Запрашиваем у пользователя ввод числа K
        K = int(input("Введите значение K: "))
        #Вызываем функцию для сдвига списка
        shift_list_left(A, K)
    except ValueError as e:
        print(f"Произошла ошибка: {e}")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")




