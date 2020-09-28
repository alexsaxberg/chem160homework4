from cards import *
ntrials=1000
awins=0
tie=0
for i in range(ntrials):
    adeck=deck()
    adeck.shuffle()
    bdeck=deck()
    bdeck.shuffle()
    ascore=0
    bscore=0
    while adeck.cardsleft()>0 and bdeck.cardsleft()>0:
        acard=adeck.dealcard()
        bcard=bdeck.dealcard()
        if acard.value()>bcard.value():
            ascore+=1
        else:
            bscore+=1
    if ascore==bscore:
            tie+=1
    

print("tie percentage=",tie/ntrials)
