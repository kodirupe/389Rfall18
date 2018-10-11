Writeup 5 - Binaries I
======

Name: Kodi Rupe
Section: 0101

I pledge on my honor that I havie not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Kodi Rupe

## Assignment 5 Writeup

First I notice that there are 3 parameters. This means the parameters are in rdi,rsi, and rdx. This requires a register, rcx to be initalized to 0. Use the cmp instruction to see if rcx is equal to strl. If so return, this means the strl is 0. Otherwise, enter the loop. rdi is a pointer so it is used by doing mov ptr[rdi + rcx], rsi. At the end of each iteration, we check using the cmp instruction if rcx == strl. If so we exit the loop, otherwise we jump back to the beginning. Then we set rdi+rcx to '\0'


Looking at the problem, I noticed that there are 3 parameters. This means that the parameters are in rdi,rsi, and rdx. The first 2 paramaters are pointers so they are 64bit values, and the len is an integer a 32 bit value. This program requires a loop and thus jump instructions and a couple labels. This is going to look like: initalize a register, x,  to 0. Then check if it is less than len (rdx) using the cmp instruction. If so, enter the loop, if not jump to the label L1. Inside the loop do mov r, [esi + x] where are is an arbitrary register. Then do 
mov ptr[rdi + x], r to move src[i] to dst[x]. Then increment i using the add instruction. Then check if x is less than rdx, if so go back to L2, otherwise set the last index of dst to '\0'.

   
Unfortunately, I was unable to test and debug this. I had a lot going on at the beginning of the week and got a late start. Ive also had issues with downloading Kali so I was unable to run on the VM. I tried to run on my local machine but I ended up getting errors.
