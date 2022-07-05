![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Django Blog Cheat Sheet (full): 
## Setting up basic Django Project and Deploying to Heroku

<strong>Warning: Terminal command update</strong><br>
Since this video was created, Django has introduced a new version that will be automatically installed if you use the command in the video.
To ensure that you get the same version of django and gunicorn used in this video and so that nothing breaks as you do the walkthrough, instead of the command pip3 install django gunicorn, please use this:

### pip3 install 'django<4' gunicorn
This will install Django 3.2 which is the LTS (Long Term Support) version of Django and is therefore preferable to use over the newest beta Django 4.
<br>

## Step 1: Installing Django and supporting libraries

Note: It is recommended when you are still learning this content that you type out each line of code, rather than copying and pasting. This will help you learn!

<table>
  <tr>
    <th>Key:</th>
  </tr>
  <tr>
    <td>PROJ_NAME = codestar</td>
    <td>APP_NAME = blog</td>
  </tr>
                  
</table>

### In the Terminal:

<table>
  <tr>
    <th>#</th>
    <th>Step</th>
    <th>Code</th>
  </tr>
  <tr>
    <td>1.</td>
    <td>Install Django and gunicorn:</td>
    <td>pip3 install 'django<4' gunicorn</td>
  </tr>
  <tr>
    <td>2.</td>
    <td>Install supporting libraries:</td>
    <td>pip3 install dj_database_url psycopg2</td>
  </tr>
  <tr>
    <td>3.</td>
    <td>Install Cloudinary Libraries</td>
    <td>pip3 install dj3-cloudinary-storage</td>
  </tr>
    <tr>
    <td>4.</td>
    <td>Create requirements file</td>
    <td>pip3 freeze --local > requirements.txt</td>
  </tr>
    <tr>
    <td>5.</td>
    <td>Create Project (codestar 2021)</td>
    <td>django-admin startproject PROJ_NAME .
    <br><strong>(Don’t forget the . )</strong>
    </td>
  </tr>
    <tr>
    <td>6.</td>
    <td>Create App (blog)</td>
    <td>python3 manage.py startapp APP_NAME</td>
  </tr>
</table>

### settings.py

<table>
  <tr>
    <th>#</th>
    <th>Step</th>
    <th>Code</th>
  </tr>
  <tr>
    <td>7.</td>
    <td>Add to installed apps</td>
    <td>
        
    INSTALLED_APPS = [
    ...
    'APP_NAME',
    ]    
  </tr>
  <tr>
    <td>*</td>
    <td>Save file</td>
    <td></td>
  </tr>
</table>

### In the Terminal:

<table>
  <tr>
    <th>#</th>
    <th>Step</th>
    <th>Code</th>
  </tr>
  <tr>
    <td>8.</td>
    <td>Migrate Changes</td>
    <td>python3 manage.py migrate</td>
  </tr>
  <tr>
    <td>9.</td>
    <td>Run Server to Test</td>
    <td>python3 manage.py runserver</td>
  </tr>
</table>


## Step 2: Deploying an app to Heroku
4 stages:

1. Create the Heroku app
1. Attach the database
1. Prepare our environment and settings.py file
1. Get our static and media files stored on Cloudinary.

<hr>

### Note: Error fix
If you get the error below during the steps to deployment:<br>
<strong>django.db.utils.OperationalError: FATAL: role "somerandomletters" does not exist</strong><br>
Please run the following command in the terminal to fix it:<br>
<strong style="color: red">unset PGHOSTADDR</strong>
<hr>

## 2.1 Create the Heroku app

In heroku.com: (Note: must be logged in)

<table>
  <tr>
    <th>#</th>
    <th>Step</th>
    <th>Code</th>
  </tr>
  <tr>
    <td>1.</td>
    <td>Create new Heroku App</td>
    <td>APP_NAME, Location = Europe</td>
  </tr>
  <tr>
    <td>2.</td>
    <td>Add Database to App Resources</td>
    <td>Located in the Resources Tab, Add-ons, search and add e.g. ‘Heroku Postgres’</td>
  </tr>
  <tr>
    <td>3.</td>
    <td>Copy DATABASE_URL value</td>
    <td>Located in the Settings Tab, click reveal Config Vars, Copy Text</td>
  </tr>
</table>

## 2.2 Attach the Database:

### In gitpod:
<table>
  <tr>
    <th>#</th>
    <th>Step</th>
    <th>Code</th>
  </tr>
  <tr>
    <td>4.</td>
    <td>create new env.py file on top level directory</td>
    <td>E.g. env.py</td>
  </tr>
</table>

### In env.py
<table>
  <tr>
    <th>#</th>
    <th>Step</th>
    <th>Code</th>
  </tr>
  <tr>
    <td>5.</td>
    <td>Import os library</td>
    <td>import os</td>
  </tr>
  <tr>
    <td>6.</td>
    <td>Set environment variables</td>
    <td>os.environ["DATABASE_URL"] = "<strong style="color: red">Paste in Heroku DATABASE_URL Link</strong>"</td>
  </tr>
  <tr>
    <td>7.</td>
    <td>Add in secret key</td>
    <td>os.environ["SECRET_KEY"] = "<strong style="color: red">Make up your own randomSecretKey</strong>"</td>
  </tr>
</table>

### In heroku.com
<table>
  <tr>
    <th>#</th>
    <th>Step</th>
    <th>Code</th>
  </tr>
  <tr>
    <td>8.</td>
    <td>Add Secret Key to Config Vars</td>
    <td>SECRET_KEY, “randomSecretKey”</td>
  </tr>
</table>

## 2.3 Prepare our environment and settings.py file:

### In settings.py
<table>
  <tr>
    <th>#</th>
    <th>Step</th>
    <th>Code</th>
  </tr>
  <tr>
    <td>9.</td>
    <td>Reference env.py<br>(Note: font in bold is new)</td>
    <td>from pathlib import Path<br><strong>import os<br>import dj_database_url<br><br>if os.path.isfile("env.py"):<br>&ensp;import env</strong></td>
  </tr>
  <tr>
    <td>10.</td>
    <td>Remove the insecure secret key and replace - links to the SECRET_KEY variable on Heroku<br>(Note: font in bold is new)</td>
    <td>SECRET_KEY = os.environ.get('SECRET_KEY')</td>
  </tr>
  <tr>
    <td>11.</td>
    <td>Comment out the old DataBases Section</td>
    <td>

    # DATABASES = {
    #     'default': {
    #         'ENGINE': 'django.db.backends.sqlite3',
    #         'NAME': BASE_DIR / 'db.sqlite3',
    #     }
    # }
</td>
  </tr>
  <tr>
    <td>12</td>
    <td>Add new DATABASES Section<br>- links to the DATATBASE_URL variable on Heroku</td>
    <td>

        DATABASES = {
            'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
        }
</td>
  </tr>
</table>

### In the Terminal
<table>
  <tr>
    <th>#</th>
    <th>Step</th>
    <th>Code</th>
  </tr>
  <tr>
    <td>13.</td>
    <td>Save all files and Make Migrations</td>
    <td>python3 manage.py migrate</td>
  </tr>
</table>

## 2.4 Get our static and media files stored on Cloudinary:

### In Cloudinary.com: (Note: must be logged in)
<table>
  <tr>
    <th>#</th>
    <th>Step</th>
    <th>Code</th>
  </tr>
  <tr>
    <td>1.</td>
    <td>Copy your CLOUDINARY_URL e.g. API Environment Variable.</td>
    <td>From Cloudinary Dashboard</td>
  </tr>
</table>

### In env.py:
<table>
  <tr>
    <th>#</th>
    <th>Step</th>
    <th>Code</th>
  </tr>
  <tr>
    <td>2.</td>
    <td>Add Cloudinary URL to env.py - be sure to paste in the correct section of the link</td>
    <td>os.environ["CLOUDINARY_URL"] = "cloudinary://************************"</td>
  </tr>
</table>

### In Heroku:
<table>
  <tr>
    <th>#</th>
    <th>Step</th>
    <th>Code</th>
  </tr>
  <tr>
    <td>3.</td>
    <td>Add Cloudinary URL to Heroku Config Vars - be sure to paste in the correct section of the link</td>
    <td>Add to Settings tab in Config Vars e.g. COUDINARY_URL, cloudinary://************************</td>
  </tr>
  <tr>
    <td>4.</td>
    <td>Add DISABLE_COLLECTSTATIC to Heroku Config Vars (temporary step for the moment, will be removed before deployment)</td>
    <td>e.g. DISABLE_COLLECTSTATIC, 1</td>
  </tr>
</table>

### In settings.py:
<table>
  <tr>
    <th>#</th>
    <th>Step</th>
    <th>Code</th>
  </tr>
  <tr>
    <td>5.</td>
    <td>Add Cloudinary Libraries to installed apps</td>
    <td>

    INSTALLED_APPS = [
    …,
    'cloudinary_storage',
    'django.contrib.staticfiles',
    'cloudinary',
    …,
    ]
</td>
<strong>(note: order is important)</strong>
  </tr>
  <tr>
    <td>6.</td>
    <td>Tell Django to use Cloudinary to store media and static files Place under the Static files Note </td>
    <td>

    STATIC_URL = '/static/'

    STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    
    MEDIA_URL = '/media/'
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'</td>
  </tr>
  <tr>
    <td>7.</td>
    <td>Link file to the templates directory in Heroku Place under the BASE_DIR line</td>
    <td>TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')</td>
  </tr>
  <tr>
    <td>8.</td>
    <td>Change the templates directory to TEMPLATES_DIR Place within the TEMPLATES array</td>
    <td>
    
    TEMPLATES = [
    {
        …,
        'DIRS': [TEMPLATES_DIR],
       …,
            ],
        },
    },
    ]
