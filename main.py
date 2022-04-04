import random
import time
import sys

##Set maximum random number
mrnumber=99
mod = ""
unumber = 0



##Create a function to delay print 
def delay_print(s):
  for c in s:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.02)
  print("\n")

##Create the game
def engame():
  ##Generate random number
  rnumber = random.randint(1, mrnumber)
  ##Set user number
  unumber = 0
  ##Create boolean won statement
  won = False
  ##Create loop if won == True game ends
  while won != True:
    delay_print("\nType a number < "+str(mrnumber+1))
    unumber = int(input())
    ##Check if user won
    if rnumber == unumber:
      won = True
      delay_print("\nNice you won!")
      time.sleep(3)
      return
    ##Ask user if he needs a hint
    delay_print("\nDo you need a hint? (YES/no)")
    ##Answer to the hint question
    while True:
      answer = input()
      ##If enter output
      if answer == "":
          if unumber > rnumber:
            delay_print("\nThe number u typed is higher then the random generated number")
            break
          elif unumber < rnumber:
            delay_print("\nThe number u typed is lower then the random generated number.")
            break
         ##If yes output               
      if answer == "yes" or answer== "YES":
          ##Hints
          if unumber > rnumber:
            delay_print("\nThe number u typed is higher then the random generated number.")
            break
          ##Hints
          elif unumber < rnumber:
            delay_print("\nThe number u typed is lower then the random generated number.")
            break
        ##If no output
      elif answer == "no" or answer == "NO":
        delay_print("Ok, try again")
        break
        ##If answer is something not recognized gives error
      elif answer != "no" or answer != "yes":
        delay_print("Error: type yes/no")

##Tutorial
def entutorial():
  delay_print(" About the game:\n A random number gets generated,\n try to find it you can use the hints to get some help.\n (Comment if u need new kind of hints or more stuff. :D)")
  delay_print(" About the difficulties:\n The default difficulty is set to medium\n Easy difficulty has the maximum random generated number as 9 \n Medium difficulty has the maximum random generated number as 99\n Hard difficulty has the maximum random generated number as 999\n Custom difficulty has the maximum random generated number as a custom number.")
  time.sleep(3)
  return

##Difficulties
def endifficulties():
  global mrnumber
  delay_print("\n There are 4 difficulties, \n Easy, Medium, Hard, Custom. \n Type E, M, H, C to select the difficulty, \n in the tutorial there will be more explaination about them. \n Type the difficulty you want:")
  
  ##Difficulty statemnts
  while True:
    difficulty=input()
    if difficulty == "E" or difficulty == "e":
      mrnumber=9
      break
    elif difficulty == "M" or difficulty == "m":
      mrnumber=99
      break
    elif difficulty == "H" or difficulty == "h":
      mrnumber=999
      break
    elif difficulty == "C" or difficulty == "c":
      print("Type a max random number 0>")
      mrnumber=int(input())
      break
    elif difficulty != "E" or difficulty != "M" or difficulty != "H" or difficulty != "C" or difficulty != "e" or difficulty != "m" or difficulty != "h" or difficulty !="c":
      delay_print("Error: type E/M/H/C")






      

##italian game
def itgame():
  ##Generate random number
  rnumber = random.randint(1, mrnumber)
  ##Set user number
  unumber = 0
  ##Create boolean won statement
  won = False
  ##Create loop if won == True game ends
  while won != True:
    delay_print("\nInserisci un numero < "+str(mrnumber+1))
    unumber = int(input())
    ##Check if user won
    if rnumber == unumber:
      won = True
      delay_print("\nBravo hai vinto!")
      time.sleep(3)
      return
    ##Ask user if he needs a hint
    delay_print("\nHai bisogno di un indizio? (SI/no)")
    ##Answer to the hint question
    while True:
        answer = input()
        ##If enter output
        if answer == "":
            if unumber > rnumber:
              delay_print("\nIl numero da te inserito è più alto del numero generato randomicamente")
              break
            elif unumber < rnumber:
              delay_print("\nIl numero da te inserito è più basso del numero generato randomicamente")
              break
         ##If yes output               
        if answer == "si" or answer== "SI":
            ##Hints
            if unumber > rnumber:
              delay_print("\nIl numero da te inserito è più alto del numero generato randomicamente")
              break
            ##Hints
            elif unumber < rnumber:
              delay_print("\nIl numero da te inserito è più basso del numero generato randomicamente")
              break
        ##If no output
        elif answer == "no" or answer == "NO":
          delay_print("Ok, riprova")
          break
        ##If answer is something not recognized gives error
        elif answer != "no" or answer != "si":
          delay_print("Error: scrivi si/no")





def close():
  if mrnumber-10==unumber+1 or mrnumber-10==unumber+2 or mrnumber-10==unumber+3 or mrnumber-10==unumber+4 or mrnumber-10==unumber+5 or mrnumber-10==unumber+6 or mrnumber-10==unumber+7 or mrnumber-10==unumber+8 or mrnumber-10==unumber+9 or mrnumber-10==unumber+10 or mrnumber-10==unumber-1 or mrnumber-10==unumber-1 or mrnumber-10==unumber-2 or mrnumber-10==unumber-3 or mrnumber-10==unumber-4 or mrnumber-10==unumber-5 or mrnumber-10==unumber-6 or mrnumber-10==unumber-7 or mrnumber-10==unumber-8 or mrnumber-10==unumber-9 or mrnumber-10==unumber-10:
    print("Close one!")
    
  elif mrnumber+10==unumber-1 or mrnumber+10==unumber-1 or mrnumber+10==unumber-2 or mrnumber+10==unumber-3 or mrnumber+10==unumber-4 or mrnumber+10==unumber-5 or mrnumber+10==unumber-6 or mrnumber+10==unumber-7 or mrnumber+10==unumber-8 or mrnumber+10==unumber-9 or mrnumber+10==unumber-10 or mrnumber+10==unumber+1 or mrnumber+10==unumber+2 or mrnumber+10==unumber+3 or mrnumber+10==unumber+4 or mrnumber+10==unumber+5 or mrnumber+10==unumber+6 or mrnumber+10==unumber+7 or mrnumber+10==unumber+8 or mrnumber+10==unumber+9 or mrnumber+10==unumber+10:
    
    print("Close one!")
          

