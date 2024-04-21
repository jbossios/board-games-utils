import streamlit as st
from random import uniform

def main():
    st.title("Azul Queen's Garden")
    st.title("Scoring Wheel for End Of The Round")

    # Add space between title and button using HTML line breaks
    st.markdown("<br>", unsafe_allow_html=True)

    # List of images (i.e. results)
    options = [i for i in range(1, 13)]

    # Button to trigger the spin of the scoring wheel
    if st.button("Spin the wheel"):
        case = round(uniform(1, len(options)))
        st.image(f'./option_{case}.png', caption=f'Patterns to be used for scoring')

if __name__ == "__main__":
    main()