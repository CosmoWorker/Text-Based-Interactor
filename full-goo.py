import random, time, math, csv, secrets, string, webbrowser #mysql.connector as mc
def main(): #main program

    print("_"*90)
    print("                  \t\tDIGITAL INTERACTOR                ")
    print("_"*90)

    def loading(): #loading
        time.sleep(0.2)
        print('\nL',end='')
        time.sleep(0.2)
        print('o',end='')
        time.sleep(0.2)
        print('a',end='')
        time.sleep(0.2)
        print('d',end='')
        time.sleep(0.2)
        print('i',end='')
        time.sleep(0.2)
        print('n',end='')
        time.sleep(0.2)
        print('g',end='')
        time.sleep(0.2)
        print('.',end='')
        time.sleep(0.4)
        print('.',end='')
        time.sleep(0.5)
        print('.',end='')

    time.sleep(1.40)
    print("\nComputer : Hi!, I am your personal digital interactor here with you.")
    time.sleep(1.35)
    print("\nComputer : What do you wanna be called ?")
    na=input("\nUser : ").lower()
    time.sleep(1.45)

    print("\nComputer : How are you", na, "?") #question for the user
    mat=input("\nUser : ").lower()

    if ("what"or "how" and "about" or "are" and "you") in mat: 
        print("\nComputer : Thanks, I am good thank you!.")

    print("\nComputer :", na, ", if you want to do some activities type 'yes', else 'no'")
    uc=input("\nUser : ").lower()
    

    if "no" in uc: #decider 

            p=na.upper()
            print('\n')
            print("_"*90)
            print("\t\t\tTHANK YOU FOR USING OUR PROGRAM",p,'\t\t\t')
            print("_"*90)
            time.sleep(3)   
            exit()
    
    elif "yes" in uc:
        print("\nComputer : Great!, I have a lot of options where you can engange yourself in")
        time.sleep(1)
        print("\n\t   Here are they:\n")
        time.sleep(1)
        def menu(): #2ndary main progain 
            print('\t\t','* '*25)
            print("\t\t *\t\t\t\t\t\t *\n\t\t *\t\t1.Random Number Generator\t *\n\t\t *\t\t2.Math Calculator\t\t *\n\t\t *\t\t3.Mini Games\t\t\t *\n\t\t *\t\t4.Password Generator\t\t *\n\t\t *\t\t5.Make A Toss\t\t\t *\n\t\t *\t\t6.Creating Random Table\t\t *\n\t\t *\t\t7.Roll A Die\t\t\t *\n\t\t *\t\t8.To Use Browser\t\t *\n\t\t *\t\t9.To Exit\t\t\t *\n\t\t *\t\t\t\t\t\t *")
            print('\t\t','* '*25)
            print("\nComputer : Choose which among the one you would be interested in?")
            ch=input("\nUser : ")   
            time.sleep(1)
            while True:
                if ch=="1":
                    print('\n')
                    print('_'*90)
                    print('\n')
                    print('- RANDOM NUMBER GENERATOR')
                    def ranum():
                        print('\n')
                        print("\nComputer : For a random number, type 'RN' and For a random number between a specific range, type 'SN'.")
                        time.sleep(1.35)
                        cho=input("\nUser : ").lower()  
                        
                        def opt():
                            print("\nComputer : do you want to try it again, yes or no")  
                            uch=input("\nUser : ").lower()
                            
                            if "yes" in uch:
                                ranum()
                            else: 
                                time.sleep(0.3)
                                print('\n')
                                print('_'*90)
                                print('\n')
                                menu()

                        if "sn" in cho:
                            print("\nComputer : there is a  range from which you what a number")
                            print("\nComputer : what is the lower range?")
                            lr=int(input("\nUser : "))
                            print("\nComputer : what is the upper range?")
                            ur=int(input("\nUser : "))
                            a=random.randint(lr,ur)
                            print("\nComputer : the random number from your selected range is", a)
                            opt()
                            

                        elif 'rn' in cho:
                            print("\nComputer : For integer number type 'I' and for real number type 'R'")
                            uk=input("\nUser : ").lower()
                            if uk=='i':
                                oc=random.randint(-9999999999999999,999999999999999999)
                                print('\nComputer : ',oc)
                                opt()
                            elif uk=='r':
                                ot=random.random()
                                print('\nComputer : ',ot)
                                opt()




                    ranum()
                elif ch=='9':
                    p=na.upper()
                    print('\n')
                    print("_"*90)
                    print("\t\t\tTHANK YOU FOR USING OUR PROGRAM",p,'\t\t\t')
                    print("_"*90)
                    time.sleep(3)   
                    exit()
                    
                elif ch=="2":
                    print('\n')
                    print('_'*90)
                    print('\n')
                    print('- MATH CALCULATOR')
                    def mathc():
                        print("\nComputer : What do you want to calculate: \n\t  1 - Random math expression\n\t  2 - Trignometric math expression\n\t  - To exit to main menu, type 'exit'")     
                        chc=input("\nUser : ").lower()
                        time.sleep(1.5)
                        if chc=="1":
                            print("\nComputer : Enter any math expression below involving operators to calculate")
                            me=input("\nUser : ")
                            rsl=eval(me)
                            print("\nComputer : The result of %s is %s" % (me,rsl))
                            time.sleep(0.3)
                            mathc()
                        elif chc=="2":
                            print("\nComputer : Which trignometric function value do you need - \n\t   1.Sin \n\t   2.Cos \n\t   3.Tan \n\t   4.Cosec \n\t   5.Sec \n\t   6.Cot" )
                            tch=input("\nUser : ").lower()
                            if tch=="1":
                                print("\nComputer : Enter the value below")
                                sich=eval(input("\nUser : "))
                                print("\nComputer : The result for it is-", math.sin(sich))
                                time.sleep(0.3)
                                mathc()
                            elif tch=="2":
                                print("\nComputer : Enter the value below")
                                coch=eval(input("\nUser : "))
                                print("\nComputer : The result for it is-", math.cos(coch))
                                time.sleep(0.3)
                                mathc()
                            elif tch=="3":
                                print("\nComputer : Enter the value below")
                                tach=eval(input("\nUser : "))
                                print("\nComputer : The result for it is-", math.tan(tach))
                                time.sleep(0.3)
                                mathc()
                            elif tch=="4":
                                print("\nComputer : Enter the value below")
                                cosch=eval(input("\nUser : "))
                                print("\nComputer : The result for it is-", 1/math.sin(cosch))
                                time.sleep(0.3)
                                mathc()
                            elif tch=="5":
                                print("\nComputer : Enter the value below")
                                sech=eval(input("\nUser : "))
                                print("\nComputer : The result for it is-", 1/math.cos(sech))
                                time.sleep(0.3)
                                mathc()
                            elif tch=="6":
                                print("\nComputer : Enter the value below")
                                ctch=eval(input("\nUser : "))
                                print("\nComputer : The result for it is-", 1/math.tan(ctch))
                                time.sleep(0.3)
                                mathc()
                            else:
                                print("\nComputer : Enter correctly")
                                time.sleep(0.3)
                                mathc()
                        

                        elif chc=='exit':
                            time.sleep(0.3)
                            print('\n')
                            print('_'*90)
                            print('\n')
                            menu()
                            

                        else: 
                            print("\nComputer : Enter from the given choice correctly") 
                    mathc()
                elif ch=="4":
                    print('\n')
                    print('_'*90)
                    print('\n')
                    print('- PASSWORD GENERATOR')
                    def ps():
                        print("\nComputer : If you want to have a secure password, enter the password length below")
                        pl=int(input("\nUser : "))
                        le=string.ascii_letters
                        di=string.digits
                        sc=string.punctuation
                        ra=le+di+sc
                        pwd=""   
                        for i in range(pl):
                            pwd+="".join(secrets.choice(ra))
                        loading()
                        print('\n')
                        print("\nComputer : The password generated is", pwd)
                        print("\nComputer : If you want to generate another password type 'yes', else type 'no' ")
                        nco=input("\nUser : ").lower()
                        if nco=="yes":
                            time.sleep(0.3)
                            ps()
                        else :
                            time.sleep(0.3)
                            print('\n')
                            print('_'*90)
                            print('\n')
                            menu()
                    ps()
                        
                elif ch=="7":
                    print('\n')
                    print('_'*90)
                    print('\n')
                    print('- ROLLING DICE')
                    def RD():
                        print("\nComputer : Rolling Dice...")
                        time.sleep(3.0)
                        print("\nComputer : The value is ", random.randint(1,6))
                        time.sleep(0.5)
                        print('\nComputer : Type "yes" if you want roll the dice again and type "no" if you want to go to menu')
                        rep = input("\nUser : ").lower()
                        if rep=="yes":
                            time.sleep(0.3)
                            RD()
                        else:
                            time.sleep(0.3)
                            print('\n')
                            print('_'*90)
                            print('\n')
                            menu()
                    RD()
                elif ch=="5":
                    print('\n')
                    print('_'*90)
                    print('\n')
                    print('- COIN TOSS')
                    def TOS():
                        TC=["Heads", "Tails"]
                        print("\nComputer : Tossing a coin...")
                        rt=random.choices(TC)
                        toss=''
                        for i in rt:
                            toss=toss+i
                        print("\nComputer : It is ",toss)
                        print('\nComputer : Type "yes" if you want toss the coin again and type "no" if you want to go to menu')
                        ct=input("\nUser : ").lower()
                        if ct=="yes":
                            time.sleep(0.3)
                            TOS()
                        else:
                            time.sleep(0.3)
                            print('\n')
                            print('_'*90)
                            print('\n')
                            menu()
                    TOS()


                elif ch=="6":
                    print('\n')
                    print('_'*90)
                    print('\n')
                    print('- CREATING RANDOM TABLES')
                    print("\nComputer : Do you want to create a table with records on 'mysql' or 'excell' ?")
                    fco=input("\nUser : ").lower()
                    if fco=="excell":
                        def cstab():
                            global toop
                            print('\nComputer : Please write a file name.')
                            top=input('\nUser : ')
                            toop=top+'.csv'

                            f=open(toop, "a+", newline='')
                            print("\nComputer : Enter the amount of columns you need below")
                            a=int(input("\nUser : "))
                            print("\nComputer : Now enter the column name you want below")
                            lst=[]
                            for i in range(a):
                                v=input("\nUser : ")
                                lst.append(v)
                            r=csv.writer(f)
                            r.writerow(lst)   
                            while True:
                                bls=[]
                                for i in range(a):
                                    print("\nComputer : Enter the record below for ", lst[i ]," column")
                                    lv=input("\nUser : ")
                                    bls.append(lv)
                                r.writerow(bls)
                                print("\nComputer : Do you want to enter again, Yes/No")
                                rv=input("\nUser : ").lower()
                                if rv=="no":
                                    break   
                            f.close()
                        cstab()
                        print("\nComputer : Do you want to display records, yes/no?")
                        dk=input("\nUser : ").lower()
                        if dk in "yes":
                            def concs():
                                f=open(toop, "r+", newline='')
                                ics=csv.reader(f)
                                print('\n')
                                for i in ics:
                                    print(i)
                                f.close()
                            concs()
                            time.sleep(0.3)
                            print('\n')
                            print('_'*90)
                            print('\n')
                            menu()

                        elif dk=='no':
                            time.sleep(0.3)
                            print('\n')
                            print('_'*90)
                            print('\n')
                            menu()
                            
                           
                    '''elif fco=="mysql":
                      cr=c.cursor()
                       print("\nComputer :  Do you want to create database, Yes/No ?")
                       chi=input("\nUser : ").lower()
                        if chi=="yes":
                             print("\nComputer : Write the command to create ")
                             jo=input("\nUser : ")
                             cr.execute(jo)
                             time.sleep(0.3)
                             print('\nComputer : Please write the command to use it')
                              uoi=input('\nUser : ')
                        
                             cr.execute(uoi)
                              
                              
                       else :
                           print("\nComputer : write the command to use it")
                           jos=input("\nUser: ")
                           cr.execute(jos)
                        c.commit()
                        
                        def mqlqs():
                            
                           print('\nComputer : Enter the commands in order to work on mysql. ')
                           s=input('\nUser : ')
                           cr.execute(s)

                           print("\nComputer : do you want to fetch the data, yes/no?")
                            asl=input("\nUser : ").lower()
                            if "yes" in asl:
                               r=cr.fetchall()
                               l=[]
                               for each in r: 
                                   print(each)
                                c.commit()
                                time.sleep(2.0)
                                print('\n\nComputer : Do you want to write more "commands" or go back to "menu" ?')
                                fearo=input('\nUser : ').lower()
                                if fearo=='menu':
                                   print('\n')
                                   time.sleep(0.3)
                                   print('\n')
                                   print('_'*90)
                                   print('\n')
                                   menu()
                                elif fearo=='commands':
                                   print('\n')
                                   print('_'*90)
                                   mqlqs()
                                   print('\n')
                                    

                           elif 'no' in asl:
                               print('\n\nComputer : Do you want to write more "commands" or go back to "menu" ?')
                               fea=input('\nUser : ').lower()
                               if fea=='menu':
                                   print('\n')
                                   time.sleep(0.3)
                                   print('\n')
                                   print('_'*90)
                                   print('\n')
                                   menu()
                                elif fea=='commands':
                                   print('\n')
                                   print('_'*90)
                                   mqlqs()
                                    print('\n')
                                
                            
                                    
                            c.commit()
                            c.close()  
                        mqlqs()'''  
                elif ch=='3':
                    def Minigames():
                        
                        def RPS(): #RPS
                        
                        

                            def title(): #title
                                print('_'*90)
                                print('\n\t\t\t\t*-.WELCOME TO RPS.-*\n')
                                    
                            title()
                            def normal_game(): #Normal game
                                
                                print('\n')
                                print('_'*90)
                                bot_choices=['rock','paper','scissors']
                                bot=random_choice=random.choice(bot_choices)
                                user_choice=input('\nPlease choose between Rock, Paper & Scissors : ').lower() #user choice
                                if bot==user_choice : #Draw
                                    print('\nComputer chose ',bot,' and you chose ',user_choice,' .')
                                    print('\n IT IS A DRAW! \n')
                                    
                                    

                                elif bot=='paper' and user_choice=='rock': #Rock-Paper
                                    print('\nComputer chose ',bot,' and you chose ',user_choice,' .')
                                    print('\n COMPUTER WINS! \n')
                                    
                                    

                                elif bot=='scissors' and user_choice=='rock': #Rock-Scissors
                                    print('\nComputer chose ',bot,' and you chose ',user_choice,' .')
                                    print('\n YOU WIN! \n')
                                    
                                    

                                elif bot=='scissors' and  user_choice=='paper': #Paper-Scissors
                                    print('\nComputer chose ',bot,' and you chose ',user_choice,' .')
                                    print('\n COMPUTER WINS! \n')
                                    
                                    

                                elif bot=='Rock' and user_choice=='paper': #Paper-Rock
                                    print('\nComputer chose ',bot,' and you chose ',user_choice,' .')
                                    print('\n YOU WIN! \n')
                                    
                                    
                                
                                elif bot=='Rock' and user_choice=='scissors': #Scissors-Rock
                                    print('\nComputer chose ',bot,' and you chose ',user_choice,' .')
                                    print('\n COMPUTER WINS! \n')
                                    
                                    
                                
                                elif bot=='Paper' and user_choice=='scissors': #Scissors-Paper
                                    print('\nComputer chose ',bot,' and you chose ',user_choice,' .')
                                    print('\n YOU WIN! \n')
                                    
                                
                                else:
                                    print('_'*50)
                                    print('\n PLEASE CHOOSE AGAIN.\n')
                                    print('_'*50)
                                    normal_game()
                                    
                                
                                def WPAQfunction():
                                    WPAQ=input('\nDo you wanna play again ?\n- Type "Yes" or "No" : ').lower() #WPAQ = WANNA PLAY AGAIN QUESTION
                                    
                                    if WPAQ=='yes':
                                        normal_game()
                                    
                                    elif WPAQ=='no':
                                        print('\nLoading... \n')
                                        time.sleep(2)
                                        print('\n')
                                        menu()
                                    
                                    else:
                                        print('_'*50)
                                        print('\n PLEASE CHOOSE AGAIN.\n')
                                        print('_'*50)
                                        WPAQfunction()
                                WPAQfunction()
                                
                            
                            
                            def rules(): #rules
                                print('\n')
                                print('_'*90)
                                print('\n\t\t1. PLEASE ONLY CHOSE THE CHOICE FROM THE GIVEN OPTIONS.')
                                print('\n\t\t2. THIS IS HOW THE GAME WORKS :\n\t\t- ROCK BEATS SCISSORS.\n\t\t- PAPER BEATS ROCK.\n\t\t- SCISSORS BEAT PAPER.')
                                print('\n\t\t3. HAVE FUN :D \n')
                                print('_'*90)

                                def Qfunctionv4():
                                    WPAQv2=input('\nDo you want to exit or go back to menu ?\n- Type "exit" to exit and "menu" to go back to menu : ').lower() #Q = QUESTION
                                    if WPAQv2=='menu':
                                        print('\nLoading... \n')
                                        time.sleep(2)
                                        print('\n')
                                        menu()
                                
                                    elif WPAQv2=='exit':
                                        print('_'*90)
                                        print('\n*-.THANK YOU FOR PLAYING RPS, HAVE A NICE DAY.-*\n') #exit 
                                        print('_'*90)
                                        exit()
                                
                                    else:
                                        print('_'*50)
                                        print('\n PLEASE CHOOSE AGAIN.\n')
                                        print('_'*50)
                                        Qfunctionv4()
                                Qfunctionv4()
                            
                            
                            def menu(): #menu
                                
                                print('_'*90)
                                print('\n1) Which gamemode you want to play ?\n- For Normmal game type "1".\n- For rules type "2".\n- To exit the program type "exit".')
                                menu_choice=input('\nCHOICE : ') #choice
                                print('\n')
                                
                                if menu_choice=='1':
                                    
                                    print('GOING TO NORMAL GAME.\n') #nornal
                                    print('Loading... ')
                                    time.sleep(2)
                                    normal_game()

                                elif menu_choice=='2':
                                    
                                    print('GOING TO RULES.\n') #rules
                                    print('Loading... ')
                                    time.sleep(2)
                                    rules()
                                
                                elif menu_choice.lower()== 'exit':
                                    print('_'*90)
                                    print('\n\t\t*-.THANK YOU FOR PLAYING RPS, HAVE A NICE DAY.-*\n') #exit 
                                    print('_'*90)
                                    print('\n')
                                    main_menu()
                                    

                                
                                else:
                                    print('\n PLEASE CHOOSE AGAIN.\n')
                                    menu()
                            menu()
                        def WORD(): #WORD GAME

                            def titlev2(): #title
                                print('_'*90)
                                print('\n\t\t\t\t*-.WELCOME TO WORD GAME.-*\n')
                                print('_'*90)
                            titlev2()
                        
                        
                            def dec_(): #In function go back menu question
                                    print('\nDo you want to go back to menu ? or exit ?\n-Type "menu" to go to menu.\n-Type "exit" to exit.')
                                    mc=input('\nCHOICE : ').lower()
                                    if mc=='menu':
                                        time.sleep(0.7)
                                        menuv2() 
                                
                                    elif mc=='exit':
                                        exit()

                                    else:
                                        print('\nPlease type from the given option.')
                                        time.sleep(0.4)
                                        dec_()
                                    
                            
                            
                            def easy(): #Easy mode
                                
                                l=['Apple','Brown','Water','Grass','Lemon','Sharp','Space','Slice','Ghost']
                                d={
                                'Apple':'It is most valuable tech brand.',
                                'Brown':'What is the colour of a wooden stick ?',
                                'Water':'We drink this in regular bases.',
                                'Grass':'What do you cows eat ?',
                                'Lemon':'Something you add to water for refreshment.',
                                'Sharp':'Dont play with knives because it is ?',
                                'Space':'Planets exist in ?',
                                'Slice':'Another word for chop.',
                                'Ghost':'BOO!'}
                                word=random.choices(l,k=1) # Random
                                str1=''
                                for each in word:
                                    str1+= each
                                
                                print('\n\nYou got 3 chances to guess.')
                                time.sleep(1)
                                print('\nGOODLUCK!!\n')
                                time.sleep(1)

                                print('\nYOUR WORD IS :')
                                

                                time.sleep(2)
                                print('\n_',str1[1],'_','_','_')

                                for i in d:
                                    if i==str1:
                                        time.sleep(0.76)
                                        print('\nHINT : ',d[i])




                                answer=str1.lower()
                                def choosen():
                                    for each in range (1):
                                        user=input('\n\nPlease enter your the word you think it is : ').lower()
                                        if user==answer:
                                            print('\nCONGRATS, YOU GOT IT RIGHT!\n')
                                            print('\nDo you want to go back to menu ? or exit ?\n-Type "menu" to go to menu.\n-Type "exit" to exit.')
                                            mc=input('\nCHOICE : ').lower()
                                            if mc=='menu':
                                                time.sleep(0.7)
                                                menuv2() 
                                            
                                            elif mc=='exit':
                                                print('\n')
                                                main_menu() 

                                            else:
                                                print('\nPlease type from the given option.')
                                                time.sleep(0.4)
                                                dec_()
                                            

                                        elif user!=answer:
                                            time.sleep(0.7)
                                            print('\n\nOops, you got it wrong, give it another try :D') 
                                            

                                        

                                        


                                choosen()

                                print('\n_',str1[1],str1[2],'_','_')

                                choosen()

                                print('\n_',str1[1],str1[2],'_',str1[4])

                                choosen()

                                print('\nThe word was : ',answer)

                                dec_()
                                

                            def hard(): #Hard mode
                                
                                l=['Exchequer','Macaronic','Abounding','Preterite','Aspersion','Abdictor','Alchemist','Innocuous']
                                d={
                                'Exchequer':'The British governmental department.', 
                                'Macaronic':'characterized by a mixture of two languages',
                                'Abounding':'very plentiful (or) abundant',
                                'Preterite':'expressing a past action or state.',
                                'Aspersion':'an attack on the reputation or integrity of someone or something',
                                'Abdictor':'fail to fulfil or undertake (a responsibility or duty)',
                                'Alchemist':'a person who transforms or creates something through a seemingly magical process (It Is a famous book)',
                                'Innocuous':'not harmful or offensive'}
                                
                                word=random.choices(l,k=1) #Random
                                str1=''
                                for each in word:
                                    str1+= each
                                
                                print('\n\nYou got 4 chances to guess.')
                                time.sleep(1)
                                print('\nGOODLUCK!!\n')
                                time.sleep(1)

                                print('\nYOUR WORD IS :')

                                time.sleep(2)
                                print('\n_',str1[1],'_','_','_','_','_','_')

                                for i in d:
                                    if i==str1:
                                        time.sleep(0.76)
                                        print('\nHINT : ',d[i])




                                answer=str1.lower()
                                def choosen():
                                    for each in range (1):
                                        user=input('\n\nPlease enter your the word you think it is : ').lower()
                                        if user==answer:
                                            print('\nCONGRATS, YOU GOT IT RIGHT!\n')
                                            print('\nDo you want to go back to menu ? or exit ?\n-Type "menu" to go to menu.\n-Type "exit" to exit.')
                                            mc=input('\nCHOICE : ').lower()
                                            if mc=='menu':
                                                time.sleep(0.7)
                                                menuv2() 
                                            
                                            elif mc=='exit':
                                                exit()
                                            
                                            else:
                                                print('\nPlease type from the given option.')
                                                time.sleep(0.4)
                                                dec_()
                                            
                                            

                                        elif user!=answer:
                                            time.sleep(0.7)
                                            print('\n\nOops, you got it wrong, give it another try :D') 
                                            

                                        

                                        


                                choosen()

                                print('\n_',str1[1],str1[2],'_','_','_','_','_')

                                choosen()

                                print('\n_',str1[1],str1[2],'_',str1[4],'_','_','_')

                                choosen()

                                print('\n',str1[0],str1[1],str1[2],'_',str1[4],'_','_','_')

                                choosen()

                                print('\nThe word was : ',answer)

                                dec_()
                            
                            

                            def menuv2(): #Main game menu
                                chose=input('\nDo you want to play "easy" mode or "hard" mode ? \n\n\t Type "exit" to exit\n\nCHOICE : ').lower()
                                if chose=='hard':
                                    hard()
                                elif chose=='easy':
                                    easy()
                                elif chose=='exit':
                                    print('\n')
                                    main_menu()
                                else:
                                    print('\nPlease type from the given option.')
                                    time.sleep(0.4)
                                    menuv2()
                                            
                            menuv2()  
                        def NG(): #NUMBER GAME

                            def titlev3(): #title
                                print('_'*90)
                                print('\n\t\t\t\t*-.WELCOME TO GUESS THE NUMBER.-*\n')
                                print('_'*90)
                            titlev3()
                            

                            lower = int(input("Enter Lower bound:- "))
                            
                            upper = int(input("Enter Upper bound:- "))
                            

                            x = random.randint(lower, upper)
                            print("\n\tYou've only ",
                                round(math.log(upper - lower + 1, 2)),
                                " chances to guess the integer!\n")
                            

                            count = 0
                            

                            while count < math.log(upper - lower + 1, 2):
                                count += 1
                            
                            
                                guess = int(input("Guess a number:- "))
                            
                                
                                if x == guess:
                                    print("Congratulations you did it in ",
                                        count, " try")
                                    print('\n')
                                    time.sleep(2)
                                    main_menu()
                                elif x > guess:
                                    print("You guessed too small!")
                                elif x < guess:
                                    print("You Guessed too high!")
                            

                            if count >= math.log(upper - lower + 1, 2):
                                print("\nThe number is %d" % x)
                                print("\tBetter Luck Next time!")
                                print('\n')
                                time.sleep(2)
                                main_menu()
                                
                        def QUIZZ(): #GK QUIZ
                            def qtitle(): #title
                                print('\n')
                                print('_'*90)
                                print('\n\t\t\t\t*-.WELCOME TO GK.-*\n')
                            qtitle()
                            print('_'*90)
                            print("\nComputer : Let's have some quick challenge and see how many you can answer correctly")
                            time.sleep(1.25)
                            while True:
                                print("\nComputer : Which mode do you want to play- normal, or hard")
                                mch=input("\nUser : ").lower()
                                if mch=="hard":
                                    time.sleep(1.25)
                                    print("\nComputer : let's begin ")    
                                    ques=("1.Epsom (England) is the place associated with?:","2.First Afghan War took place in:",
                                        "3.Fathometer is used to measure:", "4.Hockey was introduced in the Asian Games in:",
                                        "5.Federation Cup, World Cup, Allywyn International Trophy and Challenge Cup are awarded to winners of:",
                                        "6.First International Peace Congress was held in London in:",
                                        "7.Georgia, Uzbekistan and Turkmenistan became the members of UNO in:","8. Which of the following causes Poliomyelitis?:",
                                        "9.Zawar (Rajasthan) is famous for",
                                        "10.Where is the permanent secretariat of the SAARC(South Asian Association for Regional Cooperation)?:")
                                    opt=(("A. Horse racing", "B. Polo", "C. Shooting",  "D. Snooker"), 
                                        ("A. 1839", "B. 1843","C. 1833","D. 1848"),
                                        ("A. Earthquakes", "B. Rainfall", "C. Ocean depth","D. Sound intensity"),
                                        ("A. 1958 in Tokyo", "B. 1962 in Jakarta","C. 1966 in Bangkok","D. 1970 in Bangkok"),
                                        ("A. Tennis", "B. Volleyball","C. Basketball","D. Cricket"),
                                        ("A. 1564","B. 1798","C. 1843","D. 1901"),
                                        ("A. 1991","B. 1992", "C. 1993", "D. 1994"),
                                        ("A. Dengue virus", "B. Enterovirus", "C. Mumps virus","D. Rhabdovirus"),
                                        ("A. ship manufacturing", "B. zinc mines","C. salt","D. major port"),
                                        ("A. Kathmandu", "B. New Delhi","C. Islamabad","D. Colombo"))
                                    ans=("A", "A", "C", "A", "B", "C", "B", "B", "B", "A")
                                    guess=[]
                                    scor=0
                                    quno=0
                                    for i in ques:
                                        print("_"*10)
                                        print("\nComputer : ",i)
                                        for j in opt[quno]:
                                            print(j)
                                        print("\nComputer : Enter (A, B, C, D):")
                                        gues=input("\nUser : ").upper()
                                        guess.append(gues)
                                        if gues==ans[quno]:
                                            scor+=1
                                            print("\nComputer : Correct!! :-D")
                                        else:
                                            print("\nComputer : Incorrect!! :-(")
                                            print("\nComputer :",ans[quno],"is the correct answer")
                                        quno+=1
                                    print("_"*10)
                                    print(" \nComputer :  RESULTS ")
                                    print("\nComputer : answers-", end='')
                                    for k in ans:
                                        print(' ',k,'  ', end="")
                                    print()
                                    print("\nComputer : guesses-", end='')
                                    for l in guess:
                                        print(' ', l,'  ', end='')
                                    print()
                                    print("\nComputer : Your score is ", scor,"/10")
                                    print("\nComputer : Do you want to play this again?-(yes or no)")
                                    ninp=input("\nUser : ").lower()
                                    if ninp=="yes":
                                        return True
                                    elif ninp=='no':
                                        main_menu()
                                elif mch=="normal":
                                    time.sleep(1.25)
                                    print("\nComputer : let's begin ")
                                    ques=("1.Which launch vehicle is capable of placing around 1540 kg of INSAT class of satellites in geosynch-ronous transfer orbit of earth?:",
                                        "2.Which of the following acts as a resistance against in the body?:",
                                        "3.Where was the headquarters of European Union located?:", "4.Where did world cup soccer tournament took place (2010)?:",
                                        "5.Which of the following cities will be the host of XIX Commonwealth Games 2010?:",
                                        "6.Which of the following UN agencies has its headquarters at Paris?:", "7.Film and TV institute of India is located at:",
                                        "8.Which is post-harvest folk dance in Assam?:" , "9.Which is the major mineral found in Punjab?:"
                                        "10.During World War II, when did Germany attack France?:")
                                    opt=(("A. SLV-S","B. PSLV","C. ASLV","D. GSLV"),
                                        ("A. Carbohydrates","B. Red corpuscles","C. Vitamins","D. White corpuscles"),
                                        ("A. Brussels","B. Paris","C. London","D. Rome"),
                                        ("A. Japan and South Korea","B. France","C. South Africa","D. West Germany"),
                                        ("A. London","B. Delhi","C. Melbourne","D. Auckland"),
                                        ("A. UNESCO","B. ILO","C. FAO","D. IMO"),
                                        ("A. Pune (Maharashtra)","B. Rajkot (Gujarat)","C. Pimpri (Maharashtra)","D. Perambur (Tamilnadu)"),
                                        ("A. Bihu","B. Ojapali","C. Ankia Nat","D. None of the above"), 
                                        ("A. Coal","B. Gold","C. Salt","D. Iron "),                           
                                        ("A. 1940","B. 1941","C. 1942","D. 1943"))
                                    ans=("D", "D", "A", "C", "B", "A", "A","A", "C","A")
                                    guess=[]
                                    scor=0
                                    quno=0
                                    for i in ques:
                                        print("_"*10)
                                        print("\nComputer : ",i)
                                        for j in opt[quno]:
                                            print(j)
                                        print("\nComputer : Enter (A, B, C, D):")
                                        gues=input("\nUser : ").upper()
                                        guess.append(gues)
                                        if gues==ans[quno]:
                                            scor+=1
                                            print("\nComputer : Correct!! :-D")
                                        else:
                                            print("\nComputer : Incorrect!! :-(")
                                            print("\nComputer :",ans[quno],"is the correct answer")
                                        quno+=1
                                    print("_"*10)
                                    print(" \nComputer :  RESULTS ")
                                    print("\nComputer : answers-", end='')
                                    for k in ans:
                                        print(' ', k,'  ', end="")
                                    print()
                                    print("\nComputer : guesses-", end='')
                                    for l in guess:
                                        print(' ', l,'  ', end='')
                                    print()
                                    print("\nComputer : Your score is ", scor,"/10")
                                    print("\nComputer : Do you want to play this again?-(yes or no)")
                                    ninp=input("\nUser : ").lower()
                                    if ninp=="yes":                            
                                        return True
                                    elif ninp=='no':
                                        main_menu()
                                

                        def main_menu(): #main menu of minigames
                            def Main_title(): #title
                                print('_'*90)
                                print('\n\t\t\t\t*-.WELCOME TO MINIGAMES.-*\n')
                            Main_title()
                            print('_'*90)
                            print('\n-> Which game you want to play ?\n- For RPS type "1".\n- For Word game type "2".\n- For Guess The Number type "3".\n- For GK Quiz type "4".\n- If you want to go to menu type "menu".')
                            menu_choicee=input('\nCHOICE : ') #choicG
                            print('\n')
                            
                            if menu_choicee=='1':
                                print('GOING TO RPS.\n') #nornal
                                print('\nLoading... \n')
                                time.sleep(2)
                                
                                RPS()
                            
                            elif menu_choicee=='2':
                                
                                print('GOING TO WORD GAME.\n') #impossible
                                print('\nLoading... \n')
                                time.sleep(2)
                                WORD()
                            elif menu_choicee=='3':
                                
                                print('GOING TO GUESS THE NUMBER..\n') #guess_number
                                print('\nLoading... \n')
                                time.sleep(2)
                                NG()

                            elif menu_choicee=='4':
                                
                                print('GOING TO GK QUIZ..\n') #gk quick
                                print('\nLoading... \n')
                                time.sleep(2)
                                QUIZZ()
                            elif menu_choicee.lower()== 'menu':
                                print('_'*90)
                                print('\n\t\t\t\t*-.GOING BACK TO MENU.-*\n') #exit 
                                print('_'*90)
                                time.sleep(2)
                                menu()
                            else:
                                print('PLEASE CHOOSE AGAIN.\n')
                                time.sleep(2)
                                main_menu()
                        main_menu()
                    
                    Minigames()
                elif ch=='8':
                    def web():
                        def Webbrotitle(): #title
                                print('\n')
                                print('_'*90)
                                print('\n')
                                print('- WEB BROWSER')
                        Webbrotitle()
                        print('\nComputer : Please enter what you want search pls.')
                        search=input('\nUser : ')

                        print('\nComputer : Which website do you want me to search on?\n1. Youtube\n2. Google')
                        sch=input('\nUser : ')
                        loading()
                        print('\n')
                        if sch=='1':
                            webbrowser.open('https://www.youtube.com/search?q='+search)
                            print('\n')
                            print('_'*90)
                            
                            exit()
                            
                        elif sch=='2':
                            webbrowser.open('https://www.google.com/search?q='+search)
                            print('\n')
                            print('_'*90)
                            exit()
                    web()

            

        
        menu()
             
                
main()                     
                  
