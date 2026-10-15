# Music Playlist Manager 

class playlist:

    # STEP 1 - Parameterized constuctor: runs the moment the playlist is created 
    def __init__(self,name,genre):
        self.name = name
        self.genre = genre
        self.songs = []
        print(f"playlist '{self.name}' ({self.genre}) is ready")

    # STEP 2 - Add a song to the playlist
    def __int__(self, song):
        self.songs.append(song)
        print(f"'{song}' added to {self.name}.")

    # STEP 3 - Remove a song from the playlist
    def  remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"'{song}' removed.")
        else:
            print(f"'{song}' not found in the playlist.")

    # STEP 4 - Display all the songs
    def display(self):
        print("f\n--{self.name} ({self.genre}) ---")
        if self.songs:
            for i, song in enumerate(self.songs, 1):
                print(f"  {i}. {song}")
            else:
                print(" No songs yet. Add some!")

    # STEP 5 - Destructor: runs  automatically whenthe playlist is deleted 
    def __del__(self):
        print(f"Playlist '{self.name}' has been deleted. goodbye!")

# Object creation (constuctor fires here)
my_playlist = playlist("Road Trip Mix", "Pop")

#step 6 - Menu-drive program using the playlist class 
while True:
    print("\nl. Add song 2. Remove song 3. view playlist 4. Delete & Quit")
    choice = input("Enter your choices: ")

    if choice == "1":
        song = input("Enter song name: ")
        my_playlist.add_song(song)
    elif choice == "2":
        song = input("Enter song to remove:")
        my_playlist.remove_song(song)
    elif choice == "3":
            my_playlist.displayed()
    elif choice == "4":
         del my_playlist   #destuctor fires here
         break
    else:
        print("Invalid Choice. Enter 1, 2, 3, or 4")        