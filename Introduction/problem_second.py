# Install an external module and use it
import pyttsx3
engine = pyttsx3.init()
engine.say("This is a demo text to see how the pyttsx3 text to speech works")
engine.runAndWait()