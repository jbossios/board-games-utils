import streamlit as st
from random import uniform

def main():
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
        if len(players) > 1:
            # Select a random player
            case = round(uniform(0, len(players) - 1))
            st.success(f"{players[case]} starts first!")
        else:
            st.warning("Please enter at least two players.")

if __name__ == "__main__":
    main()