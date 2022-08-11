import os

# Константы путей
FILES_DIR   = 'files'
OUTPUT_FILE = 'out.txt'
ROOT_PATH   = os.getcwd()

# Абсолютный текущий путь
full_path = os.path.join(ROOT_PATH, FILES_DIR)

# Список файлов по пути FILES_DIR
files = os.listdir(full_path)

# Заполняем словарь файлов в формате:
# {
#   'filename1': {
#        'lines',    # число строк
#        'data'      # содержимое файла
#       },
#   'filename2': {'lines', 'data'},
#   ...    
# }
files_dict = {}
# цикл по всем файлам
for file in files:
    with open(os.path.join(full_path, file), encoding='utf-8') as f:
        num_lines = 0
        data = ''
        # в цикле считываем построчно файл 
        # и считаем число строк и сохраняем само содержимое
        for line in f:
            data += line
            num_lines += 1
        # добавление информации о файле в словарь
        files_dict[file] = {
            'lines': num_lines,
            'data': data
            }

print(files_dict)

# сортировка по числу строк в файле (поле 'lines')
files_dict_sorted = sorted(files_dict.items(), key = lambda item: item[1]['lines'])
print(files_dict_sorted)

# сохранение выходного файла
with open(os.path.join(ROOT_PATH, OUTPUT_FILE), "w", encoding="utf-8") as die31:
    for item in files_dict_sorted:
        die31.write(item[0]+'\n')
        die31.write(str(item[1]['lines'])+'\n')
        die31.write(item[1]['data']+'\n')
