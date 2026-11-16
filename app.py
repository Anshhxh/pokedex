
import streamlit as st
from pokemon import get_pokemon, get_pokemon_list, get_pokemon_by_type


# Cached API functions

@st.cache_data(ttl=3600)
def fetch_pokemon(name):
    return get_pokemon(name)


@st.cache_data(ttl=3600)
def fetch_pokemon_collection(limit, offset):
    return get_pokemon_list(limit, offset)

@st.cache_data(ttl=3600)
def fetch_pokemon_by_type(type_name):
    return get_pokemon_by_type(type_name)

@st.cache_data(ttl=3600)
def fetch_all_pokemon():
    return get_pokemon_list(limit=100000, offset=0)


TYPE_COLORS = {
    "normal": "#A8A878",
    "fire": "#F08030",
    "water": "#6890F0",
    "electric": "#F8D030",
    "grass": "#78C850",
    "ice": "#98D8D8",
    "fighting": "#C03028",
    "poison": "#A040A0",
    "ground": "#E0C068",
    "flying": "#A890F0",
    "psychic": "#F85888",
    "bug": "#A8B820",
    "rock": "#B8A038",
    "ghost": "#705898",
    "dragon": "#7038F8",
    "dark": "#705848",
    "steel": "#B8B8D0",
    "fairy": "#EE99AC"
}



# ---------------- PAGE CONFIGURATION ----------------

st.set_page_config(
    page_title="My Pokedex",
    page_icon="⚡",
    layout="wide"
)

page = st.sidebar.radio("Navigation",["Search Pokemon", "Pokemon Collection"])

if page == "Search Pokemon":
    # ---------------- APPLICATION HEADER ----------------

    st.title("⚡POKEDEX")
    st.caption("Explore the world of Pokemon, one creature at a time.")

    st.divider()


    # ---------------- SEARCH SECTION ----------------

    with st.form("pokemon_search"):

        col1, col2 = st.columns([4, 1])

        with col1:
            pokemon_name = st.text_input(
                "Search Pokemon",
                placeholder="Enter Pokemon name or ID..."
            )

        with col2:
            st.write("")
            st.write("")
            search_button = st.form_submit_button(
                "Search",
                use_container_width=True
            )

        # ---------------- FETCH POKEMON DATA ----------------

    if search_button:

        if not pokemon_name.strip():

            st.warning("Please enter a Pokemon name.")

        else:

            with st.spinner("Searching Pokemon..."):

                data = fetch_pokemon(pokemon_name)

            if data:

                st.success("Pokemon found!")

                # ---------------- PROFILE SECTION ----------------

                left, right = st.columns([1, 2])

                with left:

                    st.subheader(
                        data["name"].capitalize()
                    )

                    st.caption(
                        f"National Pokedex No. #{data['id']:03d}"
                    )

                    image_url = (
                        data["sprites"]["other"]
                        ["official-artwork"]["front_default"]
                    )

                    if image_url:
                        st.image(image_url, width=300)

                    else:
                        st.info("Artwork unavailable.")

                    # Pokemon types

                    st.markdown("### Types")

                    for item in data["types"]:

                        pokemon_type = item["type"]["name"]

                        color = TYPE_COLORS.get(
                            pokemon_type,
                            "#808080"
                        )

                        st.markdown(
                            f"""
                            <span style="
                                background-color: {color};
                                color: white;
                                padding: 8px 18px;
                                border-radius: 20px;
                                margin-right: 8px;
                                font-weight: bold;
                                display: inline-block;
                            ">
                                {pokemon_type.capitalize()}
                            </span>
                            """,
                            unsafe_allow_html=True
                        )


                    # Abilities

                    st.markdown("### Abilities")

                    for item in data["abilities"]:

                        ability = (
                            item["ability"]["name"].capitalize()
                        )

                        if item["is_hidden"]:
                            st.write(f"- {ability} (Hidden)")

                        else:
                            st.write(f"- {ability}")

                with right:

                    st.subheader("Pokemon Information")

                    # Basic details

                    c1, c2, c3 = st.columns(3)

                    c1.metric(
                        "Height",
                        f"{data['height'] / 10} m"
                    )

                    c2.metric(
                        "Weight",
                        f"{data['weight'] / 10} kg"
                    )

                    c3.metric(
                        "Base Experience",
                        data["base_experience"] if data["base_experience"] is not None else "N/A"
                    )

                    st.divider()

                    # Base statistics

                    st.subheader("Base Statistics")

                    for item in data["stats"]:

                        stat_name = (
                            item["stat"]["name"].capitalize()
                        )

                        stat_value = item["base_stat"]

                        st.write(
                            f"**{stat_name}: {stat_value}**"
                        )

                        st.progress(
                            min(stat_value / 255, 1.0)
                        )

                    # Total stats

                    total_stats = sum(
                        item["base_stat"]
                        for item in data["stats"]
                    )

                    st.divider()

                    st.metric(
                        "Total Base Stats",
                        total_stats
                    )

            else:

                st.error(
                    "Pokemon not found. Please check the name "
                    "or try again."
                )

    else:

        st.info(
            "Search for a Pokemon to explore its information."
        )



