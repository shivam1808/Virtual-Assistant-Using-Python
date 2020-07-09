from time_details import get_time, get_date
from database import *
from input_module import take_input
from output_module import output
from internet import check_internet_connection, check_on_wikipedia
import assistant_details
from music import *

from web import open_facebook, open_google, close_browser
from display import change_wallpaper
from news import get_news


def  process(query):


	if 'play' in query and 'music' not in query:
		answer = get_answer_from_memory("play")
	else:
		answer = get_answer_from_memory(query)

	if answer == "get time details":
		return ('Time is '+ get_time())

	elif answer == "change name":
		output("Okay! what do u want to call me")
		temp = take_input()
		if temp == assistant_details.name:
			return "Can't change. I think you are happy with my old name"
		else:
			update_name(temp)
			assistant_details.name = temp
			return "Now you can call me " + temp

	elif answer == "tell date":
		return "Date is " + get_date()

	elif answer == "on speak":
		return turn_on_speech()

	elif answer == "off speak":
		return turn_off_speech()

	elif answer == "open facebook":
		open_facebook()
		return "opening facebook"

	elif answer == "open google":
		open_google()
		return "opening google"

	elif answer == "close browser":
		close_browser()
		return "closing browser"

	elif answer == "check internet connection":
		if check_internet_connection():
			return "Internet is Connected"
		else:
			return "Internet Not Connected"

	elif answer == "play music":
		return play_music()

	elif answer == "pause music":
		return pause_music()

	elif answer == "stop music":
		return stop_music()

	elif answer == "next song":
		return next_song()

	elif answer == "previous song":
		return previous_song()

	elif answer == "play":
		return play_specific_song(query)

	elif answer == "change wallpaper":
		return change_wallpaper()

	elif answer == "get news":
		return get_news()

	else:

		output("Dont know this one should i search on internet?")
		ans = take_input()
		if "yes" in ans:
			answer = check_on_wikipedia(query)
			if answer != "":
				return answer
		else:

			output("Can you please tell me what it means?")
			ans = take_input()
			if "it means" in ans:
				ans = ans.replace("it means", "")
				ans = ans.strip()

				value = get_answer_from_memory(ans)

				if value == "":
					return "Can't help with this one"

				else:
					insert_question_and_answer(query, value)
					return "Thanks, I will remember it for the next time"

			else:
				return "Can't help with this one"

		return "Nothing"