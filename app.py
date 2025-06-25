
import streamlit as st
# ---------------------- CONFIGURACIÓN DE PÁGINA ----------------------
st.set_page_config(page_title="Portafolio de Luciana Huertas", page_icon=":sparkles:", layout="wide")
# Menú en el sidebar
menu = st.sidebar.radio(
    "Navegación",
    ["General", "Currículum", "Fortalezas", "Intereses", "Galería de momentos", "Contacto y Referencias"]
)

# ---------------------- INFO PERSONAL ----------------------
info = {
    "Pronoun": "ella",
    "Name": "Luciana",
    "Full_Name": "Luciana Huertas",
    "Intro": "Soy estudiante de Publicidad en la PUCP y apasionada por cambiar el mundo",
    "About": """¡Hola, soy Luciana! Me apasiona aprender sobre temáticas nuevas que involucren el cambio social, y también me encanta trabajar en proyectos que me apasionen y creen un impacto significativo. 
    Actualmente me encuentro trabajando como Guía PUCP y en busca del próximo voluntariado que transforme el mundo. ¡En este portafolio podrás descubrir más sobre mí y mis ideas!""",
    "City": "Lima, Perú",
    "Email": "luciana.huertas.a@gmail.com",
    "Photo": "https://i.imgur.com/XMGcTff.png",
    "CV": "https://i.imgur.com/LTDspUS.png"
}

endorsements = {
    "img1": "https://i.imgur.com/wLsNunU.jpeg",
    "img2": "https://i.imgur.com/4wbxvlA.jpeg",
    "img3": "https://i.imgur.com/3QCImVD.jpeg",
    "img4": "https://i.imgur.com/A1ylzev.jpeg",
    "img5": "https://i.imgur.com/RzILaDj.jpeg",
    "img6": "https://i.imgur.com/izxTzzY.jpeg"
}

embed_rss = {
    'rss':"""<div style="overflow-y: scroll; height:500px; background-color:white;"> 
        <div id="retainable-rss-embed" 
        data-rss="https://www.instagram.com/luciana.hrts/"
        data-maxcols="3" 
        data-layout="grid"
        data-poststyle="inline" 
        data-readmore="Leer más" 
        data-buttonclass="btn btn-primary" 
        data-offset="0"></div></div> 
        <script src="https://www.twilik.com/assets/retainable/rss-embed/retainable-rss-embed.js"></script>"""
}

# ---------------------- INTERFAZ ----------------------
# Foto e Introducción
st.write("Accede a la información completa a través del menú en la parte superior a la izquierda")
st.title(info["Full_Name"])
st.image(info["Photo"], width=150)
st.subheader(info["Intro"])
st.markdown(f"📍 {info['City']} | ✉️ {info['Email']}")

# Mostrar secciones según el menú
if menu == "General":
    st.header("Sobre mí")
    st.write(info["About"])

elif menu == "Currículum":
    st.header("📂 Currículum")
    st.write("Explora los intereses y experiencia de Luciana a tarvés de su CV, donde podrás encontrar información completa de su desarrollo como persona y profesional.")
    st.image(info["CV"], width=200)
    
elif menu == "Fortalezas":
    st.header("💪 Fortalezas")
    st.write("Luciana posee gran facilidad de habla y carisma, así como un fuerte sentido de la colaboración y el trabajo en equipo efectivo. Siempre está dispuesta a ayudar y destacar.")

elif menu == "Intereses":
    st.header("🎯 Intereses")
    st.write("Luciana tiene una gran pasión por investigar temáticas sociales que afecten actualmente al mundo. También encuentra una gran pasión por la producción de contenido audiovisual. Busca mezclar ambos ámbitos para desarrollarse dentro del enfoque publicitario.")

elif menu == "Galería de momentos":
    st.header("Galería de momentos")
    col1, col2, col3 = st.columns(3)
    col1.image(endorsements["img1"])
    col1.image(endorsements["img4"])
    col2.image(endorsements["img2"])
    col2.image(endorsements["img5"])
    col3.image(endorsements["img3"])
    col3.image(endorsements["img6"])

elif menu == "Contacto y Referencias":
    st.header("Contacto")
    st.markdown('[✉️ Escríbeme un correo](mailto:luciana.huertas.a@gmail.com)', unsafe_allow_html=True)
    st.header("📌 Referencias")
    st.write("Referencias disponibles a solicitud.")
    st.header("Instagram")
    st.markdown("""
    <a href="https://www.instagram.com/luciana.hrts/" target="_blank">
        <button style='padding: 10px 20px; background-color: #E1306C; color: white; border: none; border-radius: 5px;'>Visita mi Instagram 📸✨</button>
    </a>
    """, unsafe_allow_html=True)

