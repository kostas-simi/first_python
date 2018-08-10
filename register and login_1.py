import sqlite3
from datetime import datetime,date


conn = sqlite3.connect('data/Containers.db')
c = conn.cursor()

def countContainers(x,y):
    z = x - y
    if z>=0 and z<=170:
        return True
    return False



boxesOut = 0
dataIn = list()
dataOut = list()




while True:
    choice = input('Do you want to: Register(R/r) or Login(L/l)? ')
    if choice == 'R' or choice == 'r' :
        newUser = input('Please choose a username: ')
        newPassword = input('Please choose a password: ')
        c.execute (''' INSERT INTO USERS (USERNAME,PASSWORD)
                VALUES(?,?)''',(newUser,newPassword) )
        conn.commit()
        print('Regitration successful','username: ',newUser,' password: ',newPassword)
        break
    elif choice == 'L' or choice == 'l' :
        Tries = 0
        while Tries < 3:
            username = input('Give me username: ')
            psw = input('Give me your password: ')
            c.execute('''SELECT PASSWORD FROM USERS WHERE USERNAME = ? ''',(username,) )
            usr = c.fetchone()
        
            if usr[0] == psw :
                print('Welcome, ',username)
                while True:
                    boxesIn = input('Give the number of containers that entered the warehouse. ')
                    boxesOut = input('Give the number of containers that exited the warehouse. ')
                    boxesIn = int(boxesIn)
                    boxesOut = int(boxesOut)
                    #boxesLeft = boxesIn - boxesOut
                    #if boxesLeft >=0 and boxesLeft <=170:
                    if countContainers(boxesIn,boxesOut):
                        dataIn.append(boxesIn)
                        dataOut.append(boxesOut)
                        c.execute(''' SELECT MAX(DAYNO) FROM CONTAINERS''')
                        DayNo = c.fetchone()
                        if DayNo[0] is None :
                            DayNo = 1
                        else : DayNo = int(DayNo[0]) + 1
                        #print (DayNo)
                        c.execute (''' INSERT INTO CONTAINERS (DAYNO,CONTAINERSIN,CONTAINERSOUT,RECORDTIME)
                                        VALUES(?,?,?,?)''', (DayNo,boxesIn,boxesOut,datetime.now()) )
                        conn.commit()
                    else:
                        continue
                    Controler =  input('End of Data Entry Yes(Y/y)/No: ') 
                    if Controler == 'Y' or Controler == 'y':
                        break
                    
                    print(dataIn)
                    print(dataOut)



            else:
                Tries = Tries + 1
                print('Wrong combination of username and password')
                print('Left Tries: ', 3 - Tries)
                continue
            
    else:
        print('Wrong value, please choose again: ')
        continue
    
