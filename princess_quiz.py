tone = 0 
scorch = 0 
ronin = 0 
northstar = 0 
monarch = 0 
ion = 0 
legion = 0 
notitan = 0
print("Titan Picker ! ")
#question 1
answer = input("What giant robot size do you prefer ? (l)arge, (m)edium, or (s)mall or (n)o titan at all ")
if answer == 'l':
    legion+=1
    scorch+=1
elif answer == 'm':
    tone+=1
    monarch+=1
    ion+=1
elif answer == 's':
    ronin+=1
    northstar+=1
elif answer == 'n':
    notitan+=90

answer2 == input("How fast do you want your titan to move? (v)ery fast, (n)ormal speed, or (s)low")
if answer == 'v':
    northstar+=1
    ronin==1
elif answer == 'n':
    ion+=1
    tone+=1
    monarch+=1
elif answer == 's':
    legion+=1
    scorch+=1

    answer3 == input(" What range do you like to fight at? (c)lose range, (m)edium range, (l)ong range.")
    if answer == 'c':
        ronin+=1
    elif answer == 'm':
        monarch+=1

    elif answer == 'l':
        legion+=1
        ion+=1
        northstar+=1
        tone+=1
    answer4 == input("what type of weapon sounds cooler for a giant robot to have ? (s)hotgun/sword, (r)ailgun, (m)inigun, (c)annon, (e)nergy rifle,)(t)hermite luancher, or (n)ormal gun")
    if answer == 's':
        ronin+=1
    elif answer == 'r':
        northstar+=1
    elif answer == 'm':
        legion+=1
    elif answer == 'c':
        tone+=1
    elif answer == 'e':
        ion+=1
    elif answer == 'n':
        monarch+=1
    elif answer == 't':
        scorch+=1
    answer5 == input("what titan class sounds coolest? (a)tlas, (s)trider, or (o)gre")
    if answer == 'a':
        ion+=1
        tone+=1
        monarch+=1
    elif answer == 's':
        northstar+=1
        ronin+=1


    elif answer == 'o':
        scorch+=1
        legion+=1
    answer == input("What Titan is best ? (b)T, (n)orthstar, (l)egion, (s)corch, (r)onin, (i)on, (m)onarch, or (t)one ")
    
    if answer == 'b':
        print ("That is the only right answer")

    elif answer == 'n':
        northstar+=1
    elif answer == 'l':
        legion+=1
    elif answer == 's':
        scorch+=1
    elif answer == 'r':
        ronin+=1
    elif answer == 'i':
        ion+=1
    elif answer == 'm':
        monarch+=1
    elif answer == 't':
        tone+=1
    #results 
        #Northstar
    if northstar > legion and northstar > monarch and northstar > ion and northstar > ronin and northstar > scorch and northstar > tone :
        print("You Get a Northstar Titan !")
        #Legion
    elif legion > northstar and legion > monarch and legion > ion and legion > ronin and legion > scorch and legion > tone :
        print("You get a Legion Titan ! ")
        #Ronin
    elif ronin > legion and ronin > monarch and ronin > ion and ronin > northstar and ronin > scorch and ronin > tone :
        print("You get the best Titan , Ronin !")
        #Ion
    elif ion > legion and ion > monarch and ion > northstar and ion > ronin and ion > scorch and ion > tone :
        print("You get a Ion Titan ! ")
        #tone
    elif tone > legion and tone > monarch and tone > ion and tone > ronin and tone > scorch and tone > northstar :
        print("You should be ashamed of yourself becasue you get a Tone Titan !")
        #Monarch
    elif monarch > legion and monarch > tone and monarch > ion and monarch > ronin and monarch > scorch and monarch > northstar :
        print("You get a Monacrh Titan! ")
    #no titan 
    elif notitan > legion and notitan > tone and notitan > ion and notitan > ronin and notitan > scorch and notitan > northstar :
        print(" You failed everyone , you dont get a titan ")