def lobbyChoice():
    print("\nYou return to the lobby...")
    selectionInput = input("\nDo you want to choose another door or do you wish to leave? (door or leave)")
    if selectionInput == "door" or selectionInput == "Door":
        doorSelection()
    elif selectionInput == "leave" or selectionInput == "Leave":
        print("Thank you for visiting The Rooms...\nBUT YOU CAN NEVER LEAVE HAHAHAHA\n*The exit has disappeared*\n"
              "You must keep exploring till the end")


#############################################

# Room 1
def room1():
    print("\nYou enter Room 1...\nYou see a painting, a sculpture, and a vase\n")
    room1Response1 = input("What would you like to look at first or would you like to leave Room 1? ")
    if room1Response1.lower() == "painting":
        painting()
        room1Response2 = input(
            "\nWhat would you like to look at the sculpture, or the vase, or would you like to leave Room 1? ")
        if room1Response2.lower() == "sculpture":
            sculpture()
        elif room1Response2.lower() == "vase":
            vase()
        elif room1Response2.lower() == "leave":
            print("\nYou are leaving Room 1...")
            lobbyChoice()

    elif room1Response1.lower() == "sculpture":
        sculpture()
        room1Response2 = input(
            "\nWhat would you like to look at the painting, or the vase, or would you like to leave Room 1? ")
        if room1Response2.lower() == "painting":
            painting()
        elif room1Response2.lower() == "vase":
            vase()
        elif room1Response2.lower() == "leave":
            print("\nYou are leaving Room 1...")
            lobbyChoice()

    elif room1Response1.lower() == "vase":
        vase()
        room1Response2 = input(
            "\nWhat would you like to look at the sculpture, or the painting, or would you like to leave Room 1? ")
        if room1Response2.lower() == "sculpture":
            sculpture()
        elif room1Response2.lower() == "painting":
            painting()
        elif room1Response2.lower() == "leave":
            print("\nYou are leaving Room 1...")
            lobbyChoice()
    else:
        print("This is an invalid choice.")


# Room 1 : painting
def painting():
    print("\nThe painting appears to be colorful but abstract to where you can't understand its meaning...")


# Room 1 : sculpture
def sculpture():
    print("\nThe sculpture appears to be made of granite and looks like Michelangelo's David... seems pretty heavy...")


# Room 1 : vase
def vase():
    print("\nThe vase appears to be made of chinese porcelain and was made during the Qin Dynasty...")


#############################################

# Room 2
def room2():
    print("\nYou enter Room 2...\nYou see a NES, a N64, and a Gameboy\n")
    room2Response1 = input("What would you like to look at first or would you like to leave Room 2? ")
    if room2Response1.lower() == "nes":
        NES()
        room2Response2 = input(
            "\nWhat would you like to look at the N64, or the Gameboy, or would you like to leave Room 2? ")
        if room2Response2.lower() == "N64":
            N64()
        elif room2Response2.lower() == "gameboy":
            Gameboy()
        elif room2Response2.lower() == "leave":
            print("\nYou are leaving Room 2...")
            lobbyChoice()

    elif room2Response1.lower() == "N64":
        N64()
        room2Response2 = input(
            "\nWhat would you like to look at the NES, or the Gameboy, or would you like to leave Room 2? ")
        if room2Response2.lower() == "NES":
            NES()
        elif room2Response2.lower() == "Gameboy":
            Gameboy()
        elif room2Response2.lower() == "leave":
            print("\nYou are leaving Room 2...")
            lobbyChoice()

    elif room2Response1.lower() == "Gameboy":
        Gameboy()
        room2Response2 = input(
            "\nWhat would you like to look at the NES, or the N64, or would you like to leave Room 2? ")
        if room2Response2.lower() == "NES":
            NES()
        elif room2Response2.lower() == "N64":
            N64()
        elif room2Response2.lower() == "leave":
            print("\nYou are leaving Room 2...")
            lobbyChoice()
    else:
        print("This is an invalid choice.")


# Room 2: NES
def NES():
    print("\nIt's a retro gaming system... must have been a pioneer for gaming history.")


# Room 2: N64
def N64():
    print("\nIt's a retro gaming system... seems like it's the NES but better.")


