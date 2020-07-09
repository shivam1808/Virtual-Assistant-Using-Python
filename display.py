import os
import random

def change_wallpaper():

	wallpaper_path = '/home/shivam-gupta/Pictures/Wallpapers'
	wallpapers = os.listdir(wallpaper_path)

	#os.system("export GIO_EXTRA_MODULES=/usr/lib/x86_64-linux-gnu/gio/modules/")

	wallpaper = random.choice(wallpapers)

	command = 'export GIO_EXTRA_MODULES=/usr/lib/x86_64-linux-gnu/gio/modules/'+'\n'+'gsettings set org.gnome.desktop.background picture-uri file:///'+wallpaper_path+"/"+wallpaper
	os.system(command)

	return "Wallpaper changed"


