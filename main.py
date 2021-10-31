# -*- coding: utf-8 -*-
from razeni_mnohoclenu import mergesort
import re

opacny = lambda m: [(-clen[0], clen[1]) for clen in m]  # vrátí mnohočlen opačný


def zjednodusovani(m):  # zjednoduší mnohočlen
    for clen_i in range(len(m)):
        m[clen_i] = (m[clen_i][0], sorted(m[clen_i][1]))

    promenne = []
    m_return = []
    for clen in m:
        if clen[1] not in promenne:
            promenne.append(clen[1])

    for promenna in promenne:
        koeficient = 0

        for clen in m:
            if clen[1] == promenna:
                koeficient += clen[0]

        m_return.append((koeficient, promenna))

    return m_return


def scitani(m1, m2):  # sečte mnohočleny m1 a m2
    m_return = m1 + m2
    m_return = zjednodusovani(m_return)
    return m_return


def odcitani(m1, m2):  # odečte mnohočlen m2 od m1
    m_return = scitani(m1, opacny(m2))
    return m_return


def nasobeni_c(c1, c2):  # vynásobí člen c1 a c2
    koeficient = c1[0] * c2[0]
    promenne = scitani(c1[1], c2[1])
    return (koeficient, promenne)


def nasobeni(m1, m2):           # vynásobí mnohočlen m1 a m2
    m_return = []

    for clen1 in m1:
        for clen2 in m2:
            m_return.append(nasobeni_c(clen1, clen2))

    m_return = zjednodusovani(m_return)
    return m_return


def deleni_c(c1, c2):           # vydělí člen c1 členem c2
    koeficient = c1[0] / c2[0]
    promenne = odcitani(c1[1], c2[1])
    return (koeficient, promenne)


def deleni(m1, m2):             # vydělí mnohočlen m1 mnohočlenem m2
    m_return = []

    for clen1 in m1:
        for clen2 in m2:
            m_return.append(deleni_c(clen1, clen2))

    m_return = zjednodusovani(m_return)
    return m_return


def visualize(m):               # převede mnohočlen čitelný pro počítače na mnohočlen čitelný lidmi
    m = mergesort(m)
    mocniny = '⁰¹²³⁴⁵⁶⁷⁸⁹'
    txt = ''

    for clen in m:
        if int(clen[0]) == clen[0]:
            clen = (int(clen[0]), clen[1])
        if clen[0] != 0:
            if clen[0] > 0:
                txt += f' +{str(clen[0])}'
            else:
                txt += f' -{str(abs(clen[0]))}'

            for prommenna in clen[1]:
                if prommenna[0] == int(prommenna[0]):
                    prommenna = (int(prommenna[0]), prommenna[1])
                if prommenna[0] == 1:
                    txt += prommenna[1]
                elif prommenna[0] != 0:
                    mocnina = str(prommenna[0])
                    txt += prommenna[1] + mocnina

    if txt[1] == '+':
        txt = txt[2:]
    else:
        txt = txt[1:]

    return txt


def devisualize(txt):               # převede mnohočlen čitelný lidmi na mnohočlen pro počítače
    prvni_promenna = re.search(r'[a-z]', txt).group()

    str_m = txt.split(' ')
    for clen_i in range(len(str_m)):
        if str_m[clen_i][0] == '+':
            str_m[clen_i] = str_m[clen_i][1:]

    m = []

    for clen in str_m:
        koeficient_str = ''
        for char in clen:
            if char.isdigit() or char in set('.,-'):
                koeficient_str += char
            else:
                break
        koeficient = float(koeficient_str.replace(',', '.', 1))
        clen_bez_koef = clen[len(koeficient_str):]

        promenne = []
        if set(clen_bez_koef) & set('qqwertyuiopasdfghjklzxcvbnm'):
            pismeno = ''
            stupen = ''
            for char in clen_bez_koef:
                if char in set('qwertyuiopasdfghjklzxcvbnm') and not pismeno:
                    pismeno = char

                elif (char.isdigit() or char in set('.,-')) and pismeno:
                    stupen += char

                else:
                    if stupen == '':
                        stupen = '1'
                    promenne.append((float(stupen), pismeno))
                    pismeno = char
                    stupen = ''
            if stupen == '':
                stupen = '1'
            promenne.append((float(stupen), pismeno))
            pismeno = char
            stupen = ''

            m.append((koeficient, promenne))

        else:
            m.append((koeficient, [(0, prvni_promenna)]))

    return m


if __name__ == '__main__':
    m1 = [(-1, [(1, 'x')]), (2, [(1, 'x')]), (3.5, [(1, 'y')])]
    m2 = [(3, [(1, 'y')]), (-2, [(1, 'y')]), (1.5, [(1, 'x')])]

    m = [(12, [(0, 'a')]), (-6, [(2, 'a')]), (3, [(1, 'a')])]
    c = (3, [(1, 'a')])

    c1 = (3, [(1, 'x'), (1, 'y')])
    c2 = (2, [(1, 'x')])

    print(visualize(m))
