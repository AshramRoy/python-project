def AddIP():
    IP = input("please enter Your IP Address:")
    listIP = []
    filename = "C:/Users/roya/Desktop/cd - 1 CyberArk/11.txt"
    file = open(filename, "r")
    file_lines = file.read()
    listIP = file_lines.split("\n")
    if IP in listIP:
        print("this IP address is already on the list")
    else:
        listIP.append(IP)
        print("this IP is been add :" + str(IP))
    print(listIP)

def searchIP():
    IP = input("Search for an address:")
    listIP = []
    filename = "C:/Users/roya/Desktop/cd - 1 CyberArk/11.txt"
    file = open(filename, "r")
    file_lines = file.read()
    listIP = file_lines.split("\n")
    if IP in listIP:
        print("this Ip address is Exists in the list " + str(listIP))
    else:
        print("this Ip address is not Exists in the list" + str(listIP))
        print(IP)

def delateIP():
    IP = input("delate IP address:")
    listIP = []
    filename = "C:/Users/roya/Desktop/cd - 1 CyberArk/11.txt"
    file = open(filename, "r")
    file_lines = file.read()
    listIP = file_lines.split("\n")
    if IP in listIP:
        listIP.remove(IP)
        print(listIP)
        print("This IP Address is been remove")
    else:
        print("this IP address is not Been exist")
        print(listIP)

def printlist():
    listIP = []
    filename = "C:/Users/roya/Desktop/cd - 1 CyberArk/11.txt"
    file = open(filename, "r")
    file_lines = file.read()
    listIP = file_lines.split("\n")
    print(listIP)

def searchDic():
    dicsionry = {"www.google.com": "8.8.8.8", "www.youtube.com": "4.4.4.4", "wwww.facebook.com": "5.5.5.5",
                 "wwww.ebay.com": "7.7.7.7"}
    URL=input("Search for URL:")
    if URL in dicsionry:
        print("is been found :" + URL)
        print(dicsionry)
    else:
        print( URL + " not Been found")

def addTOdictinres():
    URL=input("Please Enter URL: ")
    IP=input("Please Enetr IP: ")
    dicsionry = {"www.google.com": "8.8.8.8", "www.youtube.com": "4.4.4.4", "wwww.facebook.com": "5.5.5.5",
                 "wwww.ebay.com": "7.7.7.7"}
    dicsionry.update({URL:IP})
    print(dicsionry)

def delatedictinres():
    dicsionry = {"www.google.com": "8.8.8.8", "www.youtube.com": "4.4.4.4", "wwww.facebook.com": "5.5.5.5",
                 "wwww.ebay.com": "7.7.7.7"}
    URL = input("Please Enter URL: ")
    dicsionry.pop(URL)
    print("Delete is been set ")
    print(dicsionry)

def updateURLIP():
    dicsionry = {"www.google.com": "8.8.8.8", "www.youtube.com": "4.4.4.4", "wwww.facebook.com": "5.5.5.5",
                 "wwww.ebay.com": "7.7.7.7"}
    URL = input("Please Enter URL: ")
    IP = input("Please Enter IP: ")
    dicsionry[URL]=IP
    print("Update is been set!")
    print(dicsionry)

def printdic():
    dicsionry = {"www.google.com": "8.8.8.8", "www.youtube.com": "4.4.4.4", "wwww.facebook.com": "5.5.5.5",
                 "wwww.ebay.com": "7.7.7.7"}
    print(dicsionry)
printdic()



















