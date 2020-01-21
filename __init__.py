# number adding
from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG, getLogger

__author__ = 'pythona620/prasad'
LOGGER = getLogger(__name__)

class NumberAddingSkill(MycroftSkill):

# MyNameIs = input("Ask user for something")
# MyFriendNameIs = input("Ask user for something")

# str3 = MyNameIs+MyFriendNameIs
# c = MyNameIs +" "+"and"+" "+ MyFriendNameIs

	myname = str
	myfriendname = str
	
	def get_numerical_response(self, dialog):
		while True:
			val = self.get_response(dialog)
			try:
				val = str
				return val
			except ValueError:
				self.speak_dialog("invalid.input")
			except:
				self.speak_dialog("input.error")

	@intent_handler(IntentBuilder("").require("Adding").optionally("Play").optionally("Suggest"))
	def handle_start_game_intent(self, message):
		self.speak_dialog("start.game")

		# get myname
		myname = self.get_numerical_response("get.myname")
		# get myfriendname
		myfriendname = self.get_numerical_response("get.myfriendname")
		answer = myname + myfriendname
		# yip=str(answer)
		self.speak_dialog("add.two.numbers.is",{"answer":answer})
	def stop(self):		
		pass
def create_skill():
	return NumberAddingSkill()
