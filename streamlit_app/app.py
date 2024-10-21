import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Ruta relativa al archivo data.csv
data_path = os.path.join(os.path.dirname(__file__), '../data/data.csv')

# Verificar si el archivo existe en la ruta especificada
if not os.path.exists(data_path):
    st.error(f"File not found: {data_path}")
else:
    # Cargar el dataset
    df = pd.read_csv(data_path)

    # Título de la aplicación
    st.title('Data Visualization App')

    # Descripción de la aplicación
    st.markdown("""
    Esta aplicación web permite visualizar diferentes gráficos del dataset.
    """)

    # Mostrar las primeras cinco filas del dataset
    st.subheader('Dataset Overview')
    st.write(df.head())

    # Descripción de las columnas
    st.markdown("""
    **Descripción de las columnas:**
    - `User_ID`: Identificador único del usuario.
    - `Age`: Edad del usuario.
    - `Gender`: Género del usuario.
    - `Technology_Usage_Hours`: Horas de uso de tecnología por día.
    - `Social_Media_Usage_Hours`: Horas de uso de redes sociales por día.
    - `Gaming_Hours`: Horas de juego por día.
    - `Screen_Time_Hours`: Horas de tiempo de pantalla por día.
    - `Mental_Health_Status`: Estado de salud mental del usuario.
    - `Stress_Level`: Nivel de estrés del usuario.
    - `Sleep_Hours`: Horas de sueño por día.
    """)

    # Conclusiones del proyecto
    st.subheader('Conclusiones del Proyecto')
    st.markdown("""
    Las conclusiones del proyecto destacan la importancia de la limpieza y visualización de datos para comprender patrones y tendencias en los datos. El análisis proporciona información sobre cómo el uso de la tecnología afecta los indicadores de salud mental.

    1. **Acceso a Sistemas de Apoyo**:
       - Las personas con mejor acceso a sistemas de apoyo tienden a participar en más actividades físicas y reportan un mejor estado de salud mental. Las personas con mejor acceso a sistemas de apoyo, como amigos, familia o servicios comunitarios, tienden a participar en más actividades físicas. Esto puede deberse a que el apoyo social proporciona motivación y oportunidades para ser más activos. Además, estas personas también reportan un mejor estado de salud mental, posiblemente porque el apoyo social puede reducir el estrés y proporcionar un sentido de pertenencia y seguridad.

    2. **Impacto del Entorno Laboral**:
       - Un entorno laboral negativo puede estar asociado con menos horas de sueño. Un entorno laboral negativo, caracterizado por altos niveles de estrés, malas relaciones con colegas o jefes y condiciones de trabajo insatisfactorias, puede estar asociado con menos horas de sueño. El estrés y la ansiedad generados por un mal ambiente de trabajo pueden dificultar la capacidad de relajarse y dormir bien.

    3. **Uso del Apoyo en Línea**:
       - Las personas que pasan más tiempo utilizando apoyo en línea tienden a participar en menos actividades físicas. Las personas que pasan más tiempo utilizando apoyo en línea, como foros, redes sociales o servicios de chat, tienden a participar en menos actividades físicas. Esto puede deberse a que el tiempo dedicado a estas actividades en línea reduce el tiempo disponible para el ejercicio físico. Además, el uso excesivo de dispositivos electrónicos puede llevar a un estilo de vida más sedentario.

    4. **Uso de Tecnología y Redes Sociales**:
       - No existe una relación fuerte entre el uso de la tecnología y el uso de las redes sociales. No existe una relación fuerte entre el uso de la tecnología y el uso de las redes sociales. Esto sugiere que el tiempo que las personas pasan utilizando tecnología (como computadoras, tabletas y teléfonos inteligentes) no está necesariamente relacionado con el tiempo que pasan en redes sociales. Las personas pueden usar la tecnología para una variedad de actividades que no incluyen las redes sociales, como trabajar, estudiar o entretenerse.

    5. **Género y Uso de Tecnología**:
       - El uso de la tecnología es similar entre diferentes géneros en este conjunto de datos. El uso de la tecnología es similar entre diferentes géneros en este conjunto de datos. Esto indica que no hay diferencias significativas en la cantidad de tiempo o la forma en que hombres y mujeres utilizan la tecnología. Ambos géneros parecen tener patrones de uso de tecnología comparables.
    """)


# Sidebar para la navegación
st.sidebar.title('Navigation')
options = st.sidebar.radio('Select a chart:', [
    'Age Distribution', 'Gender Distribution', 'Technology Usage by Gender', 
    'Social Media Usage by Gender', 'Stress Level by Gender', 'Gaming Hours by Gender', 
    'Sleep Hours Distribution by Range'
])


