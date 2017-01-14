#!/usr/bin/env python3
import glob
import subprocess
import shutil
import re

p="./docs/"
shutil.rmtree(p)
shutil.copytree("./src",p)
c=0
for fn in glob.glob(p+"*.htm"):
	c+=1
	with open(fn, "r+") as f:
		data = f.read()
		data=data.replace("<body>","""<body>source: <a href="http://www.palikanon.com/english/sangaha/sangaha.htm">http://www.palikanon.com/english/sangaha/sangaha.htm</a><script type="text/javascript" id="cool_find_script" src="find6.js"></script><style>.highlight{	background-color: blue;}.find_selected{	background-color: green;} a {color: blue;text-decoration: none; /* no underline */}</style>""")
		data=data.replace("../../","")
		data=data.replace("../images/","")
		data=data.split("<p>")
		for i,v in enumerate(data):
			data[i]="<a name='%s-%s' href='?#%s-%s'>&nbsp;</a>"%(c,i,c,i)+data[i]
		f.seek(0)
		f.write("<p>".join(data))
		f.truncate()		
		#data=data.split("<hr>")
		#for i,v in enumerate(data):
		#	data[i]="%s<a name='%s-%s' href='?#%s-%s'><img src=lnk.png /></a>"%(v,c,i,c,i)
		#f.seek(0)
		#f.write("<hr>".join(data))
		#f.truncate()
combFnP=p+"index.htm"
try:
	shutil.rmtree(combFnP)
except:
	pass
subprocess.check_output("cat %s*.htm > %s"%(p,combFnP), shell=True)
with open(combFnP, "r+") as f:
	data = f.read().split("</style>")
	h1=data.pop(0)
	for i,v in enumerate(data):
		data[i]=v.split("</body>")[0]
	data="<hr>".join(data)
	data="%s</style>%s</body></html>"%(h1,data)
	f.seek(0)
	f.write(data)
	f.truncate()
