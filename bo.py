import time
import random

weaponlist = []
gun = "gun"

def vraag18():
    answer1 = input("""je vindt het nog steeds erg die dood van je familie, ga je toch zelfmoord plegen? ja of nee
    """)
    if answer1 == "ja":
        print ("""je pleegden zelfmoord en hing te rusten aan een boom.""")
        vraag4(weaponlist, gun)
    elif answer1 == "nee":
        print ("je bleef bij de taliban en bleef mensen gruwelijk vermoorden")
        vraag4(weaponlist, gun)

    else:
        vraag18(weaponlist)

def vraag17(weaponlist):
    answer1 = input("""je hebt erge verdriet door de dood van je familie wat doe je.
    a = ga je van de taliban vluchten
    of b = doorgaan als taliban strijder
    """)
    if answer1 == "a":
        print ("""je bent met succes gevlucht en kwam toevallig aan in de buurt van een vliegveld.""")
        vraag4(weaponlist, gun)
    elif answer1 == "b":
        print ("je besloot te voet te gaan.")
        vraag4(weaponlist, gun)

    else:
        vraag17(weaponlist)

def vraag16(weaponlist):
    answer1 = input("""je hebt erge verdriet door de dood van je familie wat doe je.
    a = ga je van de taliban vluchten
    of b = doorgaan als taliban strijder
    """)
    if answer1 == "a":
        print ("""je bent met succes gevlucht en kwam toevallig aan in de buurt van een vliegveld.""")
        vraag17()
    elif answer1 == "b":
        print ("je blijft mensen doden en terorizeren.")
        vraag18()

    else:
        vraag16(weaponlist)

def vraag15(weaponlist):
    answer1 = input("""je hebt je ouders vermoord hoe nu verder.
    a. pleeg zelfmoord
    b. tegen taliban  strijden 
    of c. zo verder gaan
    """)
    if answer1 == "a":
        print ("""je wou toch de taliban laten boeten,
        en ging zelf moordend naar het kamp en schoot overal, maar na een tijdje werdt jij neergeschoten.""")
        exit()
    elif answer1 == "b":
        print ("de taliban doodden je")
        vraag15(weaponlist)
    elif answer1 == "c":
        print ("je ging verder als taliban strijder.")
        vraag14(weaponlist)

    else:
        vraag16(weaponlist)

def vraag14(weaponlist):
    answer1 = input("""wil je het leger uit vluchten? 
    ja of nee
    """)
    if answer1 == "ja":
        print ("""je fammilie was geobserdeerd met de taliban en schoten je neer door verraad.""")
        exit()
    elif answer1 == "nee":
        print ("je vluchten niet en bleef anderen afhanen doden, en je hebt er plezier in. voor eeuwig.")
        exit()

    else:
        vraag14(weaponlist)

def vraag13(weaponlist):
    answer1 = input("""je ging naar de aangewezen plek en melde je met succes aan bij de taliban.
    je wordt als soldaat het veld opgestuur en je ziet je ouders wat doe je. 
    a = je schiet ze neer 
    b = laat ze met rust 
    of c haal ze over om aan te sluiten
    """)
    if answer1 == "a":
        print ("""je schoot ze neer en je hebt daar veel verdriet van.""")
        vraag15(weaponlist)
    elif answer1 == "b":
        print ("je liet ze met rust maar ze werden later door een collega neergeschoten")
        vraag15(weaponlist)
    elif answer1 == "c":
        print ("je probeerden het en daardoor sloten ze bij je aan want ze wilden niet dood.")
        vraag14(weaponlist)

    else:
        vraag13(weaponlist)

def vraag12(weaponlist):
    answer1 = input("""je gaat naar griekenland hoe?
    a = met een gestolen auto of 
    b = te voet of
    c te kameel
    (vraag6)
    """)
    if answer1 == "a":
        print ("""een taliban soldaat kwam je tegen en schoot je neer""")
        exit()
    elif answer1 == "b":
        print ("je stool wat net voor de taliban soldaat om de hoek je zag je overleefden jhet en komt aan bij een vliegveld")
        vraag4(weaponlist, gun)
    elif answer1 == "c":
        print ("je stool wat net voor de taliban soldaat om de hoek je zag je overleefden jhet en komt aan bij een vliegveld")
        vraag4(weaponlist, gun)

    else:
        vraag12(weaponlist)

