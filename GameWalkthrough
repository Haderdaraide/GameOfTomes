import time
import random

name = ""
scruffyExists = False

def enterHouseTwoPrompt():
    """
    Approaching the house, user is prompted to enter or not - if they do not, GAME OVER!
    """

    print "\nYou and the Tomb King drive for hours..."
    time.sleep(1)
    print "You finally arrive to a big, dark and degrading home..."
    time.sleep(3)
    print "\nTome King: ... "
    print "Tome King: I never wanted to come back here... welcome to my childhood home."
    time.sleep(3)
    print "You and the Tome King get out of the car and approach the home\n"
    time.sleep(2)

    acceptableAnswerFlag = False
    while not acceptableAnswerFlag:
        enterHome = raw_input("Alright, " + name + ", here we go. Want to go in Y/N? ")

        if enterHome == "Y":
            houseTwoIntro()
            acceptableAnswerFlag = True
        elif enterHome == "N":
            print "User doesn't want to go in ---- GAME OVER"
            acceptableAnswerFlag = True
            return
        else:
            print "\nthat wasn't a correct response, please provide Y (yes) or N (no)\n"



def houseTwoIntro():
    """
    Intro for the second house, user is prompted to inquire about a picture of a girl they step on
    """

    print "\nYou enter a ragged and destroyed home"
    print "couches flipped over"
    print "TV smashed in"
    time.sleep(4)
    print "\nnothing is salvageable here...\n"
    time.sleep(3)
    print "You step on a picture of a girl, smiling, and she looks happy holding a diploma\n"
    time.sleep(3)

    acceptableAnswerFlag = False
    while not acceptableAnswerFlag:

        whoIsThisGirlPrompt = raw_input("Ask the Tomb King who is this girl Y/N? ")
        if whoIsThisGirlPrompt == "Y":
            sisterText()
        if whoIsThisGirlPrompt == "N":
            print "\n You decide not to ask who this girl is.\n"
            print "You assume she may be some family member or a friend, but you can't be sure.\n"
        else:
            print "\nthat wasn't a correct response, please provide Y (yes) or N (no)\n"

def sisterText():
    """
    Text conversation about Helga (Tome King's sister) the picture user steps on and inquires about
    """

    time.sleep(2)
    print "\nthe Tome King begins to tear up as he holds the picture."
    time.sleep(2)
    print "Tome King: This is Helga, she was brilliant with the sweetest heart."
    time.sleep(4)
    print name + "..."
    time.sleep(2)
    print "She was my sister..."
    time.sleep(4)
    print "There was none that could match her in the realm of sciences, earth, the elements, chemistry, farming..."
    time.sleep(4)
    print "It all came naturally to her..she was a top graduate at the university of knowledge"
    time.sleep(4)
    print "\nThere was an accident, she tried to create the perfect specimen. - a specimen of perfect health!\n"
    time.sleep(4)
    print "She built a garden, one that rapidly grows food, but she created a monster....\n"
    time.sleep(2)
    print "poor Scruffy..."
    time.sleep(2)

def gardenSetUp():
    """
    Intro to the garden scene, Tome King explains the garden to user
    """

    time.sleep(2)
    print "\n\nAs you walk out, you see a MASSIVE garden."
    print "You see big bags of different seeds and a massive well in the middle"
    time.sleep(5)
    print "You pick up a random seed from a bag and toss it far into the garden"
    time.sleep(5)
    print "the ground rumbles, eventually shaking as if it's an earthquake!!"
    time.sleep(5)
    print "You look to your thrown seed, and within seconds, a bright orange carrot popped up! Ready to be harvested!"
    time.sleep(5)
    print "Tome King: This is my sister's garden, where she spent most of her studies"
    time.sleep(5)
    print "Tome King: It groves food in seconds, and the science behind is fasci...\n"
    time.sleep(4)
    print "ROOOOOOOOOAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAARRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR\n"
    time.sleep(4)
    print "Tome King: Oh NO! SCRUFFY!!!!!"
    time.sleep(3)
    print "My sister's beloved dogs! The one she tested, and trained to obsess with health and prolonged life!!!!"
    time.sleep(3)
    print "\nScruffy jumps in the middle of the garden, roars again, he looks hungry and FURIOUS!!!\n"
    time.sleep(4)
    print "Tome King: QUICKLY! WE MUST FEED HIM!!!"
    time.sleep(4)
    print "\nTome King: GRAB THOSE SEEDS, LET'S GET PLANTING!"

