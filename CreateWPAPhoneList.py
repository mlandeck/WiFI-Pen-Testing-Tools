# usage: python CreateWPAPhoneList.py <area code>
# example: python CreateWPAPhoneList.py 408
# Your wordlist can be found in the file "phonelist.txt"


def append_digits(num):
    num = str(num)
    with open("phonelist.txt", "w") as f:
        for i in range(1, 9999999):
            f.write(num + str(i).zfill(9) + "\n")

append_digits(123)
