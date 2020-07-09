import os 
import assistant_details as ad
import file_search


music_path = "/home/shivam-gupta/Music/"



def play_music():

	if ad.is_ubuntu():
		os.system("rhythmbox-client --play")
		return "Playing Music"

	else:
		return "For windows its not available"


def pause_music():
	
	if ad.is_ubuntu():
		os.system("rhythmbox-client --pause")
		return "Music Paused"

	else:
		return "For windows its not available"


def stop_music():
	
	if ad.is_ubuntu():
		os.system("rhythmbox-client --stop")
		return "Music Stoped"

	else:
		return "For windows its not available"

def next_song():
	
	if ad.is_ubuntu():
		os.system("rhythmbox-client --next")
		return "Playing Next Song"

	else:
		return "For windows its not available"

def previous_song():
	
	if ad.is_ubuntu():
		os.system("rhythmbox-client --previous")
		return "Playing Previous Song"

	else:
		return "For windows its not available"

def play_specific_song(song_name):

	song_name = song_name.replace('play', '')

	if ad.is_ubuntu():

		file_search.set_root(music_path)
		songs = file_search.searchFile(song_name)
		try:
			song_uri = songs[0]
			command = 'rhythmbox-client --play-uri="' + song_uri + '"'
			os.system(command)
			return "Playing " + song_name
		except:
			return ("Song not found in your computer")

	else:
		return "For windows its not available yet"