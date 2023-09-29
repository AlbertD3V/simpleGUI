import PySimpleGUI as sg

######## Modelagem da janela!
layout =[
    [sg.Text("My Mind")],
    [sg.Radio("No Pain", "RADI01"),sg.Radio("No Gain","RADI01"),sg.Radio("No Pain No Gain","RADI01", default=True), sg.Button('exe')],
    [sg.Multiline('', s=(50,8))],
    [sg.Multiline('', s=(50,8)), sg.Column([[sg.Button('aply')],[sg.Button('cancel')]])]
]

######### Crianção da janela com base no layout definido.
window = sg.Window("Aplicação", layout)

######### Loop infinito que mantem a janela aberta
while True:
    evento, valor = window.read() #"ESCUTADOR" de eventos que retorna o evento e os valores!
    if evento == sg.WIN_CLOSED: # Verifica se o botão 'x' foi clicado e fecha a aplicação
        break

window.close() # fecha a janela