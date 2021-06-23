import time
from colorama import Fore,Back,init
init()
def FUNRED(i):
    print(i+Fore.RESET+Back.RESET,end = " ")
    return  input()
def displayPrice(num="__all__"):
    f = open("pl","r")
    r = f.read().split("\n")
    if "" in r:
        r.remove("")
    if num=="__all__":
        print(Fore.GREEN+"\n".join(r))
        return ""
    if num=="product name":
        product = FUNRED(Fore.RED+Back.WHITE+"product name : ").lower()
        for i in r:
            if product in i.split(",")[1].lower():
                print(Fore.RED+Back.WHITE+i)
        return ""
    if num=="price":
        price = FUNRED(Fore.RED+Back.WHITE+"price : ")
        for i in r:
            if price in i.split(","):
                print(Fore.RED+Back.WHITE+i)
        return ""
    try:
        print(r[num-1])
    except IndexError:
        print(Fore.RED+Back.WHITE+"OUT OF RANGE")
def editPrice():
    f = open("pl","r")
    r = f.read().split("\n")
    if "" in r:
        r.remove("")
    for i in r:
        print(Fore.GREEN+i)
    x = int(FUNRED(Fore.RED+Back.WHITE+"edit sl no. :"))
    x = x if x<=len(r) else "invalid"
    if x=="invalid":
        print(Fore.RED+Back.WHITE+"invalid FUNRED")
        return ""
    pre,post = "\n".join(r[:x-1]).strip(),"\n".join(r[x:]).strip()+"\n"
    f = open("pl","w")
    f.write(pre+"\n"+str(x)+","+FUNRED("product name : ")+","+FUNRED("price : ")+"\n"+post)
    f.close()
def saveNewPrice(username,passwrd):
    r = open("pl","r").read().split("\n")
    if "" in r:
        r.remove("")
    f = open("pl","a+")
    slno = len(r)+1
    passwrd = passwrd if "%" not in passwrd else str(eval(passwrd.replace("%","/100")))
    f.write(f"{slno},{username},{passwrd}\n")
    f.close()
while True:
    print(Fore.MAGENTA+"\nTo save new procudt press 1\nTo see all product press 2\nTo see product with Sl No. press 3\nTo search product with 'product name' press 4\nTo search product with 'price' press 5\nTo edit product press 6\nAny other key to exit\n")
    x = FUNRED("")
    if x=="1":
        saveNewPrice(FUNRED(Fore.RED+Back.WHITE+"product name : "),FUNRED(Fore.RED+Back.WHITE+"price : "))
    elif x=="2":
        displayPrice("__all__")
    elif x=="3":
        displayPrice(int(FUNRED(Fore.RED+Back.WHITE+"Sl No. : ")))
    elif x=="4":
        displayPrice("procuct name")
    elif x=="5":
        displayPrice("price")
    elif x=="6":
        editPrice()
    else:
        break
    time.sleep(1)
    print("SUCCESSFULL!!")
