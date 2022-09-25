import random
import constantes


def temperaturaDefinida():
    if constantes.releStatus == True:
        constantes.temperaturaBase += random.uniform(1, 3)
        return constantes.temperaturaBase
    else:
        constantes.temperaturaBase -= random.uniform(1, 3)
        return constantes.temperaturaBase


def statusAquecedor(estado: str):
    if estado == 'on':
        print('Modo automático do aquecedor LIGADO')
        constantes.releHabilitado = True

    else:
        print('Modo automático do aquecedor DESLIGADO')
        constantes.releHabilitado = False


def statusRele():
    if constantes.releHabilitado:
        if constantes.temperaturaBase < 30:
            print(f'aquecedor ligado: Temperatura atual {constantes.temperaturaBase:,.2f} ºC')
            constantes.releStatus = True
        else:
            print(f'aquecedor desligado: Temperatura atual {constantes.temperaturaBase:,.2f} ºC')
            constantes.releStatus = False
    else:
        constantes.releStatus = False
