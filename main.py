from colorama import Fore, Style, init
import hashlib
import sys
from time import gmtime, strftime

init()

def md5c(inhash):
    i = 0
    print(Fore.GREEN + f"trying to crack hash: {inhash} type: md5")
    hashing = (hashlib.md5)
    with open("wordlist.txt", "r") as h:
        word = [ line.strip() for line in h.read().split("\n") if line ]

    for line in word:
        res = (hashing)(bytes(line, "utf-8")).hexdigest()

        if res == inhash:
            print(Fore.BLUE + "[" + strftime("%H:%M:%S") + "] " + Fore.GREEN + "Found hash: " + res + " | Result: " + line)
            input("Press enter to continue... ")
            exit()
        else:
            i += 1
            print(Fore.BLUE + "[" + strftime("%H:%M:%S") + "] " + Fore.RED + "False hash: " + res + " | " + line)

def sha1c(inhash):
    i = 0
    print(Fore.GREEN + f"trying to crack hash: {inhash} type: sha1")
    hashing = (hashlib.sha1)
    with open("wordlist.txt", "r") as h:
        word = [ line.strip() for line in h.read().split("\n") if line ]

    for line in word:
        res = (hashing)(bytes(line, "utf-8")).hexdigest()

        if res == inhash:
            print(Fore.BLUE + "[" + strftime("%H:%M:%S") + "] " + Fore.GREEN + "Found hash: " + res + " | " + line)
            input("Press enter to continue... ")
            exit()
        else:
            i += 1
            print(Fore.BLUE + "[" + strftime("%H:%M:%S") + "] " + Fore.RED + "False hash: " + res + " | " + line)

def sha256c(inhash):
    i = 0
    print(Fore.GREEN + f"trying to crack hash: {inhash} type: sha256")
    hashing = (hashlib.sha256)
    with open("wordlist.txt", "r") as h:
        word = [ line.strip() for line in h.read().split("\n") if line ]

    for line in word:
        res = (hashing)(bytes(line, "utf-8")).hexdigest()

        if res == inhash:
            print(Fore.BLUE + "[" + strftime("%H:%M:%S") + "] " + Fore.GREEN + "Found hash: " + res + " | " + line)
            input("Press enter to continue... ")
            exit()
        else:
            i += 1
            print(Fore.BLUE + "[" + strftime("%H:%M:%S") + "] " + Fore.RED + "False hash: " + res + " | " + line)

def sha512c(inhash):
    i = 0
    print(Fore.GREEN + f"trying to crack hash: {inhash} type: sha512")
    hashing = (hashlib.sha512)
    with open("wordlist.txt", "r") as h:
        word = [ line.strip() for line in h.read().split("\n") if line ]

    for line in word:
        res = (hashing)(bytes(line, "utf-8")).hexdigest()

        if res == inhash:
            print(Fore.BLUE + "[" + strftime("%H:%M:%S") + "] " + Fore.GREEN + "Found hash: " + res + " | " + line)
            input("Press enter to continue... ")
            exit()
        else:
            i += 1
            print(Fore.BLUE + "[" + strftime("%H:%M:%S") + "] " + Fore.RED + "False hash: " + res + " | " + line)



try:
    if sys.argv[1] == "-md5":
        inhash = sys.argv[2]
        md5c(inhash)
    elif sys.argv[1] == "-sha1":
        inhash = sys.argv[2]
        sha1c(inhash)
    elif sys.argv[1] == "-sha256":
        inhash = sys.argv[2]
        sha256c(inhash)
    elif sys.argv[1] == "-sha512":
        inhash = sys.argv[2]
        sha512c(inhash)
except:
    print(Fore.RED + f"Wront usage! Make sure you did 'python3 {sys.argv[0]} <hashtype (like: -md5)> <hash>'\n\nSupported hashes: md5, sha1, sha256 and sha512")
