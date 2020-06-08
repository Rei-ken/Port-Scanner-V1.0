from socket import *

def banner():
        print("""
###########################################################

#------------------PORT SCAN V 1.0-----------------------#

#--------------------Coder By Rei-ken-------------------#

###########################################################
""")
        
def scan():
        
        if __name__ == '__main__':
                hedef=input("Hedef: ")
                hedef_ip=gethostbyname(hedef)
                print("taranıyor:",hedef_ip)
        
                for i in range(6555):
                                baglantı=socket(AF_INET,SOCK_STREAM)
                                port_tarama=baglantı.connect_ex((hedef_ip,i))
                                if(port_tarama==0):
                                        print("Açık port: %d " %(i))
                                baglantı.close()
        input("tarama sonlandırıldı.")

banner()
scan()
