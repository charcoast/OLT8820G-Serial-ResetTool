import serial
ser = None

def verifica_porta(porta): # Verifica se a porta digitada está ativa no SO
    try:
        porta_verificar = serial.Serial(porta)
        porta_verificar.close()
        print('Porta válida\n')
        return porta

    except serial.SerialException:
        print('Porta inválida\n')
        return None
        
def main():
    global ser
    porta = None
    while True: # Loop para que o usuário digite uma porta até que ela seja válida
        input_porta = str(input('Informe a porta: '))
        porta = verifica_porta(input_porta)
        if porta:
            break
    ser = serial.Serial(porta,'115200') #Inicia a comunicação serial na velocidade 115200, padrão da OLT
    ser.close() # Fecha qualquer conexão já existente na porta 
    ser.open() # Inicia uma nova conexão na porta
    print('Conectado à porta ' + porta)
    aguarda_boot()
    executa_comandos(b'cd datastor\n')
    ser.close()

def executa_comandos(comando):
    retorno = []
    ser.write(comando)
    ser.readline()
    
    

def aguarda_boot(): # Aguarda pela mensagem de boot e o interrompe
    print('Aguardando o boot da OLT. \nReinicie-a para que o processo inicie.')

    boot_interrupt_msg = 'Prepare to load full image...'

    while True:
        rec = ser.readline()
        print(rec.decode('utf-8'))
        
        for boot_interrupt_msg in rec.decode('utf-8'):
            ser.write(b'zhone\n\n')
            print('zhone')
            return None

if __name__ == "__main__":
    main()
    
    
