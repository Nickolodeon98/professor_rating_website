import requests
#from prettytable import PrettyTable


url = 'https://fy16sj.pythonanywhere.com/'

# use for loop to find all the titles of modules
# list function
def list():
    output = requests.get(url + 'list').text
    print(output)


def view():
    output = requests.get(url + 'professor/view').text
    print(output)

def rate(profId, modCode, y, term, rating):
    # if url == '':
    #     return print("Log in first!")
    info = {'pro_id':profId, 'm_code':modCode, 'y':y, 'term':term, 'rating':rating}
    requests.post(url + 'rate', data=info)
    # print(response.text)


def average(professorId, moduleId):
    # if url == '':
    #     return print("Log in first!")
    average = requests.get(url + 'rate/average/%s/%s' % (moduleId, professorId)).text
    if average == -1:
        print('Cannot find the rating for this module and professor')
	exit(1)
    professor_name = requests.get(url + 'professor/code/name/%s' % professorId).text
    if professor_name == -1:
        print("Cannot find professor name")
	exit(1)
    module_name = requests.get(url + 'module/name/%s' % moduleId).text
    if module_name == -1:
        print("Cannot find module names")
	exit(1)
    print('\nThe rating of ' + professor_name + ' (' + professorId + ')' + ' in module ' + module_name + ' (' + moduleId + ')' + ' is ' + '*'*int(average))


def register(username, email, password):
    info = {'username': username, 'email': email, 'password': password}
    response = requests.post(url + 'register', data=info)
    print(response.text)

def login(login_url, username, password):
    info = {'username': username, 'password': password}
    response = requests.post(('https://' + login_url + '/log_in'), data=info)
    print(response.text)


def logout():
    response = requests.get(url + 'log_out')
    print(response.text)

def main():
    while(1):
        inputlist = input('>>> ')
        cmd = inputlist.split(' ')
        if cmd[0] == 'register':
            userId = input('Username: ')
            e_mail = input('Email: ')
            passcode = input('Password: ')
            register(userId, e_mail, passcode)
        elif cmd[0] == 'login':
            if len(cmd) == 1:
                print("Wrong Input!")
            elif len(cmd) > 2:
                print("Wrong Input!")
            else:
                userId = input('Username: ')
                passcode = input('Password: ')
                login(cmd[1], userId, passcode)
        elif cmd[0] == 'logout':
            logout()
        elif cmd[0] == 'list':
            list()
        elif cmd[0] == 'view':
            view()
        elif cmd[0] == 'average':
            if len(cmd) <= 2:
                print("Wrong Input!")
            elif len(cmd) > 3:
                print("Wrong Input!")
            else:
                average(cmd[1], cmd[2])
        elif cmd[0] == 'rate':
            if len(cmd) < 6:
                print("Wrong Input!")
            elif len(cmd) > 6:
                print("Wrong Input!")
            else:
                rate(cmd[1], cmd[2], cmd[3], cmd[4], cmd[5])
        elif cmd[0] == 'quit':
            break
        else:
            print("Wrong Input!")

if __name__ == '__main__':
    main()

