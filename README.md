# StealthProbes
StealthProbe is a tool used for scanning/pinging IOT devices, whilst keeping your network IP hidden. This is done by using tor network proxies. 


# Installation Process 
##### 1st Clone the repo
```
git clone https://github.com/KenjiDoom/StealthProbes.git
```
##### 2nd Install packages (Ubutnu and Arch)
```
pip install -r requirments.txt && sudo apt-get install tor
pip install -r requirments.txt && sudo pacman -S tor
```
##### 3rd Setup tor with password (change password here)
```
$ tor --hash-password TEST_PASSWORD 
```
##### 4th Step is to copy the hash into the torrc file.
You can use / to quick search a keyword, in this case look for CookieAuthentication 1
```
vim /etc/tor/torrc
/CoockieAuthentication 1 
```
Once you find it enable it by removing the hastag, Also enable HashedControlPassword & ControlPort 9051
Remove the old hash & Input your new one, It should look something like this
`[
ControlPort 9051
## If you enable the controlport, be sure to enable one of these
## authentication methods, to prevent attackers from accessing it.
HashedControlPassword 16:ECE06C3C0EBEEA816015C9DD04E8607B34C8CF148E357AA19F1B527723
CookieAuthentication 1
]
`
