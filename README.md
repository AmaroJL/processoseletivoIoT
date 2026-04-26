# Processo Seletivo – Intensivo Maker | IoT
## Etapa Prática – Sistemas Embarcados

Bem-vindo(a) à **etapa prática do processo seletivo para o Intensivo Maker | IoT**.

Esta atividade tem como objetivo avaliar suas competências em **Sistemas Embarcados**, com foco em **organização de projeto, lógica de firmware e simulação de hardware**, a partir da aplicação prática dos conhecimentos adquiridos nos cursos EAD da etapa anterior.

> 🎯 **Objetivo principal**  
> Avaliar sua capacidade de **planejar, estruturar e desenvolver** uma solução funcional de sistemas embarcados, seguindo boas práticas de engenharia.

---

## 🏁 Passo 0 – Antes de Tudo

Se você **nunca utilizou Git ou GitHub**, não se preocupe.  
Siga atentamente os passos abaixo — eles fazem parte do processo de aprendizagem esperado.

---

### 1️⃣ Criação de Conta no GitHub

1. Acesse: https://github.com  
2. Clique em **Sign up**  
3. Crie sua conta gratuita seguindo as instruções da plataforma  

> 📌 O GitHub será utilizado para:
> - Envio do seu projeto  
> - Versionamento do código  
> - Correção e validação automática via GitHub Actions  

---

### 2️⃣ Instalação do Git

O **Git** é a ferramenta responsável pelo controle de versões do seu código.

### Windows
Baixe e instale o **Git Bash**:  
https://git-scm.com/downloads

### Linux / macOS
Verifique se o Git já está instalado:

```bash
git --version
```
> Caso não esteja, instale pelo gerenciador de pacotes do seu sistema.

## ⚙ Passo 1 – Preparando o Ambiente

Para desenvolver o desafio, você deverá criar uma cópia deste repositório no seu GitHub.

### 1️⃣ Fork do Repositório
No canto superior direito desta página, clique em Fork

<img width="219" height="45" alt="image" src="https://github.com/user-attachments/assets/5d629626-513a-445c-ba0f-e5bb3e225187" />


Uma cópia do repositório será criada no seu perfil do GitHub

> 🔎 O Fork permite que você trabalhe de forma independente, sem alterar o repositório original do processo seletivo.

### 2️⃣ Clone do Repositório

No repositório do seu Fork, clique em **<> Code**

<img width="149" height="52" alt="image" src="https://github.com/user-attachments/assets/abbd331b-a005-4633-89c6-afd16acbe828" />

Copie a URL e execute no terminal:

```bash
git clone https://github.com/SEU_USUARIO/nome-do-repositorio.git
cd nome-do-repositorio
```

> O comando git clone cria uma cópia local do repositório para desenvolvimento.

### 3️⃣ Preparação do Ambiente de Execução

Você pode executar o projeto de duas formas. Escolha apenas uma.

#### 🔹 Opção A – Ambiente Python Local

**Requisitos:**

- Python 3.10 ou 3.11
- pip

**Instale as dependências:**

```bash
pip install -r requirements.txt
```

#### 🔹 Opção B – Dev Container (Recomendado)

Este repositório inclui um Dev Container, garantindo um ambiente padronizado.

**Requisitos:**

- VS Code
- Docker instalado
- Extensão Dev Containers

**Passos:**

1. Abra o repositório no VS Code
2. Clique em “Reopen in Container”
3. Aguarde a criação automática do ambiente

> ➡️ Todas as dependências serão instaladas automaticamente.

## 🔐 Passo 2 – Criando sua API Key do Wokwi

A simulação do projeto será executada automaticamente via GitHub Actions, utilizando o Wokwi CLI.

Para isso, você precisa gerar uma API Key.

1. Acesse: https://wokwi.com/dashboard/ci
2. Faça login (Google ou GitHub)
3. Clique em Generate API Token
4. Copie a chave gerada (exemplo: wokwi-xxxxxxxx)

>⚠️ Importante
- Nunca faça commit dessa chave
- Ela deve ser armazenada apenas como secret no GitHub

## 🔒 Passo 3 – Configurando a API Key no GitHub (Secrets)

