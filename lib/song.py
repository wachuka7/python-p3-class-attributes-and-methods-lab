class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.__class__.add_song_to_count()
        self.add_to_genres()
        self.add_to_artists()
        self.add_to_genre_count()
        self.add_to_artist_count()

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    def add_to_genres(self):
        if self.genre not in self.__class__.genres:
            self.__class__.genres.append(self.genre)

    def add_to_artists(self):
        if self.artist not in self.__class__.artists:
            self.__class__.artists.append(self.artist)

    def add_to_genre_count(self):
        if self.genre not in self.__class__.genre_count:
            self.__class__.genre_count[self.genre] = 1
        else:
            self.__class__.genre_count[self.genre] += 1

    def add_to_artist_count(self):
        if self.artist not in self.__class__.artist_count:
            self.__class__.artist_count[self.artist] = 1
        else:
            self.__class__.artist_count[self.artist] += 1