elif page == "Pokemon Collection":

    st.title("Pokemon Collection")
    st.caption("Explore the complete National Pokedex.")

    st.divider()

    # ---------------- FETCH COMPLETE LIST ----------------

    with st.spinner("Loading complete Pokedex..."):

        collection = fetch_all_pokemon()

    if not collection:

        st.error("Unable to load Pokemon collection.")

    else:

        all_pokemon = collection["results"]

        # ---------------- SEARCH AND FILTER ----------------

        st.subheader("Find your Pokemon")

        col1, col2 = st.columns([2, 1])

        with col1:

            search_query = st.text_input(
                "Search Pokemon",
                placeholder="Enter any Pokemon name..."
            ).lower().strip()

        with col2:

            selected_type = st.selectbox(
                "Filter by Type",
                [
                    "All", "Normal", "Fire", "Water",
                    "Electric", "Grass", "Ice", "Fighting",
                    "Poison", "Ground", "Flying", "Psychic",
                    "Bug", "Rock", "Ghost", "Dragon",
                    "Dark", "Steel", "Fairy"
                ]
            )

        # ---------------- FILTER BY NAME ----------------

        filtered_pokemon = [
            pokemon
            for pokemon in all_pokemon
            if search_query in pokemon["name"]
        ]

        # ---------------- FILTER BY TYPE ----------------

        if selected_type != "All":

            with st.spinner(
                f"Finding {selected_type} Pokemon..."
            ):

                type_data = fetch_pokemon_by_type(
                    selected_type
                )

            if type_data:

                type_pokemon_names = {
                    item["pokemon"]["name"]
                    for item in type_data["pokemon"]
                }

                filtered_pokemon = [
                    pokemon
                    for pokemon in filtered_pokemon
                    if pokemon["name"] in type_pokemon_names
                ]

            else:

                st.error("Unable to retrieve Pokemon type data.")
                filtered_pokemon = []

        st.divider()

        # ---------------- PAGINATION ----------------

        limit = 12

        total_count = len(filtered_pokemon)

        max_offset = (
            ((total_count - 1) // limit) * limit
            if total_count > 0 else 0
        )

        if "pokemon_offset" not in st.session_state:
            st.session_state.pokemon_offset = 0

        # Prevent invalid page after changing filters
        if st.session_state.pokemon_offset > max_offset:

            st.session_state.pokemon_offset = max_offset

        offset = st.session_state.pokemon_offset

        current_page = filtered_pokemon[
            offset:offset + limit
        ]

        total_pages = max(
            1,
            (total_count + limit - 1) // limit
        )

        st.write(
            f"Found **{total_count}** Pokemon"
        )

        st.caption(
            f"Page {offset // limit + 1} of {total_pages}"
        )

        # ---------------- DISPLAY POKEMON CARDS ----------------

        if current_page:

            columns = st.columns(3)

            for index, pokemon in enumerate(current_page):

                with columns[index % 3]:

                    details = fetch_pokemon(pokemon["name"])

                    if details:

                        with st.container(border=True):

                            image_url = (
                                details["sprites"]["other"]
                                ["official-artwork"]["front_default"]
                            )

                            if image_url:
                                st.image(
                                    image_url,
                                    width=180
                                )

                            st.subheader(
                                f"#{details['id']:03d} "
                                f"{details['name'].capitalize()}"
                            )

                            for item in details["types"]:

                                pokemon_type = item["type"]["name"]

                                color = TYPE_COLORS.get(
                                    pokemon_type,
                                    "#808080"
                                )

                                st.markdown(
                                    f"""
                                    <span style="
                                        background-color: {color};
                                        color: white;
                                        padding: 5px 12px;
                                        border-radius: 15px;
                                        margin-right: 5px;
                                        font-size: 12px;
                                        display: inline-block;
                                    ">
                                        {pokemon_type.capitalize()}
                                    </span>
                                    """,
                                    unsafe_allow_html=True
                                )

        else:

            st.warning("No Pokemon found matching your search and filters.")

        st.divider()

        # ---------------- PAGINATION BUTTONS ----------------

        col1, col2, col3 = st.columns([1, 2, 1])

        with col1:

            if st.button(
                "Previous",
                disabled=(offset == 0),
                use_container_width=True
            ):

                st.session_state.pokemon_offset = max(
                    0, offset - limit
                )

                st.rerun()

        with col2:

            st.write(
                f"Page {offset // limit + 1} / {total_pages}"
            )

        with col3:

            if st.button(
                "Next",
                disabled=(offset + limit >= total_count),
                use_container_width=True
            ):

                st.session_state.pokemon_offset = (
                    offset + limit
                )

                st.rerun()
