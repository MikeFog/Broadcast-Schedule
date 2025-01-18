from datetime import timedelta

# # Функция для преобразования времени в секунды
# def time_to_seconds(time_str):
#     h, m, s = map(int, time_str.split(':'))
#     return h * 3600 + m * 60 + s

# # Функция для преобразования секунд в строку времени
# def seconds_to_time(seconds):
#     return str(timedelta(seconds=seconds))

# Открываем файл и читаем данные
with open(r"c:\Work\AdvertAg\Broadcast Schedule\files\Европа плюс  (Ярославль)_12_11_2024_0300-2359.txt", 'r', encoding='cp1251') as file:
    lines = file.readlines()

# Инициализация переменных
blocks = []  # Список для хранения блоков
current_block = []  # Текущий блок
total_duration = timedelta()  # Общая продолжительность всех блоков

# Обработка строк
for line in lines:
    parts = line.strip().split(',')
    if parts[0] == '"BT"':  # Начало блока
        current_block = []  # Начинаем новый блок
    elif parts[0] == '"E"':  # Конец блока
        if current_block:  # Если блок не пустой
            blocks.append(current_block)  # Добавляем блок в список
            current_block = []  # Сбрасываем текущий блок
    else:
        current_block.append(parts)  # Добавляем строку в текущий блок

# Обработка каждого блока
for block in blocks:
    block_duration = timedelta()  # Продолжительность текущего блока
    for parts in block:
        if len(parts) >= 6 and parts[4].endswith('.mp3"'):  # Проверяем, что это MP3-файл
            duration_str = parts[5].strip('"')  # Получаем продолжительность
            if duration_str:  # Если продолжительность указана
                h, m, s = map(int, duration_str.split(':'))
                block_duration += timedelta(hours=h, minutes=m, seconds=s)
    total_duration += block_duration  # Добавляем продолжительность блока к общей
    print(f"Продолжительность блока: {block_duration.total_seconds()}")

print(f"Общая продолжительность всех блоков: {total_duration.total_seconds()}")