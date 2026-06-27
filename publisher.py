import random
import time
import paho.mqtt.client as mqtt

# Configuração do broker MQTT
BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "fazenda/umidade"

# Cria o cliente MQTT
client = mqtt.Client()

# Conecta ao broker
client.connect(BROKER, PORT)

print("Simulação iniciada...")

while True:
    # Gera um valor aleatório de umidade entre 10% e 80%
    umidade = random.randint(10, 80)

    # Publica o valor no tópico MQTT
    client.publish(TOPIC, umidade)

    print(f"Umidade enviada: {umidade}%")

    # Aguarda 5 segundos antes de enviar outro valor
    time.sleep(5)
