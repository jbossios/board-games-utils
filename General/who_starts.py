import streamlit as st
from random import uniform

def main():

   # Sidebar
    with st.sidebar:
        st.write('Other apps:')
        url = 'https://link.jonathanbossio.com/board-games-utils-azul-spin-the-scoring-wheel'
        st.write("[Azul Queen's Garden -> Scoring Wheel for End Of The Turn](%s)" % url)

    st.title("Player Selector App")

    # Ask the user to input the number of players
    num_players = st.number_input("Enter the number of players (2 to 10)", min_value=2, max_value=10, step=1)

    # Create a list to store the names of the players
    players = []
    for i in range(num_players):
        player_name = st.text_input(f"Enter name of Player {i+1}")
        players.append(player_name)

    # Button to trigger the selection
    if st.button("Select which player should start"):
        # Make sure names were provided
        tests_passed = True
        for i, name in enumerate(players, 1):
            if not name:
                st.warning(f"The name of player {i} is missing, please enter the name for player {i}.")
                tests_passed = False
        # Make sure there are at least 2 players
        if tests_passed:
            # Select a random player
            case = round(uniform(0, len(players) - 1))
            st.success(f"{players[case]} starts first!")

if __name__ == "__main__":
    main()