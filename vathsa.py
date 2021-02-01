import random

##Bilal Imports
import bilalUtil as bu

##Make vathsa rain money randomly
def rainMoney():
    if random.SystemRandom().randint(0,20) == 5:
        text = ""
        for i in range(0,random.SystemRandom().randint(1,10)):
            if bu.trueOrFalse():
                text += "\N{money-mouth face}"
    return text