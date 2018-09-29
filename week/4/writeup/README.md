Writeup 3 - Pentesting I
======

Name: Kodi Rupe
Section: 0101

I pledge on my honor that I havie not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Kodi Rupe

## Assignment 4 Writeup

### Part 1 (45 pts)
*Put your writeup >= 300 words here in response to the part 1 prompt*
First, I used the hint that the server was vulnerable to a commandline inection attack. So, after running nc cornerstoneairlines.co 45 and the prompt asked for an IP, I tried injecting commands. First, I did ;ls. I was able to see all the directories on the server. After that, I attempted to go into the root directory with the cd command and then list sub directories. This lead to no where. I attempted to do this for a few directories and eventually I tried the home directory. I used the command ;cd home;ls. I saw a suspicious file named flag.txt. Then, I used the command ;cd home;head flag.txt. The head command prints out the beginning of the file. The flag is CMSC389R-{p1ng_as_a_$erv1c3}. Krueger should sanitize all inputs to the server. For example, if he eliminated ; and & from the inputs I wouldn't have been able to perform this attack. Eliminating all special characters or preceding all special characters with a \ would prevent the server from interpreting it as if it was a command

### Part 2 (55 pts)
*Put your writeup >= 200 words here in response to part 2 prompt. Your code for part 2 should be copied into a file in the /writeup directory and pushed there as well*

First, I wrote main. I created a while loop that acts as the outer shell. This will continue to ask for commands until quit is inputted. When the shell command is inputted, it goes into an inner shell that is facilitated by another while loop. Within the inner shell, if a command changes directories, I keep track of these changes in a string, concatenated each time a directory change occurs. If the command does not change directories, I call execute_command with the string that contains the directory changes concatenated with the current command. The quit command exits to the outer shell. For the pull command, I used split to strip the white space. Then I called execute_cmd with cat and the 2nd to last entry of the array from the split command. In execute command I opened the socket, connected to the socket, and use the send function followed by '\n'. I do a 2 second delay. Then I use the receieve function. 