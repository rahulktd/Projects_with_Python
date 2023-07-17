import lyricsgenius

api_key = "****************************************************************"

x = lyricsgenius.Genius(api_key)
first_line = input("Name: ")
lyrics_search = x.search_song(first_line)

if lyrics_search:
    print(lyrics_search.lyrics)
else:
    print("Lyrics not found for the specified song.")