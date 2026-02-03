import streamlit as st

st.title("Calculadora de Ahorro Energético con VFD")

st.write("Esta aplicación estima el ahorro anual al instalar un Variador de Frecuencia (VFD) en un motor eléctrico.")

potencia = st.number_input("Potencia del motor (kW)", min_value=0.1, value=10.0)
horas = st.number_input("Horas de operación anual", min_value=1, value=4000)
reduccion = st.slider("Reducción de velocidad (%)", 10, 50, 20)

consumo_sin = potencia * horas
factor = (1 - reduccion / 100) ** 3
consumo_con = consumo_sin * factor
ahorro = consumo_sin - consumo_con

st.subheader("Resultados")
st.write(f"Consumo sin VFD: {consumo_sin:.2f} kWh")
st.write(f"Consumo con VFD: {consumo_con:.2f} kWh")
st.write(f"Ahorro anual: {ahorro:.2f} kWh")
