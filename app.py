import streamlit as st

# ---------------------- CONFIGURACIÓN DE PÁGINA ----------------------
st.set_page_config(page_title="Portafolio de Luciana Huertas", page_icon="✨", layout="wide")

# ---------------------- ESTILOS PERSONALIZADOS ----------------------
st.markdown("""
    <style>
        body {
            background-color: #FAF9F6;
        }
        .main {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.05);
        }
        h1, h2, h3 {
            font-family: 'Georgia', serif;
            color: #5C3D71;
        }
        p {
            font-family: 'Helvetica Neue', sans-serif;
            font-size: 16px;
            color: #333;
        }
        .section {
            background-color: #ffffff;
            padding: 25px;
            margin-bottom: 25px;
            border-radius: 12px;
            box-shadow: 0 3px 8px rgba(0,0,0,0.05);
        }
        .intro-text {
            font-size: 18px;
            color: #6E5580;
            font-weight: 500;
        }
    </style>
""", unsafe_allow_html=True)

# ---------------------- MENÚ ----------------------
menu = st.sidebar.radio(
    "🌸 Navegación",
    ["Sobre mí", "Portafolio", "Fortalezas", "Intereses", "Contacto y Referencias"]
)

# ---------------------- INFO PERSONAL ----------------------
info = {
    "Pronoun": "ella",
    "Name": "Luciana",
    "Full_Name": "Luciana Huertas",
    "Intro": "Soy estudiante de Publicidad en la PUCP y apasionada por cambiar el mundo.",
    "About": """¡Hola, soy Luciana! Me apasiona aprender sobre temáticas nuevas que involucren el cambio social, y también me encanta trabajar en proyectos que me apasionen y generen un impacto significativo. 
    Actualmente me encuentro trabajando como Guía PUCP y en busca del próximo voluntariado que transforme el mundo. ¡En este portafolio podrás descubrir más sobre mí y mis ideas!""",
    "City": "Lima, Perú",
    "Email": "luciana.huertas.a@gmail.com",
    "Photo": "https://i.imgur.com/XMGcTff.png",
    "CV": "https://i.imgur.com/LTDspUS.png"
}

endorsements = {
    "img1": "https://i.imgur.com/wLsNunU.jpeg",
    "img2": "https://i.imgur.com/4wbxvlA.jpeg",
    "img3": "https://i.imgur.com/3QCImVD.jpeg"
}

# ---------------------- PORTADA E INTRODUCCIÓN ----------------------
st.markdown("<div class='section'>", unsafe_allow_html=True)
col1, col2 = st.columns([1, 3])

with col1:
    st.image(info["Photo"], width=180)

with col2:
    st.markdown(f"<h1>{info['Full_Name']}</h1>", unsafe_allow_html=True)
    st.markdown(f"<p class='intro-text'>{info['Intro']}</p>", unsafe_allow_html=True)
    st.markdown(f"📍 {info['City']} &nbsp;&nbsp;&nbsp; ✉️ {info['Email']}")
st.markdown("</div>", unsafe_allow_html=True)

# ---------------------- SECCIONES ----------------------
if menu == "Sobre mí":
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.header("👩 Sobre mí")
    st.write(info["About"])
    st.markdown("</div>", unsafe_allow_html=True)

elif menu == "Portafolio":
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.header("📂 Portafolio")
    st.write("Explora los intereses y experiencia de Luciana en este portafolio, donde podrás encontrar información completa de su desarrollo como persona y profesional.")
    st.image(info["CV"], width=250)
    st.markdown("</div>", unsafe_allow_html=True)

elif menu == "Fortalezas":
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.header("💪 Fortalezas")
    st.write("Luciana posee gran facilidad de habla y carisma, así como un fuerte sentido de la colaboración y el trabajo en equipo efectivo. Siempre está dispuesta a ayudar y destacar.")
    st.markdown("</div>", unsafe_allow_html=True)

elif menu == "Intereses":
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.header("🎯 Intereses")
    st.write("Luciana tiene una gran pasión por investigar temáticas sociales que afecten actualmente al mundo. También encuentra una gran pasión por la producción de contenido audiovisual. Busca mezclar ambos ámbitos para desarrollarse dentro del enfoque publicitario.")
    st.markdown("</div>", unsafe_allow_html=True)

elif menu == "Contacto y Referencias":
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.header("📞 Contacto")
    st.markdown('[✉️ Escríbeme un correo](mailto:luciana.huertas.a@gmail.com)', unsafe_allow_html=True)
    
    st.header("📌 Referencias")
    st.write("Referencias disponibles a solicitud.")
    
    st.header("📸 Instagram")
    st.markdown("""
        <a href="https://www.instagram.com/luciana.hrts/" target="_blank">
            <button style='padding: 10px 20px; background-color: #E1306C; color: white; border: none; border-radius: 8px;'>Visita mi Instagram ✨</button>
        </a>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ---------------------- SECCIÓN MOMENTOS ----------------------
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.header("📷 Momentos")
col1, col2, col3 = st.columns(3)
col1.image(endorsements["img1"], use_column_width=True)
col2.image(endorsements["img2"], use_column_width=True)
col3.image(endorsements["img3"], use_column_width=True)
st.markdown("</div>", unsafe_allow_html=True)

