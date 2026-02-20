import streamlit as st
import pandas as pd


st.set_page_config(page_title="Proyecto Python", page_icon="🐍")

with st.sidebar:
    # Agregamos logo al 
    st.image("https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg", width=70)
    st.title("Python")
    
    with st.expander("🏠 Home", expanded=True):
        opcion = st.radio("Selecciona un módulo:", ["Presentacion", "Ejercicio 01", "Ejercicio 02", "Ejercicio 03", "Ejercicio 04"])

if opcion == "Presentacion":
    
    st.markdown("<h1 style='text-align: center;'>🐍 Proyecto Python Fundamentals</h1>", unsafe_allow_html=True)
    

    
    st.markdown("""
    ### 🎯 Objetivo del Proyecto
    El presente trabajo tiene como objetivo **consolidar y aplicar** los conocimientos adquiridos durante las sesiones del módulo de fundamentals.
    
    Se hace uso de programación propia de **Python** y librerías clave como:
    * **Streamlit** (Interfaz de usuario)
    * **Pandas** (Cálculos)
    """)

    # Cuadros informativos para autor y fecha
    col1, col2 = st.columns(2)
    with col1:
        st.info(f"*Módulo:*\n\n - Python Fundamentals")
    with col2:
        st.success(f"*Elaborado por:*\n\n - Cesar Enrique Nanfuñay Ñiquen")
    
    st.caption("📅 **Fecha de entrega:** 22 de febrero, 2026")

elif opcion == "Ejercicio 01":
    # Aquí insertamos el código del Verificador de Presupuesto
    st.title("💰 Verificador de Presupuesto")
    st.subheader("Ejercicio 1: Variables y Condicionales")
    
    presupuesto = st.number_input("Ingresa tu presupuesto total:", min_value=0.0, step=10.0)
    gasto = st.number_input("Ingresa el gasto realizado:", min_value=0.0, step=10.0)

    if st.button("Evaluar Gasto"):
        diferencia = presupuesto - gasto
        
        if gasto <= presupuesto:
            st.success(f"✅ ¡Estás dentro del presupuesto! Te sobran: ${diferencia:.2f}")
        else:
            st.warning(f"⚠️ El presupuesto ha sido excedido por: ${abs(diferencia):.2f}")
        
        st.write(f"La diferencia actual es de: **${diferencia:.2f}**")

elif opcion == "Ejercicio 02":
    st.title("📊 Registro de Actividades Financieras")
    st.subheader("Ejercicio 2 : Listas y Diccionarios")
    
    #Para iniciar la lista
    if 'lista_actividades' not in st.session_state:
        st.session_state.lista_actividades = []

    #Formulario de entrada de datos
    with st.form("form_actividad"):
        col1, col2 = st.columns(2)
        with col1:
            nombre = st.text_input("Nombre de la actividad:", placeholder="Ej: Cena, Viaje, Luz")
            tipo = st.selectbox("Tipo de actividad:", ["Alimentación", "Transporte", "Servicios", "Ocio", "Otros"])
        with col2:
            presupuesto_act = st.number_input("Presupuesto asignado:", min_value=0.0, step=1.0)
            gasto_real_act = st.number_input("Gasto real efectuado:", min_value=0.0, step=1.0)
        
        btn_agregar = st.form_submit_button("Agregar Actividad")

    #Para guardar en el diccionario y la lista
    if btn_agregar:
        nueva_actividad = {
            "nombre": nombre,
            "tipo": tipo,
            "presupuesto": presupuesto_act,
            "gasto_real": gasto_real_act
        }
        st.session_state.lista_actividades.append(nueva_actividad)
        st.success(f"Actividad '{nombre}' agregada con éxito.")

    #Mostrar la lista en formato tabla usando DataFrame
    if st.session_state.lista_actividades:
        st.write("### Resumen de Actividades")
        df = pd.DataFrame(st.session_state.lista_actividades)
        st.dataframe(df, use_container_width=True)

        #Recorrer la lista y evaluar las actividades actividad
        st.write("### Evaluación de Estado")
        for act in st.session_state.lista_actividades:
            if act['gasto_real'] <= act['presupuesto']:
                st.write(f"✅ **{act['nombre']}**: Dentro del presupuesto (Ahorraste ${act['presupuesto'] - act['gasto_real']:.2f})")
            else:
                st.write(f"❌ **{act['nombre']}**: Presupuesto excedido (Exceso de ${act['gasto_real'] - act['presupuesto']:.2f})")
    else:
        st.info("Aún no hay actividades registradas. ¡Usa el formulario de arriba!")


