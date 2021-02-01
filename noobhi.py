import random
import sys

##Randomly pick noobhi title
def random_title():
    titles = ['Pottufier of the Mokkai', 'Causer of the Enrage', 'Fan of the Imaginary', 'Queen of the Dramas', 'Asaradhavan of the Idhukulam', 'Slut of the Cups', 'Flexus Maximus','Whore of the Disney Princesses', 'Thrower of Games', 'Owner of Big Brain', 'Talker of the Shit', 'Fantasy Winner of the UCL Fantasy', 'The Chuth of the Chith', 'Psychopathetic Specific Case Arguer', 'Cucker in the Sex', 'Sucker of the Android', 'Mate of the Soul of Giri', 'Tearer of the Shirts', 'Fucker of Roaches', 'Finisher of Civ Games', 'Area guy who is Ukram', 'The Jabaitee', 'Gui de Tur', 'Cunt-ellectual']
    n = random.SystemRandom()
    x = n.randint(0,len(titles))
    title = titles[x]
    return title