def gardenGamePlayPrompt():
    """
    User is prompted to play the garden game - respond with either Y (yes) or N (no)
    """
    acceptableAnswer = False

    while not acceptableAnswer:
        gameInit = raw_input("Play garden survival to satisfy the dog's health cravings? Y/N? ")
        if gameInit == "Y":
            return gameInit
        if gameInit == "N":
            return gameInit
        else:
            print "\n that wasn't a correct response, please provide Y (yes) or N (no)\n"


def gardenGameExitText():
    """
    Once the user beats the game, this exit text is providing ending the sequence
    """

    print "\nWith all of your effort, Scruffy rolls on his side, sated and happily drifts to sleep....."
    time.sleep(4)
    print "Tome King: " + name + ", that. was. spectacular."
    time.sleep(4)
    print "Tome King: You were running, and diving, and tossing seeds like a hero!"
    time.sleep(4)
    print "\nTome King: Well, I guess you should know..especially because I made you come all the way out here.\n"
    time.sleep(4)
    print "Tome King: We grew up together here..."
    time.sleep(2)
    print "Tome King kicks a rock while staring at the ground"
    time.sleep(4)
    print "\nTome King: I am not just talking about Helga and me.\n"
    time.sleep(4)
    print "Tome King: Mr can't read good..\n"
    time.sleep(4)
    print "Tome King: He's our brother."
    time.sleep(5)
    print "..."
    time.sleep(1)
    print "Tome King: He never was the brightest, but man oh man was he strong."
    time.sleep(4)
    print "\nTome King: Why did you have to do it... why... Helga just wanted to help....it's why she studied....\n"
    time.sleep(4)
    print "Tome King: Alright " + name + " I don't want to distract us from the plan."
    time.sleep(3)
    print "\nWe must get that tome back!"
    time.sleep(4)
    print "Let's head back to the minivan, I am sure I know where to find him now...\n"
    time.sleep(3)


def scruffyBecomesYourPuppyOrNot():
    """
    Scruffy returns, and user is prompted to take Scruffy as their new puppy or not!
    """

    print "As you and the Tome King start to head out of the home, you hear a familiar ruffle behind you\n"
    time.sleep(4)
    print "You both turn around and...it's Scruffy!!!!\n"
    time.sleep(4)
    print "Tome King: You HAVE to be kidding me, as he gets into some odd fighting stance!\n"
    time.sleep(4)
    print "Scruffy roles over, and looks like.. he looks like..."
    time.sleep(1)
    print "he wants a belly rub?"
    time.sleep(3)
    rubHisBelly()
    print "Now what is this??"
    time.sleep(3)
    print "Scruffy looks like he wants to come with you!!\n"
    time.sleep(4)
    takeScruffyWithYou()



#The game below...



    #Game Functions

def userChoicePrompt():
    """
    User is prompted to either plant a new crop or throw something at Scruffy to sate his hunger
    """

    acceptableAnswerFlag = False
    while not acceptableAnswerFlag:
        print "\nWhat would you like to do? plant or throw"
        userChoice = raw_input("Type your choice: ")
        if userChoice == "plant":
            return userChoice
        if userChoice == "throw":
            return userChoice
        else:
            print "\nthat wasn't a correct response, please type either plant or throw\n"


    #Core user choices

def plant():
    """
    User is prompted for what they would like to plant in the garden
    """

    print ""
    correctItems = ["apples", "carrots", "lettuce"]
    acceptableAnswer = False
    while not acceptableAnswer:
        plantCrop = raw_input("What would you like to plant? apples, carrots, or lettuce:  ")
        if plantCrop in correctItems:
            acceptableAnswer = True
        else:
            print "\nIncorrect input, please type exactly what you see out of the options\n"
    return plantCrop

