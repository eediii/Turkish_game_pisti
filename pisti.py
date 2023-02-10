import random

cards = ["kup2","kup3","kup4","kup5","kup6","kup7","kup8","kup9","kup10","kupJ","kupQ","kupK","kupA",
        "kar2","kar3","kar4","kar5","kar6","kar7","kar8","kar9","kar10","karJ","karQ","karK","karA",
        "mac2","mac3","mac4","mac5","mac6","mac7","mac8","mac9","mac10","macJ","macQ","macK","macA",
        "sin2","sin3","sin4","sin5","sin6","sin7","sin8","sin9","sin10","sinJ","sinQ","sinK","sinA",
]

first = []
for i in range(0,3):
    r1 = cards[random.randint(0,len(cards)-1)]
    first.append(r1)
    cards.remove(r1)
pc_hand = []
person_hand = []
middle = []
person_score = []
pc_score = []
r = cards[random.randint(0,len(cards)-1)]
middle.append(r)
cards.remove(r)
count = 0
pc = 0
person = 0
pisti_pc = 0
pisti_person = 0
ans = "y"

while ans == "y":
    while  count != 24:
        if pc_hand == []:
            for i in range(0,4):
                r2 = cards[random.randrange(len(cards))]
                pc_hand.append(r2)
                cards.remove(r2)

        if person_hand == []:
            for i in range(0,4):
                r3 = cards[random.randrange(len(cards))]
                person_hand.append(r3)
                cards.remove(r3)

        count+=1    
        if middle != []:
            print("Diğer kartlar :",*middle)
            print("Ortadakı kart :",middle[len(middle)-1])
        for i in range(0,len(person_hand)):
            print(person_hand[i],f'({i+1})')

        choice = int(input("Kart seç aga :"))-1
        if middle != []:
            if person_hand[choice][3:] == middle[len(middle)-1][3:] or person_hand[choice][3:] == "J":
                if len(middle) == 1 and person_hand[choice][3:] != "J":
                    pisti_person=+1
                person = choice
                person_score.append(person_hand[choice])
                person_hand.remove(person_hand[choice])
                for i in range(0,len(middle)):
                    person_score.append(middle[i])
                while first != []:
                    i = 0
                    person_score.append(first[0])
                    first.remove(first[i])
                    i+=1    
                middle = []
                if cards == []:
                    pc=+1
            else:
                middle.append(person_hand[choice])
                person_hand.remove(person_hand[choice])
        else:
            middle.append(person_hand[choice])
            person_hand.remove(person_hand[choice])


        if middle != []:
            my_lovely = []

            for i in range(0,len(pc_hand)):
                if pc_hand[i][3:] == middle[len(middle)-1][3:]:
                    my_lovely.append(pc_hand[i])

            if my_lovely == []:
                for i in range(0,len(pc_hand)):
                    if pc_hand[i][3:] == "J":
                        my_lovely.append(pc_hand[i])

            if my_lovely != []:
                if len(middle) == 1 and my_lovely[0] != "J":
                    pisti_pc=+1
                pc = pc_hand.index(my_lovely[0])
                pc_score.append(my_lovely[0])
                pc_hand.remove(my_lovely[0])
                for i in range(0,len(middle)):
                    pc_score.append(middle[i])
                while first != []:
                    i = 0
                    pc_score.append(first[0])
                    first.remove(first[i])
                    i+=1
                middle = []
                my_lovely = []
            else:
                choice_pc = int((random.randrange(len(pc_hand))))  
                middle.append(pc_hand[choice_pc])
                pc_hand.remove(pc_hand[choice_pc]) 
        else:
            choice_pc = int((random.randrange(len(pc_hand))))  
            middle.append(pc_hand[choice_pc])
            pc_hand.remove(pc_hand[choice_pc]) 

    if pc>person:
        for i in range(0,len(middle)):
            pc_score.append(middle[i])  
    else:
        for i in range(0,len(middle)):
            person_score.append(middle[i])


    scores = ["karJ","macJ","kupJ","sinJ","karA","macA","kupA","sinA"]
    rpc_score = []
    for i in range(0,len(scores)):
        if scores[i] in pc_score:
            rpc_score.append(scores[i])

    rperson_score = []
    for i in range(0,len(scores)):
        if scores[i] in person_score:
            rperson_score.append(scores[i])
            
    if person_score > pc_score:
        for i in range(0,3):
            rperson_score.append("")
    elif person_score < pc_score:
        for i in range(0,3):
            rpc_score.append("")

    for i in range(0,pisti_pc*10):
        rpc_score.append("")
    for i in range(0,pisti_person*10):
        rperson_score.append("")

    if "kar10" in pc_score:
        for i in range(0,3):
            rpc_score.append("")
    else:
        for i in range(0,3):
            rperson_score.append("")

    if "sin2" in pc_score:
        for i in range(0,2):
            rpc_score.append("")
    else:
        for i in range(0,2):
            rperson_score.append("")

    print("Senin skorun :", len(rperson_score))
    print("PC'in skoru :", len(rpc_score))
    ans = input("Again ?(y,n)")
