
def func_gener_uniq_tuple():
    tu_moduj_skladnie = "" #tutaj w cudzysłowiach eklep składnie else if w języku jaki trzeba
    opcjonalne_zamkniecie_warunku = "" #tutaj w cudzysłowiach można wkleić np. zamknięcie klamrowe
    ilosc_kombinacji = 0 #ile unikatów chcesz wygenerować -> format int

    q = set()
    while len(q) < ilosc_kombinacji:
        q.add(tuple(__import__('random').randint(0,1) for z in range(18)))

    for i in q: open('texter.txt', 'a').write(tu_moduj_skladnie + f"{i}" + opcjonalne_zamkniecie_warunku + '\n')
func_gener_uniq_tuple()


def func_gener_uniq_list():
    tu_moduj_skladnie = "" #tutaj w cudzysłowiach eklep składnie else if w języku jaki trzeba
    opcjonalne_zamkniecie_warunku = "" #tutaj w cudzysłowiach można wkleić np. zamknięcie klamrowe
    ilosc_kombinacji = 50 #ile unikatów chcesz wygenerować -> format int

    q = set()
    while len(q) < ilosc_kombinacji:
        q.add(tuple(__import__('random').randint(0,1) for z in range(18)))

    for i in q: open('texter.txt', 'a').write(tu_moduj_skladnie + f"{list(i)}" + opcjonalne_zamkniecie_warunku + '\n')
func_gener_uniq_list()


def func_gener_uniq_list_kamil():
    ilosc_kombinacji = 2**18 #ile unikatów chcesz wygenerować -> format int

    q = set()
    z = 1
    while len(q) < ilosc_kombinacji:
        q.add(tuple(__import__('random').randint(0,1) for z in range(18)))

    for i in q:
        open('texter.txt', 'a').write(f"else if (num == {z})"+"{"+f"{list(i)}" + "}"+'\n')
        z+=1
func_gener_uniq_list_kamil()