elif opcion == "Ejercicio 03":
    st.title("📈 Proyección de Retornos")
    st.subheader("Ejercicio 3: Funciones y Programación Funcional")
    #Definimos la función de cálculo
    def calcular_retorno(presupuesto, tasa, meses):
        # Fórmula: Retorno = presupuesto * tasa * meses
        return presupuesto * (tasa / 100) * meses
    #Para poder ingresar los datos
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            nombre_act = st.text_input("Nombre de la inversión/actividad:", value="Inversión A")
            presupuesto_act = st.number_input("Presupuesto a invertir:", min_value=0.0, value=1000.0)
        
        with col2:
            tasa = st.slider("Tasa de retorno mensual (%)", 0.0, 20.0, 5.0)
            meses = st.number_input("Tiempo (meses):", min_value=1, value=12)
    
    #Ejecución del cálculo
    if st.button("Calcular Retorno"):
        # Creamos una lista momentánea con la actividad ingresada
        actividades_temp = [{"nombre": nombre_act, "presupuesto": presupuesto_act}]

        # Aplicamos map y lambda, lambda toma el diccionario 'x', extrae el presupuesto y usa la función
        resultados = list(map(lambda x: {
            "nombre": x["nombre"],
            "retorno": calcular_retorno(x["presupuesto"], tasa, meses)
        }, actividades_temp))
        #Finalmente mostramos los resultados
        for res in resultados:
            st.success(f"El retorno esperado para **{res['nombre']}** es de: **${res['retorno']:.2f}**")


elif opcion == "Ejercicio 04":
    st.title("🏗️ Programación Orientada a Objetos")
    st.subheader("Ejercicio 4: Clase Actividad")

    #Creamos la Clase
    class Actividad:
        def __init__(self, nombre, tipo, presupuesto, gasto_real):
            self.nombre = nombre
            self.tipo = tipo
            self.presupuesto = presupuesto
            self.gasto_real = gasto_real

        #Para evaluar el presupuesto
        def esta_en_presupuesto(self):
            return self.gasto_real <= self.presupuesto

        #Para devolver resumen
        def mostrar_info(self):
            return f"Actividad: {self.nombre} | Categoría: {self.tipo}"

    
    st.info("Crea un objeto de la clase 'Actividad' ingresando los datos abajo:")
    
    col1, col2 = st.columns(2)
    with col1:
        nombre = st.text_input("Nombre:", value="Proyecto Web")
        tipo = st.selectbox("Tipo:", ["Inversión", "Gasto Fijo", "Gasto Variable"])
    with col2:
        pres = st.number_input("Presupuesto ($):", min_value=0.0, value=500.0)
        gasto = st.number_input("Gasto Real ($):", min_value=0.0, value=450.0)

    if st.button("Instanciar Clase y Mostrar Info"):
        #Convertir los datos en un Objeto
        mi_actividad = Actividad(nombre, tipo, pres, gasto)

        #Mostramos la información usando los métodos del objeto
        st.markdown("## 📝 Información del Objeto")
        st.write(mi_actividad.mostrar_info())
        
        # Uso del método esta_en_presupuesto() para la lógica de colores
        if mi_actividad.esta_en_presupuesto():
            st.success(f"✅ ¡Cumple con el presupuesto! (Diferencia: ${mi_actividad.presupuesto - mi_actividad.gasto_real})")
        else:
            st.error(f"❌ Presupuesto excedido (Déficit: ${mi_actividad.gasto_real - mi_actividad.presupuesto})")
            
        # Demostración de acceso a atributos
        st.code(f"""
        # Datos internos del objeto:
        Objeto: {mi_actividad}
        Atributo Nombre: {mi_actividad.nombre}
        Atributo Presupuesto: {mi_actividad.presupuesto}
        """)


