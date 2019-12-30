#A class to take in the player info such as health, merchandie, attack
class Player:
    def __init__( self,name,luck,merchandise,attackPhrase):
        self.name=name
        self.luck=luck
        self.merchandise=merchandise
        self.attack=attackPhrase
    
#A class to take in the enemy info such as health, attachprase and action    
class Enemy:
    def __init__(self,name,luck,attackPhrase,action):
        self.name=name
        self.luck=luck
        self.attackPhrase=attackPhrase
        self.action=action

import random
def main():
    print("Hi welcome to the Omni Hussle! The name of the game is to get all of the merchandise to Customer Service without running out of luck ")

    # Starts the game and checks to see if the user enters right input
    Start=input("Would you like to play? Press (s) to start or (q) to quit: ")
    while(Start!='s' and Start!='q'):
        print("Sorry wrong input! Please try again!")
        Start=input("Would you like to play? Press (s) to start or (q) to quit: ")
    
    while(Start!='q'):
       
        name=input("Please enter your player name: ")
        
        User=Player(name,100,2,"Divergence")
        print("Welcome {0} a new order just came in and needs delivered to Customer Service".format(User.name))
        #The enemy's info
        #The enemys health start from lowest to highest according to the enemy being faced
        Customer=Enemy("Annoyance",25,"Heads up here comes Annoyance she will talk your leg off","Talking")
        Boss=Enemy("Boss",75,"Run the Boss is coming with more work","Talking")
        LP=Enemy("LP",50,"LP is calling time to Clean the fitting rooms","Talking")
        dice=random.randrange(0,2)
        steps=10
        print("*********************************************************************")
        #Starts the actual game play
        print("Customer Service is just {0} steps away".format(steps))
        # Asks if the user wants move forward in game. If yes can play or no ends game and breaks out of program
        Decision=input("Do you want to move forward (y/n) ")
        while(Decision!='y' and Decision !='n'):
            print("Sorry wrong input! Please try again!")
            Decision=input("Do you want to move forward (y/n) ")
        if(Decision=='y'):
            dice1=random.randrange(0,2)
            dice2=random.randrange(1,4)
            #A dice roll decides whether or not the user faces an enemy or not
            #The dice roll decides number of merchandise the player can find
            if(dice1==1):
                User.merchandise=User.merchandise+dice2
                print("You found {0} items of merchandise in Mens".format(dice2))
                print("{0} had {1} items of merchandise".format(User.name,User.merchandise))
                print("    ")
            else:
                print(Customer.attackPhrase)
                fight=False
                while(not fight):
                    dice=random.randrange(1,7)
                    turn=dice
                    #This dice decises the turns
                    if(turn==1 or turn==3 or turn==5):
                        print("     ")
                        print("{0} is {1}".format(Customer.name,Customer.action))
                        User.luck =User.luck-5
                        print("{0} has {1} points of luck left".format(User.name,User.luck))
                        if(User.luck==0):
                            print("End luck: {0}".format(User.luck))
                            print("End merchandise: {0}".format(User.merchandise))
                            print("The {0} has won".format(Customer.name))
                            fight=True
                        turn=dice
                    else:
                        print("       ")
                        print("Attacking {0}".format(Customer.name))
                        Customer.luck=Customer.luck-5
                        print("{0} has {1} points of luck left".format(Customer.name,Customer.luck))
                    
                        if(Customer.luck==0):
                            print("    ")
                            print("{0} has been helped".format(Customer.name))
                            fight=True
                        turn=dice
            
        else:
            print("SUPRISE")
            print("To move on you need to answer this triva question or have to start all over again!")
            Answer=int(input("How many locations does Maryville have? "))
            if(Answer==4):
                print("Congrats you are correct! You are transported 2 steps ahead!")
            
            else:
                print("Maybe next time! Thanks for playing!")
                print("End luck: {0}".format(User.luck))
                print("End merchandise: {0}".format(User.merchandise))
                break
              
           
        print("*********************************************************************")
        # Asks if the user wants move forward in game. If yes can play or no ends game and breaks out of program
        print("Just 8 steps away from Customer Service")       
        Decision=input("Do you want to move forward (y/n) ")
        while(Decision!='y' and Decision !='n'):
            print("Sorry wrong input! Please try again!")
            Decision=input("Do you want to move forward (y/n) ")
            print("    ")
            
        if(Decision=='y'):
            #Dice decides if face enemy or not and one decides number of merchandise found   
            dice1=random.randrange(0,2)
            dice2=random.randrange(1,4)
            if(dice1==1):
                User.merchandise=User.merchandise+dice2
                print("You found {0} items of merchandise in Juniors".format(dice2))
                print("{0} had {1} items of merchandise".format(User.name,User.merchandise))
            else:
                print(LP.attackPhrase)
                fight=False
                while(not fight):
                    dice=random.randrange(1,7)
                    turn=dice
                    #Dice decides turn in fight 
                    if(turn==1 or turn==3 or turn==5):
                        print("     ")
                        print("{0} is {1}".format(LP.name,LP.action))
                        User.luck =User.luck-5
                        print("{0} has {1} points of luck left".format(User.name,User.luck))
                        if(User.luck==0):
                            print("End luck: {0}".format(User.luck))
                            print("End merchandise: {0}".format(User.merchandise))
                            print("{0} has won".format(LP.name))
                            fight=True
                        turn=dice
                    else:
                        print("       ")
                        print("Attacking {0}".format(LP.name))
                        LP.luck=LP.luck-5
                        print("{0} has {1} points of luck left".format(LP.name,LP.luck))
                    
                        if(LP.luck==0):
                            print("   ")
                            print("{0} has been helped".format(LP.name))
                            fight=True
                        turn=dice
        else:
             
            print("SUPRISE")
            print("To move on you need to answer this triva question or have to start all over again!")
            Answer=int(input("How many miles is Maryville from downtown St.Louis? "))
            if(Answer==22):
                print("Congrats you are correct! You are transported 2 steps ahead!")
            
            else:
                print("Maybe next time! Thanks for playing!")
                print("End luck: {0}".format(User.luck))
                print("End merchandise: {0}".format(User.merchandise))
                break
        print("*********************************************************************")
        # Asks if the user wants move forward in game. If yes can play or no ends game and breaks out of program
        print("Just 6 steps away from Customer Service")       
        Decision=input("Do you want to move forward (y/n) ")
        while(Decision!='y' and Decision !='n'):
            print("Sorry wrong input! Please try again!")
            Decision=input("Do you want to move forward (y/n) ")
        
        #Dice decides if face enemy or not and one decides number of merchandise found    
        if(Decision=='y'):
                
            dice1=random.randrange(0,2)
            dice2=random.randrange(1,4)
            if(dice1==1):
                User.merchandise=User.merchandise+dice2
                print("You found {0} items of merchandise in Jewelry".format(dice2))
                print("{0} had {1} items of merchandise".format(User.name,User.merchandise))
                print("You made it to customer service and delivered the order")
                print("End luck: {0}".format(User.luck))
                print("End merchandise: {0}".format(User.merchandise))
            else:
                print(Boss.attackPhrase)
                fight=False
                while(not fight):
                    dice=random.randrange(1,7)
                    turn=dice
                    #The dice decides turn so that game play does not go same way each time  
                    if(turn==1 or turn==3 or turn==5):
                        print("     ")
                        print("{0} is {1}".format(Boss.name,Boss.action))
                        User.luck =User.luck-5
                        print("{0} has {1} points of luck left".format(User.name,User.luck))
                        if(User.luck==0):
                            print("End luck: {0}".format(User.luck))
                            print("End merchandise: {0}".format(User.merchandise))
                            print("{0} has won".format(Boss.name))
                            fight=True
                        turn=dice
                    else:
                        print("       ")
                        print("Attacking {0}".format(Boss.name))
                        Boss.luck=Boss.luck-5
                        print("{0} has {1} points of luck left".format(Boss.name,Boss.luck))
                    
                        if(Boss.luck==0):
                            print("    ")
                            print("{0} has been helped".format(Boss.name))
                            print("End luck: {0}".format(User.luck))
                            print("End merchandise: {0}".format(User.merchandise))
                            print("You made it to customer service and delivered the order")
                            fight=True
                        turn=dice
        else:
            print("SUPRISE")
            print("To move on you need to answer this triva question or start all over again!")
            Answer=int(input("How many online Graduate students does Maryville have? "))
            if(Answer==4200):
                print("Congrats you are correct! You are transported 6 steps ahead!")
                print("End luck: {0}".format(User.luck))
                print("End merchandise: {0}".format(User.merchandise))
                print("You made it to customer service and delivered the order")
            else:
                print("Maybe next time! Thanks for playing!")
                print("End luck: {0}".format(User.luck))
                print("End merchandise: {0}".format(User.merchandise))
                break
        Start=input("Would you like to continue playing or would you like to stop?(s/q):")
                    
main()  
 
    
            
           

    
    
    