# Room 2: Gameboy
def Gameboy():
    print("\nIt's a retro handheld gaming system... seems like a fun thing to play still.")


#############################################

# Room 3
def room3():
    print("\nYou enter Room 3...\nYou see a sword, a gun, and a bat\n")
    room3Response1 = input("What would you like to look at first or would you like to leave Room 3? ")
    if room3Response1.lower() == "sword":
        sword()
        room3Response2 = input(
            "\nWhat would you like to look at the gun, or the bat, or would you like to leave Room 3? ")
        if room3Response2.lower() == "gun":
            gun()
        elif room3Response2.lower() == "bat":
            bat()
        elif room3Response2.lower() == "leave":
            print("\nYou are leaving Room 3...")
            lobbyChoice()

    elif room3Response1.lower() == "gun":
        gun()
        room3Response2 = input(
            "\nWhat would you like to look at the sword, or the bat, or would you like to leave Room 3? ")
        if room3Response2.lower() == "sword":
            sword()
        elif room3Response2.lower() == "bat":
            bat()
        elif room3Response2.lower() == "leave":
            print("\nYou are leaving Room 3...")
            lobbyChoice()

    elif room3Response1.lower() == "bat":
        bat()
        room3Response2 = input(
            "\nWhat would you like to look at the sword, or the gun, or would you like to leave Room 3? ")
        if room3Response2.lower() == "sword":
            sword()
        elif room3Response2.lower() == "gun":
            gun()
        elif room3Response2.lower() == "leave":
            print("\nYou are leaving Room 3...")
            lobbyChoice()
    else:
        print("This is an invalid choice.")


# Room 3: sword
def sword():
    print("\nIt's very sharp... I should be careful...")


# Room 3: gun
def gun():
    print("\nLooks like a vintage gun you would see in the 1950's or 1960's")


# Room 3: bat
def bat():
    print("\nYou can hurt someone if you swing very hard with this... I shouldn't touch this")


#############################################

# Room 4
def room4():
    print("\nYou enter Room 4...\nYou see a football, a baseball, and a basketball\n")
    room4Response1 = input("What would you like to look at first or would you like to leave Room 4? ")
    if room4Response1.lower() == "football":
        football()
        room4Response2 = input(
            "\nWhat would you like to look at the baseball, or the basketball, or would you like to leave Room 4? ")
        if room4Response2.lower() == "baseball":
            baseball()
        elif room4Response2.lower() == "basketball":
            basketball()
        elif room4Response2.lower() == "leave":
            print("\nYou are leaving Room 4...")
            lobbyChoice()

    elif room4Response1.lower() == "baseball":
        baseball()
        room4Response2 = input(
            "\nWhat would you like to look at the football, or the basketball, or would you like to leave Room 4? ")
        if room4Response2.lower() == "football":
            football()
        elif room4Response2.lower() == "basketball":
            basketball()
        elif room4Response2.lower() == "leave":
            print("\nYou are leaving Room 4...")
            lobbyChoice()

    elif room4Response1.lower() == "basketball":
        basketball()
        room4Response2 = input(
            "\nWhat would you like to look at the football, or the baseball, or would you like to leave Room 4? ")
        if room4Response2.lower() == "football":
            football()
        elif room4Response2.lower() == "baseball":
            baseball()
        elif room4Response2.lower() == "leave":
            print("\nYou are leaving Room 4...")
            lobbyChoice()
    else:
        print("This is an invalid choice.")


# Room 4: football
def football():
    print("\nIt's a football... says NFL on the front of it.")


# Room 4: baseball
def baseball():
    print("\nIt's been used a lot, it's wearing down from the usage.")


# Room 4: basketball
def basketball():
    print("\nLooks brand new, I wonder what it is doing here...")


#############################################

