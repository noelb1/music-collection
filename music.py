class MusicCollection:
    def __init__(self):
        self.songs = []

    def add_song(self, title, artist):
        song = Song(title, artist)
        self.songs.append(song)

    def view_songs(self):
        for i,song in enumerate(self.songs):
            print(i+1, ":",song.title,"by",song.artist)

    def search_song(self, title):
        for song in self.songs:
            ifsong.title.lower() == title.lower():
                returnsong
        return None

    def delete_song(self, title):
        song = self.search_song(title)
        ifsong:
            self.songs.remove(song)
            print(f'{title} has been deleted from collection')
        else:
            print(f'{title} not found in collection')

    def update_song(self, title, new_title, new_artist):
        song = self.search_song(title)
        ifsong:
            song.title = new_title
            song.artist = new_artist
            print(f'{title} has been updated to {new_title} by {new_artist}')
        else:
            print(f'{title} not found in collection')
            
    def download_song(self, youtube_url, title, artist, save_path):
        yt = YouTube(youtube_url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        video_path = audio_stream.download()
        self.add_song(title, artist)
        print(f'{title} by {artist} has been downloaded and added to the collection')
        
        audio = AudioSegment.from_file(video_path)
        audio.export(f'{save_path}/{title}.mp3', format='mp3')
        print(f'{title} has been saved to {save_path}')

music_collection = MusicCollection()
youtube_url = 'https://www.youtube.com/watch?v=JGwWNGJdvx8'
save_path = 'path/to/save/folder'
music_collection.download_song(youtube_url, 'Shape of You', 'Ed Sheeran', save_path)
music_collection.view_songs()
