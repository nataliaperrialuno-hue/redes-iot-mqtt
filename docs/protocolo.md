# Escolha do Protocolo MQTT

## Objetivo

O objetivo deste projeto é simular a comunicação entre dispositivos de uma aplicação de Internet das Coisas (IoT), utilizando o protocolo MQTT.

## Por que o MQTT?

O MQTT foi escolhido por ser um protocolo leve, eficiente e amplamente utilizado em aplicações IoT. Seu modelo de comunicação Publish/Subscribe permite que dispositivos troquem informações em tempo real sem a necessidade de comunicação direta entre eles.

## Vantagens

- Baixo consumo de banda.
- Comunicação em tempo real.
- Fácil implementação.
- Ideal para dispositivos com poucos recursos.
- Alta escalabilidade.

## Aplicação no projeto

Neste projeto, um sensor de umidade publica informações em um broker MQTT. Um controlador permanece inscrito nesse tópico para receber os dados e, futuramente, será responsável por decidir quando o sistema de irrigação deverá ser acionado.
