cafea = int(input('Cate cafele pot face astazi: '))
rez_lapte = int(input('Cate rezerve lapte avem: '))
while True:
    while True:
        tip = input('Ce VREI?   Espresso (e|E) | Cappuccino (c|C):')
        tip = tip.lower()
        if tip in ['e', 'c']:
            break
    if tip == 'e':
        espresso = int(input("cate cafele espresso doriti? "))
        cafea = cafea - espresso
    elif tip == 'c':
        capp = int(input('cam cat cappucino vrei? '))
        cafea = cafea - capp
        rez_lapte = rez_lapte - 2*capp
    print('Mai pot face ', cafea, ' cafele si mai am ', rez_lapte, ' lapte')

    # mecanism de oprire bucla - BREAK
    stop = input('Doresti sa te opresti? y/Y pentru oprire ')
    if stop == 'y' or stop == 'Y':
        break
print("gata! mai am ", cafea, ' cafele')

