import curses,os,time,random,gc
from scapy.all import *

m='wlan0mon'
SCP=[]

def catch_pkt(p):
	if p.haslayer(Dot11) and p.type == 2:
		if len(SCP) < 10:
			SCP.append(p)
sniff(iface=m,prn=catch_pkt,timeout=8)
print(len(SCP),' packets in list. ')

def handle_selection(pkt):
	print(pkt.show())
	while True:
		sendp(pkt,iface=m,count=1,verbose=0)
def run(stv):
	if len(SCP) <= 0:
		print('no packets found')
		return
	curses.curs_set(0)
	idx=0
	stv.clear()
	while True:
		stv.clear()
		for i,text in enumerate(SCP):
			if i == idx:
				stv.addstr(i,0,f"{text}",curses.A_REVERSE)
			else:
				stv.addstr(i,0,f"{text}")
		stv.refresh()
		key = stv.getch()
		if key == curses.KEY_UP and idx > 0:
			idx-=1
		elif key == curses.KEY_DOWN and idx < len(SCP)-1:
			idx+=1
		if key == ord('s'):
			os.system('clear')
			handle_selection(SCP[idx])
			break
curses.wrapper(run)