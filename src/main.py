import machine
import dht
import time

sensor_dht = dht.DHT22(machine.Pin(15))
sensor_presenca = machine.ADC(machine.Pin(34))
sensor_presenca.atten(machine.ADC.ATTN_11DB) 
led_seguro = machine.Pin(21, machine.Pin.OUT)
led_alarme = machine.Pin(19, machine.Pin.OUT)
botao = machine.Pin(18, machine.Pin.IN, machine.Pin.PULL_UP)

LIMITE_PRESENCA = 40000  
LIMITE_TEMP_FOGO = 50.0  

sistema_armado = True
ultimo_tempo_dht = 0
ultima_leitura_temp = None
ultimo_clique_botao = 0

def alternar_sistema(pino):
    global sistema_armado, ultimo_clique_botao
    agora = time.ticks_ms()
    if time.ticks_diff(agora, ultimo_clique_botao) > 300:
        sistema_armado = not sistema_armado
        print(f"Sistema {'ARMADO' if sistema_armado else 'DESARMADO'}")
        ultimo_clique_botao = agora

botao.irq(trigger=machine.Pin.IRQ_FALLING, handler=alternar_sistema)

def main():
    global ultimo_tempo_dht, ultima_leitura_temp
    print("Sistema de Segurança Iniciado (ESP32)...")

    print("Teste") 
    
    while True:
        if sistema_armado:
            agora = time.ticks_ms()
            
            if time.ticks_diff(agora, ultimo_tempo_dht) > 2000 or ultima_leitura_temp is None:
                try:
                    sensor_dht.measure()
                    ultima_leitura_temp = sensor_dht.temperature()
                    ultimo_tempo_dht = agora
                except OSError:
                    pass
            
            presenca = sensor_presenca.read_u16()
            
            if ultima_leitura_temp is not None:
                if presenca > LIMITE_PRESENCA or ultima_leitura_temp > LIMITE_TEMP_FOGO:
                    led_seguro.off()
                    led_alarme.value(not led_alarme.value()) 
                    time.sleep(0.1) 
                else:
                    led_seguro.on()
                    led_alarme.off()
        else:
            led_seguro.off()
            led_alarme.off()

        time.sleep(0.1) 

if __name__ == "__main__":
    main()