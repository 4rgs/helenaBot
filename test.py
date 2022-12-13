# importing the pyttsx library
import pyttsx3
  
# initialisation
engine = pyttsx3.init()
  
# testing
engine.say("My first code on text-to-speech")
engine.say("Thank you, Geeksforgeeks")
engine.runAndWait()
