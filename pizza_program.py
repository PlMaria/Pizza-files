import random
import pprint

def pizza():
    print("Домашняя-Пицца приветствует!")
    print("Программа для заказа пиццы.")
    print("Спасибо, что выбрали нашу компанию!","\n")
    adress=input("Укажите адрес доставки: ")
    P=dict()
    P['ПЕППЕРОНИ']={'Cостав':"Пепперони, моцарелла, томатный соус",'size':{'S':"395", 'M':"545"}}
    P['МАРГАРИТА']={'Состав': 'Томаты, моцарелла, томатный соус','size':{'S':"395", 'M':"545"}}
    P['ГАВАЙСКАЯ']={'Состав': 'Курица, ветчина, ананас, моцарелла, томатный соус','size':{'S':"415",'M':"595"}}
    print('Пиццы в наличии:')
    pprint.pprint(P)
    L=[]
    
    while True:
        pizza=input('Укажите пиццу для заказа или "выход" для окончания ввода: ')
        if pizza=='выход':
            break
        elif pizza.upper() in P:
            choose_size=input('Укажите размер пиццы (S или M): ')
            price=int(P[pizza.upper()]['size'][choose_size])
            k=int(input('Укажите количество: '))
            D=dict()
            D['pizza_order']={'count':k,'pizza':pizza.upper(),'size':choose_size, 'Price': k*price}
            L.append(D)
        else:
            print("Ошибка. Повторите ввод.")

    while True:
        date=input("Укажите срок доставки (сегодня, завтра): ")
        if date.lower() in ['сегодня','завтра']:
            break
        else:
            print("Ошибка. Повторите ввод.")
            
    time=input("Укажите время доставки: ")
    contact=input("Укажите контактные данные: ")

    D=dict()
    D['adress']={adress}
    D['contact']={contact}
    D['date']={date}
    D['time']={time}
    print("Заказ: ")
    pprint.pprint(D)
    pprint.pprint(L)

    p=[]
    for i in L:
        k=i['pizza_order']['Price']
        p.append(k)
    summary=sum(p)

    print('''Итог:  ''',summary)

    if len(L)==3:
        minim=min(p)
        index=p.index(min(p))     
        print('''Пицца ''', list(P.keys())[index],''' с наименьшей стоимостью:''',minim, "руб.")
        print('''Убрали стоимость пиццы ''', list(P.keys())[index],''' из заказа''')
        summary=summary-minim
        print('''Итог:  ''',summary)

    if list(D['date'])[0]=='завтра':
        
        sale=summary*0.05
        print('''Скидка 5%: ''',sale)
        print('''Итог c учетом скидки: ''', (summary-sale))
        

    return "Заказ принят"

print(pizza())
