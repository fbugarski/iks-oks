

def prikaz_tabla(tabla):
    print('---------')    
    print('|' +tabla[7]+' |'+tabla[8]+'| '+tabla[9]+ '|')
    print('---------')
    print('|' +tabla[4]+' |'+tabla[5]+'| '+tabla[6]+ '|')
    print('---------')
    print('|' +tabla[1]+' |'+tabla[2]+'| '+tabla[3]+ '|')
    print('---------')    

test_tabla = ['#','1','2','3','4','5','6','7','8','9']
print('Pozicije su kao na numerickoj tastaturi!')


def igrac_input():
     
    znak = ''

    while znak != 'X' and znak != 'O':
        znak = input('Igrac 1, izaberite X ili O: ').upper()
        print("Izvinite, izaberite znak X or O ")

    igrac1 = znak

    if igrac1 == 'X':
        igrac2 = 'O'
    else:
        igrac2 = 'X'
    return(igrac1,igrac2)


def postavi_znak(tabla, znak, pozicija):

    tabla[pozicija] = znak

prikaz_tabla(test_tabla)

def provera_pobede(tabla,znak):

    if tabla[1] == tabla[2] == tabla[3] == znak:
        return True
    if tabla[4] == tabla[5] == tabla[6] == znak:
        return True
    if tabla[7] == tabla[8] == tabla[9] == znak:
        return True
    if tabla[1] == tabla[4] == tabla[7] == znak:
        return True
    if tabla[2] == tabla[5] == tabla[8] == znak:
        return True
    if tabla[3] == tabla[6] == tabla[9] == znak:
        return True
    if tabla[1] == tabla[5] == tabla[9] == znak:
        return True
    if tabla[3] == tabla[5] == tabla[7] == znak:
        return True
    return False

test_tabla = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

print(provera_pobede(test_tabla,'X'))

import random

def prvi_bira():
    flip = random.randint(0,1)
    if flip == 0:
        return "Igrac 1"
    else :
        return "Igrac 2"


def provera_polja (tabla, pozicija):
    return tabla[pozicija] == ' '

def provera_cele_table(tabla):
    return len([x for x  in tabla if x  == '#']) == 1
        

def izbor_igraca(tabla):

    pozicija = 0

    while pozicija not in [1,2,3,4,5,6,7,8,9] or not provera_polja(tabla,pozicija):
        pozicija = int(input('Izaberi poziciju: (1-9)'))
        
    return pozicija

def igraj_ponovo():
        igraj_ponovo = input("Ako zelite da igrate ponovo ukucajte da. ")
        if igraj_ponovo == 'da':
          return True
        else:
            return False

print("Dobrodosli u iks-oks!!!")

while True:
    tabla = [' ']*10
    igrac1_znak,igrac2_znak = igrac_input()

    potez = prvi_bira()
    print ( potez + ' prvi igra')

    igraj_igru = input('Spremni za pocetak? da ili ne? ')

    if igraj_igru == 'da':
        igra_moze_da_pocne = True
    else:
        igra_moze_da_pocne = False

    while igra_moze_da_pocne:
        if potez == 'Igrac 1':

            prikaz_tabla(tabla)
            pozicija = izbor_igraca(tabla)
            postavi_znak(tabla,igrac1_znak,pozicija)

            if provera_pobede(tabla,igrac1_znak):
                prikaz_tabla(tabla)
                print('Igrac 1 je pobedio!!!')
                igra_moze_da_pocne = False
            else:
                if provera_cele_table(tabla):
                    prikaz_tabla(tabla)
                    print("Nereseno!!!")
                    break
                else:
                    potez = 'Igrac 2'


        else:

            prikaz_tabla(tabla)
            pozicija = izbor_igraca(tabla)
            postavi_znak(tabla,igrac2_znak,pozicija)

            if provera_pobede(tabla,igrac2_znak):
                prikaz_tabla(tabla)
                print('Igrac 2 je pobedio!!!')
                igra_moze_da_pocne = False
            else:
                if provera_cele_table(tabla):
                    prikaz_tabla(tabla)
                    print("Nereseno!!!")
                    break
                else:
                    potez = 'Igrac 1'

    if not igraj_ponovo():
        print('Hvala na igranju, vidimo se uskoro!')