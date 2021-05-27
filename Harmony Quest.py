import time
import random
from tkinter import *
username=input("Enter your name: ")


#_______FILES
README = '''1. Enter a valid input whenever prompted.
2. Read each line to get a better understanding of each scene.'''
ABOUT = '''In this interactive adventure game, the player is placed into a fantasy world with nothing more than a sword, a shield and a red pendant to companion him. A fairy accompanies the player, explaining his course of action. The player is presented with the Herculean task of defeating the dragon, who has been the scourge of the village dwellers. He engages in riveting battles against his challengers on his path and adds handy material to his inventory. In this game of brain and brawn, the player is confronted with bamboozling riddles and puzzles. In the end, he meets with the dragon, and battles him in an attempt to relieve the village from the tyranny of this bloodthirsty beast.
'''
console_ins="The game will run on the IDLE console after you press the START button given below."
inv = {"Sword": "A basic sword. Well, it's better than using your bare hands.",
       "Shield": "A simple iron shield. Defends you from attacks.",
       "Red pendant": "A mysterious red pendant. It emits a soft glow."}


#_______Game functions
def player_hp(hpg):
    if hpg > 0:
        print("Your HP: ", hpg)


# Answers
option_A = ("A", "a")
option_B = ("B", 'b')
option_C = ("C", "c")
option_D = ("D", "d")
option_E = ("E", "e")


def tp(text):
    for x in text:
        print(x, end='')
        time.sleep(random.randint(5, 9) / 100)
    print()


def contd():
    input("Press Enter to continue \n")


def wel_msg():
    tp("Well,well,well look who's here!")
    tp(
        "I don't want to bother you with my introduction, but I am your narrator and I will guide you through the story. Hope you enjoy!")
    contd()
    tp(
        "FAIRY: Your main goal in this is to find the dragon and kill him so that the people in town can again live peacefully. Sounds easy right? But don't take it like that.")
    print("Good luck ", username)
    input("Press Enter to continue \n")

# _-_-_-_-
# Robert
def Robert():
    hpr = 100
    hpg = 100
    input("Robert: Hey, " + username + ", where are you going? \n Press Enter to reply \n")
    print(username + ": It's none of your business.")
    tp(
        "Robert: Better turn back, or I'll take you down with my beautiful golden arrows!")
    while hpr > 0:
        weapon = input("""Choose an attack:
        A. Sword
        B. Agility
        C. Dodge \n""")
        if weapon in option_A:
            hpr -= 75
            hpg -= 80
            print(
                "Robert attacked you with this Bow & Arrow and you were unable to control your body for 30s"
            )
        elif weapon in option_B:
            hpr -= 25
            hpg -= 5
            print("Robert was tricked by your agility skills")
        elif weapon in option_C:
            hpr -= 5
            hpg -= 0
            print("You dodged Robert's attack and punched him")
        else:
            print("You attack is invalid but Robert punched you!")
            hpg-=5
        if hpr <= 0:
            print("Opponent's HP: 0")
        else:
            print("Opponent's HP:", hpr)
        player_hp(hpg)
    if hpr <= 0:
        print("You defeated Robert!")
        input("Press Enter to search Robert's belongings.")
        tp(
            "You found a bow and arrows! They have been added to your inventory.")
        tp("You use some of Robert's supplies ot heal yourself.")
        inv["Bow and Arrows"] = "A powerful bow with poison-tipped arrows."
        hpg = 100
        input("Press Enter to continue \n")