def throw(bag):
    """
    User is prompted for what they would like to throw at Scruffy
    """

    print ""
    acceptableChoices = ["apples", "carrots", "lettuce", "water"]
    acceptedChoice = False
    while not acceptedChoice:
        throwAtScruffy = raw_input("What would you like to throw at Scruffy? apples, carrots, lettuce or water: ")

        if throwAtScruffy in acceptableChoices:
            if throwAtScruffy == "water":
                acceptedChoice = True
            elif bag[throwAtScruffy] > 0 or bag[throwAtScruffy] == "unlimited":
                acceptedChoice = True
            else:
                print "\nYou don't have enough " + throwAtScruffy + " in your bag to throw that!"
        else:
            print "\nThat wasn't a correct command, please type exactly what you see in the options provided\n"
    return throwAtScruffy


    #Function helpers

def plantDecision(newPlant):
    """
    Based on what user inputs for plant function, they will be provided with text about what happens from the decision
    """

    if newPlant == "apples":
        print "\nYou run to the bag and toss an apple seed into the garden!"
        time.sleep(1)
        print "Out pops an apple - you add it to the bag!\n"
        time.sleep(2)
    if newPlant == "lettuce":
        print "\nYou run to the bag and toss a lettuce seed into the garden!"
        time.sleep(1)
        print "Out pops a head of lettuce - you add it to the bag!\n"
        time.sleep(2)
    if newPlant == "carrots":
        print "\nYou run to the bag and toss a carrot seed into the garden!"
        time.sleep(1)
        print "Out pops a big orange carrot - you add it to the bag!\n"
    time.sleep(2)

def throwDecision(itemThrown):
    """
    Based on what user inputs for throw function, they will be provided with text about what happens from the decision
    """

    if itemThrown == "apples":
        print "\nYou wind up, and toss an apple at Scruffy!"
        time.sleep(3)
        print "He happily munches on the apple, wagging his tail\n"
    if itemThrown == "carrots":
        print "\nYou wind up, and toss a carrot at Scruffy!"
        time.sleep(3)
        print "He happily munches on the carrot, wagging his tail\n"
    if itemThrown == "lettuce":
        print "\nYou wind up, and toss a head of lettuce at Scruffy!"
        time.sleep(3)
        print "He happily munches on the lettuce, wagging his tail\n"
    if itemThrown == "water":
        print "\nYou run to the well and fill up a bucket near by. You leave it for Scruffy!"
        time.sleep(3)
        print "He happily laps up the water in the bucket, wagging his tail\n"
    time.sleep(3)

def helgasSpecialSeed():
    """
    Helga's special seed, a random generator
    if 1 is rolled, the function returns True (signaling extra crops were grown (3))
    else - returns false, no extra crops, user gets normal amount (1)
    """

    randomNum = random.randint(1, 3)
    if randomNum == 1:
        return True
    else:
        return False




    #Everything scruffy related

def currentHunger(scruffyHunger):
    """
    Scruffy's current hunger is printed
    """

    print "\nScruffy's current hunger is: " + str(scruffyHunger)
    print ""


def scruffyDesires():
    """
    User is told what Scruffy's current hunger is.
    returns a tuple
    tuple[1] = desire code word
    tupl[2] = desire description (presented to user)
    """

    print ""
    urgesList = {"apples": "Scruffy looks like he wants something round and juicy!",
                     "carrots": "Scruffy looks like he wants something orange and crunchy!",
                     "lettuce": "Scruffy looks like he wants something green and leafy!",
                     "water": "Scruffy looks thirsty!"}

    randomKey = random.choice(urgesList.keys())
    randomSentence = urgesList[randomKey]

    return (randomKey, randomSentence)

def rubHisBelly():
    """
    User is prompted to rub Scruffy's belly, building initial relationship
    """

    acceptableAnswerFlag = False
    while not acceptableAnswerFlag:
        rubRequest = raw_input("rub Scruffy's belly Y/N? ")
        if rubRequest == "Y":
            acceptableAnswerFlag = True
            print "\nYou give Scruffy a good olll belly rubbb..."
            time.sleep(1)
            print "He seems to love it!\n"
            time.sleep(2)
        elif rubRequest == "N":
            acceptableAnswerFlag = True
            print "\nHe looks sad, but jumps up and looks up at you."
            time.sleep(2)
            print "\nhe is kind of cute...\n"
            time.sleep(2)
        else:
            print "\nThat wasn't a correct command, please type exactly what you see\n"

