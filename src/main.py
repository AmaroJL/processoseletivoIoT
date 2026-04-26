import machine
import dht
import time
import sys

print("Teste")
sys.stdout.flush()

print("Sistema de Seguranca Iniciado (ESP32 MicroPython)...")

sensor_dht = dht.DHT22(machine.Pin(4))
sensor_presenca = machine.ADC(machine.Pin(34))
sensor_presenca.atten(machine.ADC.ATTN_11DB)
led_seguro = machine.Pin(21, machine.Pin.OUT)
led_alarme = machine.Pin(19, machine.Pin.OUT)
botao = machine.Pin(18, machine.Pin.IN, machine.Pin.PULL_UP)

LIMITE_PRESENCA = 40000
LIMITE_TEMP_FOGO = 50.0

sistema_armado = True
ultimo_tempo_dht = 0
ultima_leitura_temp = 25.0

while True:
    try:
        if sistema_armado:
            agora = time.ticks_ms()
            
            if time.ticks_diff(agora, ultimo_tempo_dht) > 2000:
                try:
                    sensor_dht.measure()
                    ultima_leitura_temp = sensor_dht.temperature()
                    ultimo_tempo_dht = agora
                except OSError:
                    pass 
            
            presenca = sensor_presenca.read_u16()
            
            if presenca > LIMITE_PRESENCA or ultima_leitura_temp > LIMITE_TEMP_FOGO:
                led_seguro.off()
                led_alarme.value(not led_alarme.value()) 
            else:
                led_seguro.on()
                led_alarme.off()
        else:
            led_seguro.off()
            led_alarme.off()

        if botao.value() == 0:
            sistema_armado = not sistema_armado
            time.sleep(0.3)

        time.sleep(0.1)

    except Exception as e:
        print("Erro:", e)
        time.sleep(1)