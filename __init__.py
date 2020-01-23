# names adding
from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG, getLogger

__author__ = 'pythona620/prasad'
LOGGER = getLogger(__name__)

class NameAddingSkill(MycroftSkill):
#python code
# MyNameIs = input("Ask user for something")
# MyFriendNameIs = input("Ask user for something")

# str3 = MyNameIs+MyFriendNameIs
# c = MyNameIs +" "+"and"+" "+ MyFriendNameIs
	def get_names(self, dialog):  #get input from mic
		yip = self.get_response(dialog) 
		return yip
		
	@intent_handler(IntentBuilder("").require("funny").optionally("Play").optionally("Suggest"))
	def handle_start_game_intent(self, message):
		self.speak_dialog("start.game")

		# get myname
		myname = self.get_names("get.myname")
		# get myfriendname
		myfriendname = self.get_names("get.myfriendname")
		answer = myname + myfriendname #adding names

		self.speak_dialog("friends",{"answer":answer}) #output
	def stop(self):		
		pass
def create_skill():
	return NameAddingSkill()
