def zadiak_year(year):
    a = {0: "крыса", 1: "бык", 2: "тигр", 3: "кролик", 4: "дракон", 5: "змея", 6: "лошадь", 7: "овца", 8: 'обезьяна',
         9: 'курица', 10: 'собака', 11: 'свинья'}
    return a[(year - 1972) % 12]


def zadiak_month(month, day):
    m = ['Водолей', 'Рыбы', 'Овен', 'Телец', 'Близнецы', 'Рак', 'Лев', 'Дева', 'Весы', "Скорпион", "Стрелец", "Козерог"]
    d = (20, 19, 21, 20, 21, 22, 23, 23, 23, 24, 23, 22)
    month = month - 1
    if day > d[month]:
        return m[month]
    else:
        return m[month - 1]


def zadiak_info(date):
    a = date.split('.')
    year = int(a[2])
    month = int(a[1])
    day = int(a[0])
    return zadiak_year(year), zadiak_month(month, day)