# app.py
import streamlit as st

st.set_page_config(page_title="Calculadora de IMC", page_icon="💪")

st.title("Calculadora de IMC")

# Campos de entrada na barra lateral ou no corpo principal
nome = st.text_input("Digite seu nome:")
peso_str = st.text_input("Digite seu peso (kg):")
altura_str = st.text_input("Digite sua altura (cm):")

if st.button("Calcular IMC"):
    # --- Validação dos dados ---
    if not nome or not peso_str or not altura_str:
        st.error("Por favor, preencha todos os campos.")
    else:
        try:
            peso = float(peso_str.replace(',', '.'))
            altura_cm = float(altura_str.replace(',', '.'))
            if peso <= 0 or altura_cm <= 0:
                raise ValueError
            
            # --- Lógica de cálculo ---
            altura_m = altura_cm / 100
            imc = peso / (altura_m ** 2)

            # Classificação
            if imc < 18.5: classificacao = 'Abaixo do peso'
            elif imc < 25: classificacao = 'Peso normal'
            elif imc < 30: classificacao = 'Sobrepeso'
            elif imc < 35: classificacao = 'Obesidade grau I'
            elif imc < 40: classificacao = 'Obesidade grau II'
            else: classificacao = 'Obesidade grau III'

            # --- Exibição do resultado ---
            st.success(f"Olá, {nome}!")
            st.metric(label="Seu IMC é", value=f"{imc:.2f}", delta=classificacao)

            # Meta de peso
            if imc < 18.5:
                peso_meta = abs(peso - 18.5 * altura_m**2)
                st.info(f'Para atingir o "Peso normal", você precisa ganhar {peso_meta:.2f} kg.')
            elif imc >= 25:
                peso_meta = abs(peso - 25 * altura_m**2)
                st.info(f'Para atingir o "Peso normal", você precisa perder {peso_meta:.2f} kg.')

        except ValueError:
            st.error("Peso e altura devem ser números válidos e positivos.")