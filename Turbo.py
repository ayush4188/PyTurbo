import requests
import json
import random
from tkinter import *
from tkinter import messagebox
import sys

tryn = 0
master = Tk()

def turbo():

    global tryn
    global master
    global text1
    global insert
    params = {
        'username': e1.get(),
        'password': e2.get(),
        'target': e3.get()
    }

    #sesssion

    s = requests.session()

    url1 = "https://www.instagram.com/accounts/login/"

    r1 = s.get(url1)
    
    csrf1 = r1.cookies.get_dict()['csrftoken']
    
    url2 = 'https://www.instagram.com/accounts/login/ajax/'
    

    #login info
    
    username = params['username']

    password = params['password']

    targets = params['target']

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
        messagebox.showinfo("Uh oh", "Invalid Account Info Or Accept Sus Request On Instagram")
        print("$Failed")
        
    else:
        csrf = r2.cookies.get_dict()['csrftoken']
        print('$Authenticated')
        turboin = True
        #start monitoring the username
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
            'x-requested-with': 'XMLHttpRequest',
            'Connection': 'keep-alive'
        }
        
        df = {
            'first_name': 'Claimed',
            'email': '{}xxx@protonmail.com'.format(str(random.randint(11111111, 99999999))),
            'username': params['target'],
            'phone_number':'',
            'gender': '3',
            'biography':'',
            'external_url':'',
            'chaining_enabled': 'on'
        }
        urlf = "https://www.instagram.com/accounts/edit/"
        master.update()
        res = None
        s.headers.update(hf)
        
        while turboin == True:
            tryn += 1
            if tryn % 20 == 0:
                text1.delete("1.0", END)
                text1.insert("1.0", tryn)
                master.update()

            print('Try:{0}, Target:{1}, Code:{2}'.format(tryn, params['target'], res))
            
            try:
                res = requests.get('https://www.instagram.com/{0}'.format(params['target']))
                if res.status_code == 404:
                    s.post(urlf, data=df)
                    messagebox.showinfo("Dead", "Killed @{0} | {1} tries".format(params['target'], tryn))
                    print("\nThreads Killed - Close Program")
                    turboin = False
                    master.destroy()
                    exit(0)
            except:
                print("\nconnection closed to instagram. Rebooting...\n")
                turboin = False
                turbo()

if __name__ == '__main__':
    print("$output console")
    l1 = Label(master, text="Username", bg="black", fg="red")
    l2 = Label(master, text="Password", bg="black", fg="red")
    l3 = Label(master, text="Target", bg="black", fg="red")
    e1 = Entry(master, bg="black", fg="yellow")
    e2 = Entry(master, bg="black", fg="yellow", show="*")
    e3 = Entry(master, bg="black", fg="yellow")

    b1 = Button(master, text='Beam', bg="black", fg="#00FF1A", command=turbo)

    text1 = Text(master, height=1, width=15, bg="black", fg="#90FFFC")
    text1.insert("1.0", tryn)
    
    master.title('$$')
    l1.pack(fill=X,pady=0)
    e1.pack(fill=X,pady=0)
    l2.pack(fill=X,pady=0)
    e2.pack(fill=X,pady=0)
    l3.pack(fill=X,pady=0)
    e3.pack(fill=X,pady=0)
    b1.pack(fill=X,pady=0)
    text1.pack(fill=X,pady=0)
    text1.bind('<1>', lambda event: text1.focus_set())

    master.mainloop()
