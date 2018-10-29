import random

def pizza():
    print("Домашняя-Пицца приветствует!")
    print("Программа для заказа пиццы.")
    print("Спасибо, что выбрали нашу компанию!","\n")
    street=input("Укажите адрес доставки: ")
    lis=[['ГАВАЙСКАЯ',['M',595], ['S',415]],
         ['МАРГАРИТА',['M',545], ['S',395]],
         ['ПЕППЕРОНИ',['M',545], ['S',395]]]
    ls=[]
    for i in lis:
        ls.append(i[0])
    print(
        '''
***************** Пиццы в наличии:
{'ГАВАЙСКАЯ': {'consist': ['курица',
                            'ветчина',
                            'ананас',
                            'моцарелла',
                            'томатный соус'],
                'size_price': {'M': 595, 'S': 415}},
'МАРГАРИТА': {'consist': ['томаты', 'моцарелла', 'томатный соус'],
                'size_price': {'M': 545, 'S': 395}},
'ПЕППЕРОНИ': {'consist': ['пепперони', 'моцарелла', 'томатный соус'],
                'size_price': {'M': 545, 'S': 395}}}
*****************
        '''
        )
    name=[]
    size=[]
    price=[]
    count=[]
    date=[]
    tm=[]
    contact=[]
    while True:
        x=input("Укажите пиццу для заказа или 'выход' для окончания ввода: ")
        if x in ls:
            name.append(x)
            for i in lis:
                if x==i[0]:
                    y=input("Укажите размер пиццы (S или M): ")
                    for j in i:
                        if y==j[0]:
                            size.append(y)
                            price.append(j[1])
            z=int(input("Укажите количество: "))
            count.append(z)
        elif x=="выход":
            break
        elif x not in ls:
            print("Ошибка. Повторите ввод.")
    while True:
        x=input("Указать срок доставки (сегодня, завтра): ")
        if x not in ['сегодня','завтра']:
            print("Ошибка. Повторите ввод.")
        else:
            date.append(x)
            break
    x=input("Указать время доставки: ")
    tm.append(x)
    x=input("Указать контактные данные: ")
    contact.append(x)
    
    print(
        '''
***************** Заказ:
{'contact': ''',contact,''',
 'date': ''',date)
    print("'pizza_order': ")
    for i in range(len(name)):
        print("\t","[{'count': ",count[i],", 'pizza': ",name[i],", 'size': ",size[i])
    print('''
 'tm': '12'}
*****************
    ''')

    summary=0
    for i in range(len(price)):
        summary=summary+(price[i]*count[i])

    print('''
*** Итог:  ''',summary)
    
    if len(name)==3:
        minim=min(price)
        index=price.index(min(price))     
        print('''
*** Пицца ''', name[index],''' с наименьшей стоимостью:''',minim, "руб."
              )
        print('''
*** Убрали стоимость пиццы ''', name[index],''' из заказа'''
              )

    if date[0]=='завтра':
        summary=summary-minim
        sale=summary*0.05
        print('''
Скидка 5%: ''',sale)
        print('''
Итог c учетом скидки: ''', (summary-sale))

    return "Заказ принят"

print(pizza())

'''
Домашняя-Пицца приветствует!
Программа для заказа пиццы.
Спасибо, что выбрали нашу компанию! 

Укажите адрес доставки: улица Грибоедова, 30-32

***************** Пиццы в наличии:
{'ГАВАЙСКАЯ': {'consist': ['курица',
                            'ветчина',
                            'ананас',
                            'моцарелла',
                            'томатный соус'],
                'size_price': {'M': 595, 'S': 415}},
'МАРГАРИТА': {'consist': ['томаты', 'моцарелла', 'томатный соус'],
                'size_price': {'M': 545, 'S': 395}},
'ПЕППЕРОНИ': {'consist': ['пепперони', 'моцарелла', 'томатный соус'],
                'size_price': {'M': 545, 'S': 395}}}
*****************
        
Укажите пиццу для заказа или 'выход' для окончания ввода: 
Ошибка. Повторите ввод.
Укажите пиццу для заказа или 'выход' для окончания ввода: ГАВАЙСКАЯ
Укажите размер пиццы (S или M): S
Укажите количество: 1
Укажите пиццу для заказа или 'выход' для окончания ввода: МАРГАРИТА
Укажите размер пиццы (S или M): M
Укажите количество: 1
Укажите пиццу для заказа или 'выход' для окончания ввода: ПЕППЕРОНИ
Укажите размер пиццы (S или M): S
Укажите количество: 1
Укажите пиццу для заказа или 'выход' для окончания ввода: выход
Указать срок доставки (сегодня, завтра): 
Ошибка. Повторите ввод.
Указать срок доставки (сегодня, завтра): завтра
Указать время доставки: 12
Указать контактные данные: 921

***************** Заказ:
{'contact':  ['921'] ,
 'date':  ['завтра']
'pizza_order': 
	 [{'count':  1 , 'pizza':  ГАВАЙСКАЯ , 'size':  S
	 [{'count':  1 , 'pizza':  МАРГАРИТА , 'size':  M
	 [{'count':  1 , 'pizza':  ПЕППЕРОНИ , 'size':  S

 'tm': '12'}
*****************
    

*** Итог:   1355

*** Пицца  ПЕППЕРОНИ  с наименьшей стоимостью: 395 руб.

*** Убрали стоимость пиццы  ПЕППЕРОНИ  из заказа

Скидка 5%:  48.0

Итог c учетом скидки:  912.0
Заказ принят
'''
