import random as r
global turn
global shots
global dealerHealth
global playerHealth
#turn 0 is dealer, turn 1 is player
turn = 0
shots = []
playerInv = []
dealerInv = []
dealerHealth = 3
playerHealth = 3
length = r.randint(4, 8)
def beer():
    if turn == 0 && "beer" in dealerInv:
        dealerInv.remove("beer")
        shots.pop[0]
    elif turn == 1 && "beer" in playerInv:
        playerInv.remove("beer")
        shots.pop[0]
def reload():
    while len(shots) <= length:
        shots.append(r.randint(0, 1))
    saveshots()
def saveshots():
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
    if shots[0] == 1:
        if turn == 0:
            dealerHealth -= 1
            turn += 1
        else:
            playerHealth -= 1
            turn -= 1
    elif turn == 0:
        turn -= 1
    else:
        turn += 1
    del shots[0]
    if len(shots) == 0:
        reload()
    else:
        saveshots()
def otherShot():
    if shots[0] == 1:
        if turn == 0:
            playerHealth -= 1
            turn += 1
        else:
            dealerHealth -= 1
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
while True:
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

    pickle = input("self or other?")
    if pickle == "self":
        selfShot()
    elif pickle == "other":
        otherShot()
    turn -= 1
    print(str(dealerHealth) + " / " + str(playerHealth))

