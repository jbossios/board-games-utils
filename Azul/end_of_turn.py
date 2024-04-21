import streamlit as st
import matplotlib.image as mpimg
from random import uniform

def main():
    # st.markdown("<h1 style='text-align: center;'>Azul: Queen's Garden</h1>", unsafe_allow_html=True)
    # st.markdown("<h2 style='text-align: center;'>Scoring Wheel for End of The Round</h2>", unsafe_allow_html=True)
    st.title("Azul Queen's Garden")
    st.title("Scoring Wheel for End Of The Round")

    # Add space between title and button using HTML line breaks
    st.markdown("<br>", unsafe_allow_html=True)

    options = [i for i in range(1, 13)]
    # Button to trigger the sping of the wheel
    if st.button("Spin the wheel"):
        case = round(uniform(1, len(options)))
        img = mpimg.imread(f'option_{case}.png')
        st.image(img, caption=f'Patterns to be used for scoring')

if __name__ == "__main__":
    main()