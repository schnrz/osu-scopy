# osu-scopy
Short script to copy songs from osu! folders

This script will take mp3s files inside osu! `Songs` structured folders and copy them into another given folder path.


### Notes~
Run the script via python console~! 

The process may take several minutes depending on disk's speeds while copying and the amount of songs.
It renames .mp3 files it takes while running so you may notice changes made inside the game, might recommend to use f5 when entering game to refresh maps list and check everything's in order (it should tho).
~~testing took around 30 mins, did this while bored w~~


#### Folders
- `dst` is the folder the files will be copied to
- `songs` Songs folder inside the osu! one, path must end in *'osu!/Songs'*

_Please keep in mind repeated song name files will be added a number before the .mp3 extension to save them._


#### Files
- **osu!scopy.py** main script, ~~may update sometime idk~~
- **osu!scopy_old.py** deprecated script, saved for log purposes
