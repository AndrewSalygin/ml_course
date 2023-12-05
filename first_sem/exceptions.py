# file=resources/exceptions/file1.csv
# rows=3
# cols=4
# n=12
# m=10
# игрушка;"коробка с карандашами";свечка;лего;кукла;"свитер с оленями";мячик;расчёска;молоток;яблоко

# file=resources/exceptions/file2.csv
# rows=2
# cols=2
# n=4
# m=5
# саквояж;картина;корзина;картонка;"маленькая собачонка"

import csv
import math


def check_and_parse_params():
    params = {
        'file': 'input.csv',
        'rows': None,
        'cols': None,
        'n': None,
        'm': None,
        'items': []
    }

    one_items_flag = True
    one_file_name = True
    for count_param in range(6):
        try:
            input_string = input()
        except EOFError:
            exit(0)
        if ';' in input_string and one_items_flag:
            params['items'] = [item.strip('""') for item in input_string.split(';')]
            one_items_flag = False
        else:
            entry = input_string.split('=')
            if len(entry) != 2:
                raise ValueError(f'Неправильный формат параметра')
            key, value = entry

            # Приводим ввод к нормальному виду
            key = key.strip().lower()
            value = value.strip()

            if (key == 'file' or key == 'f') and not one_file_name:
                raise ValueError(f'Параметр file уже указывался')
            if key == 'file' or key == 'f' and one_file_name:
                one_file_name = False
                params['file'] = value
            elif key == 'number' or key == 'n':
                params['n'] = value
            elif key == 'm' or key == 'pigeons':
                params['m'] = value
            elif key == 'rows' or key == 'cols':
                params[key] = value
            else:
                raise ValueError(f'Неизвестный параметр: {key}')
    params['items'].sort()
    return params


def read_csv(file_path):
    try:
        with open(file_path, newline='') as csvfile:
            items_list = list(csv.reader(csvfile))
            return items_list
    except Exception as ex:
        raise IOError(f"Ошибка чтения csv файла '{file_path}': {ex}")


def validate_params(params):
    required_params = ['rows', 'cols', 'n', 'm']

    for param in required_params:
        try:
            if not params[param]:
                raise RuntimeError(f'Не указан необходимый параметр: {param}')
            params[param] = int(params[param])
        except ValueError as e:
            raise ValueError(f'Неправильное численное значение для {param}: {e}')

    if len(params['items']) != params['m']:
        raise ValueError('Количество переданных параметров в items не соответствует заявленным в m')


def check_csv_data(csv_data, params):
    items = []
    if len(csv_data) != params['rows']:
        raise ValueError('Количество строк в файле не совпадает с переданным параметром')
    for row in csv_data:
        if len(row) != params['cols']:
            raise ValueError('Количество столбцов в файле не совпадает с переданным параметром')
        for cols in row:
            # обработка случая 'мячик,расчёска,молоток,яблоко'
            local_items = cols.split(',')
            for x in local_items:
                if x != "":
                    items.append(x)
    items.sort()
    if params['n'] != params['cols'] * params['rows']:
        raise ValueError('Несоответствие параметров n, rows и cols')
    if params['m'] == len(items):
        if params['items'] != items:
            raise ValueError('Элементы из файла и параметра не совпадают')
    else:
        raise ValueError('Количество элементов из файла и параметра не совпадает')


def formulate_dirichlet_principle(params):
    if params['m'] > params['n']:
        print(f"По принципу Дирихле: Если в {params['n']} ящиках лежит {params['m']} предметов, то "
              f"хотя бы в одном ящике лежит не менее {math.ceil(params['m'] / params['n'])} предметов")
    else:
        print(f"По принципу Дирихле: Если в {params['n']} ящиках лежит {params['m']} предметов, то "
              f"пустых ящиков как минимум {params['n'] - params['m']}")


try:
    params = check_and_parse_params()
    validate_params(params)
    csv_data = read_csv(params['file'])
    check_csv_data(csv_data, params)
    formulate_dirichlet_principle(params)
except ValueError as e:
    print(f"Ошибка: {e}")
except IOError as e:
    print(f"Ошибка: {e}")
except RuntimeError as e:
    print(f"Ошибка: {e}")