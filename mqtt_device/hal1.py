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
        print('ligou aquecedor')
        constantes.releHabilitado = True

    else:
        print('desligou o aquecedor')
        constantes.releHabilitado = False


def statusRele():
    if constantes.releHabilitado:
        if constantes.temperaturaBase < 30:
            print('statusRele: aquecedor ligado')
            constantes.releStatus = True
        else:
            print('statusRele: aquecedor desligado')
            constantes.releStatus = False
    else:
        constantes.releStatus = False
