from datetime import datetime
ant = []
acum = 0
com = 0
app = 0
with open('iteraciones.txt ', 'r') as fichero:
    for linea in fichero.readlines():
        el = linea.split(',')
        if com > 0:
            if el[0] == ant [0]:
                fechAct = datetime.strptime(el[1].replace('\n',''), '%m/%d/%Y')
                fechAnt = datetime.strptime(ant[1].replace('\n',''), '%m/%d/%Y')
                dias = abs(fechAct-fechAnt).days
                acum += dias
                app +=1
            else:
                print(ant[0], ' ',int(acum/app))
                acum=0
                app=0
        ant= el[:]
        com = com+1
    print(ant[0], ' ', int(acum/app))
