import time
import random

global name
global scruffyExists
name = ""
scruffyExists = False


#Initialize and Walkthrough functions

def start():
    """
    Game init!
    """

    intro()
    acceptableAnswerFlag = False
    while not acceptableAnswerFlag:
        getStarted = raw_input("\nTome King: Hey! You look able bodied and eager to learn, wan't to help me find it? Y/N? ")
        if getStarted == "Y":
            acceptableAnswerFlag = True
            storyWalkThrough()
        if getStarted =="N":
            acceptableAnswerFlag = True
            print "Tome King: ok then..."
            userQuits()
            return
        else:
            print "\nthat wasn't a correct response, please type either Y (yes) or N (no)\n"
            time.sleep(3)


def storyWalkThrough():
    """
    The 'main' function walking through each part of the story
    """
    #Get the user's name
    userProvidesTheirName()
    time.sleep(3)

    #Get in minivan prompt
    hopInCar = getInMinivan()
    if hopInCar == "N":
        userQuits()
        return 0
    time.sleep(2)

    #Entering his home sequence
    enterHomePrompt = enterHouseOnePrompt()
    if enterHomePrompt == "Y":
        houseOneIntro()
    if enterHomePrompt == "N":
        userQuits()
        return()

    #play math game
    gameRequest = raw_input("Play a game of math wits with Mr Abacus? If you say no, the Time King dies, and it's game over Y/N? ")
    if gameRequest == "Y":
        AdditionProblems()
    else:
        print "fine, let the Tome King die..."
        userQuits()
        return

    #house exit conversation
    houseOneComplete()

    #get back in car to next destination
    hopInCar = getInMinivan()
    if hopInCar == "N":
        userQuits()
        return



#Story text helper functions

    #Game Intro

def intro():
    """
    Game Intro! Welcome to the game of tomes!
    """

    print '\nOh, Hello There! Welcome to THE GAME OF TOMES!\n'
    time.sleep(3)
    print "My name is Sir. Reads Too Much."
    time.sleep(2)
    print "Most people call me - the Tome King\n"
    time.sleep(3)
    print "Tome King: I have been studying all my life, and I have compiled everything I know in THE GOLDEN TOME!"
    time.sleep(3)
    print "Tome King: but...I lost it..got home from a night out, blacked out, woke up, no tome"
    time.sleep(5)
    print "Tome King: I bet it was that scoundrel, Mr. can't read good...jealous.."
    time.sleep(3)


    #FIRST HOUSE enterHouseOnePrompt/houseOneIntro/houseOneComplete 3 functions

def enterHouseOnePrompt():
    """
    You approach the home, Tome King prompts you to enter. if user quits, game over.
    """

    print "Tome King: Alright, we made it to his home, I don't see any car parked. Maybe he's gone?"
    time.sleep(3)
    goInsideHouse = raw_input("Tome King: Want to break in? remember it's ok, we are hunting for knowledge Y/N? ")
    if goInsideHouse == "Y":
        return goInsideHouse
    if goInsideHouse == "N":
        print "Tome King: You are weak, I am finding someone else. *shoves you out of the minivan*"
        time.sleep(2)

    return goInsideHouse


def houseOneIntro():
    """
    Approaching the firsty house intro, encounter Mr. Abacus - user prompted to play Math Game
    escape
    """

    print "\nYou and the Tome King, get out the car and approach the door"
    time.sleep(4)
    print "Tome King: Wait a minute.. something doesn't feel right..."
    time.sleep(4)
    print "Tome King kicks down the door, and yells - " + name + " follow me, QUICKLY!"
    time.sleep(4)
    print "Tome King: Oh no! It can't be!!!\n"
    time.sleep(4)
    print "you both walk into the living room, and it's trashed, standing over a flipped sofa is a haggard looking man, he peers at you through thick rimmed glasses"
    time.sleep(5)
    print "Tome King: Mr. Abacus, what.. what are you doing here?!?"
    time.sleep(4)
    print "\nYou ask Tome King quickly who this man is\n"
    time.sleep(4)
    print "He doesn't notice you saying anything\n"
    time.sleep(3)
    print "\nMr. Abacus: I taught you, Tome King, I taught you the world of math.\n"
    time.sleep(4)
    print "MR Abacus: But I could never progress further then math! I want to learn to write, to sing! That knowledge always escaped me!"
    time.sleep(4)
    print "Mr Abacus: Now I know that Mr can't read good stole the TOME! IT WILL BE MIIINNNEEEEE\n"
    time.sleep(5)
    print "Mr Abacus has taken control of the house! The doors lock mysteriously, and the Tome King falls to the floor in pain\n"
    time.sleep(4)
    print "Mr Abacus: YOU CAN ONLY ESCAPE IF YOU BEAT ME IN A GAME OF MATH WITS!!!!!!!!"


