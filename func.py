from arquivo import Arquivo

path = "./imageB.png"
arquivo = Arquivo(path)

x = arquivo.setPacotes()



# print(x[0][0])
# print(x[0][1])
# print(x[0][2])
# print(x[0][3])
# print(x[0][4])
# print(x[0][5])
# print(x[0][6])
# print(x[0][7])
# print(x[0][8])
# print(x[0][9])


for e in x:
    print(e[3],e[4],e[5])
    print(len(e))



