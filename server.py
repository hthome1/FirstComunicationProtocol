from enlace import *
import time
from comunicador import Comunicador
from arquivo import Arquivo


#arduinoDue
serialName = "COM6"


def main():
    try:
        #declaramos um objeto do tipo enlace com o nome "com". Essa é a camada inferior à aplicação. Observe que um parametro
        #para declarar esse objeto é o nome da porta.
        server = Comunicador(serialName)


        print("-------------------------")
        print('Porta Com habilitada')
        print("-------------------------")
        


        #Parte do HandShake

        doingIt = True

        while doingIt == True:

            server.getHead()
            print("head")
            server.getPayload()
            print("payload")
            server.getEop()
            print("eop")
            server.sendAcknowlage()
            print("mando aknolage")
            server.joinPackages(server.payload)
            if server.package_index == (server.nPackage - 1):
                doingIt = False


        imageW = "./recebidaTeste.png"
        print("-------------------------")
        print ("Salvando dados no arquivo :")
        print (" - {}".format(imageW))
        f = open(imageW, 'wb')
        f.write(server.complete_payload)

        f.close()   

        print("-------------------------")
        print("imagem recebida e salva")
        print("-------------------------")
        print("Comunicação Finalizada")

        server.end()


    except:
        print("ops! :-\\")
        server.end()
        print(" desa")
        
if __name__ == "__main__":
    main()
