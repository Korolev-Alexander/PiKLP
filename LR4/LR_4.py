
import os
import shutil

# Путь к папке, где находятся все подпапки с фото и видео
source_dir = 'C:/путь/к/папке'

# Путь к новой папке, куда будут скопированы все файлы
destination_dir = 'C:/путь/к/новой/папке'

# Расширения файлов, которые нужно скопировать
extensions = ('.jpg', '.png', '.mp4', '.avi', '.mov')

# Создаем новую папку, если она не существует
if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)

# Проходим по всем файлам в исходной директории и её подпапках
for root, dirs, files in os.walk(source_dir):
    for file in files:
        # Проверяем, соответствует ли расширение файла одному из указанных
        if file.lower().endswith(extensions):
            # Полный путь к исходному файлу
            source_file = os.path.join(root, file)
            # Полный путь к файлу в новой папке
            destination_file = os.path.join(destination_dir, file)
            # Копируем файл в новую папку
            shutil.copy2(source_file, destination_file)
            print(f'Скопирован файл: {source_file} -> {destination_file}')

print('Сбор файлов завершен.')