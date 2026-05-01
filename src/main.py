import machine
import dht
import time
import network
import urequests
#from config import TELEGRAM_TOKEN, CHAT_ID

print("Teste")

print("=========================================")
print(" Sistema de Segurança com IoT (Telegram) ")
print("=========================================")

print("Conectando ao Wi-Fi...", end="")
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect('Wokwi-GUEST', '')

while not wifi.isconnected():
    print(".", end="")
    time.sleep(0.5)
print("\nWi-Fi Conectado! IP:", wifi.ifconfig()[0])

def enviar_telegram(mensagem):
    print("Enviando alerta para o celular...")
    msg_url = mensagem.replace(" ", "%20")
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={msg_url}"
    try:
        resposta = urequests.get(url)
        resposta.close()
        print("Mensagem entregue com sucesso no Telegram!")
    except Exception as e:
        print("Erro ao mandar o Telegram:", e)

sensor_dht = dht.DHT22(machine.Pin(13))
sensor_presenca = machine.ADC(machine.Pin(34))
sensor_presenca.atten(machine.ADC.ATTN_11DB)
sensor_porta = machine.Pin(32, machine.Pin.IN, machine.Pin.PULL_UP)

led_seguro = machine.Pin(26, machine.Pin.OUT)
led_alarme = machine.Pin(27, machine.Pin.OUT)

sirene = machine.PWM(machine.Pin(25))
sirene.duty(0) 

pinos_linhas = [19, 18, 5, 17]
pinos_colunas = [16, 4, 2, 15]

linhas = [machine.Pin(pino, machine.Pin.OUT) for pino in pinos_linhas]
colunas = [machine.Pin(pino, machine.Pin.IN, machine.Pin.PULL_UP) for pino in pinos_colunas]

mapa_teclas = [
    ['1', '2', '3', 'A'],
    ['4', '5', '6', 'B'],
    ['7', '8', '9', 'C'],
    ['*', '0', '#', 'D']
]

def ler_teclado():
    for i, linha in enumerate(linhas):
        linha.value(0) 
        for j, coluna in enumerate(colunas):
            if coluna.value() == 0: 
                linha.value(1) 
                return mapa_teclas[i][j]
        linha.value(1) 
    return None

LIMITE_PRESENCA = 40000
LIMITE_TEMP_FOGO = 50.0

sistema_armado = True
ultimo_tempo_dht = 0
ultima_leitura_temp = 25.0
alarme_ativo = False
SENHA_CORRETA = "1234"
senha_digitada = ""
ultimo_clique = 0

print("Sistema iniciado. Ambiente ARMADO.")
enviar_telegram("O Sistema de Segurança IoT foi ligado!")

while True:
    try:
        tecla = ler_teclado()
        agora = time.ticks_ms()
        
        if tecla and time.ticks_diff(agora, ultimo_clique) > 300:
            print("*", end="")
            senha_digitada += tecla
            ultimo_clique = agora
            
            if len(senha_digitada) == 4:
                print() 
                if senha_digitada == SENHA_CORRETA:
                    sistema_armado = not sistema_armado
                    if sistema_armado:
                        print(">> Sistema ARMADO <<")
                        enviar_telegram("Sistema ARMADO via teclado.")
                    else:
                        print(">> Sistema DESARMADO <<")
                        enviar_telegram("Sistema DESARMADO via teclado.")
                else:
                    print(">> Senha Incorreta! <<")
                    enviar_telegram("TENTATIVA DE ACESSO: Senha incorreta digitada no teclado!")
                senha_digitada = "" 

        if sistema_armado:
            if time.ticks_diff(agora, ultimo_tempo_dht) > 2000:
                try:
                    sensor_dht.measure()
                    ultima_leitura_temp = sensor_dht.temperature()
                    ultimo_tempo_dht = agora
                except OSError:
                    pass 
            
            presenca = sensor_presenca.read_u16()
            porta_aberta = (sensor_porta.value() == 1) 
            
            if presenca > LIMITE_PRESENCA or ultima_leitura_temp > LIMITE_TEMP_FOGO or porta_aberta:
                if not alarme_ativo:
                    if porta_aberta:
                        alerta_msg = "ALERTA: Porta ou Janela foi aberta!"
                    elif ultima_leitura_temp > LIMITE_TEMP_FOGO:
                        alerta_msg = f"ALERTA DE FOGO! Temperatura em {ultima_leitura_temp}°C"
                    else:
                        alerta_msg = "ALERTA: Presença detectada!"
                        
                    print(alerta_msg)
                    enviar_telegram(f"🚨 {alerta_msg} 🚨") 
                    alarme_ativo = True
                    
                led_seguro.off()
                led_alarme.value(not led_alarme.value()) 
                
                sirene.duty(512) 
                if led_alarme.value():
                    sirene.freq(1200) 
                else:
                    sirene.freq(800)  
                    
            else:
                if alarme_ativo:
                    print("Sistema Normalizado. Ambiente Seguro.")
                    enviar_telegram("✅ Sistema normalizado. Ambiente seguro novamente.")
                    alarme_ativo = False
                    
                led_seguro.on()
                led_alarme.off()
                sirene.duty(0) 
                
        else:
            led_seguro.off()
            led_alarme.off()
            sirene.duty(0)
            if alarme_ativo:
                alarme_ativo = False 

        time.sleep(0.05) 
        
    except Exception as e:
        print("Erro no loop:", e)
        time.sleep(1)