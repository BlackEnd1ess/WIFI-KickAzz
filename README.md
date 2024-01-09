# WIFI-KickAzz
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

