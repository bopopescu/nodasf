{"filter":false,"title":"settings.py","tooltip":"/nodanewssf/settings.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":78,"column":0},"end":{"row":81,"column":5},"action":"remove","lines":["    'default': {","        'ENGINE': 'django.db.backends.sqlite3',","        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),","    }"],"id":14},{"start":{"row":78,"column":0},"end":{"row":85,"column":6},"action":"insert","lines":["    'default': {","        'ENGINE': 'django.db.backends.postgresql_psycopg2',","        'NAME': os.environ['DB_NAME'],","        'USER': os.environ['DB_USER'],","        'PASSWORD': os.environ['DB_PASSWORD'],","        'HOST': os.environ['DB_HOST'],","        'PORT': os.environ['DB_PORT'],","    },"]}],[{"start":{"row":122,"column":0},"end":{"row":126,"column":0},"action":"remove","lines":["# Static files (CSS, JavaScript, Images)","# https://docs.djangoproject.com/en/2.1/howto/static-files/","","STATIC_URL = '/static/'",""],"id":15},{"start":{"row":122,"column":0},"end":{"row":140,"column":59},"action":"insert","lines":["SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')","SECURE_SSL_REDIRECT = True","# Allow all host headers","ALLOWED_HOSTS = ['*']","","# Static files (CSS, JavaScript, Images)","# https://docs.djangoproject.com/en/1.8/howto/static-files/","","STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')","","# Extra places for collectstatic to find static files.","STATICFILES_DIRS = (","    os.path.join(PROJECT_ROOT, 'static'),",")","db_from_env = dj_database_url.config(conn_max_age=500)","DATABASES['default'].update(db_from_env)","AWS_STORAGE_BUCKET_NAME = os.environ['S3_BUCKET']","AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']","AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']"]}],[{"start":{"row":124,"column":0},"end":{"row":126,"column":0},"action":"remove","lines":["# Allow all host headers","ALLOWED_HOSTS = ['*']",""],"id":16}],[{"start":{"row":138,"column":59},"end":{"row":139,"column":0},"action":"insert","lines":["",""],"id":17}],[{"start":{"row":139,"column":0},"end":{"row":147,"column":53},"action":"insert","lines":["STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'    ","AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME","STATICFILES_LOCATION = 'static'","STATICFILES_STORAGE = 'custom_storages.StaticStorage'","STATIC_URL = \"https://%s/%s/\" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)","MEDIAFILES_LOCATION = 'media'","MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')","MEDIA_URL = \"https://%s/%s/\" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)","DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'"],"id":18}],[{"start":{"row":28,"column":20},"end":{"row":28,"column":21},"action":"insert","lines":[","],"id":19}],[{"start":{"row":28,"column":21},"end":{"row":28,"column":22},"action":"insert","lines":[" "],"id":20}],[{"start":{"row":28,"column":22},"end":{"row":28,"column":33},"action":"insert","lines":["'127.0.0.1'"],"id":21}],[{"start":{"row":45,"column":59},"end":{"row":46,"column":0},"action":"insert","lines":["",""],"id":22},{"start":{"row":46,"column":0},"end":{"row":46,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":46,"column":0},"end":{"row":46,"column":46},"action":"insert","lines":["\t'whitenoise.middleware.WhiteNoiseMiddleware',"],"id":23}],[{"start":{"row":142,"column":24},"end":{"row":142,"column":25},"action":"insert","lines":["N"],"id":25},{"start":{"row":142,"column":25},"end":{"row":142,"column":26},"action":"insert","lines":["o"]},{"start":{"row":142,"column":26},"end":{"row":142,"column":27},"action":"insert","lines":["d"]},{"start":{"row":142,"column":27},"end":{"row":142,"column":28},"action":"insert","lines":["a"]},{"start":{"row":142,"column":28},"end":{"row":142,"column":29},"action":"insert","lines":["S"]},{"start":{"row":142,"column":29},"end":{"row":142,"column":30},"action":"insert","lines":["F"]},{"start":{"row":142,"column":30},"end":{"row":142,"column":31},"action":"insert","lines":["/"]}],[{"start":{"row":145,"column":23},"end":{"row":145,"column":24},"action":"insert","lines":["N"],"id":26},{"start":{"row":145,"column":24},"end":{"row":145,"column":25},"action":"insert","lines":["o"]},{"start":{"row":145,"column":25},"end":{"row":145,"column":26},"action":"insert","lines":["d"]},{"start":{"row":145,"column":26},"end":{"row":145,"column":27},"action":"insert","lines":["a"]},{"start":{"row":145,"column":27},"end":{"row":145,"column":28},"action":"insert","lines":["S"]}],[{"start":{"row":145,"column":28},"end":{"row":145,"column":29},"action":"insert","lines":["F"],"id":27},{"start":{"row":145,"column":29},"end":{"row":145,"column":30},"action":"insert","lines":["/"]}],[{"start":{"row":40,"column":13},"end":{"row":41,"column":0},"action":"insert","lines":["",""],"id":28},{"start":{"row":41,"column":0},"end":{"row":41,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":41,"column":4},"end":{"row":41,"column":6},"action":"insert","lines":["''"],"id":29}],[{"start":{"row":41,"column":5},"end":{"row":41,"column":6},"action":"insert","lines":["s"],"id":30},{"start":{"row":41,"column":6},"end":{"row":41,"column":7},"action":"insert","lines":["o"]},{"start":{"row":41,"column":7},"end":{"row":41,"column":8},"action":"insert","lines":["t"]},{"start":{"row":41,"column":8},"end":{"row":41,"column":9},"action":"insert","lines":["r"]}],[{"start":{"row":41,"column":8},"end":{"row":41,"column":9},"action":"remove","lines":["r"],"id":31},{"start":{"row":41,"column":7},"end":{"row":41,"column":8},"action":"remove","lines":["t"]},{"start":{"row":41,"column":6},"end":{"row":41,"column":7},"action":"remove","lines":["o"]}],[{"start":{"row":41,"column":6},"end":{"row":41,"column":7},"action":"insert","lines":["t"],"id":32},{"start":{"row":41,"column":7},"end":{"row":41,"column":8},"action":"insert","lines":["o"]},{"start":{"row":41,"column":8},"end":{"row":41,"column":9},"action":"insert","lines":["r"]},{"start":{"row":41,"column":9},"end":{"row":41,"column":10},"action":"insert","lines":["a"]},{"start":{"row":41,"column":10},"end":{"row":41,"column":11},"action":"insert","lines":["g"]},{"start":{"row":41,"column":11},"end":{"row":41,"column":12},"action":"insert","lines":["e"]},{"start":{"row":41,"column":12},"end":{"row":41,"column":13},"action":"insert","lines":["s"]}],[{"start":{"row":41,"column":14},"end":{"row":41,"column":15},"action":"insert","lines":[","],"id":33}],[{"start":{"row":141,"column":29},"end":{"row":141,"column":30},"action":"insert","lines":["h"],"id":34},{"start":{"row":141,"column":30},"end":{"row":141,"column":31},"action":"insert","lines":["e"]},{"start":{"row":141,"column":31},"end":{"row":141,"column":32},"action":"insert","lines":["r"]},{"start":{"row":141,"column":32},"end":{"row":141,"column":33},"action":"insert","lines":["o"]},{"start":{"row":141,"column":33},"end":{"row":141,"column":34},"action":"insert","lines":["k"]}],[{"start":{"row":141,"column":33},"end":{"row":141,"column":34},"action":"remove","lines":["k"],"id":35},{"start":{"row":141,"column":32},"end":{"row":141,"column":33},"action":"remove","lines":["o"]},{"start":{"row":141,"column":31},"end":{"row":141,"column":32},"action":"remove","lines":["r"]},{"start":{"row":141,"column":30},"end":{"row":141,"column":31},"action":"remove","lines":["e"]},{"start":{"row":141,"column":29},"end":{"row":141,"column":30},"action":"remove","lines":["h"]}],[{"start":{"row":149,"column":53},"end":{"row":150,"column":0},"action":"insert","lines":["",""],"id":37}],[{"start":{"row":150,"column":0},"end":{"row":151,"column":0},"action":"insert","lines":["",""],"id":39}],[{"start":{"row":151,"column":0},"end":{"row":164,"column":64},"action":"insert","lines":["AWS_ACCESS_KEY_ID = 'AKIAIT2Z5TDYPX3ARJBA'","AWS_SECRET_ACCESS_KEY = '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'","AWS_STORAGE_BUCKET_NAME = 'sibtc-static'","AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME","AWS_S3_OBJECT_PARAMETERS = {","    'CacheControl': 'max-age=86400',","}","AWS_LOCATION = 'static'","","STATICFILES_DIRS = [","    os.path.join(BASE_DIR, 'mysite/static'),","]","STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)","STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'"],"id":40}],[{"start":{"row":151,"column":0},"end":{"row":153,"column":40},"action":"remove","lines":["AWS_ACCESS_KEY_ID = 'AKIAIT2Z5TDYPX3ARJBA'","AWS_SECRET_ACCESS_KEY = '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'","AWS_STORAGE_BUCKET_NAME = 'sibtc-static'"],"id":41}],[{"start":{"row":150,"column":0},"end":{"row":151,"column":0},"action":"remove","lines":["",""],"id":42}],[{"start":{"row":152,"column":0},"end":{"row":154,"column":1},"action":"remove","lines":["AWS_S3_OBJECT_PARAMETERS = {","    'CacheControl': 'max-age=86400',","}"],"id":43}],[{"start":{"row":155,"column":0},"end":{"row":157,"column":1},"action":"remove","lines":["STATICFILES_DIRS = [","    os.path.join(BASE_DIR, 'mysite/static'),","]"],"id":44},{"start":{"row":154,"column":0},"end":{"row":155,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":141,"column":0},"end":{"row":150,"column":0},"action":"remove","lines":["STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'    ","AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME","STATICFILES_LOCATION = 'NodaSF/static'","STATICFILES_STORAGE = 'custom_storages.StaticStorage'","STATIC_URL = \"https://%s/%s/\" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)","MEDIAFILES_LOCATION = 'NodaSF/media'","MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')","MEDIA_URL = \"https://%s/%s/\" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)","DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'",""],"id":45},{"start":{"row":140,"column":59},"end":{"row":141,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":143,"column":23},"end":{"row":144,"column":0},"action":"remove","lines":["",""],"id":46}],[{"start":{"row":142,"column":0},"end":{"row":143,"column":0},"action":"remove","lines":["",""],"id":47}],[{"start":{"row":144,"column":64},"end":{"row":145,"column":0},"action":"insert","lines":["",""],"id":48},{"start":{"row":145,"column":0},"end":{"row":146,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":146,"column":0},"end":{"row":162,"column":53},"action":"insert","lines":["AWS_STORAGE_BUCKET_NAME = os.environ['S3_BUCKET']","AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']","AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']","","    # Tell django-storages that when coming up with the URL for an item in S3 storage, keep","    # it simple - just use this domain plus the path. (If this isn't set, things get complicated).","    # This controls how the `static` template tag from `staticfiles` gets expanded, if you're using it.","    # We also use it in the next setting.","STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'    ","AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME","STATICFILES_LOCATION = 'static'","STATICFILES_STORAGE = 'custom_storages.StaticStorage'","STATIC_URL = \"https://%s/%s/\" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)","MEDIAFILES_LOCATION = 'media'","MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')","MEDIA_URL = \"https://%s/%s/\" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)","DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'"],"id":49}],[{"start":{"row":146,"column":0},"end":{"row":149,"column":0},"action":"remove","lines":["AWS_STORAGE_BUCKET_NAME = os.environ['S3_BUCKET']","AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']","AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']",""],"id":50}],[{"start":{"row":151,"column":0},"end":{"row":152,"column":0},"action":"remove","lines":["STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'    ",""],"id":51}],[{"start":{"row":151,"column":0},"end":{"row":152,"column":0},"action":"remove","lines":["AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME",""],"id":52}],[{"start":{"row":142,"column":0},"end":{"row":143,"column":0},"action":"remove","lines":["AWS_LOCATION = 'static'",""],"id":53}],[{"start":{"row":150,"column":0},"end":{"row":151,"column":0},"action":"remove","lines":["STATICFILES_LOCATION = 'static'",""],"id":54}],[{"start":{"row":144,"column":0},"end":{"row":145,"column":0},"action":"insert","lines":["STATICFILES_LOCATION = 'static'",""],"id":55}],[{"start":{"row":142,"column":55},"end":{"row":142,"column":67},"action":"remove","lines":["AWS_LOCATION"],"id":56},{"start":{"row":142,"column":55},"end":{"row":142,"column":75},"action":"insert","lines":["STATICFILES_LOCATION"]}],[{"start":{"row":144,"column":0},"end":{"row":144,"column":31},"action":"remove","lines":["STATICFILES_LOCATION = 'static'"],"id":57}],[{"start":{"row":142,"column":0},"end":{"row":143,"column":0},"action":"insert","lines":["",""],"id":58}],[{"start":{"row":142,"column":0},"end":{"row":142,"column":31},"action":"insert","lines":["STATICFILES_LOCATION = 'static'"],"id":59}],[{"start":{"row":153,"column":0},"end":{"row":154,"column":0},"action":"remove","lines":["STATIC_URL = \"https://%s/%s/\" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)",""],"id":60}],[{"start":{"row":147,"column":0},"end":{"row":152,"column":0},"action":"remove","lines":["","    # Tell django-storages that when coming up with the URL for an item in S3 storage, keep","    # it simple - just use this domain plus the path. (If this isn't set, things get complicated).","    # This controls how the `static` template tag from `staticfiles` gets expanded, if you're using it.","    # We also use it in the next setting.",""],"id":61},{"start":{"row":146,"column":0},"end":{"row":147,"column":0},"action":"remove","lines":["",""]},{"start":{"row":145,"column":0},"end":{"row":146,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":41,"column":0},"end":{"row":41,"column":15},"action":"remove","lines":["    'storages',"],"id":62},{"start":{"row":40,"column":13},"end":{"row":41,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":129,"column":55},"end":{"row":130,"column":0},"action":"insert","lines":["",""],"id":63}],[{"start":{"row":130,"column":0},"end":{"row":130,"column":46},"action":"insert","lines":["STATIC_ROOT = os.path.join(BASE_DIR, 'static')"],"id":64}],[{"start":{"row":129,"column":0},"end":{"row":129,"column":55},"action":"remove","lines":["STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')"],"id":65}],[{"start":{"row":130,"column":44},"end":{"row":130,"column":45},"action":"insert","lines":["f"],"id":66},{"start":{"row":130,"column":45},"end":{"row":130,"column":46},"action":"insert","lines":["i"]},{"start":{"row":130,"column":46},"end":{"row":130,"column":47},"action":"insert","lines":["l"]},{"start":{"row":130,"column":47},"end":{"row":130,"column":48},"action":"insert","lines":["e"]},{"start":{"row":130,"column":48},"end":{"row":130,"column":49},"action":"insert","lines":["s"]}],[{"start":{"row":130,"column":34},"end":{"row":130,"column":35},"action":"remove","lines":["R"],"id":67},{"start":{"row":130,"column":33},"end":{"row":130,"column":34},"action":"remove","lines":["I"]},{"start":{"row":130,"column":32},"end":{"row":130,"column":33},"action":"remove","lines":["D"]},{"start":{"row":130,"column":31},"end":{"row":130,"column":32},"action":"remove","lines":["_"]},{"start":{"row":130,"column":30},"end":{"row":130,"column":31},"action":"remove","lines":["E"]},{"start":{"row":130,"column":29},"end":{"row":130,"column":30},"action":"remove","lines":["S"]},{"start":{"row":130,"column":28},"end":{"row":130,"column":29},"action":"remove","lines":["A"]},{"start":{"row":130,"column":27},"end":{"row":130,"column":28},"action":"remove","lines":["B"]}],[{"start":{"row":130,"column":27},"end":{"row":130,"column":28},"action":"insert","lines":["P"],"id":68},{"start":{"row":130,"column":28},"end":{"row":130,"column":29},"action":"insert","lines":["r"]},{"start":{"row":130,"column":29},"end":{"row":130,"column":30},"action":"insert","lines":["o"]},{"start":{"row":130,"column":30},"end":{"row":130,"column":31},"action":"insert","lines":["j"]},{"start":{"row":130,"column":31},"end":{"row":130,"column":32},"action":"insert","lines":["e"]},{"start":{"row":130,"column":32},"end":{"row":130,"column":33},"action":"insert","lines":["c"]},{"start":{"row":130,"column":33},"end":{"row":130,"column":34},"action":"insert","lines":["t"]}],[{"start":{"row":130,"column":33},"end":{"row":130,"column":34},"action":"remove","lines":["t"],"id":69},{"start":{"row":130,"column":32},"end":{"row":130,"column":33},"action":"remove","lines":["c"]},{"start":{"row":130,"column":31},"end":{"row":130,"column":32},"action":"remove","lines":["e"]},{"start":{"row":130,"column":30},"end":{"row":130,"column":31},"action":"remove","lines":["j"]},{"start":{"row":130,"column":29},"end":{"row":130,"column":30},"action":"remove","lines":["o"]},{"start":{"row":130,"column":28},"end":{"row":130,"column":29},"action":"remove","lines":["r"]}],[{"start":{"row":130,"column":28},"end":{"row":130,"column":29},"action":"insert","lines":["R"],"id":70},{"start":{"row":130,"column":29},"end":{"row":130,"column":30},"action":"insert","lines":["O"]},{"start":{"row":130,"column":30},"end":{"row":130,"column":31},"action":"insert","lines":["T"]}],[{"start":{"row":130,"column":30},"end":{"row":130,"column":31},"action":"remove","lines":["T"],"id":71}],[{"start":{"row":130,"column":27},"end":{"row":130,"column":30},"action":"remove","lines":["PRO"],"id":72},{"start":{"row":130,"column":27},"end":{"row":130,"column":39},"action":"insert","lines":["PROJECT_ROOT"]}],[{"start":{"row":149,"column":53},"end":{"row":150,"column":0},"action":"insert","lines":["",""],"id":73}],[{"start":{"row":150,"column":0},"end":{"row":150,"column":65},"action":"insert","lines":["DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'"],"id":74}],[{"start":{"row":149,"column":0},"end":{"row":149,"column":53},"action":"remove","lines":["DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'"],"id":75},{"start":{"row":148,"column":74},"end":{"row":149,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":39,"column":33},"end":{"row":40,"column":0},"action":"insert","lines":["",""],"id":76},{"start":{"row":40,"column":0},"end":{"row":40,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":40,"column":4},"end":{"row":40,"column":6},"action":"insert","lines":["''"],"id":77}],[{"start":{"row":40,"column":5},"end":{"row":40,"column":6},"action":"insert","lines":["s"],"id":78},{"start":{"row":40,"column":6},"end":{"row":40,"column":7},"action":"insert","lines":["t"]},{"start":{"row":40,"column":7},"end":{"row":40,"column":8},"action":"insert","lines":["o"]},{"start":{"row":40,"column":8},"end":{"row":40,"column":9},"action":"insert","lines":["r"]},{"start":{"row":40,"column":9},"end":{"row":40,"column":10},"action":"insert","lines":["a"]},{"start":{"row":40,"column":10},"end":{"row":40,"column":11},"action":"insert","lines":["g"]},{"start":{"row":40,"column":11},"end":{"row":40,"column":12},"action":"insert","lines":["e"]},{"start":{"row":40,"column":12},"end":{"row":40,"column":13},"action":"insert","lines":["s"]}],[{"start":{"row":40,"column":14},"end":{"row":40,"column":15},"action":"insert","lines":[","],"id":79}],[{"start":{"row":145,"column":0},"end":{"row":145,"column":64},"action":"remove","lines":["STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'"],"id":80},{"start":{"row":144,"column":76},"end":{"row":145,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":40,"column":4},"end":{"row":40,"column":15},"action":"remove","lines":["'storages',"],"id":81},{"start":{"row":40,"column":0},"end":{"row":40,"column":4},"action":"remove","lines":["    "]},{"start":{"row":39,"column":33},"end":{"row":40,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":28,"column":32},"end":{"row":28,"column":33},"action":"remove","lines":["'"],"id":82},{"start":{"row":28,"column":31},"end":{"row":28,"column":32},"action":"remove","lines":["1"]},{"start":{"row":28,"column":30},"end":{"row":28,"column":31},"action":"remove","lines":["."]},{"start":{"row":28,"column":29},"end":{"row":28,"column":30},"action":"remove","lines":["0"]},{"start":{"row":28,"column":28},"end":{"row":28,"column":29},"action":"remove","lines":["."]},{"start":{"row":28,"column":27},"end":{"row":28,"column":28},"action":"remove","lines":["0"]},{"start":{"row":28,"column":26},"end":{"row":28,"column":27},"action":"remove","lines":["."]},{"start":{"row":28,"column":25},"end":{"row":28,"column":26},"action":"remove","lines":["7"]},{"start":{"row":28,"column":24},"end":{"row":28,"column":25},"action":"remove","lines":["2"]},{"start":{"row":28,"column":23},"end":{"row":28,"column":24},"action":"remove","lines":["1"]},{"start":{"row":28,"column":22},"end":{"row":28,"column":23},"action":"remove","lines":["'"]},{"start":{"row":28,"column":21},"end":{"row":28,"column":22},"action":"remove","lines":[" "]}],[{"start":{"row":28,"column":20},"end":{"row":28,"column":21},"action":"remove","lines":[","],"id":83}],[{"start":{"row":114,"column":14},"end":{"row":114,"column":15},"action":"remove","lines":["T"],"id":84},{"start":{"row":114,"column":13},"end":{"row":114,"column":14},"action":"remove","lines":["U"]}],[{"start":{"row":114,"column":13},"end":{"row":114,"column":14},"action":"remove","lines":["C"],"id":85}],[{"start":{"row":114,"column":13},"end":{"row":114,"column":30},"action":"insert","lines":["America/Vancouver"],"id":86}],[{"start":{"row":40,"column":13},"end":{"row":41,"column":0},"action":"insert","lines":["",""],"id":87},{"start":{"row":41,"column":0},"end":{"row":41,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":41,"column":4},"end":{"row":41,"column":6},"action":"insert","lines":["''"],"id":88}],[{"start":{"row":41,"column":5},"end":{"row":41,"column":6},"action":"insert","lines":["s"],"id":89},{"start":{"row":41,"column":6},"end":{"row":41,"column":7},"action":"insert","lines":["t"]},{"start":{"row":41,"column":7},"end":{"row":41,"column":8},"action":"insert","lines":["o"]},{"start":{"row":41,"column":8},"end":{"row":41,"column":9},"action":"insert","lines":["r"]},{"start":{"row":41,"column":9},"end":{"row":41,"column":10},"action":"insert","lines":["a"]},{"start":{"row":41,"column":10},"end":{"row":41,"column":11},"action":"insert","lines":["g"]},{"start":{"row":41,"column":11},"end":{"row":41,"column":12},"action":"insert","lines":["e"]},{"start":{"row":41,"column":12},"end":{"row":41,"column":13},"action":"insert","lines":["s"]}],[{"start":{"row":41,"column":14},"end":{"row":41,"column":15},"action":"insert","lines":[","],"id":90}],[{"start":{"row":147,"column":0},"end":{"row":147,"column":1},"action":"insert","lines":["#"],"id":91}],[{"start":{"row":147,"column":0},"end":{"row":147,"column":1},"action":"remove","lines":["#"],"id":92}],[{"start":{"row":148,"column":74},"end":{"row":149,"column":0},"action":"insert","lines":["",""],"id":93}],[{"start":{"row":149,"column":0},"end":{"row":149,"column":74},"action":"insert","lines":["MEDIA_URL = \"https://%s/%s/\" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)"],"id":94}],[{"start":{"row":148,"column":0},"end":{"row":148,"column":1},"action":"insert","lines":["#"],"id":95}],[{"start":{"row":149,"column":25},"end":{"row":149,"column":26},"action":"remove","lines":["s"],"id":96},{"start":{"row":149,"column":24},"end":{"row":149,"column":25},"action":"remove","lines":["%"]}],[{"start":{"row":149,"column":24},"end":{"row":149,"column":25},"action":"insert","lines":["{"],"id":97},{"start":{"row":149,"column":25},"end":{"row":149,"column":26},"action":"insert","lines":["}"]}],[{"start":{"row":149,"column":22},"end":{"row":149,"column":23},"action":"remove","lines":["s"],"id":98},{"start":{"row":149,"column":21},"end":{"row":149,"column":22},"action":"remove","lines":["%"]}],[{"start":{"row":149,"column":21},"end":{"row":149,"column":22},"action":"insert","lines":["{"],"id":99},{"start":{"row":149,"column":22},"end":{"row":149,"column":23},"action":"insert","lines":["}"]}],[{"start":{"row":149,"column":29},"end":{"row":149,"column":30},"action":"remove","lines":["%"],"id":100},{"start":{"row":149,"column":28},"end":{"row":149,"column":29},"action":"remove","lines":[" "]}],[{"start":{"row":149,"column":28},"end":{"row":149,"column":29},"action":"insert","lines":["."],"id":101}],[{"start":{"row":149,"column":29},"end":{"row":149,"column":30},"action":"insert","lines":["f"],"id":102},{"start":{"row":149,"column":30},"end":{"row":149,"column":31},"action":"insert","lines":["o"]},{"start":{"row":149,"column":31},"end":{"row":149,"column":32},"action":"insert","lines":["r"]},{"start":{"row":149,"column":32},"end":{"row":149,"column":33},"action":"insert","lines":["m"]},{"start":{"row":149,"column":33},"end":{"row":149,"column":34},"action":"insert","lines":["a"]},{"start":{"row":149,"column":34},"end":{"row":149,"column":35},"action":"insert","lines":["t"]}],[{"start":{"row":149,"column":35},"end":{"row":149,"column":36},"action":"remove","lines":[" "],"id":103}],[{"start":{"row":149,"column":78},"end":{"row":150,"column":0},"action":"insert","lines":["",""],"id":104}],[{"start":{"row":150,"column":0},"end":{"row":151,"column":0},"action":"insert","lines":["DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'",""],"id":105}],[{"start":{"row":122,"column":0},"end":{"row":123,"column":71},"action":"insert","lines":["    os.environ['DJANGO_SETTINGS_MODULE'] = 'YOURAPP.settings'","    os.environ.setdefault(\"DJANGO_SETTINGS_MODULE\", \"YOURAPP.settings\")"],"id":106}],[{"start":{"row":122,"column":0},"end":{"row":122,"column":4},"action":"remove","lines":["    "],"id":107}],[{"start":{"row":123,"column":0},"end":{"row":123,"column":4},"action":"remove","lines":["    "],"id":108}],[{"start":{"row":122,"column":46},"end":{"row":122,"column":47},"action":"remove","lines":["P"],"id":109},{"start":{"row":122,"column":45},"end":{"row":122,"column":46},"action":"remove","lines":["P"]},{"start":{"row":122,"column":44},"end":{"row":122,"column":45},"action":"remove","lines":["A"]},{"start":{"row":122,"column":43},"end":{"row":122,"column":44},"action":"remove","lines":["R"]},{"start":{"row":122,"column":42},"end":{"row":122,"column":43},"action":"remove","lines":["U"]},{"start":{"row":122,"column":41},"end":{"row":122,"column":42},"action":"remove","lines":["O"]},{"start":{"row":122,"column":40},"end":{"row":122,"column":41},"action":"remove","lines":["Y"]}],[{"start":{"row":122,"column":40},"end":{"row":122,"column":41},"action":"insert","lines":["n"],"id":110},{"start":{"row":122,"column":41},"end":{"row":122,"column":42},"action":"insert","lines":["o"]},{"start":{"row":122,"column":42},"end":{"row":122,"column":43},"action":"insert","lines":["d"]},{"start":{"row":122,"column":43},"end":{"row":122,"column":44},"action":"insert","lines":["a"]}],[{"start":{"row":122,"column":40},"end":{"row":122,"column":44},"action":"remove","lines":["noda"],"id":111},{"start":{"row":122,"column":40},"end":{"row":122,"column":50},"action":"insert","lines":["nodanewssf"]}],[{"start":{"row":123,"column":55},"end":{"row":123,"column":56},"action":"remove","lines":["P"],"id":112},{"start":{"row":123,"column":54},"end":{"row":123,"column":55},"action":"remove","lines":["P"]},{"start":{"row":123,"column":53},"end":{"row":123,"column":54},"action":"remove","lines":["A"]},{"start":{"row":123,"column":52},"end":{"row":123,"column":53},"action":"remove","lines":["R"]},{"start":{"row":123,"column":51},"end":{"row":123,"column":52},"action":"remove","lines":["U"]},{"start":{"row":123,"column":50},"end":{"row":123,"column":51},"action":"remove","lines":["O"]},{"start":{"row":123,"column":49},"end":{"row":123,"column":50},"action":"remove","lines":["Y"]}],[{"start":{"row":123,"column":49},"end":{"row":123,"column":50},"action":"insert","lines":["n"],"id":113},{"start":{"row":123,"column":50},"end":{"row":123,"column":51},"action":"insert","lines":["o"]},{"start":{"row":123,"column":51},"end":{"row":123,"column":52},"action":"insert","lines":["d"]},{"start":{"row":123,"column":52},"end":{"row":123,"column":53},"action":"insert","lines":["a"]}],[{"start":{"row":123,"column":49},"end":{"row":123,"column":53},"action":"remove","lines":["noda"],"id":114},{"start":{"row":123,"column":49},"end":{"row":123,"column":59},"action":"insert","lines":["nodanewssf"]}],[{"start":{"row":50,"column":4},"end":{"row":50,"column":5},"action":"insert","lines":["#"],"id":115}],[{"start":{"row":50,"column":4},"end":{"row":50,"column":5},"action":"remove","lines":["#"],"id":116}],[{"start":{"row":14,"column":0},"end":{"row":14,"column":20},"action":"insert","lines":["import django_heroku"],"id":117}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":14,"column":20},"end":{"row":14,"column":20},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1565107001536,"hash":"29fe06d16e81f05a844e3284e50aa3456f21b8cf"}