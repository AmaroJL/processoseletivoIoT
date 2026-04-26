import machine
import dht
import time
import sys

print("========================================")
print(" Sistema de Segurança Iniciado ")
print("========================================")

sensor_dht = dht.DHT22(machine.Pin(13))
sensor_presenca = machine.ADC(machine.Pin(34))
sensor_presenca.atten(machine.ADC.ATTN_11DB)
led_seguro = machine.Pin(26, machine.Pin.OUT)
led_alarme = machine.Pin(27, machine.Pin.OUT)
botao = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)

LIMITE_PRESENCA = 40000
LIMITE_TEMP_FOGO = 50.0

sistema_armado = True
ultimo_tempo_dht = 0
ultima_leitura_temp = 25.0

alarme_ativo = False
estado_botao_anterior = botao.value()

while True:
    try:
        if sistema_armado:
            agora = time.ticks_ms()
            
            if time.ticks_diff(agora, ultimo_tempo_dht) > 2000:
                try:
                    sensor_dht.measure()
                    ultima_leitura_temp = sensor_dht.temperature()
                    ultimo_tempo_dht = agora
                    
                    presenca_atual = sensor_presenca.read_u16()
                    print(f"[Atualização] Temp: {ultima_leitura_temp}°C | Presença: {presenca_atual}")
                    
                except OSError:
                    print("[Aviso] Falha ao ler o sensor DHT22")
            
            presenca = sensor_presenca.read_u16()
            
            if presenca > LIMITE_PRESENCA or ultima_leitura_temp > LIMITE_TEMP_FOGO:
                if not alarme_ativo:
                    print("ALERTA GERAL! Invasão ou Fogo detectado!")
                    alarme_ativo = True
                    
                led_seguro.off()
                led_alarme.value(not led_alarme.value())
            else:
                if alarme_ativo:
                    print("Sistema Normalizado. Ambiente Seguro.")
                    alarme_ativo = False
                    
                led_seguro.on()
                led_alarme.off()
        else:
            led_seguro.off()
            led_alarme.off()
            if alarme_ativo:
                alarme_ativo = False 

        estado_botao_atual = botao.value()
        if estado_botao_atual == 0 and estado_botao_anterior == 1:
            sistema_armado = not sistema_armado
            if sistema_armado:
                print("Sistema ARMADO")
            else:
                print("Sistema DESARMADO")
            time.sleep(0.3)
            
        estado_botao_anterior = estado_botao_atual

        time.sleep(0.1)
        
    except Exception as e:
        print("Erro fatal:", e)
        time.sleep(1)