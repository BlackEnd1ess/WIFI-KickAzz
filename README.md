# WIFI-KickAzz

UPDATE 26.12.2024:
Added new Script 801pkt_clone.py! This Script sniff Packets and add them into a selectable List.
This Script allow to sniff and reinject WIFI type 2 Data Frames which include
(EAPOL, EAPOL_KEY, Dot11CCMP, Data, Null Data etc..).
In the next Update i will add a Function, where make minimal Changes in this Packet
before reinjecting to Victim. Be careful and read the Warning below this Description!! Important!

# WARNING!
This script was written to test some WIFI Routers/Connected Devices for Security vulnerability or other
Protocol weakness. If you test this Script, make sure that your Testing Environment is ideally disconnected from the internet!
Resent packets can, in rare cases, actually lead to unexpected background traffic and actions and in worst case, affect the service itself.

#
What can happen in this case?

Normally, data packets that have already been processed and are being sent again are discarded. But in some cases the router has a short downtime and it can rarely happen that the manipulated data packet is pushed ahead of the legitimate packet, which means that it is actually accepted and processed. This can be enforced by leaving the router with type 2 frames so that this delay occurs more often.
Since we are mostly sending legitimate manipulated data packets, this can of course have unpredictable results for all participants in this experiment within the test environment.
The consequences could be, for example, that the device will continuously and independently try to connect to a service or protocol. It was also observed that incorrect characters and strings were written to the logs, which should normally remain within the data packet. It also happened that some apps on my smartphone needed a full reset to start again and some apps could no longer be started. These packages can cause irreversible damage to the operating system or render the device unusable, so this risk should be noted.






Testing multible Frame injection via python scapy

if you change tha value in --> return st.join(chr(random.randint(0,285)) for _ in range(random.randint(32,B)))

example: 0-285 creates mostly valid bytes (<=255). if you incrase this value, you will get more chinese,japan or korean characters/icons.
the max valid value for possible character is --> 55295, but be careful! Data packets (type 2) that have character bytes larger than 255 lead to unexpected behavior on both the target and host computers.

It affects: 
- WPA
- WPA2(Default)
- WPA2(Protected Managment Frames)
- WPA3(in a few cases)
- WPA2/3 on 5GHz (only if bot encr. are enabled)

In can confirm this works in the most cases, i have tested this in my Lab with more different Routers and Manufracturers.

The next Value where is reserved as "B" is the payload lenght. If you exceed this value, you will return a Error Message "message to long". Keep this value
between 128-490 if your use type 0. if your use type 2, then keep this value between 128-320.

What can happen if you use this script?
- Connection between AP and Station will disconnect.
- The Router can freeze for one or more minutes.
- The NetworkManager of weak devices can crash and needs to reboot to fixx this.
- Bluetooth Devices can be affected.
- possible, that your connection will reconnect to foreign device.

