Writeup 9 - Crypto I
=====

Name: Kodi
Section: Rupe

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Kodi Rupe

## Assignment 9 Writeup

### Part 1 (60 Pts)
First, I realized that I would need the hashes file contents, and the password list contents. I first read these in using readlines and strip to get rid of any trailing \n. I now have the contents separated nicely into a list. Since the salt is unknown, and it is different for each password I bruteforced it by prepending every salt to every password, used SHA512 and compared it to every entry in the hashes list. If there was a match, a password salt combination was found.The following salt password combinations were found:

Salt:k Password: neptune
Salt:m Password: jordan 
Salt:p Password: pizza
Salt:u Password:loveyou

/Users/kodi/Desktop/Screen\ Shot\ 2018-11-12\ at\ 12.05.16\ AM.png 

### Part 2 (40 Pts)

First, to get an idea of what was happening, I ran the command nc 142.93.117.193 7331 on the commandline to see what would happen. I saw that it repeatedly asked for a certain type of hash on a random string. After connecting to the server and receiving data, I would split it to have it in an array. This allowed me to easily extract the string and type of hash easily. This allowed me to easily call which hash function to use. Since I knew that the final hash would output a "You win!" I checked if this was a substring everytime data was returned from the server. If it was a substring then the flag was found. Otherwise we have to keep going. The flag is: CMSC389R-{H4sh-51!ngInG-h@sH3r}.

/Users/kodi/Desktop/Screen\ Shot\ 2018-11-12\ at\ 12.04.47\ AM.png 