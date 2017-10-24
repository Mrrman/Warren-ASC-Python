#!/usr/bin/python
from os import system
from sys import exit


class Enemy(object):
	#This base list of items for the enemies
	def __init__(self):
		self.items = []
		#self.meds = None
		#self.ammo = True
		#self.pistol = None
		#self.rifle = None
		#self.water = None
		#self.food = None
		#self.truckKeys = None


class House(object):
	#This is the base list for the items for the house
	def __init__(self):
		self.items = ["food", "clothing", "knife", "watch", "compass",
		"water", "lighter", "mediciation", "rifle", "pistol", "money",
		"ammunition"]

	def display(self):
		for num, item in enumerate(self.items):
			if not num:print "#\t\tItem\n"
			print "{}\t\t{}".format(num+1, item)

class Player(object):
	#This is the base player inventory
	def __init__(self):
		self.items = []

        
        	







def start():
        system("clear")
	print"Name: The Last Chapter"
	print"Setting: Post Apocalypse in some northern part of what used to be The United States"
	print"Time: about 2900 AD"
	print"You wake up calmly from a nice and cozy slumber to a beautiful sunrise on a cool morning, and decide to look out your window."
	print"You look around and see some deer and other fauna in the distance."
	print"As you continue to look around and enjoy nature, you see a peculiar formation of people near your humble abode"
	print"(You can either [check it out] or [proceed] with your plans for today)"

	choice = raw_input(p)

	if choice == "check out" or choice == "check it out":
		gathering_of_people()
	elif choice == "proceed":
		morning_routine()

def gathering_of_people():
        system("clear")
	print"As you approach the large crowd you start to smell something that you never had before."
	print"It reeks, whatever it had been must have been dead for a long time."
	print"The crowd seems to be circled around a person, or what is left of them, but something is quite peculiar about the person..."
	print"The \"person\" seems to still be alive while in pieces on the crowd..."
	print"(Inner concious) why is \"it\" still alive? What did this to it?"
	print"(You can either [ask around] or [observe it] closer)"

	choice = raw_input(p)

	if choice == "ask around":
		ask_crowd()
	elif choice == "observe it" or choice == "observe":
		dead("You lean in to take a closer look and it explodes, some mysterious gunk gets all over you. Your skin turns black, your vision goes black and you die.")
def dead(why):
	print why
	exit(0)

def morning_routine():
	system("clear")
	print"You decide to continue on with your morning routine. You brush your teeth and head downstairs."
	print"You make youself some eggs and coffee and while eating your food you hear a loud explosion!"
	print"You look outside and see most of the crowd covered in some mysterious black gunk"
	print"After a couple seconds you see them start to drop like flies."
	print"You rush outside to see what had happened and you notice someone sitting in a ball crying and someone else laying on the ground near you that you know covered in gunk"
	print"(You can either [talk] to the person cuddled in a ball or [go to] the person you know)"

	choice = raw_input(p)

	if choice == "talk":
		talk_one()
	elif choice == "go" or choice == "go to":
		dead_person_one()

def ask_crowd():
	system("clear")
	print"You call out \"Anyone know what happened\" and a person cuddled up in a ball near the crowd responds coldy  \"I do\""
	print"You walk up to the person who is sitting next to a contraption(it looks like a car) and ask them what had happened"
	print"The person responds with \"I was operating my new contraption when this person jumped in front of me!\""
	print"All of a sudden you hear an explosion, you and see most of the crowd covered in some mysterious black gunk"
	print"After a couple seconds you see them start to drop like flies."
	print"You and the \"Driver\" freak out and head back into your home."
	print"(Press entern to go into your house.)"

	choice = raw_input(p)

	if choice == " ":
		home()
	else:
		home()

def talk_one():
	system("clear")
	print"You walk up to the person who is sitting next to a contraption(it looks like a car) and ask him what had happened"
	print"He responds with \"I was operating my new contraption when this person jumped in front of me!\""
	print"He continues with \"Then just now it exploded and it got over everyone\""
	print"You decide to take him back inside and calm him down"
	print"(Press entern to go into your house.)"

        choice = raw_input(p)

        if choice == " ":
                home()
        else:
                home()

