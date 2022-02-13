from numpy import append


options = ["url", "wait", "screenshot", "window_size",
        "maximize","currenturl", "pagesource", 
        "title","sendkeys", "click", "clear"]

scenario = []


def xpathHelper():
    return "generycznyXpath"

def creator():
    while True:
        c = 0
        for i in options:
            c += 1
            print("Opcja " + str(c) +": " + i)
        choice = input("\n(wpisz 'quit' aby wyjsc)\nWprowadź swój wybór: ")
        if choice in options:
            addStep(choice)
        elif choice == "quit":
            break
        else:
            print("\nWprowadzono bledna odpowiedz! '" + choice + "' nie jest wlasciwa odpowiedzia!")
            print("\nWprowadz poprawna odpowiedz")
            continue
    
    print("Scenariusz testowy jest gotowy!")
    for i in scenario:
        print("\n" + str(i))

    
def addStep(choice):


    if choice == "wait":
        time = str(input("wybrano 'wait'\npodaj ilosc sekund: "))
        scenario.append(time)
    
    elif choice == "url":
        url = input("\nWprowadz url na do ktoreg powinno przejsc:\n")
        if url.startswith('https://'):
            scenario.append(["goto", url])
        else:
            print("wybierz ta opcje ponownie i wprowadz poprawny adres (musi zawierac 'https://adres.domena/'")

    elif choice == "screenshot":
        print("screenshot znajdzie sie w folderze 'screenshot' w aplikacji")
        scenario.append("ss")
    
    elif choice == "window_size":
        res = input("\npodaj rozdzielczosc okna w nastepujacy sposob: 'wysokoscxszerokosc' (e.g. 1280x720):\n")
        scenario.append(["resolution", res])

    elif choice == "maximize":
        print("\nOkno zostanie zmaksymalizowane\n")
        scenario.append("maximize")

    elif choice == "currenturl":
        link = input("\nWprowadz adres ktory powinie sie aktualnie wyswietlic:\n")
        arr = ["link", link]
        scenario.append(arr)

    elif choice == "pagesource": 
        value = input("\nWprowadz wartosc ktora powinna sie znalezc w zrodle:\n")
        arr = ["source", value]
        scenario.append(arr)
        
    elif choice == "title":
        value = input("\nWprowadz wartosc ktora powinna sie znalezc w tytule:\n")
        arr = ["title", value]
        scenario.append(arr)

    elif choice == "sendkeys":
        value = input("\n wprowadz wartosc ktora ma sie znalezc w elemencie:\n")
        xpath = input("\n pragniesz znalezc wartosc xpath automatycznie czy manualnie? 'a/m'\n")
        if xpath == "a":
            elem = xpathHelper()
        elif xpath == "m":
            elem = input("wklej Xpath: ")
        sendkeys_arr = ["sendkeys", value, elem]
        scenario.append(sendkeys_arr)

    elif choice == "click":
        xpath = input("\n pragniesz znalezc wartosc xpath automatycznie czy manualnie? 'a/m'\n")
        if xpath == "a":
            elem = xpathHelper()
        elif xpath == "m":
            elem = input("wklej Xpath: ")
        clickarr = ["click", elem]
        scenario.append(clickarr)
    elif choice == "clear":
        xpath = input("\n pragniesz znalezc wartosc xpath automatycznie czy manualnie? 'a/m'")
        if xpath == "a":
            elem = xpathHelper()
        elif xpath == "m":
            elem = input("wklej Xpath: ")
        cleararr = ["clear", elem]
        scenario.append(cleararr)
    

if __name__ == "__main__":
    creator()