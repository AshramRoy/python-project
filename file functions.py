from TEST51 import AddIP,searchIP,printlist,delateIP,searchDic,addTOdictinres,delatedictinres,updateURLIP,printdic
def menu():
    while(True):
        choice1=input("Menu\n............\n.A IP system\n.B DNS System\nSelect: ")
        if(choice1=="A"):
            choice2=input("Menu IP system\n.......\n1.search for IP address from a list \n2.add IP address to a list \n3.Delete IP Address \n4.Print all the IPs to the scren\nSelect:")
            if(choice2=="1"):
                searchIP()
            elif(choice2=="2"):
                AddIP()
            elif(choice2=="3"):
                delateIP()
            elif(choice2=="4"):
                printlist()
        elif(choice1=="B"):
             choice3=input("Menu DNS system\n.......\n1.search fro URL from A dictionary \n2.add URL + IP address to aDictionaty \n3. Delete URL from A dictonary\n4.Update the IP address of specific URL\n5. print DICsionres\n Select:")
             if(choice3=="1"):
                searchDic()
             elif(choice3=="2"):
                 addTOdictinres()
             elif(choice3=="3"):
                 delatedictinres()
             elif(choice3=="4"):
                 updateURLIP()
             elif (choice3 == "5"):
                 printdic()
        else:
            print("bad Choise")
        exit=input("Prass Yes to Exit the script Or any Type of Key to continue")
        if(exit=="Yes"):
            print("you have been Exit form the Script")
            break
        else:
            continue
menu()