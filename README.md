
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
> 
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

## Emulate a django server
``` dos
(trydjango18) D:\virtualdir\trydjango18\src>python manage.py runserver
```
> 
<pre>
Performing system checks...

System check identified no issues (0 silenced).
February 09, 2016 - 19:48:35
Django version 1.8, using settings 'trydjango18.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
</pre>

默认端口是8000, 也可以通过下列命令制定端口
``` dos
python manage.py runserver 8080
python manage.py runserver 0.0.0.0:8000
```

## 将代码提交到github
先创建repository trydjango18course
``` dos
echo "# trydjango18course" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin git@github.com:navicester/trydjango18course.git
git push -u origin master
```

# 2 First Migration
``` dos
(trydjango18) D:\virtualdir\trydjango18\src>python manage.py migrate
```
如果直接运行migrate命令，会有报错: settings.DATABASES is improperly configured,这是因为我们的database没有配置好

## 修改settings.py
添加 “ENGINE” 和 “NAME” 配置，例子中我们选用sqlite3，关于mysql的配置会有专门章节介绍
> 
<pre>
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'db.sqlite3',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}
</pre>

Database配置好了之后，再次运行migrate

``` dos
(trydjango18) D:\virtualdir\trydjango18\src>python manage.py migrate
```
> 
<pre>
Operations to perform:
  Synchronize unmigrated apps: staticfiles, messages
  Apply all migrations: contenttypes, sites, auth, sessions
Synchronizing apps without migrations:
  Creating tables...
    Running deferred SQL...
  Installing custom SQL...
Running migrations:
  Rendering model states... DONE
  Applying contenttypes.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0001_initial... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying sessions.0001_initial... OK
  Applying sites.0001_initial... OK
  </pre>
  
  python manage.py syncdb从1.9开始会被删除掉

# 3 Admin & SuperUser
**Createsuperuser**命令可以用来创建超级用户，该命令任意时间都能执行
``` dos
(trydjango18) D:\virtualdir\trydjango18\src>python manage.py createsuperuser
```
> 
<pre>
Username (leave blank to use 'alu'): alu
Email address: navicester@qq.com
Password:
Password (again):
Superuser created successfully.
</pre>

``` dos
(trydjango18) D:\virtualdir\trydjango18\src>python manage.py syncdb
```
> 
<pre>
D:\virtualdir\trydjango18\lib\site-packages\django\core\management\commands\syncdb.py:24: RemovedInDjango19Warning: The syncdb command will be removed in Django 1.9
  warnings.warn("The syncdb command will be removed in Django 1.9", RemovedInDjango19Warning)

Operations to perform:
  Synchronize unmigrated apps: staticfiles, admindocs, messages
  Apply all migrations: admin, contenttypes, sites, auth, sessions
Synchronizing apps without migrations:
  Creating tables...
    Running deferred SQL...
  Installing custom SQL...
Running migrations:
  Rendering model states... DONE
  Applying admin.0001_initial... OK
  </pre>
  
  ## enable admin
  去掉setting和url中的一些注释语句
  
  setting.py
  
  ``` python
  INSTALLED_APPS = (
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',
)
```
urls.py
``` python
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
```