# Función para mostrar el gráfico de distribución de edades
def age_distribution():
    st.subheader('Distribution of Age Groups')
    bins = [0, 18, 35, 50, 65, 100]
    labels = ['0-17', '18-34', '35-49', '50-64', '65+']
    df['Age_Group'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)
    
    plt.figure(figsize=(14, 8))
    sns.set(style="whitegrid")
    ax = sns.histplot(df['Age_Group'], color='skyblue', kde=False, edgecolor='black')
    plt.title('Distribution of Age Groups', fontsize=22, weight='bold')
    plt.xlabel('Age Group', fontsize=18)
    plt.ylabel('Count', fontsize=18)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    for p in ax.patches:
        ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()), 
                    ha='center', va='center', fontsize=12, color='black', xytext=(0, 10), 
                    textcoords='offset points')
    st.pyplot(plt)

# Función para mostrar el gráfico de distribución de género
def gender_distribution():
    st.subheader('Gender Distribution')
    gender_counts = df['Gender'].value_counts()
    
    plt.figure(figsize=(8, 8))
    colors = sns.color_palette("pastel")
    wedges, texts, autotexts = plt.pie(gender_counts, autopct='%1.1f%%', startangle=140, colors=colors, textprops=dict(color="w"))
    plt.legend(wedges, gender_counts.index, title="Gender", loc="upper right", bbox_to_anchor=(1, 0, 0.5, 1))
    plt.title('Gender Distribution', fontsize=20, weight='bold')
    plt.axis('equal')
    st.pyplot(plt)

# Función para mostrar el gráfico de uso de tecnología por género
def technology_usage_by_gender():
    st.subheader('Technology Usage Hours by Gender')
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=df, x='Gender', y='Technology_Usage_Hours', palette='pastel')
    plt.title('Technology Usage Hours by Gender', fontsize=20, weight='bold')
    plt.xlabel('Gender', fontsize=15)
    plt.ylabel('Technology Usage Hours', fontsize=15)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    st.pyplot(plt)

# Función para mostrar el gráfico de uso de redes sociales por género
def social_media_usage_by_gender():
    st.subheader('Social Media Usage Hours by Gender')
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=df, x='Gender', y='Social_Media_Usage_Hours', palette='pastel')
    plt.title('Social Media Usage Hours by Gender', fontsize=20, weight='bold')
    plt.xlabel('Gender', fontsize=15)
    plt.ylabel('Social Media Usage Hours', fontsize=15)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    st.pyplot(plt)

# Función para mostrar el gráfico de nivel de estrés por género
def stress_level_by_gender():
    st.subheader('Stress Level by Gender')
    plt.figure(figsize=(12, 8))
    sns.countplot(data=df, hue='Gender', x='Stress_Level', palette='pastel')
    plt.title('Stress Level by Gender', fontsize=20, weight='bold')
    plt.xlabel('Stress Level', fontsize=15)
    plt.ylabel('Count', fontsize=15)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.legend(title="Gender", fontsize=12, loc='upper left', bbox_to_anchor=(1, 1))
    st.pyplot(plt)

# Función para mostrar el gráfico de horas de juego por género
def gaming_hours_by_gender():
    st.subheader('Gaming Hours by Gender')
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=df, x='Gender', y='Gaming_Hours', palette='pastel')
    plt.title('Gaming Hours by Gender', fontsize=20, weight='bold')
    plt.xlabel('Gender', fontsize=15)
    plt.ylabel('Gaming Hours', fontsize=15)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    st.pyplot(plt)

# Función para mostrar el gráfico de distribución de horas de sueño por rango
def sleep_hours_distribution_by_range():
    st.subheader('Sleep Hours Distribution by Range')
    # Crear una nueva columna 'Sleep_Hours_Range' con los rangos de horas de sueño
    bins = [0, 4, 6, 8, 10, 12]
    labels = ['0-4', '4-6', '6-8', '8-10', '10-12']
    df['Sleep_Hours_Range'] = pd.cut(df['Sleep_Hours'], bins=bins, labels=labels, right=False)
    
    plt.figure(figsize=(12, 6))
    sns.countplot(data=df, x='Sleep_Hours_Range', palette='pastel')
    plt.title('Sleep Hours Distribution by Range', fontsize=20, weight='bold')
    plt.xlabel('Sleep Hours Range', fontsize=15)
    plt.ylabel('Count', fontsize=15)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    st.pyplot(plt)

# Mostrar el gráfico seleccionado
if options == 'Age Distribution':
    age_distribution()
elif options == 'Gender Distribution':
    gender_distribution()
elif options == 'Technology Usage by Gender':
    technology_usage_by_gender()
elif options == 'Social Media Usage by Gender':
    social_media_usage_by_gender()
elif options == 'Stress Level by Gender':
    stress_level_by_gender()
elif options == 'Gaming Hours by Gender':
    gaming_hours_by_gender()
elif options == 'Sleep Hours Distribution by Range':
    sleep_hours_distribution_by_range()