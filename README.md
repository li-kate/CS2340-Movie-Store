# CS2340 Movie Store
## User Story 16 - Make Site Accessible Anywhere
This is from [Chapter 13](https://learning.oreilly.com/library/view/django-5-for/9781835461556/B22457_13.xhtml#_idParaDest-251) of the textbook.
1. Make an account on [Python Anywhere](https://www.pythonanywhere.com/registration/register/beginner/).
2. Copy HTTP link from GitHub.
3. Make a new bash on PythonAnywhere and use the command `git clone http_link`.
   - **THERE IS NO GITHUB PASSWORD OPTION ANYMORE.** You need to generate an access token by going to your GitHub settings -> developer settings -> create access token and use that as the password instead when cloning.
4. Make a virtual environment in bash using the command `mkvirtualenv -p python3.10 moviesstoreenv`.
5. Install django and pillow using the command `pip install django==5.0 pillow`.
6. Go back to PythonAnywhere and add a new web app.
   - You'll need to select "Manual Configuration" and Python 3.10.
7. In the VirtualEnv section, type "moviesstoreenv" and it'll generate the file path for you.
8. For source code, type `/home/<yourusernamehere>/CS2340-Movie-Store/moviesstore`. You can leave working directory as it is or change it to be the same as the source code, it doesn't really matter.
9. Go to the wsgi.py file in the Code section of PythonAnywhere. Delete everything in the file and replace with this:
```
# +++++++++++ DJANGO +++++++++++
# To use your own django app use code like this:
import os
import sys

path = '/home/<yourusernamehere>/CS2340-Movie-Store/moviesstore'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'CS2340-Movie-Store.moviesstore.moviesstore.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```
10. Click the "Save" button at the top.
11. Go to the "Files" tab at the top and navigate to `CS2340-Movie-Store/moviesstore/moviesstore`. Then, click on settings.py.
12. Replace `ALLOWED_HOSTS = []` with `ALLOWED_HOSTS = ['*']`.
13. After `STATIC_URL = 'static/'`, add the line `STATIC_ROOT = os.path.join(BASE_DIR, 'static')`.
14. Click the "Save" button at the top.
15. Go back to the bash console and type `workon moviesstoreenv`.
16. In bash, redirect to the moviesstore folder with manage.py - for us, you should run `cd CS2340-Movie-Store/moviesstore`. You can check if manage.py is in the directory with the command `ls`.
17. Run `python manage.py collectstatic` and copy the directory they give you, which is probably `/home/<yourusernamehere>/CS2340-Movie-Store/moviesstore/static`.
18. Go to the "Web" tab and under "Static files," add the URL as `/static/` and the directory as the directory bash gave you in step 17.
19. Click the "Reload <yourusernamehere>.pythonanywhere.com" button.
20. Click the blue link to the website and enjoy :)
