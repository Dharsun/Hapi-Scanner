
#!/bin/bash
sudo apt-get update
sudo apt-get -y install golang

#Installing python3 & pip
apt-get install python3 -y
apt-get install pip -y
# Installing required Python3 modules

pip3 install colorama

go install -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest
git clone https://github.com/projectdiscovery/nuclei-templates.git