**No repositório do seu Fork:**

1. Vá em Settings
2. Acesse Secrets and variables → Actions
3. Clique em New repository secret
4. Nome: WOKWI_API_KEY
5. Valor: sua chave gerada
6. Salve

> ✔️ As GitHub Actions do template já estão preparadas para usar essa variável automaticamente.

## 🧠 Passo 4 – Desafio Técnico

Você deverá desenvolver um projeto de sistemas embarcados simulados, utilizando Python e Wokwi.

### 📁 Estrutura mínima esperada

```text
/project
 ├── src/
 │   └── main.py        # Código principal do projeto
 ├── wokwi.toml         # Configuração da simulação
 ├── diagram.json       # Circuito no Wokwi
 └── README.md          # Explicação do seu projeto
```

> Você pode expandir essa estrutura se desejar, desde que mantenha os arquivos essenciais.

### 🛠 Como Desenvolver seu Projeto

O desenvolvimento acontece principalmente nos arquivos abaixo:

#### 1️⃣ src/main.py

- Código Python executado na simulação
- Implementa a lógica do sistema embarcado
- Exemplos: controle de LEDs, leitura de sensores, estados, temporizações, etc.

#### 2️⃣ diagram.json

- Define o hardware virtual do projeto
- Componentes como:
  - LEDs
  - Botões
  - Sensores
  - Placa microcontroladora

#### 3️⃣ wokwi.toml

- Configura a simulação:
  - Tipo de placa
  - Framework
  - Dependências adicionais

#### 4️⃣ Commit e Push

Após suas alterações:

```bash
git add .
git commit -m "Descrição clara do que foi feito"
git push
```
### ⚙ Execução Automática (GitHub Actions)

A cada push, o GitHub Actions irá automaticamente:

- Executar o pipeline de build
- Rodar a simulação via Wokwi CLI
- Validar que o projeto executa sem erros

### 📌 Caso algo falhe:

- Vá até a aba Actions
- Analise os logs da execução
- Corrija e envie novamente

## 📊 Critérios de Avaliação

Esta etapa será avaliada considerando:

- Funcionamento correto da simulação
- Código organizado e legível
- Estrutura de arquivos correta
- Uso adequado do Wokwi
- Commits claros e bem descritos
- Projeto executando sem falhas nas Actions

---

## 📎 Submissão Final

Após concluir o desenvolvimento:

1. Verifique se o projeto **executa sem erros** nas GitHub Actions  
2. Confirme que todos os arquivos obrigatórios estão presentes  
3. Copie o link do **seu repositório no GitHub**

📤 Envie o link conforme as orientações do processo seletivo na plataforma **Moodle**.

---

## 📝 Relatório do Candidato

---

### 👤 Identificação do Candidato

