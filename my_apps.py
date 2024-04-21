import streamlit as st
from random import uniform

def main():

    # Select language    
    language = st.selectbox('', ['🇬🇧 English', '🇪🇸 Español'])

    # Show title
    title = {
        '🇬🇧 English': "Apps for Board Games",
        '🇪🇸 Español': 'Apps para Juegos de Mesa'
    }[language]
    st.title(title)

    # General apps
    st.header("General")
    url = 'https://link.jonathanbossio.com/board-games-utils-who-starts'
    url_text = {
        '🇬🇧 English': 'Player Selector App',
        '🇪🇸 Español': 'App para Elegir Jugador'
    }[language]
    st.write("["+url_text+"](%s)" % url)

    # Apps for Azul Queen's Garden
    header = {
        '🇬🇧 English': "Azul Queen's Garden",
        '🇪🇸 Español': "Azul Jardín de la Reina"
    }[language]
    st.header(header)
    url = 'https://link.jonathanbossio.com/board-games-utils-azul-spin-the-scoring-wheel'
    url_text = {
        '🇬🇧 English': "Scoring Wheel for End Of The Turn",
        '🇪🇸 Español': "Disco giratorio para final de la ronda"
    }[language]
    st.write("["+url_text+"](%s)" % url)

if __name__ == "__main__":
    main()