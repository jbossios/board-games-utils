import streamlit as st
from random import uniform

def main():

    # Sidebar
    with st.sidebar:
        st.write('Other apps:')
        url = 'https://link.jonathanbossio.com/board-games-utils-azul-spin-the-scoring-wheel'
        st.write("[Azul Queen's Garden -> Scoring Wheel for End Of The Turn](%s)" % url)

    # Select language
    language = st.selectbox('', ['🇬🇧 English', '🇪🇸 Español'])

    # Display title
    title = {'🇬🇧 English': 'Player Selector App', '🇪🇸 Español': 'App para seleccionar un jugador de forma aleatoria'}[language]
    st.title(title)

    # Ask the user to input the number of players
    ask_input = {
        '🇬🇧 English': 'Enter the number of players (2 to 10)',
        '🇪🇸 Español': 'Ingrese el numero de jugadores (2 a 10)'
    }[language]
    num_players = st.number_input(ask_input, min_value=2, max_value=10, step=1)

    # Create a list to store the names of the players
    players = []
    for i in range(num_players):
        ask_name = {
            '🇬🇧 English': f'Enter name of Player {i+1}',
            '🇪🇸 Español': f'Ingrese el nombre del jugador {i+1}'
        }[language]
        player_name = st.text_input(ask_name)
        players.append(player_name)

    # Button to trigger the selection
    button_text = {
        '🇬🇧 English': 'Select which player should start',
        '🇪🇸 Español': 'Quien empieza?'
    }[language]
    if st.button(button_text):
        # Make sure names were provided
        tests_passed = True
        for i, name in enumerate(players, 1):
            if not name:
                warning_text = {
                    '🇬🇧 English': f"The name of player {i} is missing, please enter the name for player {i}.",
                    '🇪🇸 Español': f'Por favor ingrese el nombre del jugador {i}.'
                }[language]
                st.warning(warning_text)
                tests_passed = False
        # Make sure there are at least 2 players
        if tests_passed:
            # Select a random player
            case = round(uniform(0, len(players) - 1))
            result = {
                '🇬🇧 English': f"{players[case]} starts first!",
                '🇪🇸 Español': f"{players[case]} empieza!"
            }[language]
            st.success(result)

if __name__ == "__main__":
    main()