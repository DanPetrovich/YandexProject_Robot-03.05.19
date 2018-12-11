# Бери столько предметов, чтобы после твоего хода количество предметов было кратно (M+1).
print('введите число')
count = int(input()) #количество камней в куче

while count > 3:
    ostatok = count % 3 #получаем остаток от деления на три
    kolichestvo = (count // 3) + ostatok

    # берем столько камней, чтобы осталось 3x +1
    if ostatok == 0:
        app_take = 2
    elif ostatok == 1:
        app_take = 3
    elif ostatok == 2:
        app_take = 1

    count = count - app_take
    print('Программа взяла', app_take)
    print('Осталось камней', count)

    user_take = int(input())

    while user_take > 3 or user_take < 1 or user_take > count:
        user_take = int(input())

    count -= user_take
    print('Осталось камней', count)

if count == 0:
    print('Ну ж то же, я проиграл!')
elif count == 1:
    app_take = 1
    print ('Программа взяла ', app_take, 'и выиграла')
elif count == 2:
    app_take = 2
    print ('Программа взяла ', app_take, 'и выиграла')
elif count == 3:
    app_take = 3
    print ('Программа взяла ', app_take, 'и выиграла')
