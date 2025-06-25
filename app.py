import streamlit as st

# ---------------------- CONFIGURACIÓN DE PÁGINA ----------------------
st.set_page_config(page_title="Portafolio de Luciana Huertas", page_icon=":sparkles:", layout="wide")

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
    "Photo": "https://i.imgur.com/XMGcTff.png"
}

endorsements = {
    "img1": "https://i.imgur.com/wLsNunU.jpeg",
    "img2": "https://i.imgur.com/4wbxvlA.jpeg",
    "img3": "https://i.imgur.com/3QCImVD.jpeg"
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
st.image(info["Photo"], width=150)
st.title(info["Full_Name"])
st.subheader(info["Intro"])
st.markdown(f"📍 {info['City']} | ✉️ {info['Email']}")

# Sección "Sobre mí"
st.header("Sobre mí")
st.write(info["About"])

# Sección Endorsements
st.header("Testimonios / Momentos")
col1, col2, col3 = st.columns(3)
col1.image(endorsements["img1"], use_column_width=True)
col2.image(endorsements["img2"], use_column_width=True)
col3.image(endorsements["img3"], use_column_width=True)

# Sección Instagram Embed
st.header("Instagram")
st.components.v1.html(embed_rss['rss'], height=600, scrolling=True)
