    
    
#Working


class Arquivo(object):
    def __init__(self, arquivo):
        self.eop = (78).to_bytes(4, byteorder="big")
        self.arquivo = arquivo
        self.arqFrag, self.total_payloads = self.frag(arquivo)
        self.index = 0

    def frag (self, arquivo):
        arquivo_binario = open(arquivo,'rb').read()
        tamanho = len(arquivo_binario)
        payloads_inteiros = tamanho // 114
        tamanho_payload_incompleto = tamanho % 114
        total_payloads = payloads_inteiros + 1
        lista = []
        for npayloads in range(0,payloads_inteiros):
            payload = b""
            for byte in range(0,114):
                indice = npayloads * 114 + byte
                #print(indice)
                payload += arquivo_binario[indice].to_bytes(1, byteorder="big")
            lista.append(payload)
        payload = b""
        for e in range(0,tamanho_payload_incompleto):
            indice = npayloads * 114 + e
            payload += arquivo_binario[indice].to_bytes(1, byteorder="big")
        lista.append(payload)
        return lista, total_payloads

    def increaseIndex(self):
        self.index +=1
    def getIndex(self):
        return self.index

    def getPayloadSize(self,index):
        return len(self.arqFrag[self.index])

    def setHeadDados(self):
        head = b""
        message_type = (2).to_bytes(1, byteorder="big")
        hs_response = (0).to_bytes(1, byteorder="big")
        error_package = (0).to_bytes(1, byteorder="big")
        nPackage = (self.total_payloads).to_bytes(1, byteorder="big")
        package_index = (self.index).to_bytes(1, byteorder="big")
        payload_size = (self.getPayloadSize(self.index)).to_bytes(1, byteorder="big")
        acknolage_confirmartion = (0).to_bytes(1, byteorder="big")
        null_bytes = (0).to_bytes(3, byteorder="big")
        head = message_type + hs_response + error_package + nPackage + package_index + payload_size +acknolage_confirmartion +null_bytes
        return head


    def setPacotes(self):
        lista = []
        pacote = b""
        for e in self.arqFrag:
            pacote = b""
            pacote = self.setHeadDados() + e + self.eop
            lista.append(pacote)
            self.increaseIndex()
        return lista