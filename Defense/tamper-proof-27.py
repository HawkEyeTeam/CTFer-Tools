import os,hashlib,json,random
#import time
disk = os.getcwd()
bak_path = '/tmp/html'
webshell_path = '/tmp/webshell'
md5_dict = {}
def main():
	if os.path.exists(webshell_path + '/dict.txt'):
		#print ('dict.txt is ok')
		two_run()
	else:
		try:
			os.makedirs(bak_path)
			os.makedirs(webshell_path)
		except:
			print 'Folder exists.'
		os.popen('cp -r * %s'%bak_path)
		print 'create bak'
		num = [a+'/'+n for a,b,c in os.walk(disk) for n in c]
		print len(num)
		for i in num:
			md5_dict[i] = md5mod(i)
		with open(webshell_path+ '/dict.txt','w') as f:
			f.write(str(md5_dict))
		cycle()
		

def two_run():
	with open(webshell_path + '/dict.txt','r') as f:
		a = json.loads(f.read().replace('\'','"'))
		global md5_dict
		md5_dict = a
	cycle()
	#with open(disk+'name.txt','a') as f:
	#	for i in num:
	#		f.write(i+'\n')
	#return num
def cycle():
	#print ('---AAA---')
	for a,b,c in os.walk(disk):
		for n in c:
			if a+'/'+n not in md5_dict:
				print (a+'/'+n + '   is upload!!!')
				os.popen('mv %s %s'%(a+'/'+n,webshell_path+'/'+n+'_'+str(random.randint(0,100))))
				#os.popen("echo Brother,Don\\'t bother>%s"%(a+'/'+n))
				with open(webshell_path+'/shell.txt','a') as f:
					f.write(a+'/'+n +'\n')
			else:
				if md5mod(a+'/'+n) != md5_dict[a+'/'+n]:
					print (a+'/'+n + ' is tamper!!!')
					os.popen('cp %s %s'%(a+'/'+n,webshell_path+'/'+n+'_'+str(random.randint(0,100))))
					#print ((a+'/'+n).strip(disk))
					#print (bak_path+((a+'/'+n).strip('disk')),a+'/'+n)
					os.popen('cp %s %s'%(bak_path+'/'+(a+'/'+n).replace(disk,'',1),a+'/'+n))
					with open(webshell_path+'/shell.txt','a') as f:
						f.write(a+'/'+n +'\n')
	del_check()
				
def del_check():
	if len([a+'/'+n for a,b,c in os.walk(disk) for n in c]) < len(md5_dict):
		print ('Missing file!!!')
		#print ('cp -r %s/* %s'%(bak_path,disk))
		os.popen('cp -r %s/* %s'%(bak_path,disk))
def md5mod(filename):
	with open(filename,'rb') as f:
		return hashlib.md5(f.read()).hexdigest()
#txt = wirte_txt()
#main()
print ('run...')
while True:
	main()
	#time.sleep(3)
#with open(filename,'rb') as f:
#	print(hashlib.md5(f.read()).hexdigest())