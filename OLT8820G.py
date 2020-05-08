import serial

def verifica_porta():
    while True:
        try:
            porta = str(input('Informe a porta: '))
            
            porta_verificar = serial.Serial(porta)
            porta_verificar.close()
            
            print('Porta válida\n')
            return porta
        except serial.SerialException:
            print('Porta inválida\n')
            continue
        

porta = verifica_porta()
ser = serial.Serial(porta,'115200')
ser.close()
ser.open()

loop_boot_interrupt = True
while True:
    rec = ser.readline()
    print(rec.decode('utf-8'))
    boot_interrupt_msg = 'Prepare to load full image...'
    for boot_interrupt_msg in rec.decode('utf-8'):
        ser.write(b'zhone\n\n')
        print('zhone')
        loop_boot_interrupt = False
        break
    

ser.close()


    
    