# _-_-_-_-_-_-
def puzzle():
    print("FAIRY: Oh look! You are at crossroads; one path leading to left and one leading to the right.")
    print(
        "You see a pair of identical twins standing at the crossroads. One always lies while the other always tells the truth. You do not know who is who.")
    a = 1
    c = 1
    d = 1
    crans = "Right"
    print("Press 1 or 2 to ask a person")

    while a == 1:
        choice = input("Enter either 1 or 2:\n")
        c = 1

        if choice != "1" and choice != "2":
            print("NOTE:Enter only 1 or 2")
            c = 0
        while c == 1:
            d = 1
            x = random.randint(1, 3)
            if x == 1:
                rightp = 1
                wrongp = 2
            else:
                rightp = 2
                wrongp = 1
            print("Given below are a list of questions you can ask the person")
            print("Choice 1:Which is the correct path?")
            print("Choice 2:What would your brother answer when asked the first question?")

            if int(choice) == rightp:

                n = input("Enter the number correspoding to the question you chose:\n")

                if n != "1" and n != "2":
                    print("Choose ONLY between 1 and 2:")
                    d = 0
                if n == "1":
                    print("Right is the way; believe or you will pay")

                elif n == "2":
                    print("Left is the way; no more to say")

            if int(choice) == wrongp:
                m = input("Enter the number corresponding to the question you chose:\n")
                if m != "1" and m != "2":
                    print("Choose ONLY between 1 and 2")
                if m == "1":
                    print("Left is the way; no more to say")

                elif m == "2":
                    print("Left is the way; no more to say")

            while d == 1:
                e = input("Enter the correct path (Left or Right):\n")
                if e == crans:
                    print("You win")
                    a = 0
                    d = 0
                    c = 0
                elif e != crans:
                    print("Try agin")
                    d = 0
                    c = 0
    tp("FAIRY: You completed the cross-road maze and reached the forest enterance")
    input("Press Enter to continue \n")


# _-_-_-_-
# Wise Man
def Wise_man():
    tp("You encounter an old ,wise man.")
    input("Press Enter to talk to him \n")
    tp("WISE MAN: You look like a brave warrior.")
    time.sleep(1)
    tp(
        "WISE MAN: However, if you wish to slay a dragon, bravery alone will not be enough.")
    time.sleep(1)
    tp(
        "WISE MAN: You will need two things to help you: fighting skills and dynamite.")
    time.sleep(1)
    tp(
        "WISE MAN: You will have to develop your skills on your own, but I can give you a golden sword.")
    time.sleep(1)
    input("You received a Golden Sword and some Dynamite! \n Press Enter to continue \n")
    inv["Golden Sword"]: "A powerful sword. Its blade gleams in the sun."
    inv["Dynamite"]: "Some explosive with great destruction power"
    tp("""WISE MAN: You will have to battle many enamies on the way which would help. Be strong!""")
    time.sleep(2)
    print("WISE MAN: You can enter the forest from there")
    inv.pop("Sword")
    input("Press Enter to continue \n")


# _-_-_-_-_-
# Lion fight
def Lion():
    hpl = 100
    hpg = 100
    tp(
        "While passing through the forest, you come across a sleeping lion blocking your path.")
    time.sleep(1)
    print("You quietly, slowly make your way around it.")
    time.sleep(1)
    print("Slower...")
    time.sleep(1)
    print("Halfway there...")
    time.sleep(1)
    print("You've almost crossed the lion!")
    time.sleep(1)
    print("CRASH!")
    print()
    tp(
        "An old branch falls from the tree. The lion wakes up and sees you. He doesn't look happy.")
    time.sleep(2)
    tp(
        "This is your chance! You can finally use the bow and arrows you took from Robert!")
    while hpl > 0:
        weapon = input("""Choose your attack:
A. Sword
B. Agility
C. Bow & Arrow
D. Dodge \n""")
        if weapon in option_A:
            hpl -= 55
            hpg -= 40
            print("The lion mauls your back.")
        elif weapon in option_B:
            hpl -= 10
            hpg -= 0
            print("You trick the lion and it runs headfirst into a tree.")
        elif weapon in option_C:
            hpl -= 85
            hpg -= 0
            print("Taking aim, you shoot an arrow at the lion.")
            print("It's a direct hit!")
        elif weapon in option_D:
            print("The lion's attack misses you by a whisker.")
        else:
            print("Invalid move!")
        print("Opponent's HP:", hpl)
        player_hp(hpg)
    if hpl <= 0:
        print("The lion falls to the ground. You've defeated it!")
        input("Press Enter to search around.\n")
        print("You find wild herbs and use them to heal yourself.")
        print()
        print("You learnt a new skill!")
        print("You can now shoot 3 arrows together.")
        hpg = 100
        input("Press Enter to continue \n")


