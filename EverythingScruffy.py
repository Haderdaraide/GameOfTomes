import time
import random



def currentHunger(scruffyHunger):
    print ""
    print "Scruffy's current hunger is: " + str(scruffyHunger)
    print ""


def scruffyDesires():
    print ""
    urgesList = {"apples": "Scruffy looks like he wants something round and juicy!",
                     "carrots": "Scruffy looks like he wants something orange and crunchy!",
                     "lettuce": "Scruffy looks like he wants something green and leafy!",
                     "water": "Scruffy looks thirsty!"}

    randomKey = random.choice(urgesList.keys())
    randomSentence = urgesList[randomKey]

    return (randomKey, randomSentence)

def rubHisBelly():
    correctInputFlag = False
    while not correctInputFlag:
        rubRequest = raw_input("rub Scruffy's belly Y/N? ")
        if rubRequest == "Y":
            correctInputFlag = True
            print ""
            print "You give Scruffy a good olll belly rubbb..."
            time.sleep(1)
            print "He seems to love it!"
        elif rubRequest == "N":
            print ""
            print "He looks sad, but jumps up and looks up at you."
            time.sleep(2)
        else:
            print ""
            print "That wasn't a correct command, please type exactly what you see"
            print ""

def takeScruffyWithYou():
    correctInputFlag = False
    while not correctInputFlag:
        takeScruffyRequest = raw_input("Take Scruffy as your new puppy Y/N? ")
        if takeScruffyRequest == "Y":
            correctInputFlag = True
            print ""
            print "You pick Scruffy up (he got smaller after the fight)"
            time.sleep(1)
            print ""
            print "You ask Scruffy if he wants to tag along?"
            time.sleep(2)
            print "Scruffy, overjoyed, jumps out of your arms, only to tackle you onto the floor"
            print "He begins to aggressively lick your face! He can't contain his excitement!!"
            time.sleep(2)
            print ""
            print "!ACQUIRED SCRUFFY!"
            print ""
            time.sleep(1)
            print "You grab a bag of fresh veggies just in case..."
        elif takeScruffyRequest == "N":
            correctInputFlag = True
            print ""
            print "You look at Scruffy, then all the wounds and scabs you got from diving in that garden."
            print ""
            time.sleep(2)
            print "You wave a meaningless goodbye to the dog, and you turn around to leave.."
        else:
            print "That wasn't a correct command, please type exactly what you see."
