import requests
from bs4 import BeautifulSoup
import json
def one():
    z =' https://raw.githubusercontent.com/openfootball/football.json/master/2020-21/es.1.clubs.json'
    a1 = []
    a2 = []

    class X():
        def __init__(self):
            self.enlace = z

    AM = X()
    r = requests.get(AM.enlace)
    data = json.loads(r.text)
    for q in data['clubs']:
        q1 = q['code']
        if q1 is not None:
            a1.append(q1)
        else:
            a2.append(q1)
    cuenta = (len(a1))
    cuenta2 = (len(a2))
    cont = cuenta + cuenta2

    a3 = a1.copy()
    s1 = open('datos.txt', 'a+')
    s1.write(f'Tenemos {cont} en la Liga, Los codigos de los clubs {a3} ')
    s1 = open('datos.txt', 'a+', encoding='utf-8')
    print(s1.read())
    aa = open('datos.txt', 'w', encoding='utf-8')
    aa.write(f'{q1},{q}')
    aa = open('datos.txt', 'r', encoding='utf-8')
    print(data)
def two():
    z = ' https://raw.githubusercontent.com/openfootball/football.json/master/2020-21/de.1.clubs.json'
    a1 = []
    a2 = []

    class X():
        def __init__(self):
            self.enlace = z

    AM = X()
    r = requests.get(AM.enlace)
    data = json.loads(r.text)
    for q in data['clubs']:
        q1 = q['code']
        if q1 is not None:
            a1.append(q1)
        else:
            a2.append(q1)
    cuenta = (len(a1))
    cuenta2 = (len(a2))
    cont = cuenta + cuenta2

    a3 = a1.copy()
    s1 = open('datos.txt', 'a+')
    s1.write(f'Tenemos {cont} en la Liga, Los codigos de los clubs {a3} ')
    s1 = open('datos.txt', 'a+', encoding='utf-8')
    print(s1.read())
    aa = open('datos.txt', 'w', encoding='utf-8')
    aa.write(f'{q1},{q}')
    aa = open('datos.txt', 'r', encoding='utf-8')
    print(data)
def three():
    z = 'https://raw.githubusercontent.com/openfootball/football.json/master/2020-21/it.1.clubs.json'
    a1 = []
    a2 = []

    class X():
        def __init__(self):
            self.enlace = z

    AM = X()
    r = requests.get(AM.enlace)
    data = json.loads(r.text)
    for q in data['clubs']:
        q1 = q['code']
        if q1 is not None:
            a1.append(q1)
        else:
            a2.append(q1)
    cuenta = (len(a1))
    cuenta2 = (len(a2))
    cont = cuenta + cuenta2

    a3 = a1.copy()
    s1 = open('datos.txt', 'a+')
    s1.write(f'Tenemos {cont} en la Liga, Los codigos de los clubs {a3} ')
    s1 = open('datos.txt', 'a+', encoding='utf-8')
    print(s1.read())
    aa = open('datos.txt', 'w', encoding='utf-8')
    aa.write(f'{q1},{q}')
    aa = open('datos.txt', 'r', encoding='utf-8')
    print(data)
def four():
    z = 'https://raw.githubusercontent.com/openfootball/football.json/master/2020-21/at.2.clubs.json'
    a1 = []
    a2 = []

    class X():
        def __init__(self):
            self.enlace = z

    AM = X()
    r = requests.get(AM.enlace)
    data = json.loads(r.text)
    for q in data['clubs']:
        q1 = q['code']
        if q1 is not None:
            a1.append(q1)
        else:
            a2.append(q1)
    cuenta = (len(a1))
    cuenta2 = (len(a2))
    cont = cuenta + cuenta2

    a3 = a1.copy()
    s1 = open('datos.txt', 'a+')
    s1.write(f'Tenemos {cont} en la Liga, Los codigos de los clubs {a3} ')
    s1 = open('datos.txt', 'a+', encoding='utf-8')
    print(s1.read())
    aa = open('datos.txt', 'w', encoding='utf-8')
    aa.write(f'{q1},{q}')
    aa = open('datos.txt', 'r', encoding='utf-8')
    print(data)
def five():
    z = 'https://raw.githubusercontent.com/openfootball/football.json/master/2020-21/en.1.clubs.json'
    a1 = []
    a2 = []

    class X():
        def __init__(self):
            self.enlace = z

    AM = X()
    r = requests.get(AM.enlace)
    data = json.loads(r.text)
    for q in data['clubs']:
        q1 = q['code']
        if q1 is not None:
            a1.append(q1)
        else:
            a2.append(q1)
    cuenta = (len(a1))
    cuenta2 = (len(a2))
    cont = cuenta + cuenta2

    a3 = a1.copy()
    s1 = open('datos.txt', 'a+')
    s1.write(f'Tenemos {cont} en la Liga, Los codigos de los clubs {a3} ')
    s1 = open('datos.txt', 'a+', encoding='utf-8')
    print(s1.read())
    aa = open('datos.txt', 'w', encoding='utf-8')
    aa.write(f'{q1},{q}')
    aa = open('datos.txt', 'r', encoding='utf-8')
    print(data)

while True:
    try:
        pr = input("""
        1.Acceder a la información la Liga España
        2.Acceder a la información de la Liga alemana
        3.Acceder a la información de la Liga italiana
        4.Acceder a la información de la Liga austríaca
        5.Acceder a la información de la Liga inglesa
        6. Exit
        :""")
        if pr == '1':
            one()
        elif pr == '2':
            two()
        elif pr == '3':
            three()
        elif pr == '4':
            four()
        elif pr == '5':
            five()
        elif pr == '6':
            break
    except ValueError:
        print('Error')