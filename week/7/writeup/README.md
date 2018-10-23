Writeup 7 - Forensics I
======

Name: Kodi Rupe
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Kodi Rupe

## Assignment 7 writeup

### Part 1 (40 pts)

1. I used the file command to find the file type, it is a JPEG image data file

2. Using exiftool, I was able to find the coordinates of where the photo was taken. I went online to a site to input coordinates to find the location. Then went on maps to determine the building name. It was taken in Chicago, IL, in the John Hancock Observatory, 360 CHICAGO observatory.

3. Using the file command, I can see that the photo was taken 8/22/18 at 11:33:24 AM

4. Using the file command, I can see that the photo was taken by an Apple iPhone 8

5. Using exiftool, I was able to find out that the photo was taken 539.5m above sea level

6.

### Part 2 (55 pts)

*SUBMIT YOUR WRITEUP DETAILING YOUR APPROACH AND SOLUTION TO THIS PROBLEM HERE (>250 words). Dont forget to include the flag!*

First I tried running the binary.I got permission denied. So I used chmod 777 to change the permission of the file to be able to run it. After running the binary it outputs where is your flag? I then ran objdump to try and figure out what was going on underneath. I ran objdump and tried to get a general understanding of what the program does. I came to the conclusion that it opens the file /tmp/.stego and writes to it after reversing some array. I noticed that many byte values were placed onto the stack at the beginning of main. This looks like it could be an array of characters. So I converted each hex character to ascii to determine that the string was /tmp/.stego. Then, I navigated to the tmp directory and the file appeared to not be there. I had to run ls -a to get the file to appear. I ran the file command on it and it said that it was a file type similar to jpeg. I compared it with the image from the first part and noticed that it was very similar yet slightly different. I opened up bless, a hex editor to see that the magic bytes of the stego file were corrupted. After fixing the magic bytes I was able to view the image which was an image of a stegosauras. I tried to run steghide on the image to find the flag but I was unable to get it to work because I did not know the passcode needed.