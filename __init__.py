from mycroft import MycroftSkill, intent_file_handler
class Count(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
    @intent_file_handler('funny.intent')
    def handle_count(self, dialog):
        self.speak_dialog(""start.game"")
        
            name1 = str(self.get("dialog"))
            name2 = str(self.get("dialog"))
            
    
            add = name1+name2
            
            print (add)
           
            answer = str(add)
            answer = add['text']
            self.speak_dialog("friends",{answer})
    def stop(self):     
        pass
def create_skill():
    return Count()  
