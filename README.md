# Campus Event Project
Sample project using Django for learning purpose. Inlude function below:
- Basic usage of Model, View, Template
- Use ModelForm to register new record and validation
- Use AdminModel to customise admin pages
- Handle errors

# Tech Stacks
- Framework: Python Django (~5.2)
- Database: SQLite
- CSS: Bootstrap (5.0)

# Project Structures
```
campus_events/
│
├── campus_events/   # Configuration (settings, urls, wsgi, asgi)
├  ├── asgi.py
├  ├── settings.py
├  ├── urls.py
├  ├── wsgi.py
├── events_app/      # Events campus app
├  ├── migrations/
├  ├── templates/
├  ├   ├── errors/
├  ├   ├  ├── 404.html
├  ├   ├  ├── 500.html
├  ├   ├── base.html
├  ├   ├── category_list.html
├  ├   ├── event_list.html
├  ├   ├── ...
│  ├── admin.py     # Admin pages customisation
│  ├── apps.py      # App configuration
│  ├── forms.py     # Forms declaration
│  ├── models.py    # Models declaration 
│  ├── urls.py      # URL route declaration
│  ├── views.py     # Logic    
├── requirements.txt # Library management
└── manage.py
└── README.md
```

## Setup 
To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt

Migration: 
```
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```

Create admin user: 
```
$ python3 manage.py createsuperuser
< Input your admin username/password >
```
Run dev-server: 
```
$ python3 manage.py runserver
```