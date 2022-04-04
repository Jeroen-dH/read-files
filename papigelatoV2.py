import yaml
with open(r"C:\Users\Jeroen\Desktop\Projecten\read-files\settings.yml", "r") as file:
    ymlimport = yaml.safe_load(file)
    print(ymlimport)
aantalbollen = 0
horentje = 0
bakje = 0
liter = 0

def toppings(aantalbollen,BakjeOfHorentje):
    topping = input ("Wat voor topping wilt u: A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus?")
    if topping == 'a':
        stap3(aantalbollen,BakjeOfHorentje,topping)
    elif topping == 'b':
        topping = 'slagroom'
        stap3(aantalbollen,BakjeOfHorentje,topping)
    elif topping == 'c':
        topping = 'Sprinkels'
        stap3(aantalbollen,BakjeOfHorentje,topping)
    elif topping == 'd':
        topping = 'Caramel Saus'
        stap3(aantalbollen,BakjeOfHorentje,topping)
    else: 
        print("Sorry dat is geen optie die we aanbieden...")
        toppings(aantalbollen,BakjeOfHorentje)

def stap2(aantalbollen):
    BakjeOfHorentje = input('Wilt u deze '+str(aantalbollen)+' bolletje(s) in A) een hoorntje of B) een bakje?: ')
    if BakjeOfHorentje == 'B'.lower():
        BakjeOfHorentje = 'bakje'
        toppings(aantalbollen,BakjeOfHorentje)
    elif BakjeOfHorentje == 'A'.lower():
        BakjeOfHorentje = 'horentje'
        toppings(aantalbollen,BakjeOfHorentje)
    else:
        print("Sorry dat is geen optie die we aanbieden...\n")
        stap2(aantalbollen)

def stap3(aantalbollen, BakjeOfHorentje, topping):
    meerbestellen = input("Hier is uw "+ str(BakjeOfHorentje) +" met " + str(aantalbollen) +" bolletje(s). Wilt u nog meer bestellen? (Y/N): ")
    if meerbestellen == 'Y'.lower():
        stap1()
    elif meerbestellen == 'N'.lower():
        bonnetje(aantalbollen, BakjeOfHorentje, topping)
        print("Bedankt en tot ziens!")
    else:
        print("Sorry dat is geen optie die we aanbieden...\n")
        stap3(aantalbollen,BakjeOfHorentje,topping)


def stap1():
    bollen = input("Hoeveel bolletjes wilt u?: ")
    bollen2 = int(bollen)
    global aantalbollen
    aantalbollen += bollen2
    if aantalbollen >= int(9):
        print("sorry, maar u moet minder bollen kiezen\n")
        stap1()
    elif aantalbollen >= int(4):
        print("dan krijgt u van mij een bakje met",aantalbollen,"bollen.\n")
        BakjeOfHorentje = 'bakje'
        smaken(aantalbollen)
        stap3(aantalbollen, BakjeOfHorentje)
    elif aantalbollen >= int(1):
        smaken(aantalbollen)
        stap2(aantalbollen)
    
    else:
        print("Sorry dat is geen optie die we aanbieden...\n")
        stap1()

def begin():
    a = input("Ben u A. particulier of B. zakelijk? : ")
    if a == 'A'.lower():
        stap1()
    elif a == 'B'.lower():
        stapZ()
    else:
        print("Dat snap ik niet....")
        begin()

def smaken(aantalbollen):
    a = 1
    while a <= int(aantalbollen):
        hoi = input(" welke smaak wilt u voor bolletje "+ str(a) +" ? Aardbei(a), chocolade(C) of vanille(v).: ")
        a = a + 1
        if hoi != "A".lower() and hoi != "C".lower() and hoi != "V".lower():
            print("Sorry dat is geen optie die we aanbieden...")
            smaken(aantalbollen)

def smaakzakelijk(liters):
    a = 1
    while a <= int(liters):
        hoi = input("Welke smaak wilt u voor liter " + str(a) + "Aardbei(a), chocolade(C) of vanille(v).: ")
        if hoi != "A".lower() and hoi != "C".lower() and hoi != "V".lower():
            print("sorry dit snap ik niet....")
            smaakzakelijk(liter)
        else: 
            a = a + 1

def stapZ():
    liters = input("\nHoeveel liters wilt u bestellen? : ")
    if liters >= '1':
        smaakzakelijk(liters)
        bonnetje2(liters)
    else:
        print("Sorry dat is geen optie die we aanbieden....\n")
        stapZ()

 

def bonnetje(aantalbollen, BakjeOfHorentje, topping):
    print("---------------","papi-gelato","---------------\n")
    if aantalbollen >= 1:
        print("Bolletjes       ", str(aantalbollen),"x €",ymlimport["bolletjes"],  "    =", aantalbollen * ymlimport["bolletjes"])
    if BakjeOfHorentje == 'bakje':
        print("Bakje            1 x","€",ymlimport["bakjes"],"    =",1*ymlimport["bakjes"])
    elif BakjeOfHorentje == 'horentje':
        print("horentje         1 x €",ymlimport["hoorentjes"],"    =",1*ymlimport["hoorentjes"])
    if topping == 'slagroom':
        print("topping          1 x €",ymlimport["toppings"]["slagroom"],"    =",(1*ymlimport["toppings"]["slagroom"]))
        print("                              ------- +\ntotaal                        =",(aantalbollen * 0,95 + 1.25 + ymlimport["toppings"]["slagroom"]) )
    elif topping == 'Sprinkels':
        print("topping          1 x €",ymlimport["toppings"]["sprinkels"],"    =",(1*ymlimport["toppings"]["sprinkels"]))
        print("                              ------- +\ntotaal                        =",(aantalbollen * 0,95 + 1.25 + ymlimport["toppings"]["sprinkels"]) )
    elif topping == 'Caramel Saus':
        print("topping          1 x €",ymlimport["toppings"]["caramel"]
        ,"    =",(1*ymlimport["toppings"]["caramel"]))
        print("                              ------- +\ntotaal                        =",(aantalbollen * 0,95 + 1.25 + int(ymlimport["toppings"]["caramel"]) ))

def bonnetje2(liters):
    som = (float(liters) * 9.80)
    print("---------------","papi-gelato","---------------\n")
    print(liters + ". Liter         "+ liters + "x €",ymlimport["liter"],   "    =", (float(liters) * ymlimport["liter"]))
    print("                               ------- +\ntotaal                        =", som)
    print("BTW (",ymlimport["btw"],")                      =", som/100*ymlimport["btw"])
    print("Bedankt en tot ziens!")
    
print("*\n*Welkom bij Papi Gelato.\n*")
begin()