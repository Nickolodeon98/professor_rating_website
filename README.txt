My first django project to build a website that rates professors and modules

To use the client, simply run the python program client.py:
python client.py
Then the command line interface is shown as the following: >>> 

There are 8 commands in total

1. register
- Register the new user.
- Simply type 'register' on command line interface

2. login 'url/'
- Log the user in
- Simply type 'login url' on command line interface, where url is the URL of server (please put '/' at the end of url, e.g. https://fy16sj.pythonanywhere.com/)

3. logout
- Log the user out
- Simply type 'logout' on command line interface

4. list
- List the information of module instances
- Simply type 'list' on command line interface

5. view
- View the ratings of professors
- Simply type 'view' on command line interface

6. average 'professor id' 'module code'
- View the average of professor in a certain module instance
- Simply type 'register professor_id module_code' on command line interface, where professor_id is the unique id of professor and module_code is the unique code of module.

7. rate 'professor id' 'module code' 'year' 'semester' 'rating'
- Rate the professor
- Simply type the command as shown above, where each parameter is self-explanatory.

8. quit
- Terminate the program
- Simply type 'register' on command line interface


The name of pythonanywhere.com domain is https://fy16sj.pythonanywhere.com
The password to be used for admin site is abcd1234.

*The PrettyTable package has been used for the list command, so please install this!
