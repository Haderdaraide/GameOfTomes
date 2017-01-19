import time
import random

    #First House challenge --ADDITION PROBLEMS--

def AdditionGameSetUpText():
    """
    Explaining the rules/correct responses to the user about the math game (ends with a countdown!)
    """

    print ""
    print ""
    print "The game will be 5 addition questions, get all 5 correct to move on!"
    time.sleep(3)
    print "if you want to quit early, just type 'quit' as an answer"
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
    print "With a swift kick in the face Mr Abacus is unconscious, and you help up the Tome King up"
    print ""
    time.sleep(4)
    print "Mr Abacus slowly begins to wither away..."

def AdditionGameUserWins():
    """
    Exit text if the user wins the game
    """

    print ""
    print "As you answer the questions correct, Mr Abacus begins to slowly wither away."
    time.sleep(3)
    print "he stares at you, not sure who this master of math could be..."
    time.sleep(3)
    print ""
    print "Mr Abacus fades..."
    time.sleep(4)
    print ""
    print "You help up the Tome King, who is slowly beginning to feel better"

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
            userAnswer = raw_input(str(firstNumber) + ' + ' + str(secondNumber) + ' =' + ' ')
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
            print ""
            print "Mr Abacus gathers more power! Try again to save the Tome King!"
            print ""
            time.sleep(3)


AdditionProblems()
