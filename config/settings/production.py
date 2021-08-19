#settings to use on production
from . base import *
DEBUG = False

ALLOWED_HOSTS = ['ip-address','www.resume.com']



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sdaumuode',
        'USER':'kalistos',
        'PASSWORD':'kal15t05',
        'HOST':'localhost',
        'PORT':''
    }
}