#A basic game built around making money from fishing lobsters and the quality of them based on weather, the main gameplay loop revolves around the weather sunny and rainy and placements of pots between the sea and the bay on a sunny day the sea pots generate 2 money and bay generates 1 money, when it rains the bay generates 2 money however the sea loses all of its lobster pots.
#due to how the artifical scores are calculated expect the higher risk to lose to the lower risk
#I decided atleast for early development to set the risk bots to safe - all at bay, mid risk - half and half, high risk- all at sea this does mean that next to all games the high risk will end up wiped out
#current game lacks checks on player inputs
import random
def maingame(player,ai,playerMoney,days,playerPots,safeAiMoney,safeAiPots,midRiskAiPots,midRiskAiMoney,highRiskAiPots,highRiskAiMoney):
    for i in range (0,days):
        weather=random.randint(1,2) #Randomly changes the weather of the day done outside of the game loop so it is consistent for both ai and player
        if player=="y" or player=="Y": #Loop included for the player side of the game
            tobuy=int(input("enter number of pots to buy pots=2 money you currently have: ", money, " ")) #Main game loop for buying will act similar to the ai however the ai doesn't have user inputs
            while tobuy*2 > money:
                tobuy=int(input("enter number of pots to buy pots=2 money you currently have: ", money, " ")) #Main game loop for buying will act similar to the ai however the ai doesn't have user inputs
            pots=pots+tobuy
            money=money-(tobuy*2)
            bay=int(input("enter number of pots to put into the bay you have ", pots, " pots "))
            sea=int(input("enter number of pots to put into the sea you have ", pots-bay, "pots left "))
            if weather==1: #Sunny weather payout
                money=money+(sea*2)
                money=money+bay
            else: #Rainy weather payout
                money=money+(bay*2)
                pots=pots-sea

        if ai=="y" or ai=="Y": #Loop for when the ai is included in the game the game loop remains the same however uses automatic settings for the ais
            #ais always assume to buy all pots possible mostly due to the fact that in most situations there isn't a benefit to not buying
            safeAiPots=safeAiPots+(safeAiMoney//2)
            safeAiMoney=safeAiMoney%2 #the reason of using modulo here is due to the fact that the bot will always max out buys meaning the only check needed is if the result is 0 or 1
            midRiskAiPots=midRiskAiPots+(midRiskAiMoney//2)
            midRiskAiMoney=midRiskAiMoney%2
            highRiskAiPots=highRiskAiPots+(highRiskAiMoney//2)
            highRiskAiMoney=highRiskAiMoney%2 # in this case there may not be much point in doing the calcuation as the high risk is unlikely to have an odd amount of money at any point
            if weather==1: #Sunny day
                safeAiMoney=safeAiMoney+safeAiPots
                midRiskAiMoney=midRiskAiMoney+(midRiskAiPots//2+midRiskAiPots%2)#Decided that any remainder pots that mid risk has goes to the bay option thats the reason for the modulo addition
                midRiskAiMoney=midRiskAiMoney+((midRiskAiPots//2)*2) #Admittedly this calculation slightly redunant but this keeps it clear in terms of what the bot is doing
                highRiskAiMoney=highRiskAiMoney+(highRiskAiPots*2)
            else: #Rainy day
                safeAiMoney=safeAiMoney+(safeAiPots*2)
                midRiskAiMoney=midRiskAiMoney+((midRiskAiPots//2+midRiskAiPots%2)*2) #Again assuming remainer goes to the safe section
                midRiskAiPots=midRiskAiPots//2
                highRiskAiPots=0 #Sums up why the highrisk isn't the best probably would be good to set it up with a high varible of placement instead of 100% as its likely to destroy itself repeatedly
    return playerMoney,safeAiMoney,midRiskAiMoney,highRiskAiMoney

def mainmenu(): #Main game loop
    playAgain="y"
    while playAgain=="y" or playAgain=="Y":
        player=input("enter y to play ")
        ai=input("enter y to play or simulate an ai game ") #Allows the user to choose to either leave the ai to play or to play themselves or to play against the ai

        playerPots=0 #Sets the player stats before game
        playerMoney=50

        safeAiPots=0 #Sets ai stats before game and refreshes them if the player wants to play again
        safeAiMoney=50
        midRiskAiPots=0
        midRiskAiMoney=50
        highRiskAiPots=0
        highRiskAiMoney=50

        days=int(input("enter number of days the game will be played for ")) #Lets the player choose the length of the game
        playerMoney,safeAiMoney,midRiskAiMoney,highRiskAiMoney=maingame(player,ai,playerMoney,days,playerPots,safeAiMoney,safeAiPots,midRiskAiPots,midRiskAiMoney,highRiskAiPots,highRiskAiMoney)
        if ((player == "y" or player == "Y") and (ai =="y" or ai=="Y")):
            print ("The game results are: player money - ", playerMoney, " safe ai money - ", safeAiMoney, " medium risk ai money - ", midRiskAiMoney, " high risk ai money - ", highRiskAiMoney) 
        elif (player=="y" or player == "Y"):
            print ("The game results are: player money - ", playerMoney)
        elif (ai=="y" or ai == "Y"):
            print ("The game results are: safe ai money - ", safeAiMoney, " medium risk ai money - ", midRiskAiMoney, " high risk ai money - ", highRiskAiMoney)
        playAgain=input("enter y to play again ") #Mechanism for the player starting again

mainmenu()
