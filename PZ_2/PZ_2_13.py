# Ввод двузначного числа
number = input("Введите двузначное число: ")

# Проверка, что введено именно двузначное число
if len(number) == 2 and number.isdigit():
    # Перестановка цифр
    swapped_number = number[1] + number[0]
    
    # Вывод результата
    print("Число после перестановки цифр:", swapped_number)
else:
    print("Ошибка: Введите корректное двузначное число.")
