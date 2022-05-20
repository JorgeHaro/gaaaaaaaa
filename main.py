#Librerias Externas
from colorama import Fore,Back,Style
#Librerias Propias
from interfaz import inicializar_ventana

if __name__ == "__main__":
    print(Fore.YELLOW + "======================================================================"+ Style.RESET_ALL)
    print(Back.BLACK+Fore.LIGHTRED_EX + """
 _______                 __   ____       __     _______        
|   __   \     /\       |  | |     \    |  |   /       \\       
|  |   \  \   /  \      |  | |  |\  \   |  |  /   ___   \\      
|  |__ /  /  / /\ \     |  | |  | \  \  |  | |   |   |   |     
|    ____/  / /__\ \    |  | |  |  \  \ |  | |   |   |   |     
|   |      /  ____  \   |  | |  |   \  \|  | |   |___|   |     
|   |     /  /    \  \  |  | |  |    \     |  \         /      
|___|    /__/      \__\ |__| |__|     \____|   \_______/       
                                                                
    """ + Style.RESET_ALL+'\033[0;m') 
    print(Fore.YELLOW + "======================================================================"+ Style.RESET_ALL)
    inicializar_ventana()