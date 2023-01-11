import sys,random
print("ROCK,PAPER,SCISSOR")
wins=0
loss=0
tie=0
while True:
    print("Enter your move r for ROCK p for PAPER s for SCISSOR q for quit")
    playerMove=input()
    print("Lost"+str(loss))
    print("Won"+str(wins))
    print("Tie"+str(tie))
    if playerMove=='q':
        sys.exit()
    if playerMove=='r':
        print("You choose ROCK")
    if playerMove=='p':
        print("You choose PAPER")
    if playerMove=='s':
        print("You choose SCISSOR")
    computersChoice=random.randint(1,3)
    if computersChoice==1:
        computerMove='r'
        print("Computer choose rock")
    if computersChoice==2:
        computerMove='p'
        print("Computer choose paper")
    if computersChoice==3:
        computerMove='s'
        print("Computer choose scissor")
    if computerMove=='r' and playerMove=='p' :
        print("Player won")
        wins=wins+1
    elif computerMove=='p' and playerMove=='s':
        print("Player won")
        wins=wins+1
    elif computerMove=='s' and playerMove=='r':
        print("Player won")
        wins=wins+1
    elif computerMove==playerMove:
        print("Tie")
        tie=tie+1
    else:
        print("Computer won")
        loss=loss+1

    