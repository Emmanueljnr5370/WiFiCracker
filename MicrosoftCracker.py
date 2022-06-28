# check how much in Udacity for how much one can pay to learn Cloud Computing.
import sys
from tqdm import tqdm
from msoffcrypto import OfficeFile
path = "C:/Users/User/OneDrive/Documents/Microsoft.docx"
wordlist = 'C:/Users/User/OneDrive/Desktop/Game1/code.txt'

"""with open(path, 'rb') as file:
    off = OfficeFile(file)
    try:
        off.load_key(password='12s4',verify_password=True)
    except Exception as e:
        print('next..',e)
    else:
        print('password found')

"""
with open(wordlist,'r') as words:
    password_list = words.readlines()
    total_passwords = len(password_list)
    for word in tqdm(password_list,total=total_passwords,unit='words'):
        with open(path,'rb') as file:
            off = OfficeFile(file)
            try:
                off.load_key(password=word.strip(),verify_password=True)
            except Exception as e:
                print('next..',e)
                continue

            else:
                print('password found',word)
                break            



