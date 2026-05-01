### 👤 Identificação do Candidato

- **Amaro Júnior Silva Luna**  
- **[GitHub](https://github.com/AmaroJL)**  

---

# Relatório do Projeto: Monitor de Segurança Residencial IoT (Smart Alarm)

## 1️⃣ Visão Geral da Solução
O projeto consiste em um **Monitor de Segurança Residencial IoT (Smart Alarm)** simulado.  
O objetivo do sistema é detectar múltiplas ameaças: invasão de perímetro (arrombamento de portas/janelas), proximidade/movimento em áreas restritas e princípios de incêndio. 

A principal inovação do projeto é a sua conectividade: ao ser acionado, o sistema não apenas emite um alerta visual e sonoro localmente, mas também envia **notificações em tempo real** para o smartphone do usuário via Telegram. A interação física de arme/desarme foi profissionalizada, exigindo a inserção de uma senha de 4 dígitos por meio de um teclado matricial.

---

## 2️⃣ Arquitetura do Sistema Embarcado
A arquitetura do firmware foi desenvolvida em **MicroPython** e estruturada em torno de uma Máquina de Estados Simples e uma arquitetura não-bloqueante voltada para IoT:

* **Conectividade Wi-Fi e API:** Na inicialização, o sistema conecta-se à rede simulada e utiliza a biblioteca `urequests` para enviar requisições HTTP GET à API do Telegram, comunicando o status do sistema de forma síncrona.
* **Varredura de Teclado (Scanning):** O sistema utiliza uma matriz de linhas e colunas para ler o teclado 4x4. A leitura é feita enviando um sinal baixo (0) para cada linha e verificando o estado das colunas, implementando também um *debounce* lógico de 300ms para evitar cliques duplos.
* **Gestão de Tempo Não-Bloqueante:** O loop principal foge do uso de `time.sleep()`. Utilizando `time.ticks_ms()`, o firmware escaneia o teclado, lê sensores digitais e modula a sirene em altíssima velocidade, enquanto respeita o intervalo de leitura de 2 segundos exigido pelo sensor de temperatura DHT22.

---

## 3️⃣ Componentes Utilizados na Simulação
A arquitetura de hardware utiliza o **ESP32 (Placa Devkit-C V4)** e está integrada no `diagram.json` da seguinte forma:

* **ESP32:** Microcontrolador central.
* **Wokwi-DHT22 (Pino 13):** Monitora temperatura para detecção de fogo (>50°C).
* **Wokwi-Potentiometer (Pino 34 / ADC):** Simula sensor de presença volumétrico/distância.
* **Wokwi-Slide-Switch (Pino 32):** Atua como sensor de perímetro (Reed Switch magnético) para detectar abertura de portas e janelas.
* **Wokwi-Membrane-Keypad:** Teclado matricial 4x4 (Pinos 19, 18, 5, 17 para linhas e 16, 4, 2, 15 para colunas) responsável pela entrada da senha de segurança.
* **Wokwi-Buzzer (Pino 25):** Atuador sonoro (Sirene) controlado via PWM.
* **LED Verde (Pino 26) e LED Vermelho (Pino 27):** Indicadores visuais de status (Seguro/Alerta).

---

## 4️⃣ Decisões Técnicas Relevantes
* **Uso de PWM para a Sirene:** Para simular um alarme realista, utilizei modulação por largura de pulso (`machine.PWM`) no pino 25. O sistema alterna dinamicamente entre frequências de 800Hz e 1200Hz, criando o som clássico de uma sirene de emergência.
* **Integração com a Nuvem (Wokwi-GUEST):** Em vez de manter o sistema isolado, utilizei a rede virtual `Wokwi-GUEST` fornecida pela plataforma. Isso permitiu tratar o simulador como um verdadeiro dispositivo IoT conectado à internet.
* **Fuga dos Strapping Pins:** Todos os pinos de hardware foram escolhidos meticulosamente para evitar os pinos de boot do ESP32 (como o pino 12). Isso evitou que a placa entrasse em modo de gravação e congelasse a simulação, garantindo estabilidade no GitHub Actions.
* **Roteamento de Serial Nativo:** O arquivo `diagram.json` foi customizado com `[ "esp:TX", "$serialMonitor:RX", "", [] ]`. Isso garante que o Wokwi Web consiga exibir os logs de conexão do Wi-Fi e os disparos do sistema adequadamente.

---

## 5️⃣ Resultados Obtidos
O sistema funciona conforme o esperado, transformando-se em um alarme IoT completo:

* **Controle de Acesso:** O sistema só permite armar e desarmar mediante a inserção correta da senha (**1234**), ignorando toques acidentais graças ao *debounce* implementado.
* **Detecção Multicanal:** O alarme dispara instantaneamente se o switch da porta for acionado, se a presença cruzar o limite ou se a temperatura subir, ativando os LEDs e a sirene alternada.
* **Notificações IoT:** As requisições HTTP funcionam perfeitamente. Mensagens personalizadas de Inicialização, Arme, Desarme e Alertas de Intrusão/Incêndio são entregues com sucesso via Telegram.
* **CI/CD:** A simulação é aprovada sem falhas na validação automática via GitHub Actions.

---

## 6️⃣ Comentários Adicionais
Durante o desenvolvimento, o maior desafio foi integrar diferentes tecnologias (PWM, leitura analógica, temporização assíncrona, varredura de matriz e requisições HTTP) dentro de um único loop `while True` sem causar gargalos (bloqueios) no processamento. 

---

##  Configuração do Telegram e Credenciais

Para garantir que os alertas do sistema sejam enviados para o seu próprio Telegram, é necessário configurar o seu próprio bot. Siga os passos abaixo:

### 1. Criando um Bot no Telegram

1. Abra o Telegram e busque pelo contato oficial **@BotFather**.
2. Inicie a conversa e envie o comando `/newbot`.
3. Escolha um **Nome** e um **Username** para o seu bot.
4. Copie o **Token HTTP API** gerado (ele será semelhante a `123456789:XXXXXXXXXXXXXXXXXXXXXXXXX`).

---

### 2. Descobrindo o seu Chat ID

1. No Telegram, busque pelo bot **@userinfobot** ou **@raw_data_bot**.
2. Inicie a conversa e envie o comando `/start`.
3. O bot responderá com os dados da sua conta. Copie o número correspondente ao **ID** (ex: `123456789`).

---

### 3. Configurando o Arquivo Local

1. Crie um arquivo chamado `config.py` na mesma pasta do projeto (junto com o `main.py`).
2. Adicione suas credenciais preenchendo com os dados que você copiou nos passos anteriores:

```python
TELEGRAM_TOKEN = "COLE_O_SEU_TOKEN_AQUI"
CHAT_ID = "COLE_O_SEU_CHAT_ID_AQUI"