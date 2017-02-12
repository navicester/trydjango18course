
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

# 4 APPS
``` dos
(trydjango18) D:\virtualdir\trydjango18\src>python manage.py startapp newsletter
```
我们不能创建两个名字完全一样的application，但是可以创建于类似“admin” 这种build-in site-packages的application

它会创建下面文件
> 
<pre>
newsletter/
     __init__.py
     models.py
     tests.py
     views.py
     </pre>

# 5 FIRST VIEW AND URL ROUTING
添加最基本的view功能

## 首先添加url
trydjango18\urls.py
``` python
urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'newsletter.views.home', name='home'),
)
```
这儿的name后面可以用在template里面的url引用，例如

templates\navbar.html

``` html
<li class="active"><a href="{% url 'home' %}">Home</a></li>
```

## 添加view里面的实现
文件`newsletter\view.py`
``` python
from django.shortcuts import render 

# Create your views here.
def home(request):
	context = {}
	return render(request, "home.html", context)

```

# 6	DJANGO SETTING OVERVIEW

``` dos
(trydjango18) D:\virtualdir\trydjango18\src>tree /F
```
> 
<pre>
D:.
│  db.sqlite3
│  manage.py
│
├─newsletter
│  │  admin.py
│  │  models.py
│  │  tests.py
│  │  views.py
│  │  __init__.py
│  │
│  └─migrations
│          __init__.py
│
└─trydjango18
        settings.py
        settings.pyc
        urls.py
        urls.pyc
        wsgi.py
        wsgi.pyc
        __init__.py
        __init__.pyc

</pre>


``` python
Django settings for trydjango18 project.
Generated by 'django-admin startproject' using Django 1.8.
For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
```

## BASE_DIR

返回当前路径

``` python
import os.path
os.path.dirname(__file__)
```

``` python
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#root of project
ROOT_URLCONF = 'trydjango18.urls'
```

## MIDDLEWARE_CLASSES
介于request和response之间

## TEMPLATES
A list containing the settings for all template engines to be used with Django. Each item of the list is a dictionary containing the options for an individual engine.

Here’s a simple setup that tells the Django template engine to load templates from the templates subdirectory inside each installed application:

``` python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
## TEMPLATE_DIRS

Default: () (Empty tuple)
Deprecated since version 1.8: Set the DIRS option of a DjangoTemplates backend instead.

List of locations of the template source files searched by django.template.loaders.filesystem.Loader, in search order.
Note that these paths should use Unix-style forward slashes, even on Windows.

## TEMPLATE_CONTEXT_PROCESSORS

Default:
``` python
(
    "django.contrib.auth.context_processors.auth",
    "django.template.context_processors.debug",
    "django.template.context_processors.i18n",
    "django.template.context_processors.media",
    "django.template.context_processors.static",
    "django.template.context_processors.tz",
"django.contrib.messages.context_processors.messages"
)
```

**Deprecated since version 1.8**: Set the 'context_processors' option in the OPTIONS of a DjangoTemplates backend instead.

A tuple of callables that are used to populate the context in RequestContext. These callables take a request object as their argument and return a dictionary of items to be merged into the context.

Changed in Django 1.8: 

Built-in template context processors were moved from django.core.context_processors to django.template.context_processors in Django 1.8.

## TEMPLATE_LOADERS
Default:
``` python
(
    'django.template.loaders.filesystem.Loader',
     'django.template.loaders.app_directories.Loader'
)
```

**Deprecated since version 1.8**: Set the 'loaders' option in the OPTIONS of a DjangoTemplates backend instead.

A tuple of template loader classes, specified as strings. Each Loader class knows how to import templates from a particular source. Optionally, a tuple can be used instead of a string. The first item in the tuple should be the Loader’s module, subsequent items are passed to the Loader during initialization. See The Django template language: for Python programmers.

# 8	TEMPLATE CONFIGURATION

``` python
# Create your views here.
def home(request):
	context = {}
	return render(request, "home.html", context)
