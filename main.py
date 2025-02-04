import random as r
global turn
global shots
global dealerHealth
global playerHealth
global damage
#turn 0 is dealer, turn 1 is player
turn = 0
damage = 1
shots = []
items = ["beer", "saw", "cigarettes", "handcuffs", "magnifyingGlass"]
playerInv = []
dealerInv = []
dealerHealth = 3
playerHealth = 3
length = r.randint(4, 8)
def beer():
    global shots
    global turn
    if (turn <= 0) & ("beer" in dealerInv):
        dealerInv.remove("beer")
        shots.pop(0)
    elif (turn >= 1) & ("beer" in playerInv):
        playerInv.remove("beer")
        shots.pop(0)
def handSaw():
    global turn
    if (turn <= 0) & ("saw" in dealerInv):
        dealerInv.remove("saw")
        damage = 2
    elif (turn >= 1) & ("saw" in playerInv):
        playerInv.remove("saw")
        damage = 2
def cigarettes():
    global turn
    if (turn <= 0) & ("cigarettes" in dealerInv):
        dealerInv.remove("cigarettes")
        dealerHealth += 1
    elif (turn >= 1) & ("cigarettes" in playerInv):
        playerInv.remove("cigarettes")
        playerHealth += 1
def handcuffs():
    global turn
    if (turn <= 0) & ("handcuffs" in dealerInv):
        dealerInv.remove("handcuffs")
        turn -= 1
    elif (turn >= 1) & ("handcuffs" in playerInv):
        playerInv.remove("handcuffs")
        turn += 1
def magnifyingGlass():
    global turn
    if (turn <= 0) & ("magnifyingGlass" in dealerInv):
        dealerInv.remove("magnifyingGlass")
        print(shots[0])
    elif (turn >= 1) & ("magnifyingGlass" in playerInv):
        playerInv.remove("magnifyingGlass")
        print(shots[0])
def reload():
    global turn
    while len(shots) <= length:
        shots.append(r.randint(0, 1))
    saveshots()
    while len(playerInv) < 4:
        playerInv.append(items[r.randint(0, 4)])
        print ("Player Inventory: " + str(playerInv))
    while len(dealerInv) < 4:
        dealerInv.append(items[r.randint(0, 4)])
        print ("Dealer Inventory: " + str(dealerInv))
def saveshots():
    global turn
    global live
    global blank
    live = 0
    blank = 0
    for i in range (len(shots)):
        if shots[i] == 0:
            blank += 1
        else:
            live += 1
def selfShot():
    global dealerHealth
    global playerHealth
    global turn
    if shots[0] == 1:
        if turn <= 0:
            dealerHealth -= damage
            turn += 1
        else:
            playerHealth -= damage
            turn -= 1
    elif turn >= 0:
        turn -= 1
    else:
        turn += 1
    del shots[0]
    if len(shots) == 0:
        reload()
    else:
        saveshots()
def otherShot():
    global dealerHealth
    global playerHealth
    global turn
    if shots[0] == 1:
        if turn <= 0:
            playerHealth -= damage
            turn += 1
        else:
            dealerHealth -= damage
            turn -= 1
    shots.pop(0)

    if len(shots) == 0:
        reload()
    else:
        saveshots()
reload()
saveshots()
print("Live Rounds: " + str(live))
print("Blank Rounds: " + str(blank))
print(shots)
while playerHealth >= 0 and dealerHealth >= 0:
    while turn == 0:
        decider = r.randint(0, 1)
        if decider == 0:
            selfShot()
        else:
            otherShot()
        saveshots()
        print (decider)
        print("Live Rounds: " + str(live))
        print("Blank Rounds: " + str(blank))
        print(str(dealerHealth) + " / " + str(playerHealth))
        print(shots)
        turn += 1
    itemInput = input("Item? ")
    if itemInput == "beer":
        beer()
    elif itemInput == "saw":
        handSaw()
    elif itemInput == "cigarettes":
        cigarettes()
    elif itemInput == "handcuffs":
        handcuffs()
    elif itemInput == "magnifyingGlass":
        magnifyingGlass()
    pickle = input("self or other?")
    if pickle == "self":
        selfShot()
    elif pickle == "other":
        otherShot()
    turn -= 1
    print(str(dealerHealth) + " / " + str(playerHealth))

