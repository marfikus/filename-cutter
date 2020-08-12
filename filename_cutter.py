
import os

def filename_cutter(path, max_name_length):
    if not os.path.exists(path):
        print("Path not found!")
        return
    
    # Получаем список элементов
    content_list = os.listdir(path)
    
    # Бежим по этому списку
    for el_full_name in content_list:
        print("=========")
        print("el_full_name:", el_full_name)
        # Склеиваем полный путь и имя элемента для дальнейшей работы
        el_path = os.path.join(path, el_full_name)
        # Нормализация на всякий случай (слэши разные...)
        el_path = os.path.normpath(el_path)
        print("el_path:", el_path)
        
        # Если это файл
        if os.path.isfile(el_path):
            print("Is file")
            # Если имя файла длиннее нормы
            if len(el_full_name) > max_name_length:
                print("Need to trim name")
                # Отделяем расширение от имени
                el_name, el_ext = os.path.splitext(el_full_name)
                # Подрезаем имя до нормы
                el_name = el_name[:max_name_length - len(el_ext)]
                # Склеиваем обратно
                el_new_full_name = el_name + el_ext
                print("el_new_full_name:", el_new_full_name)
                # Переименовываем файл 
                el_new_path = os.path.join(path, el_new_full_name)
                el_new_path = os.path.normpath(el_new_path)
                os.rename(el_path, el_new_path)
        # Иначе, если это каталог
        elif os.path.isdir(el_path):
            print("Is dir")
            # Если имя каталога длиннее нормы
            if len(el_full_name) > max_name_length:
                print("Need to trim name")
                # Подрезаем имя до нормы
                el_new_full_name = el_full_name[:max_name_length]
                print("el_new_full_name:", el_new_full_name)
                # Переименовываем каталог
                el_new_path = os.path.join(path, el_new_full_name)
                el_new_path = os.path.normpath(el_new_path)
                os.rename(el_path, el_new_path)
                el_path = el_new_path
            # Вызываем эту же функцию для этого каталога
            filename_cutter(el_path, max_name_length)

if __name__ == "__main__":
    print("=========================")
    PATH = os.getcwd() + r"\for_tests"
    filename_cutter(PATH, max_name_length=10)
    print("=========================")
    