</td>
  </tr>
    <tr>
    <td>9.</td>
    <td>Add Heroku Hostname to ALLOWED_HOSTS<br>(e.g. codestar2021)</td>
    <td>ALLOWED_HOSTS =<br> ["PROJ_NAME.herokuapp.com", "localhost"]</td>
  </tr>
</table>

### In Gitpod:
<table>
  <tr>
    <th>#</th>
    <th>Step</th>
    <th>Code</th>
  </tr>
  <tr>
    <td>10.</td>
    <td>Create 3 new folders on top level directory</td>
    <td>media, static, templates</td>
  </tr>
  <tr>
    <td>11.</td>
    <td>Create procfile on the top level directory</td>
    <td>Procfile</td>
  </tr>
</table>

### In Procfile
<table>
  <tr>
    <th>#</th>
    <th>Step</th>
    <th>Code</th>
  </tr>
  <tr>
    <td>12.</td>
    <td>Add code</td>
    <td>web: gunicorn PROJ_NAME.wsgi</td>
  </tr>
</table>
* Note: Save all files<br><br>

### In the Terminal:
<table>
  <tr>
    <th>#</th>
    <th>Step</th>
    <th>Code</th>
  </tr>
  <tr>
    <td>13.</td>
    <td>Add, Commit and Push</td>
    <td>git add .<br>git commit -m “Deployment Commit”<br>git push</td>
  </tr>
</table>

### In Heroku:
<table>
  <tr>
    <th>#</th>
    <th>Step</th>
    <th>Code</th>
  </tr>
  <tr>
    <td>14.</td>
    <td>Deploy Content manually through heroku/</td>
    <td>E.g Github as deployment method, on main branch</td>
  </tr>
</table>



