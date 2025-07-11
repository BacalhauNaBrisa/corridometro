# 🏃 Corridômetro

**Corridômetro** é um aplicativo web interativo criado com [Streamlit](https://streamlit.io), ideal para corredores que desejam calcular **velocidade**, **distância** ou **tempo** com base em diferentes unidades de medida.

![Logotipo](https://github.com/BacalhauNaBrisa/corridometro/raw/main/assets/logo.png)

## 🔗 Acesse o app

Acesse online: [https://corridometro.bacalhaunabrisa.com/](https://corridometro.bacalhaunabrisa.com/)

---

## 📦 Funcionalidades

A aplicação possui 3 abas principais:

### 🕒 Velocidade
- Informe a **distância** e o **tempo**
- Escolha unidades de entrada e saída (km/h, mph ou min/km)

### 📏 Distância
- Informe a **velocidade** e o **tempo**
- Escolha unidades de entrada e saída (metros, quilômetros ou milhas)

### ⏱️ Tempo
- Informe a **distância** e a **velocidade**
- Resultado exibido no formato `hh:mm:ss`

---

## ⚙️ Instalação Local

```bash
git clone https://github.com/BacalhauNaBrisa/corridometro.git
cd corridometro
pip install -r requirements.txt
streamlit run app.py
