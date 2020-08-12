
import os

PATH = os.getcwd() + r"\for_tests"
NAME_MAX_LENGTH = 50

def filename_cutter(path):
    if not os.path.exists(path):
        print("Path not found!")
        return
    
    # Получаем список файлов
    content_list = os.listdir(path)
    
    # Бежим по этому списку
    for el_full_name in content_list:
        print("====================================================")
        print(el_full_name)
        el_path = os.path.join(path, el_full_name)
        el_path = os.path.normpath(el_path)
        print(el_path)
        
        # Если это файл
        if os.path.isfile(el_path):
            # Если имя файла длиннее нормы
            if len(el_full_name) > NAME_MAX_LENGTH:
                # Отделяем расширение от имени
                el_name, el_ext = os.path.splitext(el_full_name)
                # Подрезаем имя до нормы
                el_name = el_name[:NAME_MAX_LENGTH]
                # Склеиваем обратно
                el_new_full_name = el_name + el_ext
                print(el_new_full_name)
                input()
                # Переименовываем файл 
        # Иначе, если это каталог
            # Вызываем эту же функцию для этого каталога
            
filename_cutter(PATH)