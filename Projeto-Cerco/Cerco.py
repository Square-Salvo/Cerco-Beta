import PySimpleGUI as sg 
from random import randrange, uniform 

sg.theme('DarkAmber')

#Layout

layout = [
    [sg.Text('Dano de fortificação')],
    [sg.Checkbox('Baixo', key='fbaixo'), sg.Checkbox('Médio', key='fmedio'), sg.Checkbox('Alta', key='falta')],
    [sg.Text('Tipo de Tropa')],
    [sg.Checkbox('Infantaria Pesada', key='pesada'), sg.Checkbox('Infantaria Leve', key='leve')],
    [sg.Text('Guarnição'), sg.Input( key='guarda')],
    [sg.Text('Tropas Invasores'), sg.Input(key='tropas')],
    [sg.Text('Habilidade do General'), sg.Input(key='general')],
    [sg.Button('Ok')],
    [sg.Output(size=(80,20))]

]

#Janela

window = sg.Window('Window Title').Layout(layout)


while True:
    button, values =window.read()
    #Dados extraídos do menu Checkbox
    #Tipo-tropa
    pesada=values['pesada']
    leve=values['leve']
    #nivel-forte
    fbaixo=values['fbaixo']
    fmedio=values['fmedio']
    falta=values['falta']
    #Imput
    guarda = int(values['guarda']) 
    tropas=int(values['tropas'])
    general=int(values['general'])
    general=general*5

    #Calculos

    #Dados Guarnição:
    d100=randrange(1,100)+general
    d150=randrange(1,150)+general
    d300=randrange(1,300)+general

    #Dados Ataque:
    d350=randrange(1,350)
    d500=randrange(1,500)
    if (fbaixo==True): 
        if (pesada==True): 

            var=guarda-d100
            tvar=tropas-d350
            window['guarda'].update(var)
            window['tropas'].update(tvar)
            print('Baixas Guarnição: ', d100)
            print('Baixas Invasores: ', d350)
            print('Baixo')
        else: 
            var=guarda-d100
            tvar=tropas-d500
            window['guarda'].update(var)
            window['tropas'].update(tvar)
            print('Baixas Guarnição: ', d100)
            print('Baixas Invasores: ', d500)
            print('Baixo')

    elif (fmedio==True): 
        if (pesada==True): 
            var=guarda-d150
            tvar=tropas-d300
            window['guarda'].update(var)
            window['tropas'].update(tvar)
            print('Baixas Guarnição: ', d150)
            print('Baixas Invasores: ', d350)
            print('Baixo')
        else: 
            var=guarda-d150
            tvar=tropas-d500
            window['guarda'].update(var)
            window['tropas'].update(tvar)
            print('Baixas Guarnição: ', d150)
            print('Baixas Invasores: ', d500)
            print('Baixo')

    else: 
        if (pesada==True): 
            var=guarda-d300
            tvar=tropas-d350
            window['guarda'].update(var)
            window['tropas'].update(tvar)
            print('Baixas Guarnição: ', d300)
            print('Baixas Invasores: ', d350)
            print('Baixo')
        else: 
            var=guarda-d300
            tvar=tropas-d500
            window['guarda'].update(var)
            window['tropas'].update(tvar)
            print('Baixas Guarnição: ', d300)
            print('Baixas Invasores: ', d500)
            print('Baixo')



    

window.close()