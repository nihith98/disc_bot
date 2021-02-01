import random

##Randomly Returns True or False
def trueOrFalse():
    n = random.SystemRandom()
    if n.randint(0,1) == 0:
        return False
    else:
        return True

