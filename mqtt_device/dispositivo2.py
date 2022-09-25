import paho.mqtt.client as mqtt
import time
from hal1 import temperaturaDefinida, statusAquecedor, statusRele
import constantes
from definicoes2 import user, password, client_id, server, port


def mensagem(client, userdata, msg):
    vetor = msg.payload.decode().split(',')
    statusAquecedor('on' if vetor[1] == '1' else 'off')
    client.publish(f'v1/{user}/things/{client_id}/response', f'ok,{vetor[0]}')


client = mqtt.Client(client_id)
client.username_pw_set(user, password)
client.connect(server, port)

client.on_message = mensagem
client.subscribe(f'v1/{user}/things/{client_id}/cmd/5')
client.loop_start()

while True:
    client.publish(f'v1/{user}/things/{client_id}/data/3', temperaturaDefinida())
    statusRele();
    if(constantes.releStatus == True):
        client.publish(f'v1/{user}/things/{client_id}/data/4', '1')
    else:
        client.publish(f'v1/{user}/things/{client_id}/data/4', '0')
    time.sleep(5)
