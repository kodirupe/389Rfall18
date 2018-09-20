Writeup 3 - OSINT II, OpSec and RE
======

Name: Kodi Rupe
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Kodi Rupe

## Assignment 3 Writeup

### Part 1 (100 pts)
*INPUT YOUR RESPONSE TO THE PROMPT HERE*

First, the IP address of the website server was easily found. The admin panel had the IP address listed in the URL bar and the I found the IP address of the server through googleiplookup. Fred Krueger could take a few measures to hide his server's IP address. Krueger should use a VPN on his server. The VPN will allow him to run the server using a virtual IP address to mask the real IP address. The VPN also encrypts the internet traffic (Doichev).

Second, I was able to use nmap to find a vulnerable port. There are programs available that are able to protect against port scanners. For example, PortSentry can protect against port scanners. Port Sentry will listen for a certain number of attempts to connect to a port and the amount of invalid requests. Upon detection of a suspicious connection, PortSentry will employ TCP wrappers and make an entry into the /etc/hosts.dent file for the suspected intruder(SANS Institute InfoSec Reading Room) .

Last, I was able to find the the opertating system that their machine was running. It was running Ubuntu, Apache/2.4.18. Krueger could use Tor. Tor hides IP address, and what operating system the server is running by sending packets through multiple machines on the Tor network. 


Works Cited Links:

https://thebestvpn.com/hide-ip/

https://www.sans.org/reading-room/whitepapers/auditing/port-scanning-techniques-defense-70

https://www.digitaltrends.com/computing/a-beginners-guide-to-tor-how-to-navigate-through-the-underground-internet/


