from data_create import name_data, surname_data, phone_data, address_data
# ввод данный 
def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате записать данные?\n\n"
    f"1 Вариант: \n"
    f"\n{name}\n{surname}\n{phone}\n{address}\n"
    f"2 Вариант:\n"
    f"\n{name};{surname};{phone};{address}\n"
    f"Выберите вариант: "))
    
    while var != 1 and var!= 2:
        print("Неправильный ввод")
        var = int(input("Введите Номер Варианта 1 или 2: "))
    
    if var == 1:
        with open("data_first_variant.csv", 'a', encoding = "utf-8") as f:
            f.write(f"\n{name}\n{surname}\n{phone}\n{address}\n")

    elif var == 2:
        with open("data_second_variant.csv", "a", encoding = "utf-8") as f:
            f.write(f"\n{name};{surname};{phone};{address}\n")
    print("Данные внесены, Спасибо.")
    
# Чтения Данный из списка
def print_data():
    print("Данные из первого файла: \n")
    with open("data_first_variant.csv", 'r', encoding ="utf-8") as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first)- 1:
                data_first_list.append(''.join(data_first[j:i+1]))
                j = i
        print("".join(data_first_list))
    
    
    print("Данные из второго файла:\n")
    with open("data_second_variant.csv", 'r', encoding ="utf-8") as f:
        data_second = f.readlines()
        print(*data_second)
    
print_data