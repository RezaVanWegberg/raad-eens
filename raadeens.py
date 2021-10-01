score = 0
ronde = 1

game = True
while game:
        from random import randint, randrange
        nummer = randint(1,1000)

        for x in range(10):
            gok = int(input("Gok een nummer van 1 t/m 1000 "))
            if gok == nummer:
                print("Goed gegokt!")
                score += 1
                ronde += 1
                break
            elif gok  > nummer and gok < nummer + 50:
                print("Jouw getal is HOGER, maar zit maximaal 50 getallen ernaast")
            elif gok < nummer and gok > nummer - 50:
                print("Jouw getal is LAGER, maar zit maximaal 50 getallen ernaast")
            elif gok > nummer:
                print("Jouw getal is HOGER dan het geheime getal")
            elif gok < nummer:
                print("Jouw getal is LAGER dan het geheime getal")  
        if gok != nummer:
            print("Helaas heb je het niet kunnen gokken. Het getal was " + str(nummer))
            ronde += 1    
        vraagkeuze = input("Wilt u nog door gaan? J/N ")
        if vraagkeuze == "J":
            print("Oke, dan gaan we nog een keer")
            print("Dit is nu de score: [" + str(score) + "] En de ronde is " + str(ronde) + "/20")
        elif vraagkeuze == "N":
            print("Oke, bedankt voor het spelen")
            game = False
        else:
            game = False
            print("Error bij ronde " + str(ronde) + "/20")
            print("Je eind score was : [" + str(score) + "]")
if ronde == 20 or vraagkeuze == "N":
    game = False            
    print("Je eind score was : [" + str(score) + "]")    