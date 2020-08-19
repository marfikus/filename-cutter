
import os

def filename_cutter(path, max_name_length):
    if max_name_length <= 0:
        print("'max_name_length' must be > 0")
        return

    if not os.path.exists(path):
        print("Path not found!")
        return
    
    # Получаем список элементов
    content_list = os.listdir(path)
    
    # Бежим по этому списку
    for el_full_name in content_list:
        print("=========")
        # Флаг разрешения переименования элемента
        rename_allowed = False
        print("el_full_name:", el_full_name)
        # Склеиваем полный путь и имя элемента для дальнейшей работы
        el_path = os.path.join(path, el_full_name)
        # Нормализация на всякий случай (слэши разные...)
        el_path = os.path.normpath(el_path)
        print("el_path:", el_path)
        
        # Если имя элемента длиннее нормы
        if len(el_full_name) > max_name_length:
            print("Need to trim name")
            # Если это файл
            if os.path.isfile(el_path):
                print("Is file")
                # Отделяем расширение от имени
                el_name, el_ext = os.path.splitext(el_full_name)
                # Подрезаем имя до нормы,
                # исключая возможность чрезмерного обрезания), чтобы до нуля и в минус не уйти
                cut_index = max_name_length - len(el_ext)
                if cut_index <= 0:
                    print("Index for the cuttering is too small: {}\n Skip this element".format(cut_index))
                    continue
                el_name = el_name[:cut_index]
                # Склеиваем обратно
                el_new_full_name = el_name + el_ext
                print("el_new_full_name:", el_new_full_name)
                # Подготавливаем путь
                el_new_path = os.path.join(path, el_new_full_name)
                el_new_path = os.path.normpath(el_new_path)
                # Проверяем на всякий случай существование такого же файла
                if not os.path.exists(el_new_path):
                    rename_allowed = True
                else:
                    print("File with the same name is already exists")
                    # Если такой файл уже есть, то добавляем в конце цифру
                    # и снова проверяем существование такого файла
                    # Когда будет найдено уникальное имя, тогда переименовываем файл
                    i = 1 # номер итерации и окончание в имени элемента
                    while True:
                        print("i:", i)
                        # Изменение имени.
                        # Формируем окончание имени
                        end_el_name = "_{}".format(i)
                        # Снова делим имя
                        el_name, el_ext = os.path.splitext(el_new_full_name)
                        if i == 1:
                            # На первой итерации надо ещё подрезать имя 
                            # на длину добавляемого окончания
                            cut_index = len(el_name) - len(end_el_name)
                            if cut_index <= 0:
                                print("Index for the cuttering is too small: {}\n Skip this element".format(cut_index))
                                break
                            el_name = el_name[:cut_index]
                        else:
                            # Если не первая итерация уже, 
                            # то надо сначала убрать старую цифру из имени
                            cut_index = len(el_name) - (len(str(i - 1)) + 1)
                            if cut_index <= 0:
                                print("Index for the cuttering is too small: {}\n Skip this element".format(cut_index))
                                break
                            el_name = el_name[:cut_index]
                            # А если добавляется разряд в окончании, то надо ещё обрезать на символ
                            # (маловероятно что такое случится, но в общем возможно... заморочки)
                            if len(str(i)) > len(str(i - 1)):
                                print("Added digit in the 'i'")
                                cut_index = len(el_name) - 1
                                if cut_index <= 0:
                                    print("Index for the cuttering is too small: {}\n Skip this element".format(cut_index))
                                    break
                                el_name = el_name[:cut_index]
                                
                        # Добавляем окончание, снова склеиваем
                        el_name += end_el_name
                        el_new_full_name = el_name + el_ext
                        print("el_new_full_name:", el_new_full_name)
                        el_new_path = os.path.join(path, el_new_full_name)
                        el_new_path = os.path.normpath(el_new_path)
                        # Снова проверяем существование
                        if not os.path.exists(el_new_path):
                            rename_allowed = True
                            break
                        i += 1
                # Переименовываем файл 
                if rename_allowed:
                    os.rename(el_path, el_new_path)
                else:
                    print("Not allowed rename this element")
                    
            # Иначе, если это каталог
            elif os.path.isdir(el_path):
                print("Is dir")
                # Подрезаем имя до нормы
                el_new_full_name = el_full_name[:max_name_length]
                print("el_new_full_name:", el_new_full_name)
                # Подготавливаем путь
                el_new_path = os.path.join(path, el_new_full_name)
                el_new_path = os.path.normpath(el_new_path)
                
                # Проверяем на всякий случай существование такого же каталога
                if not os.path.exists(el_new_path):
                    rename_allowed = True
                else:
                    print("Directory with the same name is already exists")
                    # Поиск уникального имени для каталога, почти также, как и в случае с файлом.
                    i = 1 # номер итерации и окончание в имени элемента
                    while True:
                        print("i:", i)
                        # Изменение имени.
                        # Формируем окончание имени
                        end_el_name = "_{}".format(i)
                        # Подставляю пока значение (так меньше переделывать)
                        el_name = el_new_full_name
                        if i == 1:
                            # На первой итерации надо ещё подрезать имя 
                            # на длину добавляемого окончания
                            cut_index = len(el_name) - len(end_el_name)
                            if cut_index <= 0:
                                print("Index for the cuttering is too small: {}\n Skip this element".format(cut_index))
                                break
                            el_name = el_name[:cut_index]
                        else:
                            # Если не первая итерация уже, 
                            # то надо сначала убрать старую цифру из имени
                            cut_index = len(el_name) - (len(str(i - 1)) + 1)
                            if cut_index <= 0:
                                print("Index for the cuttering is too small: {}\n Skip this element".format(cut_index))
                                break
                            el_name = el_name[:cut_index]
                            # А если добавляется разряд в окончании, то надо ещё обрезать на символ
                            # (маловероятно что такое случится, но в общем возможно... заморочки)
                            if len(str(i)) > len(str(i - 1)):
                                print("Added digit in the 'i'")
                                cut_index = len(el_name) - 1
                                if cut_index <= 0:
                                    print("Index for the cuttering is too small: {}\n Skip this element".format(cut_index))
                                    break
                                el_name = el_name[:cut_index]
                                
                        # Добавляем окончание
                        el_name += end_el_name
                        el_new_full_name = el_name
                        print("el_new_full_name:", el_new_full_name)
                        el_new_path = os.path.join(path, el_new_full_name)
                        el_new_path = os.path.normpath(el_new_path)
                        # Снова проверяем существование
                        if not os.path.exists(el_new_path):
                            rename_allowed = True
                            break
                        i += 1
                    
                # Переименовываем каталог
                if rename_allowed:
                    os.rename(el_path, el_new_path)
                    el_path = el_new_path
                else:
                    print("Not allowed rename this element")
                    # Если с continue, то пропускаем этот каталог (не заходим в него)
                    # continue
                
                # Вызываем эту же функцию для этого каталога
                filename_cutter(el_path, max_name_length)
        input()

if __name__ == "__main__":
    print("=========================")
    PATH = os.getcwd() + r"\for_tests"
    filename_cutter(PATH, max_name_length=6)
    print("=========================")
    