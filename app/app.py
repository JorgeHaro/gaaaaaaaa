from flask import Flask, render_template
from colorama import Fore,Back,Style

#from interfaz import inicializar_ventana

app = Flask(__name__)

@app.route('/')
def index():
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
    #inicializar_ventana()
    #return '<h1>Hola mundo! - subscribe</h1>'
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True) #port = 5000