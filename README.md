# Codeforces-Hacker
This is a python script written for hacking solutions during educational rounds with just entering the hack-test case.

Codeforces: Codeforces is a competitive coding platform where we can take contests as well as do other practice questions.
Codeforces hosts a umber of contests regularly. One of them is an Educational Round. It consists of a 24-hour hacking phase
in which we are allowed to see others solution and if the solution seems to fail at a particular test we can hack it by
entering the hack-test. But, opening so many solutions and checking if they are fine working code or are buggy takes a lot
of time. 

That's why to solve this problem for myself i have written a script that takes the required hack-test case and it's answer and
checks all the " ACCEPTED" solutions if they give the correct output on that case. If not then it prints the Id of the solution
,so that i can hack that solution.

I have used Selenium for navigation through the webpages as it opens a web browser and provides an insight into what the code
is actually doing. Other libraries used include Beautiful Soup, urllib, requests, time, os etc.

There are 2 files. The first one "hack.py" is the main file which takes the Contest id of the educational round. It runs through
all the submissions and checks for the "ACCEPTED" solution and rejects the Wrong submissions. Then, it calls the function from
the second file named "Testing.py". It extracts the code from the webpage and checks the code for the hack-test using Custom Invocation
online in the respective language.

The Id's of the submissions that fail on the hack-test are printed. Also the language of the submitted code is also printed. Various
lines have been commented that helped me for the debugging purposes. You can uncomment them and check for yourself to know the working of
the script.
