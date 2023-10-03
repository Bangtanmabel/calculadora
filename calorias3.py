import streamlit as st

# Título de la aplicación
st.title("Calculadoras")

# Barra lateral para la navegación entre páginas
page = st.sidebar.selectbox("Selecciona una página:", ("Inicio", "Calculadora de Calorías", "Calculadora de IMC", "Contacto"))

# Página de inicio
if page == "Inicio":
    st.header("Bienvenido a InfoMagic")
    st.write("Resolvemos tus dudas sobre calorías diarias recomendadas y tu Índice de Masa Corporal (IMC).")

    # Archivos multimedia
    st.image("balanza 1.png", caption="Imagen 1: balanza 1.png")
    st.image("balanza 2.png", caption="Imagen 2: balanza 2.png")
    st.image("balanza 3.png", caption="Imagen 3: balanza 3.png")

# Página de la calculadora de calorías
elif page == "Calculadora de Calorías":
    st.header("Calculadora de Calorías")
    st.write("Ingresa tus datos para calcular tus calorías diarias recomendadas.")

    # Entradas de usuario
    edad = st.slider("Edad", 1, 100, 25)
    peso = st.number_input("Peso (kg)", min_value=1.0, max_value=300.0, step=0.1)
    altura = st.number_input("Altura (cm)", min_value=1.0, max_value=300.0, step=0.1)
    genero = st.radio("Género", ("Masculino", "Femenino"))

    # Cálculo de calorías
    if genero == "Masculino":
        calorias = 88.362 + (13.397 * peso) + (4.799 * altura) - (5.677 * edad)
    else:
        calorias = 447.593 + (9.247 * peso) + (3.098 * altura) - (4.330 * edad)

    st.write(f"Calorías diarias recomendadas: {calorias:.2f} kcal")

# Página de la calculadora de IMC
elif page == "Calculadora de IMC":
    st.header("Calculadora de IMC")
    st.write("Ingresa tu peso en kilogramos y tu altura en metros para calcular tu IMC.")

    # Entradas de usuario
    peso_imc = st.number_input("Peso (kg)", min_value=0.0)
    altura_imc = st.number_input("Altura (m)", min_value=0.0)

    # Botón para calcular el IMC
    if st.button("Calcular IMC"):
        # Cálculo del IMC
        imc = peso_imc / (altura_imc ** 2)

        # Mostrar el resultado
        st.write(f'Tu IMC es: {imc:.2f}')

        # Interpretación del IMC
        if imc < 18.5:
            st.write('Tienes un peso bajo.')
        elif imc >= 18.5 and imc < 24.9:
            st.write('Tienes un peso saludable.')
        elif imc >= 25.0 and imc < 29.9:
            st.write('Tienes sobrepeso.')
        else:
            st.write('Tienes obesidad.')

# Página de contacto
elif page == "Contacto":
    st.header("Contacto")
    st.write("Integrantes del equipo:")
    st.write("- Gonzalo Roa (Desarrollador)")
    st.write("- Benjamin Duarte (Product Manager)")
    st.write("- Javier Vieytes (CEO)")
    st.write("- María Belén Sepúlveda (Diseñadora Gráfica)")
    st.write("- 4to medio (Curso)")

