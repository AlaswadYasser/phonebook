from logger import input_data, print_data 
from tools import edit_data, delete_data

#  Главное меню программы
def interface():
    command = 1
    
    while command > 0:
        print(
            "МЕНЮ \n",
            "1 - Вывод данных \n",
            "2 - Запись данных \n",
            "3 - Изменить данных \n",
            "4 - Удалить данных \n",
            "5 - Завершение работы",
        )
        command = int(input("\nВведите число: "))

        while command < 1 or command > 5:
            print("Неправильный ввод!")
            command = int(input("\nВведите число: "))


        match command:
            case 1:
                print_data()
            case 2:
                input_data()
            case 3:
                edit_data()
            case 4:
                delete_data()
            case 5:
                pass