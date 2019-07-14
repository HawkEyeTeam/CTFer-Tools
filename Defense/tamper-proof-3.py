import os,hashlib,json,random
#import time
disk = os.getcwd() #当前路径
bak_path = '/tmp/html' #备份路径
webshell_path = '/tmp/webshell' #可疑文件移动路径
md5_dict = {}

def main():
	if os.path.exists(webshell_path + '/dict.txt'):#判断是否为首次运行此脚本
		#print ('dict.txt is ok')
		two_run() #非首次运行执行此方法
	else:#首次运行执行
		try:
			os.makedirs(bak_path) #创建文件夹
			os.makedirs(webshell_path)
		except:
			print ('Folder exists.')
		os.popen('cp -r * %s'%bak_path) #文件备份
		print ('create bak')
		num = [a+'/'+n for a,b,c in os.walk(disk) for n in c] #文件名列表
		print (len(num))
		for i in num: #逐个计算MD5值
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
	for a,b,c in os.walk(disk):#循环遍历本目录下文件名
		for n in c:
			if a+'/'+n not in md5_dict:#如果文件名不存在创建的文件名字典中
				print (a+'/'+n + '   is upload!!!')
				os.popen('mv %s %s'%(a+'/'+n,webshell_path+'/'+n+'_'+str(random.randint(0,100))))#移动并增加随机后缀
				with open(webshell_path+'/shell.txt','a') as f:#在shell.txt中增加此上传记录
					f.write(a+'/'+n +'\n')
			else:#若果文件存在创建的文件名字典中
				if md5mod(a+'/'+n) != md5_dict[a+'/'+n]:#校验MD5值
					print (a+'/'+n + ' is tamper!!!')
					os.popen('cp %s %s'%(a+'/'+n,webshell_path+'/'+n+'_'+str(random.randint(0,100))))
					#复制到webshell目录
					os.popen('cp %s %s'%(bak_path+'/'+(a+'/'+n).replace(disk,'',1),a+'/'+n))
					#恢复文件
					with open(webshell_path+'/shell.txt','a') as f:
						f.write(a+'/'+n +'\n')
	del_check()#启动防删除检查
				
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
