def task_1():
    geo_logs = [
        {'visit1': ['Москва', 'Россия']},
        {'visit2': ['Дели', 'Индия']},
        {'visit3': ['Владимир', 'Россия']},
        {'visit4': ['Лиссабон', 'Португалия']},
        {'visit5': ['Париж', 'Франция']},
        {'visit6': ['Лиссабон', 'Португалия']},
        {'visit7': ['Тула', 'Россия']},
        {'visit8': ['Тула', 'Россия']},
        {'visit9': ['Курск', 'Россия']},
        {'visit10': ['Архангельск', 'Россия']}
    ]

    filter_geo_logs = []
    for geo_logs_dict in geo_logs:
        for el in geo_logs_dict.values():
            if el[1] == "Россия":
                filter_geo_logs.append(geo_logs_dict)

    return filter_geo_logs


def task_2():
    ids = {'user1': [213, 213, 213, 15, 213],
           'user2': [54, 54, 119, 119, 119],
           'user3': [213, 98, 98, 35]}

    ids = {'user1': [213, 213, 213, 15, 213],
           'user2': [54, 54, 119, 119, 119],
           'user3': [213, 98, 98, 35]}
    user1 = set(ids['user1'])
    user2 = set(ids['user2'])
    user3 = set(ids['user3'])
    return list(user1 | user2 | user3)


def task_3():
    queries = ['играть',
               'смотреть сериалы онлайн',
               'новости спорта',
               'афиша кино',
               'курс доллара',
               'сериалы этим летом',
               'курс по питону',
               'сериалы про спорт'
               ]

    queries_dict = {}
    sum_values = 0
    result_dict = {}
    for el in queries:
        count_word = len(el.split(' '))
        if count_word in queries_dict.keys():
            queries_dict[count_word] += 1
        else:
            queries_dict[count_word] = 1
        sum_values += 1

    for elem in queries_dict.items():
        percent = round(elem[1] / sum_values * 100, 2)
        result_dict.setdefault(elem[0], percent)

    return result_dict


def task_4():
    stats_dict = {'facebook': 55, 'yandex': 120, 'vk': 115,
                  'google': 99, 'email': 42, 'ok': 98}

    max = 0
    channel = ''
    for elem in stats_dict.items():
        if elem[1] > max:
            max = elem[1]
            channel = elem[0]
    return [max, channel]


if __name__ == '__main__':
    print('task_1')
    filter_geo_logs = task_1()
    print(f'Список визитов по России:\n {filter_geo_logs}')

    print('task_2')
    list_users = task_2()
    print(f'\nСписок уникальных гео-ID {list_users}')

    print('task_3')
    queries_dict = task_3()
    for key, value in queries_dict.items():
        print(f'Поисковый запрос из {key} слова - {value} %')

    print('task_4')
    list_result = task_4()
    print(
        f'{list_result[0]} \nКанал с максимальным объемом - {list_result[1]}')
