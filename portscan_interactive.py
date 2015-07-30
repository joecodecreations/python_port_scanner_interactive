import socket
import time

#define our prompt colors we will be using
prompt = '\033[92m'
response = '\033[95m'
other = '\033[91m'

print "clear"
print prompt+"\n\n\n"
print '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
print '+                                                                       +'
print "+ https://github.com/joecodecreations/python_port_scanner_interactive/  +"
print "+                                                                       +"
print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
print "\n\n"

#Prompt user for input variables
print prompt+ "Please select your target's IP Address\n"
target = raw_input("Example: 192.168.0.1 and hit 'enter':"+response).lower()
print prompt+"\n\n\nGreat, Now Select your Target's Lower Port Range\n"
attempt = raw_input("Example: enter 0 for lowest and hit 'enter':"+response).lower()
print prompt+"\n\n\nSelect Upper Range of max port number to check"
upperRange = raw_input("Example 8080 then hit 'enter':"+response).lower()
print prompt+"\n\n\nAre you scanning a local target or remote. We will automatically set proper delays"
thistarget = raw_input(prompt+"Enter `local` or `remote`:"+response).lower()

#set input variables to proper format
target = str(target)
attempt = int(attempt)
upperRange = int(upperRange)


#if the range is set too high reduce it to max
if upperRange > 65353:
        upperRange = 65353
        print prompt+"Up limit set to max port value"

#initial reached value set to zero for no ports found yet
reached = "0"


#one more input for displaying details
details = raw_input(prompt+"Scroll ports as they being checked- Type 'yes' or 'no':"+response).lower()

#set a default timeout
sessionTimeout = 0.0008


#set specific timeout based on what type of server we are targeting
if thistarget == "local":

        sessionTimeout = 0.0008
if thistarget == "remote":
        sessionTimeout = .8


#process through the list of ports
while attempt < upperRange:
        #start a timer
        start = time.time()
        #increase our port number
        attempt=attempt+1

        #if we are to print details print the port we are currently scanning
        if details == 'yes':

                print prompt+"Scanning Port:"+other+" %d" %  attempt
        #endless loop
        while 1==1:
                end = time.time()
                current = end-start

                #check socket connection we are going to attempt
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(sessionTimeout)

                #attempt to try the connection and if we reach it break if not wait for error or timeout
                try:
                        s.connect((target, attempt))
                        #attempt=attempt+1
                        print "Port %d reachable" % attempt
                        if reached == "0":
                                reached = str(attempt)
                        else:
                                #if the connection is there add it to our list of available ports
                                reached = reached+","+str(attempt)
                        break
                except socket.error as e:
                        #print "Error on connect: %s" % e
                        break

                #close the connection
                s.close()
                
#if we have some ports print the ports we have
if reached != 0 :
        print '\033[0m'+ "Ports Open: %s" % reached

#if we have no ports specify as so
else:
        print "No Ports Open"





