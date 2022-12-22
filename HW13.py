tickets = int(input("Количество билетов:"))
N = 1
price = 0
while N <= tickets:
    age = int(input(f"Возраст посетителя для билета № {N}: "))
    if age < 18:
        print("Стоимость билета: 0 руб.")
    elif 18 <= age < 25:
        price += 990
        print("Стоимость билета: 990 руб.")
    else:
        price += 1390
        print("Стоимость билета: 1390 руб.")
    N += 1

if tickets > 3:
    price_d = price - (price / 10)
    print(f"Сумма к оплате: {price_d} руб. (с учетом скидки 10% за покупку более 3 билетов)")
else:
    print(f"Сумма к оплате: {price} руб")
