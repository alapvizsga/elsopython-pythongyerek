#---------------------------------------------------------

def osszead(szam1, szam2):
    """ A függvény két számot kap és 
        visszatér a két szám összegével.
    """
    pass
    return szam1 + szam2


#assert osszead(14, -8) == 6
#---------------------------------------------------------

def kisebb(szam1, szam2):
    """ A függvény két számot kap és 
        visszatér a kisebbel.
    """
    pass
    if szam1 > szam2:
        return szam2
    else:
        return szam1


assert kisebb(10, -7) == -7
assert kisebb(-10, 7) == -10
#---------------------------------------------------------

def nagyobb(szam1, szam2):
    """ A függvény két számot kap és 
        visszatér a nagyobbal.
    """
    pass
    if szam1 < szam2:
        return szam2
    else:
        return szam1
        

assert nagyobb(12, -8) == 12
assert nagyobb(-12, -8) == -8
#---------------------------------------------------------

def szamtani_kozep(szam1, szam2):
    """ A függvény két számot kap és 
        visszatér a számtani középpel.
    """
    pass
    return (szam1 + szam2) / 2

assert szamtani_kozep(3, 5) == 4.0
#---------------------------------------------------------
 
def negyzet_kerulet(oldal):
    """ A függvény egy négyzet oldalhosszát kapja bemenetként és 
        visszatér a négyzet kerületével.
    """
    pass
    return oldal * 4


assert negyzet_kerulet(5) == 20
assert negyzet_kerulet(5.1) == 20.4
#---------------------------------------------------------
 
def negyzet_terulet(oldal):
    """ A függvény egy négyzet oldalhosszát kapja bemenetként és 
        visszatér a négyzet területével.
    """    
    pass
    return oldal * oldal


assert negyzet_terulet(5.0) == 25.0
#---------------------------------------------------------
 
def teglalap_kerulet(oldal1, oldal2):
    """ A függvény egy téglalap oldalhosszait kapja bemenetként és 
        visszatér a téglalap kerületével.
    """
    
    pass # Írd a kódodat a következő sorokba!
    return (oldal1 + oldal2) * 2


assert teglalap_kerulet(5, 6) == 22
#---------------------------------------------------------
 
def teglalap_terulet(oldal1, oldal2):
    """ A függvény egy téglalap oldalhosszait kapja bemenetként és 
        visszatér a téglalap területével.
    """
    pass # Írd a kódodat a következő sorokba!
    return oldal1 * oldal2

assert teglalap_terulet(5, 6) == 30          
#---------------------------------------------------------
 
def kulonbseg(szam1, szam2):
    """ A függvény két számot kap bemenetként és 
        visszatér a két szám különbségével.
    """    
    pass # Írd a kódodat a következő sorokba!
    return szam1 - szam2

assert kulonbseg(5, 6) == -1
assert kulonbseg(6, 5) == 1
#---------------------------------------------------------     

def maradek(szam1, szam2):
    """ A függvény két számot kap bemenetként és 
        visszatér a két szám osztásának maradékával.
    """    
    pass # Írd a kódodat a következő sorokba!
    return szam1 % szam2

assert maradek(9, 4) == 1
assert maradek(8, 4) == 0
     
#---------------------------------------------------------      

def paros(szam):
    """ A függvény egy számot kap bemenetként, 
        majd True-val tér vissza, ha a szám páros és 
        False-al ha a szám páratlan.
    """    
    pass # Írd a kódodat a következő sorokba!
    if szam % 2 == 0:
        return True
    else:
        return False

assert paros(12) == True
assert paros(13) == False
#---------------------------------------------------------

def kettovel_oszthato(szam):
    """ A függvény egy számot kap bemenetként és 
        True-val tér vissza, ha a szám kettővel osztható és 
        False-al ha nem.
    """    
    pass # YOUR CODE HERE
    if szam % 2 == 0:
        return True
    else:
        return False

assert kettovel_oszthato(12) == True
assert kettovel_oszthato(13) == False
#---------------------------------------------------------    
def harommal_oszthato(szam):
    """ A függvény egy számot kap bemenetként és 
        True-val tér vissza, ha a szám hárommal osztható és 
        False-al ha nem.
    """    
    pass # Írd a kódodat a következő sorokba!
    if szam % 3 == 0:
        return True
    else:
        return False

assert harommal_oszthato(15) == True
assert harommal_oszthato(16) == False     
#---------------------------------------------------------

def hettel_oszthato(szam):
    """ A függvény egy számot kap bemenetként és 
        True-val tér vissza, ha a szám héttel osztható és 
        False-al ha nem.
    """    
    pass # Írd a kódodat a következő sorokba!
    if szam % 7 == 0:
        return True
    else:
        return False

assert hettel_oszthato(21) == True
assert hettel_oszthato(22) == False           
#---------------------------------------------------------

def kocka_terfogat(oldal):
    """ A függvény bemenetként megkapja a kocka oldal hosszúságát és 
        a kocka térfogatával tér vissza.
    """    
    pass # Írd a kódodat a következő sorokba!
    return oldal ** 3
 
assert kocka_terfogat(2) == 8
assert kocka_terfogat(3) == 27          
#---------------------------------------------------------
def teglatest_terfogat(a, b, c):
    """ A függvény bemenetként megkapja a téglatest oldalainak hosszúságát és 
        a téglatest térfogatával tér vissza.
    """    
    pass # Írd a kódodat a következő sorokba!
    return a * b * c

assert teglatest_terfogat(2, 3, 4) == 24      
#---------------------------------------------------------

def derekszogu_haromszog_terulet(befogo1, befogo2):
    """ A függvény bemenetként megkapja a befogók hosszát és 
        a háromszög területével tér vissza.
    """    

    pass # Írd a kódodat a következő sorokba!
    return (befogo1 * befogo2) // 2

assert derekszogu_haromszog_terulet(3, 4) == 6      
#---------------------------------------------------------
def derekszogu_haromszog_atfogo(befogo1, befogo2):
    """ A függvény bemenetként megkapja a befogók hosszát és 
        az átfogó hosszával tér vissza.
    """    
    pass # Írd a kódodat a következő sorokba!
    return (befogo1 ** 2 + befogo2 ** 2) ** 0.5

assert derekszogu_haromszog_atfogo(3, 4) == 5.0     
#---------------------------------------------------------

def negyzet_atloja(oldal):
    """ A függvény bemenetként megkapja a négyzet oldalának hosszát és 
        az átló hosszával tér vissza.
    """    
    pass # Írd a kódodat a következő sorokba!
    return oldal * (2 ** 0.5)

assert round(negyzet_atloja(10),5) == round(14.142135623730951,5)
#---------------------------------------------------------

def teglalap_atloja(a, b):
    """ A függvény bemenetként megkapja az oldalak hosszát és 
        az átló hosszával tér vissza.
    """    
    pass # Írd a kódodat a következő sorokba!
    return (a ** 2 + b ** 2) ** 0.5

assert teglalap_atloja(3, 4) == 5.0
assert teglalap_atloja(6, 8) == 10.0
#---------------------------------------------------------

def abszolut(szam):
    """ A függvény a bemenő paraméterként kapott szám 
        abszolút értékével tér vissza.
    """    
    pass # Írd a kódodat a következő sorokba!
    if szam > 0:
        return szam
    else:
        return -szam

assert abszolut(-7) == 7
assert abszolut( 0) == 0
#========================================
