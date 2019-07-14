# CTFer-Tools
HawkEye Team CTF Tools

适用于线下AWD攻防

## 防御方向

### * 1.Tamper-proof
use: 
python3 tamper-proof-3.py
针对不同的环境编写了py2和py3
#### * 功能描述
主要功能：文件监控 防篡改
1. 生成MD5字典
   将脚本所在目录及子目录下所有文件生成字典文件保存至/tmp/webshell/dict.txt。
   {filename:md5 value}
2. 防上传
   发现不在首次运行列表中的文件移动至/tmp/webshell下并在文件名后增加随机后缀。
3. 防篡改
   检验文件名的md5值，不匹配文件会被移动至/tmp/webshell下并在文件名后增加随机后缀，并启动文件恢复。
4. 防删除
   运行时会将目录下所有文件备份至/tmp/html，发现文件丢失会将启动文件恢复。