# Room 5
def room5():
    print("\nYou enter Room 5...\nYou see an iPhone, a Samsung, and a flip phone\n")
    room5Response1 = input("What would you like to look at first or would you like to leave Room 5? ")
    if room5Response1.lower() == "iphone":
        iphone()
        room5Response2 = input(
            "\nWhat would you like to look at the Samsung, or the flip phone, or would you like to leave Room 5? ")
        if room5Response2.lower() == "samsung":
            samsung()
        elif room5Response2.lower() == "flip phone":
            flip()
        elif room5Response2.lower() == "leave":
            print("\nYou are leaving Room 5...")
            lobbyChoice()

    elif room5Response1.lower() == "samsung":
        samsung()
        room5Response2 = input(
            "\nWhat would you like to look at the iPhone, or the flip phone, or would you like to leave Room 5? ")
        if room5Response2.lower() == "iphone":
            iphone()
        elif room5Response2.lower() == "flip phone":
            flip()
        elif room5Response2.lower() == "leave":
            print("\nYou are leaving Room 5...")
            lobbyChoice()

    elif room5Response1.lower() == "flip phone":
        flip()
        room5Response2 = input(
            "\nWhat would you like to look at the iPhone, or the Samsung, or would you like to leave Room 5? ")
        if room5Response2.lower() == "iphone":
            iphone()
        elif room5Response2.lower() == "samsung":
            samsung()
        elif room5Response2.lower() == "leave":
            print("\nYou are leaving Room 5...")
            lobbyChoice()
    else:
        print("This is an invalid choice.")


# Room 5: iphone
def iphone():
    print("\nIt's an Apple iPhone, looks like one of the new models...")


# Room 5: samsung
def samsung():
    print("\nIt's a Samsung Galaxy Edge S21. Very Neat...")


# Room 5: flip phone
def flip():
    print("\nIt's a flip phone people used many years ago...")


#############################################

# Room 6
def room6():
    print("\nYou enter Room 6...\nYou see an pencil, a pen, and a marker\n")
    room6Response1 = input("What would you like to look at first or would you like to leave Room 6? ")
    if room6Response1.lower() == "pencil":
        pencil()
        room6Response2 = input(
            "\nWhat would you like to look at the pen, or the marker, or would you like to leave Room 6? ")
        if room6Response2.lower() == "pen":
            pen()
        elif room6Response2.lower() == "marker":
            marker()
        elif room6Response2.lower() == "leave":
            print("\nYou are leaving Room 6...")
            lobbyChoice()

    elif room6Response1.lower() == "pen":
        pen()
        room6Response2 = input(
            "\nWhat would you like to look at the pencil, or the marker, or would you like to leave Room 6? ")
        if room6Response2.lower() == "pencil":
            pencil()
        elif room6Response2.lower() == "marker":
            marker()
        elif room6Response2.lower() == "leave":
            print("\nYou are leaving Room 6...")
            lobbyChoice()

    elif room6Response1.lower() == "marker":
        marker()
        room6Response2 = input(
            "\nWhat would you like to look at the pencil, or the pen, or would you like to leave Room 6? ")
        if room6Response2.lower() == "pencil":
            pencil()
        elif room6Response2.lower() == "pen":
            pen()
        elif room6Response2.lower() == "leave":
            print("\nYou are leaving Room 6...")
            lobbyChoice()
    else:
        print("This is an invalid choice.")


# Room 6: pencil
def pencil():
    print("\nIt's a #2 pencil... nothing much to see here.")


# Room 6: pen
def pen():
    print("\nA black pen, but there's no ink in it.")


# Room 6: marker
def marker():
    print("\nIt's a Blue Sharpie... all the ink has dried up.")


#############################################

# main
def doorSelection():
    while True:
        response1 = input("Which door do you choose? (#1-6) ")

        match response1:
            case "1":
                room1()
            case "2":
                room2()
            case "3":
                room3()
            case "4":
                room4()
            case "5":
                room5()
            case "6":
                room6()
            case "7":
                break
            case _:
                print("\nYour input is invalid... try again")
                continue


def main():
    # starting screen and name
    print("Welcome The Rooms")
    print("-----------------\n")

    name = input("What is your name? ")
    print("Hello", name, "\n")

    # Lobby
    print("You curiously enter a building called The Rooms...\nYou see 6 doors in front of you...")
    response1 = int(input("Which door do you choose first? (#1-6) "))

    if response1 > 6 or response1 < 1:  # check to make sure user chooses a door that is given
        print("this is an invalid choice...\n")
        main()
        return

    doorSelection()  # calling upon the stated function


if __name__ == '__main__':  # initiate a designated main
    main()