- **Amaro Júnior Silva Luna**  
- **[GitHub](https://github.com/AmaroJL)**  

---

## 1️⃣ Visão Geral da Solução

O projeto consiste em um **Monitor de Segurança Residencial (Smart Alarm)** simulado. 
O objetivo do sistema é detectar possíveis invasões (usando um potenciômetro para simular proximidade/presença) e princípios de incêndio (monitorando picos de temperatura). O usuário interage com o sistema através de um botão físico para armar ou desarmar o alarme, recebendo feedback visual imediato através de LEDs de sinalização de status.

---

## 2️⃣ Arquitetura do Sistema Embarcado

A arquitetura do firmware foi desenvolvida em MicroPython e estruturada em torno de uma **Máquina de Estados Simples** (Armado / Desarmado) e arquitetura não-bloqueante:

* **Fluxo Principal (`main.py`):** O loop `while True` verifica continuamente o estado da variável global `sistema_armado`. Se ativo, ele avalia as leituras dos sensores e atualiza os atuadores (LEDs).
* **Gestão de Tempo Não-Bloqueante:** Em vez de usar `time.sleep()` extensivamente, o sistema utiliza `time.ticks_ms()` para criar temporizadores assíncronos. Isso permite ler o potenciômetro rapidamente, enquanto o sensor de temperatura é lido em intervalos maiores.
* **Leitura de Botão por Polling de Estado:** A mudança de estado (Armar/Desarmar) ocorre através da leitura contínua (*polling*) que compara o estado atual do botão com o estado anterior, garantindo uma transição limpa e evitando os travamentos comuns de Interrupções (IRQs) em simuladores web.

---

## 3️⃣ Componentes Utilizados na Simulação

A arquitetura de hardware foi migrada para o **ESP32 (Placa Devkit-C V4)** para garantir total estabilidade com a esteira de CI/CD. Os componentes foram integrados no `diagram.json` da seguinte forma:

* **ESP32:** Microcontrolador principal do sistema.
* **Wokwi-DHT22 (Pino 13):** Atua como sensor de incêndio, monitorando se a temperatura ambiente ultrapassa o limite seguro de 50°C.
* **Wokwi-Potentiometer (Pino 34 / ADC):** Simula um sensor de presença/distância granular (0 a 65535). Valores altos indicam invasão.
* **LED Verde (Pino 26):** Indicador visual de que o sistema está Armado e o ambiente está seguro.
* **LED Vermelho (Pino 27):** Indicador visual de Alerta/Invasão. Pisca intermitentemente quando um gatilho é acionado.
* **Wokwi-Pushbutton (Pino 14):** Botão de controle do usuário para alternar o estado de segurança.

---

## 4️⃣ Decisões Técnicas Relevantes

* **Fuga dos Strapping Pins:** Todos os pinos de hardware foram escolhidos meticulosamente para evitar os pinos de boot do ESP32 (como o pino 15 e 12). Isso evitou que a placa entrasse em modo de gravação e congelasse a simulação.
* **Debounce por Software:** Implementei uma lógica de debounce baseada em pequenos atrasos e controle de estado dentro da malha de verificação do botão para evitar "falsos cliques" causados por ruído mecânico.
* **Respeito ao Limite de Hardware do DHT22:** Como sensores reais DHT22 exigem um intervalo de ~2 segundos entre leituras, utilizei um temporizador baseado em `ticks_ms()` para garantir que o método `sensor_dht.measure()` só seja chamado nesse intervalo mínimo, evitando exceções do tipo `OSError`.
* **Roteamento de Serial Nativo:** O arquivo `diagram.json` foi customizado com `[ "esp:TX", "$serialMonitor:RX", "", [] ]` e a tag de ambiente do MicroPython `v1.22.0`. Isso garante que a simulação possa ser executada e validada visualmente no Wokwi Web, além de passar no GitHub Actions.

---

## 5️⃣ Resultados Obtidos

O sistema funciona conforme o esperado, atendendo a todos os requisitos do desafio:

* O projeto compila e a simulação é executada com sucesso e sem travamentos tanto no navegador quanto na Action.
* Quando o potenciômetro simula proximidade excessiva (>40.000) ou o DHT22 simula alta temperatura (>50°C), o sistema transita perfeitamente para o estado de alerta, desativando o LED Verde e ativando o LED Vermelho.
* O botão arma e desarma o sistema sem falhas, com o terminal exibindo relatórios de status controlados e limpos.
* A simulação é aprovada com sucesso na validação automática via **GitHub Actions**, respeitando os arquivos de configuração exigidos (`flasher_args.json`).

---

## 6️⃣ Comentários Adicionais

Durante o desenvolvimento, o maior desafio (e aprendizado) foi investigar o comportamento de *low-level* do hardware no simulador, descobrindo o impacto dos pinos de inicialização (Strapping Pins) na estabilidade do sistema operacional MicroPython. A transição para uma arquitetura com mapeamento de pinos seguro e a compreensão de como o simulador roteia dados seriais para CI/CD foram fundamentais para entregar uma solução robusta.

---

> ✅ Este relatório faz parte da avaliação técnica.  
> Clareza, objetividade e organização são tão importantes quanto o funcionamento do código.

---

## 🆘 Suporte

Em caso de dúvidas:

- Consulte o material dos cursos EAD
- Leia atentamente este README
- Analise os logs das GitHub Actions
- Utilize os canais oficiais para contato com os instrutores

Boa sorte no processo seletivo.
Mostre sua capacidade de pensar como um engenheiro de sistemas embarcados.
****
