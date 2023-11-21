# 1. На какое суммарное расстояние были произведены перевозки с 7 по 9 октября?
# 2. Какова средняя масса груза при автоперевозках, осуществлённых из города Осинки?
# 3. Какой суммарный расход бензина был при осуществлении перевозок с 1 по 3 октября?
# 4. Какова средняя масса груза при автоперевозках, осуществлённых в город Березки?

import csv

with open('task19.csv', newline='', encoding='windows-1251') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')

    # Первая задача
    total_distance_oct7_to_oct9 = 0

    # Вторая
    total_weight_osinki = 0
    count_osinki = 0

    # Третья
    total_fuel_oct1_to_oct3 = 0

    # Четвертая
    total_weight_berezki = 0
    count_berezki = 0

    for row in reader:
        distance = int(row['Расстояние'])
        weight = int(row['Масса груза'])
        fuel = int(row['Расход бензина'])

        if '7 октября' <= row['Дата'] <= '9 октября':
            total_distance_oct7_to_oct9 += distance

        if row['Пункт отправления'] == 'Осинки':
            total_weight_osinki += weight
            count_osinki += 1

        if '1 октября' <= row['Дата'] <= '3 октября':
            total_fuel_oct1_to_oct3 += fuel

        if row['Пункт назначения'] == 'Березки':
            total_weight_berezki += weight
            count_berezki += 1

print(f'1. Суммарное расстояние перевозок с 7 по 9 октября: {total_distance_oct7_to_oct9} км')
print(f'2. Средняя масса груза при автоперевозках из Осинок: {total_weight_osinki / count_osinki} кг')
print(f'3. Суммарный расход бензина при перевозках с 1 по 3 октября: {total_fuel_oct1_to_oct3} л')
print(f'4. Средняя масса груза при автоперевозках в Березки: {total_weight_berezki / count_berezki} кг')