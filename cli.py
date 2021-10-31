import main

info = '''
   ___  ___ ___ ___    _   ___ ___   ___   __  __ _  _  ___  _  _  ___   ___ _    ___ _  ___   __
  / _ \| _ \ __| _ \  /_\ / __| __| / __| |  \/  | \| |/ _ \| || |/ _ \ / __| |  | __| \| \ \ / /
 | (_) |  _/ _||   / / _ \ (__| _|  \__ \ | |\/| | .` | (_) | __ | (_) | (__| |__| _|| .` |\ V / 
  \___/|_| |___|_|_\/_/ \_\___|___| |___/ |_|  |_|_|\_|\___/|_||_|\___/ \___|____|___|_|\_| |_|  
                                                                                                 
PŘEHLED OPERACÍ

+ pro sčítání
- pro odčítání
* pro násboení
/ pro dělení
= pro zjednodušení mnohočlenu
e pro opuštění programu

ZÁPIS MNOHOČLENŮ

Mnohočleny se zapisují normálně.
Před znaménkem je mezera, ale za ním ne.
Mocnina se zapíše jako normální číslo.
Nikde jinde se mezera nepíše.
Je možně že se někde vyskytne ".0" navíc.
Desetinnou čárku je možné zapsat i jako čárku

Příklad:
-6a2 +3a -12

##################################################################################################################
'''
print(info)

command = ''
while command != 'e':
    command = input('příkaz: ')[:1]
    if command == '+':
        m1 = main.devisualize(input('napiš první mnohočlen: '))
        m2 = main.devisualize(input('napiše druhý mnohočlen: '))
        print(main.visualize(main.scitani(m1, m2)))
    elif command == '-':
        m1 = main.devisualize(input('napiš první mnohočlen: '))
        m2 = main.devisualize(input('napiše druhý mnohočlen: '))
        print(main.visualize(main.odcitani(m1, m2)))
    elif command == '*':
        m1 = main.devisualize(input('napiš první mnohočlen: '))
        m2 = main.devisualize(input('napiše druhý mnohočlen: '))
        print(main.visualize(main.nasobeni(m1, m2)))
    elif command == '/':
        m1 = main.devisualize(input('napiš první mnohočlen: '))
        m2 = main.devisualize(input('napiše druhý mnohočlen: '))
        print(main.visualize(main.deleni(m1, m2)))
    elif command == '=':
        m = main.devisualize(input('mnohočlen ke zjednodušení: '))
        print(main.visualize(main.zjednodusovani(m)))
    elif command == 'e':
        pass
    else:
        print('ŠPATNÝ PŘÍKAZ!')