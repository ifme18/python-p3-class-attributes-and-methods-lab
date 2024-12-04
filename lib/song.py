class Song:

    count = 0
    genre=[]
    artist=[]
    genre_count={}
    artist_count={}
    song_count={}
   
    

    def __init__(self, name, artist, genre):
        self.artist_count()
        self.add_artist()
        self.add_genres(genre)
        self.name= name
        self.artist=artist
        self.genre=genre
        self.genre_count(genre)
        self.artist_count(artist)



    
        pass
    @classmethod
    def add_genres(cls,genre):
        if genre not in cls.genre:
            cls.genre.append(genre)
        return cls.genre
    @classmethod
    def add_artist(cls,artist):
        if artist not in cls.artist:
            cls.artist.append(artist)
        return cls.artist    

    @classmethod
    def artist_count(cls , artist):
        if artist in cls.artist_count:
            cls.artist_count[artist]+=1
        else:
            cls.artist_count[artist]=1
        return cls.artist_count
        #cls.artist_count+=increment
    
    @classmethod

    def genre_count(cls,genre):
        if genre in cls.genre_count:
            cls.genre_count[genre]+=1
        else:
            cls.genre_count[genre]=1
        return cls.genre_count

    @classmethod    
    def song_count(cls ,increment=1):
        cls.count+=increment
    



   