# _-_-_-_-_-_-
# Wolves Fight
def Wolves():
    hpw, hpg = 400, 100
    tp(
        "You're almost out of the forest when you see a pack of wolves in the distance. They see you... and start running towards you.")
    time.sleep(2)
    print("Oh, the perils of being an adventurer.")
    input("Press Enter to continue \n")
    tp(
        "There are four wolves, and they now have you surrounded. You have no choice but to fight!")
    tp(
        "They're too close for you to use the bow and arrow; you'll have to ")
    while hpw > 0:
        weapon = input("""Choose your attack:
A. Sword (Recommended)
B. Agility
C. Bow & Arrow 
D. Dodge \n""")
        if weapon in option_A:
            print(
                "You moved your sword in such a manner that you killed 2 wolves at once")
            hpw -= 200
            hpg -= 30
        elif weapon in option_B:
            print(
                "You escaped from the wolves' attack but the wolves bumped into each other")
            hpw -= 40
            hpg -= 0
        elif weapon in option_D:
            print(
                "You escaped from the wolves' attack but the wolves bumped into each other")
            hpw -= 40
            hpg -= 0
        elif weapon in option_C:
            print("You shot a wolf")
            hpw -= 100
            hpg -= 10
        else:
            print("Invalid move!")
        if hpw <= 0:
            print("Opponent's HP: 0")
        else:
            print("Opponent's HP: ", hpw)
        player_hp(hpg)
    if hpw <= 0:
        print("The defeated the wolves")
        contd()
        print("FAIRY: Wow! that was awesome! You learnt a new move!")
        tp(
            "Now you can use your sword to kill 2 enemies at once and you have improved your speed")
        hpg = 100
    input("Press Enter to continue \n")


# _-_-_-_-_-_-_-
# Black smith
def Blacksmith():
    hpwl = 150
    hpg = 100
    tp(
        "BLACK SMITH: Wow! Looks like finally a warrior has completed all its tests till now.")
    time.sleep(2)
    tp(
        "BLACK SMITH: Looks like you can make it but I dont think you can without proper suit")
    y = input("Press ENTER to reply")
    print(username, " :I hope you can give me some")
    tp("BLACK SMITH: I can but you see nothing is free here")
    print(username, " :I don't have money")
    tp(
        "BLACK SMITH: hm.. can you get rid of the witch who lives about a few miles she is very disturbing")
    time.sleep(2)
    print(username,
          " :Well I don't have any other choice can you take me there?")
    time.sleep(2)
    tp("BLACK SMITH: Sure!")
    y = input("Press ENTER to follow \n")
    tp(
        "BLACK SMITH: I have a few riddles for you which we entertain you throughout the way but you get only one chance to answer")
    time.sleep(1)
    tp("Riddle 1:")
    tp("What kind of goose fights with snakes?")
    rep_1 = input("Enter answer: ")
    rep_1_ans = ("Mongoose", "mongoose", "MONGOOSE", "Mongoose ", "MONGOOSE ", "mongoose ")
    if rep_1 in rep_1_ans:
        tp("Nice! your answer is correct")
    else:
        tp("Nope! You got it wrong. It is a Mongoose ")
    print()
    time.sleep(1)

    tp("Riddle 2:")
    tp(
        "If there are four sheep, two dogs and one herds-men, how many feet are there?")
    rep_2 = int(input("Enter answer as integer: "))
    if rep_2 == 2:
        tp("You are pretty nice at this, your answer is correct")
    else:
        tp(
            "Nope! The answer is 2. Sheep have hooves; dogs have paws; only people have feet.")
    print()
    time.sleep(1)
    tp("Riddle 3:")
    tp("You answer me, although I never ask you questions. Who am I?")
    rep_3 = input("Enter your answer: ")
    rep_3_ans = ("telephone", "Telephone", "TELEPHONE", "Telephone ", "TELEPHONE ", "telephone ","Phone","phone","PHONE")
    if rep_3 in rep_3_ans:
        tp("You are really good at this! Your answer is correct")
    else:
        tp("Nope! The answer is a Telephone")
    print()
    tp("BLACK SMITH: Here is the witch's palace")
    contd()
    tp("Thanks man see you after this hope you will be ready with my suit")
    tp("FAIRY: This is your last battle before the dragon. Give your best")
    y = input("Press ENTER to fight with the witch \n")
    tp("WITCH: Eeeew hahaha")
    while hpwl > 0:
        weapon = input("""Choose your attack:
A. Sword (Recommended)
B. Agility
C. Bow & Arrow 
D. Dodge \n""")
        if weapon in option_A:
            print(
                "You attacked with sword and the stone is glowing and the witch spilt some weird portion on you")
            hpwl -= 50
            hpg -= 30
        elif weapon in option_B:
            print("You escaped from the witch and kicked off her magic wand")
            hpwl -= 20
            hpg -= 0
        elif weapon in option_D:
            print("You escaped from the witch")
            hpwl -= 0
            hpg -= 0
        elif weapon in option_C:
            print("You shot witch's magic pedant into her body")
            hpwl -= 90
            hpg -= 10
        else:
            print("Invalid move!")
        print("Opponent's HP: ", hpwl)
        player_hp(hpg)
        if hpwl <= 0:
            print(
                "You have mastered all your moves now and you are ready for the big battle")
            tp(
                "FAIRY: You have defeated the witch now you have to go back to the black smith to get your suit")
            y = input("Press ENTER to go to black smith \n")
    tp("BLACK SMITH: I knew you will be able to defeat her ")
    time.sleep(2)
    tp(
        "BLACK SMITH: While you were gone I made your suit out of gold which is light but extremely strong and heat resistent")
    y = input("Press ENTER to wear it \n")
    print(username, " :Thanks a lot!")
    tp("It is nothing in front of the favour you have done to me")
    contd()
    tp("FAIRY: That was nice! Now your HP is increased to 300")
    contd()


