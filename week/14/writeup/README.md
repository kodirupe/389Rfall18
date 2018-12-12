Writeup 10 - Crypto II
=====

Name: Kodi Rupe
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Kodi Rupe

## Assignment 10 Writeup

### Part 1 (70 Pts)

First I tried just going to the file directly by putting "http://cornerstoneairlines.co:8080/view.php?filename=/etc/passwd" into the URL. This did not work. I thought this had something to do with the firewall and thought putting an and "1 or 1" would work. So, i put "http://cornerstoneairlines.co:8080/view.php?filename=/etc/passwd or 1=1" into the URL. This did not work and just took me to a Google search. I did not really know where to go from here and was unable to get the flag.



### Part 2 (30 Pts)


On the first level, I saw that there was a query box. Since this is a XSS challenge, I assumed the script we want to run would be in there. Just as a shot in the blue, I tried entering HTML that runs a javascript, hoping that the website doesn't sanatize input. This worked, I used "<script>alert(1)</script>". 

On the second level, there was a box to enter a status. I tried the same script as the first level but this didnt work. I know a little javascript from other classes so I know that I can call an error using onerror. So I wrote HTML that would cause an error, then call a javascript alert. I thought using a src tag along with a broken link would do the trick. So I used the following as input to the text box, "<img src="brokenlink.gov" onerror="javascript:alert(1)"/>

On the third level, I noticed that there was no box to input. So, the input must go into the URL. I didnt really know where to go from here so I looked at the source code. In the chooseTab function, it uses the parameter 'num' to generate the img tag used to insert the image onto the webpage. I tried inserting javascript in as this parameter in the URL. I tried 'onerror'alert(1)';. The final URL ended up being "https://xss-game.appspot.com/level3/frame#1'onerror='alert(1)';" This worked.

On the fourth level, I tried inputting the first and second script into the timer box. This didnt work. I looked at the source code, but still didn't really know where to go. I decided to look at the hints. The hints said to enter a single quote and watch the error console. This caused a syntax error, it was an unterminated literal. Using the prior hint, we can encode a semi colon as %3b. Maybe, we can insert some command like we did in the command line injection HW. I tried entering "https://xss-game.appspot.com/level4/frame?timer=%3Balert(1)". This didnt work. The first hint said to look at the source code on how the start timer function is called. This lead to, "https://xss-game.appspot.com/level4/frame?timer=')%3Balert(1)%3Bvar b =(';"

On the fifth level there was a signup link. Upon clicking this i noticed in the URL that there is a variable called next. I thought looking into the source code on how to use this would be a good start. It is used to set the window location. So I thought I may be able to insert java code into the next. I used the URL "https://xss-game.appspot.com/level5/frame/signup?next=javascript:alert(1)". Then inserted something into the mail box, and this worked

