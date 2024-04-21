import streamlit as st
from random import uniform

def main():

    st.title("Apps for Board Games")

    # General apps
    st.header("General")
    url = 'https://link.jonathanbossio.com/board-games-utils-who-starts'
    st.write("[Player Selector App](%s)" % url)

    # Apps for Azul Queen's Garden
    st.header("Azul Queen's Garden")
    url = 'https://link.jonathanbossio.com/board-games-utils-azul-spin-the-scoring-wheel'
    st.write("[Scoring Wheel for End Of The Turn](%s)" % url)

if __name__ == "__main__":
    main()