# _-_-_-_-_-_-
# Dragon Fight
def dragonFight(player_hp, dragon_hp):
    player_max = player_hp
    dragon_max = dragon_hp
    fire = 100
    tail = 100
    far = False
    away = 0
    start = time.time()
    guard = 1
    print("The Crimson Dragon roars!")
    while player_hp > 0 and dragon_hp > 0:
        player_attack = 0
        given = 0  # Damage you give
        damage = 0  # Damage you take
        away -= 1  # Are you away or not?
        if away <= 0:
            far = False
            away = 0
        else:
            far = True
        while player_attack not in (1, 2, 3):
            player_attack = int(input("""Choose an attack number:
    1. Sword
    2. Bow and arrow
    3. Guard/Dodge
""").strip())
        if player_attack == 1:
            print("You swung your sword.")
            if far == False:
                given = 30
            else:
                given = 0
                print("You were too far away to hit the dragon!")
        if player_attack == 2:
            print("You shot your arrows.")
            given = 10 * random.randint(0, 5)
        elif player_attack == 3:
            guard = 0.5
            print("You raised your shield.")
        roll = random.choice(range(10))
        if random.randint(0, 9) == 0:
            dragon_wait = random.randint(1, 3)
            if dragon_wait == 1:
                print("A puff of steam flies out of the dragon's nostrils.")
            elif dragon_wait == 2:
                print("The dragon's ears perk up to hear a sound.")
            elif dragon_wait == 3:
                print("A nearby rock is smashed by the dragon's claws!")
        else:
            dragon_attack = random.randint(1, 4)
            if dragon_attack == 1:
                print("The dragon breathes a stream of fire!")
                if roll <= 4:  # bad roll!
                    damage = round(fire * guard)
                elif roll <= 6:
                    damage = round(fire * 0.75 * guard)
                elif roll <= 8:
                    damage = round(fire * 0.5 * guard)
                else:
                    damage = 0
            elif dragon_attack == 2:
                print("The dragon swings its mighty tail!")
                if roll <= 6:
                    damage = round(tail * guard)
                elif roll <= 7:
                    damage = round(tail * 0.75 * guard)
                elif roll <= 8:
                    damage = round(tail * 0.5 * guard)
                else:
                    damage = 0
                if far == True:
                    print("You were too far away to be hit.")
                    damage = 0
            elif dragon_attack == 3:
                print("The dragon flaps its wings and blows you far away!")
                away = 2
            elif dragon_attack == 4:
                print("The dragon's tail sends a boulder tumbling down.")
        player_hp -= damage
        dragon_hp -= given
        print("The dragon took %s damage!" % given)
        print("Dragon HP: ", dragon_hp, "/", dragon_max)
        print("Your HP: %s/%s" % (player_hp, player_max))
        if time.time() == start + 300:
            loss = True
            print("The cave collapses in on itself, trapping you inside.")
            break
    tp("FAIRY: You defeated the Dragon!")
    tp("FAIRY: We always knew you were a brave warrior and you also proved")
    print()
    tp("You have WON the game!!")


