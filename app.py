import PySimpleGUI as sg
import requests

def pegar_cotacoes(codigo_moeda):
    try:
        requisicao = requests.get(f"https://economia.awesomeapi.com.br/last/{codigo_moeda}-BRL")
        requisicao_dic = requisicao.json()
        cotacao = requisicao_dic[f'{codigo_moeda}BRL']['bid']
        return f' A moeda está cotada hoje no valor de {cotacao} reais'
    except:
        return "Código de Moeda Inválido"

sg.theme('DarkAmber')
layout = [
    [sg.Text('Cotação de moeda',font=('Arial',12))],
    [sg.InputOptionMenu(['USD','EUR','BTC','ETH'], size=(35,2), key='opcao'), sg.Button('Pesquisar')],
    [sg.Text('', key='saida')]
]

window = sg.Window("COTAÇÕES DE MOEDAS", layout)
while True:
    evento, valor = window.read()
    if evento == sg.WIN_CLOSED:
        break
    if evento == 'Pesquisar':
        entrada = valor['opcao']
        moeda = pegar_cotacoes(entrada)
        window['saida'].update(moeda)

window.close()