##italian tutorial
def ittutorial():
  delay_print(" Riguardo il gioco:\n Un numero casuale viene generato,\n prova a trovarlo puoi usare i suggerimenti per ottenere qualche aiuto.\n (Commenta se hai bisogno di un nuovo tipo di suggerimenti o più roba. :D)")
  delay_print(" Riguarda le difficoltà:\n La difficoltà di default è impostata su media\n La difficoltà facile ha il massimo numero generato a caso come 9\n La difficoltà media ha il massimo numero generato a caso come 99\n La difficoltà difficile ha il massimo numero generato a caso come 999\n La difficoltà personalizzata ha il massimo numero generato a caso come un numero personalizzato.")
  time.sleep(3)
  return

##italian difficulties
def itdifficulties():
  global mrnumber
  delay_print("\Ci sono 4 difficoltà: Facile, Media, Difficile, Personalizzata. \Digita E, M, H, C per selezionare la difficoltà, nel tutorial ci saranno ulteriori spiegazioni. \Digita la difficoltà che vuoi:")
  
  ##Difficulty statemnts
  while True:
    difficulty=input()
    if difficulty == "F" or difficulty == "f":
      mrnumber=9
      break
    elif difficulty == "M" or difficulty == "m":
      mrnumber=99
      break
    elif difficulty == "D" or difficulty == "d":
      mrnumber=999
      break
    elif difficulty == "CP" or difficulty == "p":
      print("Digitare il numero massimo casuale 0>")
      mrnumber=int(input())
      break
    elif difficulty != "f" or difficulty != "M" or difficulty != "D" or difficulty != "P" or difficulty != "f" or difficulty != "m" or difficulty != "d" or difficulty !="p":
      delay_print("Error: scrivi F/M/D/P")
##english menu stuff
def enstartprint():
  delay_print("Type P to play the game")
  delay_print("Type D to select the difficulty")
  delay_print("Type T to read the tutorial")
  delay_print("Type L to select a language")
  delay_print("Type X to quit")
##italian menu stuff
def itstartprint():
  delay_print("Scrivi P per giocare,")
  delay_print("Scrivi D per selezionare la difficoltà")
  delay_print("Scrivi T per leggere il tutorial")
  delay_print("Scrivi L per selezionare il linguaggio")
  delay_print("Scrivi X per uscire")
  
##important variables and functions
chosengl=engame
chosent=entutorial
chosend=endifficulties
chosenst=enstartprint

##English select languages
def enlanguages():
  global chosengl
  global chosent
  global chosend
  global chosenl
  global chosenst
  delay_print("\n You can select 2 languages at the moment (Italian/English).\n")

  global answer
  answer=""
  delay_print(" Type Italian or English to select the language.")
  while True:
    

    
    answer=input()
    
    if answer=="Italian" or answer == "italian" or answer=="ITALIAN":
      chosengl=itgame
      chosent=ittutorial
      chosend=itdifficulties
      chosenl="ITALIAN"
      chosenst=itstartprint
      break
    elif answer =="English" or answer == "english" or answer=="ENGLISH":
      chosengl=engame
      chosent=entutorial
      chosend=endifficulties
      chosenst=enstartprint
      break

    elif answer!="English" or answer != "english" or answer!="ENGLISH" or answer != "Italian" or answer != "italian" or answer!="ITALIAN":
      print("Error: type Italian/English")


##Italian select languages
def itlanguages():
  global chosengl
  global chosent
  global chosend
  global chosenl
  global chosenst
  delay_print("\n È possibile selezionare 2 lingue al momento (italiano/inglese).\n")

  global answer
  answer=""
  delay_print(" Digita italiano o inglese per selezionare la lingua.")
  while True:
    
    answer=input()
    
    if answer=="Italiano" or answer == "italiano" or answer=="ITALIANO":
      chosengl=itgame
      chosent=ittutorial
      chosend=itdifficulties
      chosenl="ITALIAN"
      chosenst=itstartprint
      break
    elif answer =="Inglese" or answer == "inglese" or answer=="INGLESE":
      chosengl=engame
      chosent=entutorial
      chosend=endifficulties
      chosenst=enstartprint
      break

    elif answer!="Inglese" or answer != "inglese" or answer!="INGLESE" or answer != "Italiano" or answer != "italiano" or answer!="ITALIANO":
      print("Error: scrivere Italiano/Inglese")


      
chosenl="" 
while mod != "X" and mod != "x":
  ##Some user stuff
  chosenst()
  
  mod = input()

  if mod == "P" or mod == "p":
    chosengl()

  if mod == "T" or mod == "t":
    chosent()

  if mod == "D" or mod == "d":
    chosend()

  if mod == "L" or mod == "l":
    if chosenl=="ITALIAN":
      itlanguages()
    enlanguages()
    

#Hope u liked it :)