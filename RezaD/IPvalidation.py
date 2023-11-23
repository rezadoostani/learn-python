import re


def check(Ip):
    regex = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"
    
    if re.search(regex, Ip):
        print("Valid Ip address")

    else:
        print("Invalid Ip address")


if __name__ == "__main__":
    Ip = input("Enter ip address: ")
    check(Ip)