```

如果不创建template的话, http://127.0.0.1:8000/ 将会报告下面的错误调试信息

<pre>
TemplateDoesNotExist 
Template-loader postmortem
Django tried loading these templates, in this order:
    •	Using loader django.template.loaders.filesystem.Loader: 
    •	Using loader django.template.loaders.app_directories.Loader: 
        o	D:\virtualdir\trydjango18\lib\site-packages\django\contrib\auth\templates\home.html (File does not exist)
        o	D:\virtualdir\trydjango18\lib\site-packages\django\contrib\admin\templates\home.html (File does not exist)
        o	D:\virtualdir\trydjango18\lib\site-packages\django\contrib\admindocs\templates\home.html (File does not exist)
</pre>

在newsletter下面创建template目录，并且在“INSTALLED_APPS”下面添加“newsletter”，django将会搜索该template目录
``` django
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'newsletter'
)
```

如果将newsletter注释掉，django会不找不到模板文件
> 
<pre>
Template-loader postmortem
Django tried loading these templates, in this order:
    •	Using loader django.template.loaders.filesystem.Loader: 
    •	Using loader django.template.loaders.app_directories.Loader: 
        o	D:\virtualdir\trydjango18\lib\site-packages\django\contrib\auth\templates\home.html (File does not exist)
        o	D:\virtualdir\trydjango18\lib\site-packages\django\contrib\admin\templates\home.html (File does not exist)
        o	D:\virtualdir\trydjango18\lib\site-packages\django\contrib\admindocs\templates\home.html (File does not exist)
        o	D:\virtualdir\trydjango18\src\newsletter\templates\home.html (File does not exist)
</pre>

在“newsletter”下面创建文件“home.html”, it works

本例子中，我们把templates从application目录中移到root文件夹，在src目录创建templates文件夹

修改settings.py

``` python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True, # Whether the engine should look for template source files inside installed applications.
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

如果home.html没有创建，django会抛出下面异常，否则, it works.
> 
<pre>
Template-loader postmortem
Django tried loading these templates, in this order:
    •	Using loader django.template.loaders.filesystem.Loader: 
        o	D:\virtualdir\trydjango18\src\templates\home.html (File does not exist)
    •	Using loader django.template.loaders.app_directories.Loader: 
        o	D:\virtualdir\trydjango18\lib\site-packages\django\contrib\auth\templates\home.html (File does not exist)
        o	D:\virtualdir\trydjango18\lib\site-packages\django\contrib\admin\templates\home.html (File does not exist)
        o	D:\virtualdir\trydjango18\lib\site-packages\django\contrib\admindocs\templates\home.html (File does not exist)
</pre>


# 9	MODELS
https://docs.djangoproject.com/en/1.8/ref/models/
https://docs.djangoproject.com/en/1.8/ref/models/fields/

``` python
from django.db import models

# Create your models here.
class SignUp(models.Model):
	email = models.EmailField()
	full_name = models.CharField(max_length=120, blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self): #Python 3.3 is __str__
		return self.email
```
## migrate database
makemigrations : 初始化migrations

migrates : 实际运行migrations并且存储到database

``` dos
(trydjango18) D:\virtualdir\trydjango18\src>python manage.py makemigrations
```
> 
<pre>
Migrations for 'newsletter':
  0001_initial.py:
    - Create model SignUp
</pre>

``` dos
(trydjango18) D:\virtualdir\trydjango18\src>python manage.py migrate
```
> 
<pre>
Operations to perform:
  Synchronize unmigrated apps: staticfiles, admindocs, messages
  Apply all migrations: sessions, admin, sites, auth, contenttypes, newsletter
Synchronizing apps without migrations:
  Creating tables...
    Running deferred SQL...
  Installing custom SQL...
Running migrations:
  Rendering model states... DONE
  Applying newsletter.0001_initial... OK
</pre>

如果不做修改重新执行该命令，将显示No migrations to apply

``` dos
(trydjango18) D:\virtualdir\trydjango18\src>python manage.py migrate
```

> 
<pre>
Operations to perform:
  Synchronize unmigrated apps: staticfiles, admindocs, messages
  Apply all migrations: sessions, admin, sites, auth, contenttypes, newsletter
Synchronizing apps without migrations:
  Creating tables...
    Running deferred SQL...
  Installing custom SQL...
Running migrations:
  No migrations to apply.
</pre>