def houseOneComplete():
    """
    you have defeated Mr. Abacus, and you leave the home (exit conversation)
    """

    print "Tome King: Phew, I don't know what happen..I passed out..\n"
    time.sleep(2)
    print "Tome King: Where is Mr. Abacus??\n"
    time.sleep(2)
    print "you look at Tome King, and at the space Mr Abacus stood."
    time.sleep(3)
    print "you let Tome King know that you handled it\n"
    time.sleep(2)
    print "with a huge grin, Tome King says"
    time.sleep(2)
    print "Tome King: " + name + "!" + " That's incredible! Great work!!\n"
    time.sleep(2)
    print "Tome King: alright, well, I think I might know where he is...especially if he isn't here"
    time.sleep(2)
    print "Tome King: sigh..."
    time.sleep(2)
    print "\nTome King mumbles to himself *I never thought I would to back there*"
    print "..."
    time.sleep(3)
    print "\nWELP! Let's head back to the minivan!\n"
    time.sleep(3)


        #SECOND HOUSE INTRO

def roomTwo():
    return 0

        #Third HOUSE INTRO

def roomThree():
    return 0


#Functionality helper functions


def userQuits():
    """
    If a user declines a prompt, the user has quit and the game ends
    """

    time.sleep(2)
    print "\na voice in your head says 'that was probably a good idea'\n"
    time.sleep(2)
    print "GAME OVER"

def userProvidesTheirName():
    """
    function to set global variable 'name' to user's name
    """

    global name
    theName = raw_input("What's your name? ")
    name = theName
    print "\nWelcome! %s\n" %(name)

def getInMinivan():
    """
    User is prompted to get in Mr Tome's odd minivan
    """

    print "Tome King: Alright, " + name +", hop in my minivan, let's go find Mr. can't read good!"
    time.sleep(3)
    acceptableAnswerFlag = False
    while not acceptableAnswerFlag:
        choice = raw_input("Get in this stranger's minivan Y/N? ")

        if choice == "Y":
            acceptableAnswerFlag = True
            print "\nTome King: niiceeeeee, and were off!! *vroooshhhh*"
            time.sleep(2)
            print "the car smells like it was recently febreezed...\n"
            time.sleep(2)
            if scruffyExists:
                print "Scruffy is sitting quietly in your lap."
                print "let's out a light yawn..adorable\n"
                time.sleep(3)

        if choice == "N":
            acceptableAnswerFlag = True
            print "what? why??..fine.."
            time.sleep(2)

        else:
            print "\nthat wasn't a correct response, please type either Y (yes) or N (no)\n"

    return choice


#House Challenges helper functions - each house has their own challenge, they are provided below


    #First House challenge --ADDITION PROBLEMS--

def AdditionGameSetUpText():
    """
    Explaining the rules/correct responses to the user about the math game (ends with a countdown!)
    """

    print "\n\nThe game will be 5 addition questions, get all 5 correct to move on!"
    time.sleep(3)
    print "if you want to quit early, just type 'quit' as an answer\n"
    time.sleep(4)
    print "Ready!"
    time.sleep(.5)
    print "Set!"
    time.sleep(.5)
    print "GO!"

def AdditionGameUserQuits():
    """
    Exit text if the user quits the game early
    """

    print "Instead of playing the game you just tackle and subdue him"
    time.sleep(2)
    print "With a swift kick in the face Mr Abacus is unconscious, and you help up the Tome King up\n"
    time.sleep(4)
    print "Mr Abacus slowly begins to wither away..."

def AdditionGameUserWins():
    """
    Exit text if the user wins the game
    """

    print "\nAs you answer the questions correct, Mr Abacus begins to slowly wither away."
    time.sleep(3)
    print "he stares at you, not sure who this master of math could be..."
    time.sleep(3)
    print "\nMr Abacus fades..."
    time.sleep(4)
    print "\nYou help up the Tome King, who is slowly beginning to feel better"

def AdditionProblems():
    """
    The actual math game. Flag variable starts the game, 5 math questions (addition for now) posted to user. User answers/score is tallied.
    If userScore == totalScore game ends, user wins
    if the user doesn't get all 5 correct, the math challenge will restart.
    User can quit at any time to just tackle Mr Abacus and kick him in the face!
    """

    AdditionGameSetUpText()
    gameWon = False
    while not gameWon:
        totalScore = 0
        userScore = 0
        for problem in range(5):
            firstNumber = random.randint(0, 10)
            secondNumber = random.randint(0, 10)
            answer = firstNumber + secondNumber
            userAnswer = raw_input(str(firstNumber) + ' + ' + str(secondNumber) + ' = ' + ' ')
            totalScore += 1
            if userAnswer == "quit":
                AdditionGameUserQuits()
                return 0
            if answer == int(userAnswer):
                userScore += 1
        print 'Out of a possible score of %d you scored %d correct!' %(totalScore, userScore)
        if userScore == totalScore:
            gameWon = True
            AdditionGameUserWins()
        else:
            print "\nMr Abacus gathers more power! Try again to save the Tome King!\n"
            time.sleep(3)


    #Second house challenge function --Garden Escape!--


    #Third house challenge function --??--





start()