def home():
	system("clear")
	print"You ask him for his name, he responds with \"Shia Labeauf\""
	print"As you call the police and start to tell them what had happened the driver turns on your TV"
	print"The news headline is \"Is it happening again\""
	print"The reporter states that it is happening again, reanimation of the human body"
	print"The same thing that happened about 875 years prior"
	print"The reporter says to pack 5 things into one bag and head to the nearest safe station"
	#print"(Your item choices are [food] [clothing] [knife] [watch] [compass] [water] [lighter] [medicine] (AR10)[rifle] [pistol] [money] [ammunition])"
	#print"(Enter your choices one by one please)"

	#choice = raw_input(p)
	while len(p1.items) != 5:
                system("clear")
		house.display()
		choice = raw_input("\nEnter the number of the item you want. You have {} choices left: ".format(5-len(p1.items)))
                try:
                 	item = house.items[int(choice)-1]
			p1.items.append(item)
			del house.items[int(choice)-1]
		except:
			print "Item number is not found. Try again"
          
		
        system("clear")
        print"(There is nothing else to do here at home at this time press enter to start your journey to the safe station)"
	choice = raw_input("\n[Press Enter To Continue]")
        leave()
	
	
def dead_person_one():
	system("clear")
	print"As you approach your dead friend you notice something odd about them."
	print"She seems to be decomposing rapidly and as you lean in closer one of her bones pop and the gunk gets on your left ankle"
	print"You freak out and jump back and land right next to the person crying on the ground"
	print"(You're now infected with the Last Chapter, this can and will affect the rest of your gameplay)"
	infected = True
        raw_input("\n[Press Enter To Continue]")
        reaction_one()
	
def reaction_one():
	system("clear")
	print"As you get up you notice that you notice the person crying has stopped now and is standing above you"
	print"He asks you if you're ok and helps you up"
	print"You get up and almost fall right back down, but with the help of this man he gets you back inside"
	home()

def leave():
	system("clear")
	print"You are packed and ready to go when, you head outside with all of your collected items and as you go outside you see four  military personel"
	print"They are examining and sampling the crowd that got infected when they spot you and call you over to them"
	print"They ask if you want a ride to the station with them or if you would perfer to go on foot (it's only about a mile and a half down the road"
	print"You can either [accept] the ride or politely [decline]"

	choice = raw_input(p)

	if choice == "accept":
		truckOne()
	elif choice == "decline":
		onFoot()

def truckOne():
	system("clear")
	print"Yes we would love a ride thank you"
	print"Before you leave they ask you a couple questions about the crowd and the contraption"
	print"You two answer honestly and lastly before you guys leave they ask if either of you have been bitten or infected in anyway"
	print"(You think deeply and answer either [yes] I have or [no] I havent"

	choice = raw_input(p)
	if choice == "yes":
		if infected == True:
			print"Yes I have honestly been infected"
			dead("You were immediately shot in the head afterwards and with that one fatal move you messed up")
		if infected == False:
			print"I think I have been infected, but I don't know"
			print"They test you quickly and see that you are not infected luckily, or yet..."
			insideTruck()

	if choice == "no":
		if infected == True:
			print"No I am not infected sir, any other questions?"
			print"They have no other questions for you and take you into the truck"
			insideTruck()
		if infected == False:
			print"No i havent had any contact or been anywhere near any infected people"
			print"They have no furhter questions for you and take you into their truck"
			insideTruck()

def onFoot():
	system("clear")
	print"You respond with \"No thank you guys I think we will leave room for potential women and children\""
	print"As you start to walk away one of them says \"NOW WE ARENT ASKING GET IN THE TRUCK NOW\""
	print"(Your choices are either [obey] them, [fight] back or [run] away)"
        choice = raw_input(p)

	if choice == "obey":
		insideTruck()
	elif choice == "fight":
		#I want it to read that the items are are in the bag and if so the fight will go differently
		if all(["rifle" in p1.items, "ammunition" in p1.items]):
			print"You killed all of them with no harm done to you or your buddy"
			loot()

		if all(["pistol" in p1.items, "ammunition" in p1.items]):
			print"You killed all of them, but your buddy got shot"
			hurtFriend()
		
		if "knife" in p1.items:
			print"You killed three of them and the last one ran away and you got shot in your upper right pectoral"
			lootHurt()
		else:
			dead("You died because you had no weaponry to attack and kill anyone with")

	elif choice == "run":
		print"You peel out around the side of your house and vanish into the woods with your friend"
		woods()

