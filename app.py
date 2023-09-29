import PySimpleGUI as sg
import requests

def pegar_cotacoes(codigo_moeda):
    try:
        moedas_suportadas = ['USD', 'EUR', 'BTC', 'ETH']
        if codigo_moeda not in moedas_suportadas:
            return "Moeda não suportada."
        
        requisicao = requests.get(f"https://economia.awesomeapi.com.br/last/{codigo_moeda}-BRL")
        requisicao_dic = requisicao.json()
        cotacao = requisicao_dic[f'{codigo_moeda}BRL']['bid']
        # Arredonda para 2 casas decimais
        cotacao_formatada = "{:.2f}".format(float(cotacao))
        return cotacao_formatada
    except requests.exceptions.RequestException as e:
        return f"Erro na requisição: {str(e)}"
    except KeyError:
        return "Moeda não encontrada na API."

sg.theme('DarkAmber')
layout = [
    [sg.Text('Cotação de moeda', font=('Arial', 12))],
    [sg.InputOptionMenu(['USD', 'EUR', 'BTC', 'ETH','JPY ','GBP','AUD'], size=(35, 2), key='opcao')],
    [sg.Text('Quantidade da moeda:'), sg.InputText(key='quantidade')],
    [sg.Button('Pesquisar'), sg.Button('Calcular')],
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
        window['saida'].update(f'{entrada}: {moeda} reais')
    elif evento == 'Calcular':
        entrada = valor['opcao']
        quantidade = valor['quantidade']
        moeda = pegar_cotacoes(entrada)
        if moeda.replace('.', '').isdigit() and quantidade.replace('.', '').isdigit():
            valor_total_reais = float(moeda) * float(quantidade)
            window['saida'].update(f'Valor total em reais: {valor_total_reais:.2f}')
        else:
            window['saida'].update('Valores inválidos')

window.close()
