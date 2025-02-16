from typing import Dict

def view_playlist(playlist_song: Dict[str, Dict[str, str]]) -> None:
    """
    Prints out all the songs in the playlist in a readable format.
    """
    if not playlist_song:
        print("The playlist is empty.")
    else:
        for title, details in playlist_song.items():
            print(f"{title} Artist = {details['Artist']} Genre = {details['Genre']}")

def add_song(playlist_song: Dict[str, Dict[str, str]], title: str, artist: str, genre: str) -> None:
    """
    Adds a new song to the playlist.
    
    Parameters:
    playlist_song (Dict[str, Dict[str, str]]): The playlist dictionary.
    title (str): The title of the song.
    artist (str): The artist of the song.
    genre (str): The genre of the song.
    """
    if title in playlist_song:
        print(f"Song with title '{title}' already exists. Use update_song to modify it.")
    else:
        playlist_song[title] = {
            "Artist": artist,
            "Genre": genre
        }

def update_song(playlist_song: Dict[str, Dict[str, str]], title: str, artist: str, genre: str) -> None:
    """
    Updates an existing song in the playlist.
    
    Parameters:
    playlist_song (Dict[str, Dict[str, str]]): The playlist dictionary.
    title (str): The title of the song.
    artist (str): The artist of the song.
    genre (str): The genre of the song.
    """
    if title in playlist_song:
        playlist_song[title] = {
            "Artist": artist,
            "Genre": genre
        }
    else:
        print(f"Song with title '{title}' not found in the playlist. Use add_song to add it.")

def delete_song(playlist_song: Dict[str, Dict[str, str]], title: str) -> None:
    """
    Deletes a song from the playlist.
    
    Parameters:
    playlist_song (Dict[str, Dict[str, str]]): The playlist dictionary.
    title (str): The title of the song to delete.
    """
    if title in playlist_song:
        del playlist_song[title]
    else:
        print(f"Song with title '{title}' not found in the playlist.")

def initialize_playlist() -> Dict[str, Dict[str, str]]:
    """
    Initializes the playlist with some songs.
    
    Returns:
    Dict[str, Dict[str, str]]: The initialized playlist.
    """
    return {
        "Title 1": {
            "Artist": "1",
            "Genre": "2"
        },
        "Title 2": {
            "Artist": "1",
            "Genre": "2"
        },
        "Title 3": {
            "Artist": "1",
            "Genre": "2"
        },
        "Title 4": {
            "Artist": "1",
            "Genre": "2"
        }
    }

def main() -> None:
    playlist_song = initialize_playlist()

    # Example usage of the functions
    add_song(playlist_song, "Title 5", "Artist 5", "Genere 5")
    add_song(playlist_song, "Title 6", "Artist 6", "Artist 7")  # Incorrect genre, should be "Genre 7"
    add_song(playlist_song, "Title 4", "Artist 4", "Genere 4")

    view_playlist(playlist_song)
    update_song(playlist_song, "Title 1", "1", "2")
    view_playlist(playlist_song)
    delete_song(playlist_song, "Title 1")
    view_playlist(playlist_song)
    delete_song(playlist_song, "song")
    view_playlist(playlist_song)

if __name__ == "__main__":
    main()

