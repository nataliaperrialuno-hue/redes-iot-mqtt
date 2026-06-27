import paho.mqtt.client as mqtt

BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "fazenda/umidade"

def on_message(client, userdata, message):
    umidade = message.payload.decode()
    print(f"Umidade recebida: {umidade}%")

client = mqtt.Client()

client.on_message = on_message

client.connect(BROKER, PORT)

client.subscribe(TOPIC)

print("Aguardando dados do sensor...")

client.loop_forever()
