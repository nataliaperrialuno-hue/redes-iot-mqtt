# redes-iot-mqtt
Simulação de um sistema de irrigação inteligente utilizando MQTT.
# 🌱 Sistema Inteligente de Irrigação com MQTT

## Descrição

Este projeto simula um sistema de irrigação inteligente utilizando o protocolo MQTT, amplamente empregado em aplicações de Internet das Coisas (IoT).

A ideia é simular sensores que enviam informações sobre umidade do solo, temperatura e chuva para um broker MQTT. Um controlador recebe esses dados e decide quando a irrigação deve ser ativada.

## Objetivo

Desenvolver uma aplicação que demonstre a comunicação entre dispositivos IoT utilizando o modelo Publish/Subscribe do protocolo MQTT.

## Tecnologias

- Python
- MQTT
- Biblioteca Paho MQTT

## Estrutura do Projeto

```
iot-smart-irrigation/
├── publisher.py
├── subscriber.py
├── requirements.txt
└── README.md
```

## Próximas Etapas

- Implementar o Publisher para simular os sensores.
- Implementar o Subscriber para receber os dados.
- Criar a lógica de acionamento da irrigação.
- Testar a comunicação utilizando um broker MQTT.

## Autora

Natália Perri Gonçalves
