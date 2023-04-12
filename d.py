import os
import subprocess
from concurrent.futures import ThreadPoolExecutor
from colorama import init, Fore, Style
import smtplib

# function to run nuclei scan for a single URL

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
# function to run nuclei scan for a single URL
def run_nuclei(url):
    #cmd = f"nuclei -H {headers} -u {url.strip()} -t nuclei-templates -p http://127.0.0.1:8080 -silent"
    cmd = f"nuclei -H {headers} -u {url.strip()} -t nuclei-templates -silent"
    output = []
    with subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, bufsize=1, universal_newlines=True) as p:
        for line in p.stdout:
            with open('Detailed-Nuclei-Report.txt', 'a') as f:
                f.write(f"{url.strip()} >> {line}\n")
            if any(word in line.lower() for word in ['critical', 'high', 'medium', 'low']) and "info" not in line.lower():
                output.append(line.strip())
                # save matched output to file immediately
                with open('Nuclei-results.txt', 'a') as f:
                    f.write(f"{line}")


# read URLs from file
with open(Targets, 'r') as f:
    urls = f.readlines()

# create thread pool and run nuclei scans for all URLs
with ThreadPoolExecutor(max_workers=os.cpu_count()) as executor:
    executor.map(run_nuclei, urls)
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