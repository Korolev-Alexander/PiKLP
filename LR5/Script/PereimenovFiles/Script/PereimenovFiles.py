import os

def rename_files_with_counter(folder_path, prefix, start_counter):
    # Получаем список всех файлов в папке
    files = os.listdir(folder_path)
    
    # Проверяем, что папка не пуста
    if not files:
        print("Папка пуста.")
        return
    
    # Сортируем файлы, чтобы переименование происходило по порядку
    files.sort()
    
    # Перебираем файлы и переименовываем их
    for i, file_name in enumerate(files, start=start_counter):
        # Формируем новое имя файла
        new_name = f"{prefix}-{i}{os.path.splitext(file_name)[1]}"
        
        # Полный путь к старому и новому файлу
        old_file_path = os.path.join(folder_path, file_name)
        new_file_path = os.path.join(folder_path, new_name)
        
        # Переименовываем файл
        os.rename(old_file_path, new_file_path)
        print(f"Переименовано: {file_name} -> {new_name}")

def main():
    # Ввод данных от пользователя
    prefix = input("Введите префикс для файлов: ")
    folder_path = input("Введите путь к папке: ")
    start_counter = int(input("Введите начальное значение счетчика: "))
    
    # Проверка существования папки
    if not os.path.isdir(folder_path):
        print("Указанная папка не существует.")
        return
    
    # Вызов функции для переименования файлов
    rename_files_with_counter(folder_path, prefix, start_counter)

if __name__ == "__main__":
    main()
