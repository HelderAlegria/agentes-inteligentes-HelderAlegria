import random

peliculas_por_genero = {
    "acción": [
        "Mad Max: Fury Road",
        "Die Hard",
        "John Wick",
        "The Dark Knight",
        "Avengers: Endgame"
    ],
    "comedia": [
        "Superbad",
        "The Hangover",
        "Groundhog Day",
        "Step Brothers",
        "Dumb and Dumber"
    ],
    "drama": [
        "The Shawshank Redemption",
        "Forrest Gump",
        "The Pursuit of Happyness",
        "A Beautiful Mind",
        "The Godfather"
    ],
    "terror": [
        "El conjuro",
        "A Nightmare on Elm Street",
        "It",
        "The Shining",
        "Hereditary"
    ],
    "ciencia ficción": [
        "EL señor de los anillos",
        "The Matrix",
        "Maze runner",
        "Harry Potter",
        "Interstellar"
    ],
    "romántica": [
        "The Notebook",
        "Titanic",
        "Pride and Prejudice",
        "La La Land",
        "Notting Hill"
    ]
}

def recomendar_pelicula():
    print("¡Hola! Soy tu agente de recomendaciones de películas.")
    print("Los géneros disponibles son: acción, comedia, drama, terror, ciencia ficción, romántica.")
    genero = input("¿Cuál es tu género favorito? ").lower().strip()

    if genero in peliculas_por_genero:
        pelicula = random.choice(peliculas_por_genero[genero])
        print(f"\n¡Te recomiendo ver: {pelicula}! Es una excelente película de {genero}.")
    else:
        print("\nLo siento, no tengo recomendaciones para ese género. Por favor, elige uno de los géneros disponibles.")

if __name__ == "__main__":
    recomendar_pelicula()
