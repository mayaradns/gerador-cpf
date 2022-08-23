# Gerador de CPF
import PySimpleGUI as sg
from random import randint

sg.theme('dark grey 9')

layout = [
    [sg.Image(filename='logo1.png')],
    [sg.Text('CPF', font='Arial, 20', pad=(0, (0, 10)))],
    [sg.Output(key='saida', font='Heveltica 18', pad=(0, (0, 10)))],
    [sg.Button('Gerar', font='Arial, 14', button_color=('Gray', 'Blue')),
     sg.Button('Sair', font='Arial, 14', button_color=('Gray', 'Blue'))],
]

janela = sg.Window('Gerador de CPF', element_justification='center', layout=layout, size=(350, 240))

while True:
    event, values = janela.read()

    if event == sg.WIN_CLOSED or event == 'Sair':
        break
    elif event == 'Gerar':
        num = str(randint(100000000, 999999999))

        novo_cpf = num
        reverso = 10
        total = 0

        for index in range(19):
            if index > 8:
                index -= 9

            total += int(novo_cpf[index]) * reverso

            reverso -= 1
            if reverso < 2:
                reverso = 11
                dig = 11 - (total % 11)

                if dig > 9:
                    dig = 0
                total = 0
                novo_cpf += str(dig)

        janela['saida'].update(novo_cpf)

janela.close()
