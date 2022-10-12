
from PyQt5 import QtCore, uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from playsound import playsound


count = 0  
timer = 0

### Função Pause
def pause():
    timer.blockSignals(True)
    
### Função despausar    
def play_pause():
    timer.blockSignals(False)   


### Função parar - Para o timer, reseta a variavel count e reseta a barra de progressão
def parar():
    global count
    count = 0
    tela.pb_cronometro.setValue(0)
    timer.stop()
    #timer.blockSignals(True)

### Função reset - Reset a variavel count e barra de progressão
def reset():
    global count
    count = 0
    tela.pb_cronometro.setValue(0)
    

### Função - Mensagem de erro informação dos minutos
def mens_minutos():
    msg1 = QMessageBox()
    msg1.setIcon(QMessageBox.Information)
    msg1.setWindowTitle('Atenção')
    msg1.setText('Favor informar o tempo em minutos!')
    x = msg1.exec_()

### Função display - Calcula o tempo e atualiza a barra de progressão até 100%
def display():

    global count 
    global timer
    
    try:
        tempo = int(tela.ln_tempo.text()) * 60  # Converte minutos em segundos
        valor_tempo = 100 / tempo  # 100 / tempo = valor atualiza a barra de progressão 
        count += valor_tempo  # Atualização da barra de progressão
        print(f'{count:,.2f}')
        tela.pb_cronometro.setValue(int(count))

        if count >= 100:
            playsound("sino.mp3")
            timer.stop()
            #return
    except:
        mens_minutos()
        timer.stop()

### Função Cronometro - Inicia o timer, contagem de 1 segundo e chama a função display
def cronometro():
    global timer 
    reset()
    
    if tela.ln_tempo.text() == "":
        mens_minutos()
        tela.ln_tempo.setFocus()
    else:
        
        timer = QtCore.QTimer()
        timer.timeout.connect(display)
        timer.start(1000)


app=QtWidgets.QApplication([])
tela=uic.loadUi("pomodoro.ui")
tela.setFixedSize(380, 160)
tela.bt_iniciar.clicked.connect(cronometro)
tela.bt_parar.clicked.connect(parar)
tela.bt_pause.clicked.connect(pause)
tela.bt_play.clicked.connect(play_pause)
tela.show()
app.exec()