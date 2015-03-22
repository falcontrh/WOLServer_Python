#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  untitled.py
#  
#  Copyright 2015  <pi@raspberrypi>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import socket
import time

# Port to listen on
SERVER_LISTEN_PORT = 50000
SERVER_SENDTO_PORT = 8
WOL_BROADCAST_ADDRESS = '192.168.10.255'
# Max message buffer size
MAXLINE = 4096

proc_msgs = 0

def StartServer():
	read_fd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	read_fd.bind(('', SERVER_LISTEN_PORT))
	
	proc_msgs = 1

	while True:
		data, address = read_fd.recvfrom(MAXLINE);
		if not data: continue
		print ("Received data from: %s" % str(address))
		ProcessMessages(data)
	
def ProcessMessages(packet):
	print ("Sending packet: %s" % packet)
	send_fd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	send_fd.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
	send_fd.sendto(packet, (WOL_BROADCAST_ADDRESS, SERVER_SENDTO_PORT))
	send_fd.close()	

def StopServer():
	proc_msgs = 0
	read_fd.close()

def main():
	time.sleep(5.0)
	StartServer()
	StopServer()
	return 0

if __name__ == '__main__':
	main()

