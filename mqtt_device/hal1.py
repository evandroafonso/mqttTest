import random

temperatura_base = 28
rele_automatico_status = False
import random

temperatura_base = 28
rele_automatico_status = False
rele_interruptor = False

# método que define a temperatura da estufa
def define_temperatura_estufa():
    global temperatura_base
    if rele_automatico_status:
        temperatura_base += random.uniform(1, 3)
        return temperatura_base
    else:
        temperatura_base -= random.uniform(1, 3)
        return temperatura_base

# método que define o comportamento do aquecedor: ligado ou desligado
def define_comportamento_aquecedor(estado: str):
    global rele_interruptor
    if estado == 'on':
        print('Modo automático do aquecedor LIGADO')
        rele_interruptor = True

    else:
        print('Modo automático do aquecedor DESLIGADO')
        rele_interruptor = False

# método que verifica se o aquecedor/rele precisa ser ligado ou desligado
def define_comportamento_automatico_aquecedor():
    global rele_automatico_status
    if rele_interruptor:
        if temperatura_base < 30:
            print(f'aquecedor ligado: Temperatura atual {temperatura_base:,.2f} ºC')
            rele_automatico_status = True
            return True
        elif temperatura_base > 31.5:
            print(f'aquecedor desligado: Temperatura atual {temperatura_base:,.2f} ºC')
            rele_automatico_status = False
            return False
    else:
        rele_automatico_status = False
        print(f'ATENÇÃO!! Modo automatico do aquecedor está desligado - temperatura atual {temperatura_base:,.2f} ºC')
        return False