def vraag11(weaponlist):
    answer1 = input("""je huurde een kameel met al je geld en gaat met brute fors erdoorheen.
    je hebt extreme honger en vergaat bijna van de dorst.
    a = ga je voedsel en drinken stelen
    of b bedelen ervoor
    """)
    if answer1 == "b":
        print ("""een taliban soldaat kwam je tegen en schoot je neer""")
        exit()
    elif answer1 == "a":
        print ("je stool wat net voor de taliban soldaat om de hoek je zag je overleefden jhet en komt aan bij een vliegveld")
        vraag4(weaponlist, gun)


    else:
        vraag11(weaponlist)

def vraag10(weaponlist):
    answer1 = input("""je gaat naar het vliegveld maar het is een eind verder op hoe ga je. 
    a = te voet of 
    b = met de auto
    """)
    if answer1 == "a":
        print ("""je hebt het gehaald maar bent heel erg uitgeput""")
        vraag4(weaponlist, gun)
    elif answer1 == "b":
        print ("de hele rit was je erg bang. maar je bent er levend gekomen")
        vraag4(weaponlist, gun)

    else:
        vraag10(weaponlist)


def vraag9(weaponlist):
    answer1 = input("""je ging erheen en je kreeg de verblijfsvergunning en ging leren.
    breng je je familie naar nederland ja of nee
    """)
    if answer1 == "nee":
        print ("""je fammilie ging dood en je zag ze nooit meer terug""")
        exit()
    elif answer1 == "ja":
        print ("je familie overleefden de tocht en je bent herenigt met je familie, je hebt een goede baan en een goed onderkomen.")
        exit()

    else:
        vraag9(weaponlist)



def vraag8(weaponlist):
    answer1 = input("""je bent illegaal in nederland gekomen hoe nu verder?
    a = je gaat naar een random politie agent en vraagt de weg
    b = of je loopt naar de bali van het vliegveld
    """)
    if answer1 == "a":
        print ("""de agent begreep je en wees de weg naar waar je je kan regristreren""")
        vraag9(weaponlist)
    elif answer1 == "b":
        print ("je liep naar de bali en legden alles uit, maaar ze deed haar werk en zond je weer uit en werdt vermoordt door de taliban")
        exit()

    else:
        vraag8(weaponlist)

def vraag7(weaponlist):
    print("""je gaat de woestijn
    """)
    if "voet" in weaponlist:
        if "inslaan" in weaponlist:
            print ("""je gaat de woestijn in met drinken en eten""")
            print("en je overleeft met veel energie")
        numbers = [1, 2, 3, 4, 5]
        liveordie = (random.choice(numbers))
        if liveordie == 1:
            print ("you made it")
        else:
            exit()    
        
    elif "kameel" in weaponlist:
        if "inslaan" in weaponlist:
            print ("de woestijn heb je overleeft en je voelt je nog energiek")
            vraag10(weaponlist)
        print("je bent erdoorheen maar voelt je slap en hongerig en dorstig")

    else:
        vraag7(weaponlist)

def vraag6(weaponlist):
    answer1 = input("""je gaat de woestijn in ga je inslaan? ja of nee
    """)
    if answer1 == "ja":
        print ("""je gaat de woestijn in met drinken en eten""")
        weaponlist.append("inslaan")
        vraag10(weaponlist)
    elif answer1 == "nee":
        print ("mooi je weet waar je heen wilt nu de reis nog overleven.")
        vraag10(weaponlist)

    else:
        vraag5(weaponlist)

def vraag5(weaponlist):
    answer1 = input("""je besloot naar nederland te gaan vluchten hoe?
    a = te voet 
    b = te kameel
    c = te vliegtuig
    """)
    if answer1 == "a":
        print ("""je gaat te voet""")
        weaponlist.append("voet")
        vraag12(weaponlist)
    elif answer1 == "b":
        print ("mooi je gaat te kameel.")
        weaponlist.append("kameel")
        vraag11(weaponlist)
    elif answer1 == "c":
        print ("mooie keus en een leuke ook, je gaat met het vliegtuig")
        vraag4(weaponlist, gun)

    else:
        vraag5(weaponlist)

