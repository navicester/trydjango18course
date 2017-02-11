
# 1 Start Project
## virtualenv 
``` dos
D:\>mkdir virtualdir
D:\>cd virtualdir
D:\>virtualenv trydjango18
```
> 
New python executable in trydjango18\Scripts\python.exe  
Installing setuptools, pip, wheel...done.  

``` dos
D:\virtualdir\trydjango18>ls
```
> 
Include  Lib  Scripts

视频教程里面苹果系统生成的目录是 bin include lib

激活命令 source bin/activate

Windows激活

``` dos
D:\virtualdir\trydjango18>Scripts\activate
```
> (trydjango18) D:\virtualdir\trydjango18>

``` dos
(trydjango18) D:\virtualdir\trydjango18>pip freeze
```
> wheel==0.24.0

视频教程里面生成的目录是 wsgiref==0.1.2

## 安装Django
可以从django网站获取最新的django版本信息  
https://www.djangoproject.com/download/  
通过pip安装django  
pip install django 会安装最新的版本  

``` dos
(trydjango18) D:\virtualdir\trydjango18>pip install django==1.8
```
安装完成之后可以通过pip freeze查看当前的版本信息
``` dos
(trydjango18) D:\virtualdir\trydjango18>pip freeze
```
> 
Django==1.8  
wheel==0.24.0  

pip freeze > requirements.txt将安装软件信息存储到requirements.txt  
后面可以通过pip install –r requirements.txt直接安装全部软件

## Start Project
``` dos
(trydjango18) D:\virtualdir\trydjango18>django-admin.py startproject trydjango18
(trydjango18) D:\virtualdir\trydjango18>ls
```
> Include  Lib  Scripts  pip-selfcheck.json  trydjango18

执行startproject命令后，会生成下列文件
> 
<pre>
 trydjango18/
    __init__.py
    manage.py
    settings.py
    urls.py
</pre>

为避免与virtualenv名字冲突，把项目目录改成 “src”

``` dos
(trydjango18) D:\virtualdir\trydjango18>rename trydjango18 src
(trydjango18) D:\virtualdir\trydjango18>dir
```
<pre> 
 Volume in drive D is HP_RECOVERY
 Volume Serial Number is E237-2AC8
Directory of D:\virtualdir\trydjango18
2016/02/09  19:45    <DIR>          .
2016/02/09  19:45    <DIR>          ..
2015/12/11  23:42    <DIR>          Include
2016/02/09  19:28    <DIR>          Lib
2016/02/09  19:33                60 pip-selfcheck.json
2016/02/09  19:37    <DIR>          Scripts
2016/02/09  19:42    <DIR>          src
               1 File(s)             60 bytes
               6 Dir(s)  38,498,160,640 bytes free
</pre>
               
``` dos
(trydjango18) D:\virtualdir\trydjango18>ls
```
> Include  Lib  Scripts  pip-selfcheck.json  src



