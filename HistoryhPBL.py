# Caleb McGuire, Hunter
print 'You are a Jewish citizen during the time of Hitler\'s rule. Type ok to proceed'

scenario = raw_input('> ')

while scenario != 'ok' and scenario != 'OK':
    scenario = raw_input("Sorry, I didn't catch that. Try again: ")
if 
    print 'The Nazis come through your home town.'
    print 'You have heard what they have done to other Jews from others, you have about a day what do you want to do?'
    print 'PACK your stuff and hide \nOR'
    print 'STAY where you are and hope they dont find you.'

choice = raw_input('> ')
    
while 'pack' not in choice.lower():
   choice = raw_input("Sorry, I didn't catch that. Try again:\n> ")
    
if 'pack' in choice.lower():
        print 'You pack your stuff just in time to leave.\nYou see the Nazis coming down the street on the LEFT.\nThere are two more roads you can take one that is in FRONT of you\nand, one is on the RIGHT which do you take? Front is unavable at the moment.'

elif choice == "STAY":
        print 'You stay behind hoping they will pass by.\nYou hear a banging on your door you stand frozen, the door is busted down and you are told you are under arrest by the Nazis.\nDo you RESIST arrest or do you LISTEN?'
        
if choice == "RESIST": 
        print 'You resited arrest and were killed.' #DEATH

elif choice == "LISTEN":
        print 'You are arrested and sent to a cnsontration camp via train car. On your way there you died from disease contracted due to the small space in the train car in the packed train car.' #DEATH

#-----------------------level 1----------------------------------------

stage1 = raw_input('> ')

if stage1 == "left":
        print 'You start walking towards the Nazis as you get closer they see the Star of David on your clothing and shoot you on the spot.' #DEATH

elif stage1 == "right":
        print 'You see the Nazis on your left you see your car on the right, you notice your neighbor in there window rushing to get there daughter ready, do you HELP them or LEAVE them?'

elif stage1 == "front":
    print 'Well, doing is probably better. Bear runs away.'
    
#----------------------level 2-----------------------------------------

stage2 = raw_input('> ')

if stage2 == "help":
        print 'You run to your neighbors front door the door is locked.You see a rock on the ground next to the window\nDo you pick up the rock and BUST THE WINDOW,\nDo you run BACK to your car\nOr do you BREAK THE DOOR?'
        
elif stage2 == "leave":
        print 'You get in your car and leave your neighbor behind as you drive away you see the Nazis enter the building, knowing that your neighbor was a Jew you assume they were killed.'
        
#----------------------level 3-----------------------------------------
stage3 = raw_input('> ')

if stage3 == "bust the window":
        print 'You grab the rock and throw it at the window and run up the stairs.'
        
elif stage3 == "break the door":
        print 'You break the door down, in doing so you have injured yourself.You take a quick glance at it and run up the stairs to you neighbor and tell them to get in your car.They listen and run to your car you follow at a slightly slower pace due to your injured leg.You three get in the car and drive to the outskirts of your town.'
