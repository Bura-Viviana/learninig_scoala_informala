cafea = 20
rez_lapte = 10
while True:
    espresso = input ('cate cafele espresso doriti? ')
    cafea = int(cafea)-int(espresso)
    print('Mai pot face ', cafea, ' cafele')
 # mecanism de oprire bucla - BREAK
    continuare = input('Doresti sa continui? (y/n) ')
    if continuare == 'n':
        break
print("gata! mai am ", cafea, ' cafele')

