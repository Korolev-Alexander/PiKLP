#LR3
import os
from sys import argv

DIRECTORY = r"D:\Учеба\Питон 2 курс\LR3\Test"  # Указать свой путь

def cyrillizator(letter, dic):
    for i, j in dic.items():
        letter = letter.replace(i, j)
    return letter

# Обратный словарь для замены латиницы на кириллицу
reverse_legend = {
    '_': ' ',
    'a': 'а', 'b': 'б', 'v': 'в', 'g': 'г', 'd': 'д', 'e': 'е', 'yo': 'ё', 'zh': 'ж', 'z': 'з',
    'i': 'и', 'j': 'й', 'k': 'к', 'l': 'л', 'm': 'м', 'n': 'н', 'o': 'о', 'p': 'п', 'r': 'р',
    's': 'с', 't': 'т', 'u': 'у', 'f': 'ф', 'h': 'х', 'c': 'ц', 'ch': 'ч', 'sh': 'ш', 'shch': 'щ',
    'y': 'ы', "'": 'ь', 'e': 'э', 'yu': 'ю', 'ya': 'я',

    'A': 'А', 'B': 'Б', 'V': 'В', 'G': 'Г', 'D': 'Д', 'E': 'Е', 'Yo': 'Ё', 'Zh': 'Ж', 'Z': 'З',
    'I': 'И', 'J': 'Й', 'K': 'К', 'L': 'Л', 'M': 'М', 'N': 'Н', 'O': 'О', 'P': 'П', 'R': 'Р',
    'S': 'С', 'T': 'Т', 'U': 'У', 'F': 'Ф', 'H': 'Х', 'Ts': 'Ц', 'Ch': 'Ч', 'Sh': 'Ш', 'Shch': 'Щ',
    'Y': 'Ы', "'": 'Ь', 'E': 'Э', 'Yu': 'Ю', 'Ya': 'Я'
}

for file_old in os.listdir(DIRECTORY):
    file_old_path = os.path.join(DIRECTORY, file_old)
    file_new = cyrillizator(file_old, reverse_legend)
    file_new_path = os.path.join(DIRECTORY, file_new)

    # Раскомментируйте, чтобы сделать первую букву в имени файла Прописной
    # file_new = file_new.capitalize()

    if '-p' in argv:
        if file_old == file_new:
            print('{0: <30}'.format(file_old), 'не будет переименован')
        else:
            print('{0: <30}'.format(file_old), 'будет переименован в ', file_new)
    else:
        if file_old != file_new:
            print('{0: <30}'.format(file_old), 'переименован в ', file_new)
            os.rename(file_old_path, file_new_path)