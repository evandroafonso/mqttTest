import paho.mqtt.client as mqtt
import time
from hal import temperatura, umidade, aquecedor
from definitions import user, password, client_id, server, port

def mensagem(client, userdata, msg):
    vetor = msg.payload.decode().split(',')
    aquecedor('on' if vetor [1] == '1' else 'off')
    client.publish(f'v1/{user}/things/{client_id}/response', f'ok,{vetor[0]}')
    print(vetor)


client = mqtt.Client(client_id)
client.username_pw_set(user, password)
client.connect(server, port)

client.on_message = mensagem
client.subscribe(f'v1/{user}/things/{client_id}/cmd/2')
client.loop.start()

while True:
    client.publish('v1/'+user+'/things/'+client_id+'/data/0', temperatura())
    client.publish('v1/'+user+' /things/'+client_id+'/data/1', umidade())

    time.sleep(10)


