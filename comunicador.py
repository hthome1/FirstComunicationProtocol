from enlace import *
import time

class Comunicador(object):
    def __init__(self, serialName):
        self.serialName = serialName
        self.com = enlace(serialName)
        self.com.enable()
        self.eop = (78).to_bytes(4, byteorder="big")
        self.complete_payload = b""
        self.lastPackage = -1

    def getHead(self):
        self.head, r = self.com.getData(10)
        self.message_type = self.head[0]
        self.hs_response = self.head[1]
        self.error_package = self.head[2]
        self.nPackage = self.head[3]
        self.package_index = self.head[4]
        self.payload_size = self.head[5]
        self.acknolage_confirmartion = self.head[6]

    def getPayload(self):
        self.payload, teste = self.com.getData(self.payload_size)

    def getEop(self):
        self.eop_recebida, vau= self.com.getData(4)

    def conferData(self):
        if self.payload_size == len(self.payload) and self.eop_recebida == self.eop and\
        self.package_index == self.lastPackage + 1:
            return True
        else:
            return False

    def sendAcknowlage(self):
        head = b""
        pacote = b""
        message_type = (3).to_bytes(1, byteorder="big")
        hs_response = (0).to_bytes(1, byteorder="big")
        #error_package = (self.package_index).to_bytes(1, byteorder="big")
        nPackage = (self.nPackage).to_bytes(1, byteorder="big")
        package_index = (self.package_index).to_bytes(1, byteorder="big")
        payload_size = (0).to_bytes(1, byteorder="big")
        null_bytes = (0).to_bytes(3, byteorder="big")


        if self.conferData() == False:
            error_package = (self.lastPackage + 1).to_bytes(1, byteorder="big")
            acknolege_confirmation = (1).to_bytes(1, byteorder="big")
            print("-------------------")
            print("O pacote {} esta corrompido".format(self.lastPackage + 1))
            print("Pedindo o reenvio do pacote")
            self.com.rx.clearBuffer()
        else:
            error_package = (0).to_bytes(1, byteorder="big")
            acknolege_confirmation = (0).to_bytes(1, byteorder="big")
        self.headAc = message_type + hs_response + error_package + nPackage + package_index \
        + payload_size + acknolege_confirmation + null_bytes
        pacote = self.headAc + self.eop
        self.com.sendData(pacote)
        time.sleep(0.5)

    def sendHS(self):
        head = b""
        pacote = b""
        message_type = (1).to_bytes(1, byteorder="big")
        hs_response = (0).to_bytes(1, byteorder="big")
        error_package = (0).to_bytes(1, byteorder="big")
        nPackage = (0).to_bytes(1, byteorder="big")
        package_index = (0).to_bytes(1, byteorder="big")
        payload_size = (0).to_bytes(1, byteorder="big")
        acknolege_confirmation = (0).to_bytes(1, byteorder="big")
        null_bytes = (0).to_bytes(3, byteorder="big")
        head = message_type + hs_response + error_package + nPackage + package_index \
        + payload_size + acknolege_confirmation + null_bytes
        pacote = head + self.eop
        self.com.sendData(pacote)
        time.sleep(0.5)

    def rogerHS(self):
        head = b""
        pacote = b""
        message_type = (1).to_bytes(1, byteorder="big")
        hs_response = (1).to_bytes(1, byteorder="big")
        error_package = (0).to_bytes(1, byteorder="big")
        nPackage = (0).to_bytes(1, byteorder="big")
        package_index = (0).to_bytes(1, byteorder="big")
        payload_size = (0).to_bytes(1, byteorder="big")
        acknolege_confirmation = (0).to_bytes(1, byteorder="big")
        null_bytes = (0).to_bytes(3, byteorder="big")
        head = message_type + hs_response + error_package + nPackage + package_index \
        + payload_size + acknolege_confirmation + null_bytes
        pacote = head + self.eop
        self.com.sendData(pacote)
        time.sleep(0.5)


    def end(self):
        self.com.disable()

    def sendPackage(self, x):
        self.com.sendData(x)
        time.sleep(0.5)

    def joinPackages(self, payload):
        self.lastPackage +=1 
        self.complete_payload += payload

        
        
