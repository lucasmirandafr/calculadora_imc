import streamlit as st

# título do aplicativo
st.title('Calculadora de IMC (Índice de Massa Corporal)')

# --- entradas do usuário na barra lateral (sidebar) ---
# usar a sidebar deixa a interface mais limpa
st.sidebar.header('Insira seus dados')
nome = st.sidebar.text_input('Seu nome')
peso = st.sidebar.number_input('Seu peso (kg)', min_value=0.1, format="%.2f")
altura_cm = st.sidebar.number_input('Sua altura (cm)', min_value=0.1, format="%.1f")

# --- lógica do aplicativo ---
# botão para iniciar o cálculo
if st.sidebar.button('Calcular IMC'):

    # validação dos inputs
    if not nome:
        st.error('Por favor, digite seu nome.')
    elif peso <= 0 or altura_cm <= 0:
        st.error('Por favor, insira valores válidos e positivos para peso и altura.')
    else:
        # cálculos (mesma lógica do seu código original)
        altura_m = altura_cm / 100
        imc = peso / (altura_m ** 2)
        
        # classificação do IMC
        if imc < 18.5:
            classificacao = 'Abaixo do peso'
            cor = 'orange'
        elif imc < 25:
            classificacao = 'Peso normal'
            cor = 'green'
        elif imc < 30:
            classificacao = 'Sobrepeso'
            cor = 'orange'
        elif imc < 35:
            classificacao = 'Obesidade grau I'
            cor = 'red'
        elif imc < 40:
            classificacao = 'Obesidade grau II'
            cor = 'red'
        else:
            classificacao = 'Obesidade grau III'
            cor = 'red'

        # exibição dos resultados
        st.subheader(f'Olá, {nome}! Aqui está o seu resultado:')

        # exibe o IMC e a classificação com cores
        st.metric(label="Seu IMC é", value=f"{imc:.2f}")

        if cor == 'green':
            st.success(f"**Classificação:** {classificacao}")
        elif cor == 'orange':
            st.warning(f"**Classificação:** {classificacao}")
        else:
            st.error(f"**Classificação:** {classificacao}")

        # mensagem sobre a meta de peso
        if imc < 18.5:
            peso_meta_ganhar = abs(peso - 18.5 * altura_m**2)
            st.info(f'Para atingir a faixa de "Peso normal", você precisaria **ganhar** cerca de **{peso_meta_ganhar:.2f} kg**.')
        elif imc >= 25:
            peso_meta_perder = abs(peso - 25 * altura_m**2)
            st.info(f'Para atingir a faixa de "Peso normal", você precisaria **perder** cerca de **{peso_meta_perder:.2f} kg**.')
        else:
            st.balloons()
            st.info('Parabéns, você está na faixa de peso ideal!')