def takeScruffyWithYou():
    """
    User is prompted if they want to take Scruffy along with them..he was just hungry..
    """

    global scruffyExists
    acceptableAnswerFlag = False
    while not acceptableAnswerFlag:
        takeScruffyRequest = raw_input("Take Scruffy as your new puppy Y/N? ")

        if takeScruffyRequest == "Y":
            acceptableAnswerFlag = True
            print "\nYou pick Scruffy up (he got smaller after the fight)"
            time.sleep(4)
            print "\nYou ask Scruffy if he wants to tag along?\n"
            time.sleep(3)
            print "Scruffy, overjoyed, jumps out of your arms, only to tackle you onto the floor"
            print "He begins to aggressively lick your face! He can't contain his excitement!!"
            time.sleep(5)
            print "\n!ACQUIRED SCRUFFY!\n"
            time.sleep(3)
            print "You grab a bag of fresh veggies just in case...\n"
            scruffyExists = True
        elif takeScruffyRequest == "N":
            acceptableAnswerFlag = True
            print "\nYou look at Scruffy, then all the wounds and scabs you got from diving in that garden.\n"
            time.sleep(2)
            print "You wave a meaningless goodbye to the dog, and you turn around to leave.."
        else:
            print "\nThat wasn't a correct command, please type exactly what you see.\n"




    #Everything bag related

def updateBag(bag, newPlant, updateKeyWord, helgaSeed):
    """
    Updates the bag for the user.
    takes in the bag dictionary
    thePlant that was planted or thrown
    updateKeyWord for adding or subtracting from the bag
    helgaSeed bool if it was a lucky seed or not (adding 3 instead of 1 to the bag)
    """

    if updateKeyWord == "add":
        if helgaSeed == True:
            bag[newPlant] = bag[newPlant] +3
        else:
            bag[newPlant] = bag[newPlant] + 1
    if updateKeyWord == "minus":
        bag[newPlant] = bag[newPlant] - 1

def showBag(bag):
    """
    Prints the bag for the user
    """

    print "\nHere is what's in your bag:"
    for key in bag.keys():
        print key + " " + str(bag[key])



    #Full intro

def houseTwoFullIntro():
    """
    The intro for entering the house, and setting up the garden
    """

    enterHouseTwoPrompt()
    gardenSetUp()



    #Actual Game

def main():
    """
    Garden Escape game function (housing all helper functions)
    """

    houseTwoFullIntro()
    bag = {"apples": 0,
           "carrots": 0,
           "lettuce": 0,
           "water": "unlimited"
           }

    scruffyHunger = 100

    while scruffyHunger > 0:
        currentHunger(scruffyHunger)
        scruffyDesire = scruffyDesires()
        print scruffyDesire[1]
        showBag(bag)

        promptUserForChoice = userChoicePrompt()
        helgasSeedBool = helgasSpecialSeed()

        if promptUserForChoice == "plant":
            newPlant = plant()
            plantDecision(newPlant)
            if helgasSeedBool == True:
                print "That was one of Helga's special seeds!!! 3 crops grew instead of 1!!! You add the two additional to your bag!"
                time.sleep(5)

            updateBag(bag, newPlant, "add", helgasSeedBool)
            scruffyHunger += 10

        elif promptUserForChoice == "throw":
            itemThrown = throw(bag)
            throwDecision(itemThrown)
            if itemThrown == "water":
                pass
            elif itemThrown == "throw nothing":
                scruffyHunger += 10
            else:
                updateBag(bag, itemThrown, "minus", helgasSeedBool)
            if scruffyDesire[0] == itemThrown:
                scruffyHunger -= 20
            else:
                print "Scruffy enjoyed that, but it wasn't what he desired! It only made him hungrier!!"
                scruffyHunger += 10
                time.sleep(4)

        else:
            print "You typed in an incorrect input, please type exactly what is shown in your choices"

    print "Scruffy finally calms down!!!\n"
    gardenGameExitText()
    scruffyBecomesYourPuppyOrNot()

main()