def insideTruck():
	system("clear")
	print"As you walk up to the truck they focefully shove you inside and take you hostage"
	print"You realize that they are not military and not even the slightest bit experienced because they didnt even take your bag or search you"
	print"As you sit in the middle of the back seat you see that you have a couple different options"
	print"(You can either sit and [wait] out the ride, you can [kill] the driver or you can [steer] the truck off the road)"

	choice == raw_input(p)

	if choice == "wait":
		rideOut()

	elif choice == "kill":
		if pistol == true:
			truckCrashSafe
		else:
			print"You don't have a pistol on you to kill the driver, you decide to steer the car instead"
			truckCrashBad()

	elif choice == "steer":
		truckCrashBad()

def hurtFriend():
	system("clear")
	print"Shia got shot in the stomach, and it's not looking too good..."
	print"(If you have medication you can [help] Shia, if not you can loot either [enemyOne] [enemyTwo] or [enemyThree]"

	choice = raw_input(p)

	if choice == "help":
		if "medication" in p1.items:
			del p1.items[p1.items.index("medication")]
			print"You helped Shia"
			loot()
		else:
			print"You dont have any medical supplies and your incompetance cost Shia his life"


	if choice == "enemyOne":
		#p1.items.append("medicine")
		p1.items.append("ammunition")
		p1.items.append("food")
		p1.items.append("pistol")
		choice = raw_input("You picked up medicine, ammunition, food and another pistol, you can help Shia now, \n[Press Enter To Continue]")
		saveShia()

	elif choice == "enemyTwo":
		#p1.items.append("medicine")
		p1.items.append("ammunition")
		p1.items.append("water")
		p1.tiems.append("rifle")
		choice = raw_input("You picked up medicine, ammunition, water and a rifle, you can help Shia now, \n[Press Enter To Continue]")
                saveShia()

	elif choice == "enemyThree":
		p1.items.append("truckKeys")
		p1.items.append("rifle")
		p1.items.append("ammunition")
		p1.items.append("water")
		print "You couldn't find any medicine for shia, he has died, but you do pick up truck keys, a rifle, ammunition, and water."
		choice = raw_input("With the truck keys you walk to the truck \n[Press Enter To Continue]")
		truck()
	#items append to list of person


def saveShia():
	system("clear")
	print"This is the end of the Prologue thank you for playing hope to see you back at full release"
	exit()



def truck():
	system("clear")
	print "You open the door to the truck aaannndd......."
        print"This is the end of the Prologue thank you for playing hope to see you back at full release"
	exit()


def rideOut():
	system("clear")
	print "You decide to ride out the trip..."
	print"This is the end of the Prologue thank you for playing hope to see you back at full release"
        exit()

def truckCrashSafe():
	system("clear")
	print"You, while seatbelted, shoot the driver in the head..."
	print"This is the end of the Prologue thank you for playing hope to see you back at full release"
        exit()

def truckCrashBad():
	system("clear")
	print"You take off your seatbelt and lunge for the steering wheel and take a big yank out of it..."
	print"This is the end of the Prologue thank you for playing hope to see you back at full release"
        exit()

def loot():
	system("clear")
	print "You start to loot the bodies and find some awesome gear..."
	print"This is the end of the Prologue thank you for playing hope to see you back at full release"
        exit()

def lootHurt():	
	system("clear")
	print"You got shot and are now looting the bodies with a bullet hole"
	print"This is the end of the Prologue thank you for playing hope to see you back at full release"
        exit()

def woods():
	system("clear")
	print"You make it away and run into the woods with Shia"
	print"This is the end of the Prologue thank you for playing hope to see you back at full release"
        exit()


if __name__ == '__main__':
	p ="> "
	infected = False
	p1 = Player()
	house = House()
	e1 = Enemy()
	e2 = Enemy()
	e3 = Enemy()
	start()
	







