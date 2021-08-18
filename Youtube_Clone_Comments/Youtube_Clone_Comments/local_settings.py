# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_=pd1lnurc&vel(wkmtt3v+4)=csc#h+#(&p6gm!9)&i1%l@-0'

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'youtube_db',
        'USER': 'root',
        'PASSWORD': 'ThisIsAnUnsecurePassWord',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}