'''attacks: breathing fire, swinging with tail, flapping wings
Flapping sends you far away
When far away, you have to use bow/arrow for a turn, then you come back closer
When far away, swiping misses and you take slightly less damage from fire breathing'''

#_________GAME
def main_game():
    wel_msg()
    Robert()
    puzzle()
    Wise_man()
    Lion()
    Wolves()
    Blacksmith()
    dragonFight(400, 200)
    tp("You have Completed the game! Hope you Enjoyed")

#_________MAIN MENU FUNCTIONS
def esc():
    exit_page=Toplevel()
    exit_page.resizable(0,0)
    exit_page.title("Adventure Game - Quit Menu")
    exit_page.geometry("285x200")
    exit_page.configure(bg="black")
    Label(exit_page, text="Are you sure you want to quit: ", bg="black", fg="orange red", font="Corbel 16 bold").grid(row=2)
    Label(exit_page, text="", bg="black").grid(row=3)
    yes_button=Button(exit_page, text="YES", width=20, height=2, command=quit).grid(row=4)
    Label(exit_page, text="", bg="black").grid(row=5)
    no_button = Button(exit_page, text="NO", width=20, height=2, command=exit_page.destroy).grid(row=6)

def ins():
    ins_page=Toplevel()
    ins_page.resizable(0, 0)
    ins_page.title("Adventure Game - Instructions")
    ins_page.geometry("360x200")
    ins_page.configure(bg="black")
    Label(ins_page, text="Instructions: ", bg="black", fg="thistle3", font="Corbel 20 bold").grid(row=2)
    Label(ins_page, text=README, bg="black", fg="thistle3", font="Corbel 12",wraplength=390,justify="left").grid(row=4,sticky=W)
    Label(ins_page, text="", bg="black").grid(row=5)
    Button(ins_page, text="Close Window", width=20, height=2, command=ins_page.destroy).grid(row=6)

def about():
    abt_page=Toplevel()
    abt_page.resizable(0, 0)
    abt_page.title("Adventure Game - About")
    abt_page.geometry("420x350")
    abt_page.configure(bg="black")
    about_heading=Label(abt_page, text="About: ", bg="black", fg="thistle3", font="Corbel 20 bold").grid(row=2)
    Label(abt_page, text=ABOUT, bg="black", fg="thistle3", font="Corbel 11", wraplength=410, justify="left").grid(row=4,sticky=W)
    Label(abt_page, text="", bg="black").grid(row=5)
    Button(abt_page, text="Close Window", width=20, height=2, command=abt_page.destroy).grid(row=6)


def srt():
    main = Toplevel()
    main.geometry("360x260")
    main.resizable(0, 0)
    main.configure(bg="black")
    Label(main, text="GAME: ", bg="black", fg="thistle3", font="Corbel 20 bold").grid(row=2)
    Label(main, text="", bg="black").grid(row=3)
    Label(main, text=console_ins, bg="black", fg="thistle3", font="Corbel 12 bold", wraplength=330, justify="left").grid(row=4)
    Label(main,text="",bg="black").grid(row=5)
    Button(main, text="START", width=20, height=2, command=main_game).grid(row=6)
    Label(main, text="", bg="black").grid(row=7)
    Button(main, text="Close Window", width=20, height=2, command=main.destroy).grid(row=8)


#________MAIN WINDOW
window=Tk()
window.title("Adventure game - Main Menu")
window.configure(background="black")
window.geometry("320x320")
window.resizable(0, 0)
#Heading
Label (window,text="Welcome to the adventure game!",bg="black",fg="thistle3",font="Corbel 16 bold").grid(row=2)
#Start Button
Label(window,text="",bg="black").grid(row=3)
Button(window,text="START",width=20,height=2,command=srt).grid(row=4)
#Instructions button
Label(window,text="",bg="black").grid(row=5)
Button(window,text="INSTRUCTIONS",width=20,height=2,command=ins).grid(row=6)
#About button
Label(window,text="",bg="black").grid(row=7)
Button(window,text="ABOUT",width=20,height=2,command=about).grid(row=8)
#Quit Button
Label(window,text="",bg="black").grid(row=9)
Button(window,text="QUIT",width=20,height=2,command=esc).grid(row=10)



window.mainloop()