def vraag4(weaponlist, gun):
    answer1 = input("""a. je bent naar het vliegveld gegaan, om met vliegtuig te vluchten 
    (je merkt een man op met een grote koffer die zich verdacht gedraagt wat ga je doen a het vliegveld uitrennen,
    of b hem vragen waarom hij verdacht gedraagt of 
    c je valt hem aan)
    """)
    numbers = [1, 2]
    if answer1 == "a":
        print("je renden het vliegtuig uit en ooverleefden de tocht, zonder te ontploffen door de terrorist.")
        

    elif answer1 == "c":
        print ("je valt hem aan met al je kracht")
        
        liveordie = (random.choice(numbers))
        if gun in weaponlist:
            print("leven je bent veilig aangekomen in bestemmingsland")
            if "nederland" in weaponlist:
                vraag8(weaponlist)
        if liveordie == 1:
            print("leven je bent veilig aangekomen in bestemmingsland als nederland() je bent in nederland aangekomen wat doe je?")
            if "nederland" in weaponlist:
                vraag8(weaponlist)
        elif liveordie != 1:
            print(" maar je ging dood")
            exit()
            
    elif answer1 == "b":
        print ("hij vertelde je de waarheid niet en terroriseerden jouw vliegtuig")
        
    else:
        vraag4()


def vraag3(weaponlist):
    answer1 = input("""b. je bent met succes gevlucht, waar ga je nu heen
    (a. je oma in pakistan 
    b. nederland 
    c. griekenland)(vraag2)
    """)
    
    if answer1 == "a":
        print ("""mooi je weet waar je heen wilt nu de reis nog overleven.)
        """)
        vraag4(weaponlist, gun)
    elif answer1 == "b":
        print ("mooi je weet waar je heen wilt nu de reis nog overleven.")
        weaponlist.append("nederland")
        vraag5(weaponlist)
    elif answer1 == "c":
        print("mooi je weet waar je heen wilt nu de reis nog overleven.")
        vraag12(weaponlist, gun)
    else:
        vraag3()

def vraag2(gun, weaponlist):
    answer1 = input("""je bent niet gevlucht en de taliban zijn al in de buurt van je stadje, je ziet een taliban strijder wat ga je doen?
    (a. je vraagt hem of en waar je je kan aansluiten 
    b.je doet een poging op moord 
    c. je geeft je over aan de taliban)
    """)
    numbers = [1, 2]
    if answer1 == "a":
        print("hij wees je de weg en legden uit hoe je je in kan schrijven")
        vraag13(weaponlist)

    elif answer1 == "b":      
        print ("je stromt op hem af en...")
        liveordie = (random.choice(numbers))
        if liveordie == 1:
            weaponlist.append(gun)
        if liveordie == 1:
            time.sleep(0.5)
            print("you still live")
            time.sleep(0.5)
            print("je hebt een geweer nu met kogels")
            time.sleep(0.1)
            answer2 = input("vlucht je of blijf je. ja of nee typen")
            if answer2 == "nee":
                print("de taliban doodde je")
                exit()
            if answer2 == "ja":
                print("je leeft")
                vraag3(weaponlist)
            else:
                vraag2()
        elif liveordie != 1:
            print("you died")
            exit()
        vraag2()
    elif answer1 == "c":
        print ("mooi je weet waar je heen wilt nu de reis nog overleven")
        exit()
    else:
        vraag1()

def vraag1():
    answer1 = input("""je bent geboren en getogen in afghanistan, en je bent daar heel blij. je bent ongeveer 16 jaar oud en je hebt op school veel plezier.
je ouders zijn heel succesvol en hebben best wat geld, maar opeens stormen de taliban je land in en brengen oorlog.
je bent heel bang en je hoort van je ouders dat je moet vluchten, waar wil heen vluchten(a = de woestijn,b = een stad paar kilomer verderop of c = je wilt niet vluchten):""")
    if answer1 == "c":
        print("you stayed")
        vraag2(gun, weaponlist)
    elif answer1 == "b":
        print ("je bent met succes gevlucht en overleefde het dus ook.")
        vraag3(weaponlist)
    elif answer1 == "a":
        print("je bent hartstikke dood(einde)")
        exit()
    else:
        vraag1()
vraag1()
