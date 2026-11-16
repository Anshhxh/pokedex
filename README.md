# ⚡ Pokédex — Pokémon Explorer

A Python-based Pokémon exploration application built using **Streamlit** and the **PokéAPI**.

Search, explore and discover Pokémon through an interactive web interface.

## Features

- **Pokémon Search:** Search Pokémon by name or Pokédex ID.
- **Pokémon Collection:** Browse the Pokémon collection.
- **Global Search:** Search across the available Pokémon collection.
- **Type Filtering:** Filter Pokémon by their types.
- **Pokémon Details:** View artwork, height, weight, abilities and base statistics.
- **Type-based Colours:** Visually distinguish Pokémon types.
- **Pagination:** Browse Pokémon in manageable batches.
- **API Caching:** Reduce repeated API requests using Streamlit caching.

## Technologies Used

- Python
- Streamlit
- Requests
- PokéAPI
- Git and GitHub

## Installation and Setup

1. Clone the repository:

   ```bash
   git clone YOUR_REPOSITORY_URL
   ```

2. Navigate to the project directory:

   ```bash
   cd Pokedex
   ```

3. Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

4. Activate the virtual environment (Windows):

   ```powershell
   .venv\Scripts\Activate.ps1
   ```

5. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Run the application:

   ```bash
   streamlit run app.py
   ```

## API Reference

This project uses [PokéAPI](https://pokeapi.co/), a free and open Pokémon API.

No API key is required.

## Project Structure

```text
Pokedex/
│
├── app.py
├── main.py
├── pokemon.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Future Improvements

- Pokémon evolution explorer
- Pokémon comparison
- Improved UI and responsive design
- Additional Pokémon information

## Acknowledgements

- [PokéAPI](https://pokeapi.co/) for providing Pokémon data.
- [Streamlit](https://streamlit.io/) for the Python web application framework.

---

Built as my first Python API integration project.
