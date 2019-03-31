import requests
import json
import threading
import time
import random
from multiprocessing import Process
from tkinter import *
from tkinter import messagebox


def info(l):
    #create temporary strings
    tempu = str(input('\nusername\n@'))
    tempp = str(input('password\n$'))
    tempt = str(input('target\n@'))

    l['username'] = tempu
    l['password'] = tempp
    l['target'] = tempt
    return l

def turbo():
    params = {}
    log = info(params)

    #sesssion

    s = requests.session()

    url1 = "https://www.instagram.com/accounts/login/"

    r1 = s.get(url1)
    
    csrf1 = r1.cookies.get_dict()['csrftoken']
    
    url2 = 'https://www.instagram.com/accounts/login/ajax/'
    

    #login info
    
    username = log['username']

    password = log['password']

    targets = log['target']

    data2 = {
        'username': username,
        'password': password,
        'queryParams': '{}'
    }

    #headers
    
    h2 = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/accounts/login/',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        'x-csrftoken': csrf1,
        'x-instagram-ajax': '1',
        'x-requested-with': 'XMLHttpRequest'
    }

    #init

    r2 = s.post(url2, headers=h2, data=data2)


    if r2.json()['authenticated'] == False:
        print('Bad Freshie.... Retry login')
        
        time.sleep(.2)
        turbo()
    else:
        csrf = r2.cookies.get_dict()['csrftoken']
        print('Authenticated')
        time.sleep(.2)
    turboin = True
    #start monitoring the username
    tryn = 0
    while turboin == True:
        res = requests.get('https://www.instagram.com/{0}'.format(log['target']))
        tryn = tryn + 1
        print('{0}, {1}, {2}\r'.format(tryn, log['target'], res))
        if res.status_code == 404:
            print('Tag Available')

            #init url
              
            urlf = "https://www.instagram.com/accounts/edit/"

            #post new data
              
            hf = {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/accounts/edit/',
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
                'x-csrftoken': csrf,
                'x-instagram-ajax': '1',
                'x-requested-with': 'XMLHttpRequest'
            }
            
            df = {
                'first_name': 'Too Slow',
                'email': '{}xxx@protonmail.com'.format(str(random.randint(11111111, 99999999))),
                'username': log['target'],
                'phone_number':'',
                'gender': '3',
                'biography':'Claimed Lol',
                'external_url':'',
                'chaining_enabled': 'on'
            }
            #change the acc to the turbo name
            s.post(urlf, headers=hf, data=df)
            print('Completed Turbo Killing Thread')
            messagebox.showinfo("Claimed", "Claimed @{0}".format(log['target']))
            turboin = False
            exit()
            sys.exit()

    

if __name__ == '__main__':
    print("PyTurbo")
    print("---------------------------------------")
    print("")
    #turbo()
    t = threading.Thread(target=turbo())
    t.start()
