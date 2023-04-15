import os
import subprocess
from concurrent.futures import ThreadPoolExecutor
from colorama import init, Fore, Style
import smtplib

print(Fore.RED + """
###########################################################
           #-------) Web crawler pro (---------#
                    Code By Dharsun R J 
###########################################################
""")

print(Fore.GREEN + """╔══════════════════════════════════════════════════════════════════════════════╗""" + Style.RESET_ALL)
print(Fore.YELLOW + """   Output Files : If there is no files, Means crawler doesn't find any output. \n\n""" +
   Fore.LIGHTCYAN_EX + """   Detailed-Nuclei-Report.txt""" + Style.RESET_ALL + """ = File contains entire nuclei logs \n""" +
   Fore.LIGHTCYAN_EX + """   Nuclei-results.txt """ + Style.RESET_ALL + """= File contains required nuclei results """)
print(Fore.GREEN + """╚══════════════════════════════════════════════════════════════════════════════╝
""" + Style.RESET_ALL)

Targets = input(Fore.YELLOW + "Enter file name that contains targets = " + Style.RESET_ALL)
headers = input(Fore.YELLOW + "Enter file name that contains required headers = " + Style.RESET_ALL)
print("")
print(Fore.GREEN + "Initiating Scanning..." + Style.RESET_ALL)
print("")

cmd = f"nuclei -H {headers} -l " + Targets + " -t nuclei-templates -silent"
with subprocess.Popen(cmd, stdout=subprocess.PIPE, bufsize=1, universal_newlines=True, shell=True) as p:
    for line in p.stdout:
        print(line, end="")
        fd = open("Detailed-Nuclei-Report.txt", 'a')
        txt = line + '\n'
        fd.write(txt)
        fd.close()
        if any(word in line.lower() for word in ['critical', 'high', 'medium']):
            fd = open("Nuclei-results.txt", 'a')
            txt = line + '\n'
            fd.write(txt)
            fd.close()

print(Fore.GREEN + "Completed..." + Style.RESET_ALL)
sender_email = "ddrish43@gmail.com"
receiver_email = "youcanttextme@gmail.com"
password = "sxdawwkugzpddpsv"
message = """\
Subject: Hi there
Nuclei has completed"""

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
