import os

ENVIRONMENT = bool(os.environ.get('ENVIRONMENT', False))

if ENVIRONMENT:
    try:
        API_ID = int(os.environ.get('API_ID', 0))
    except ValueError:
        raise Exception("Your API_ID is not a valid integer.")
    API_HASH = os.environ.get('API_HASH', None)
    BOT_TOKEN = os.environ.get('BOT_TOKEN', None)
    DATABASE_URL = os.environ.get('DATABASE_URL', None)
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")  # Sqlalchemy dropped support for "postgres" name.
    # https://stackoverflow.com/questions/62688256/sqlalchemy-exc-nosuchmoduleerror-cant-load-plugin-sqlalchemy-dialectspostgre
else:
    # Fill the Values
    API_ID = 14672956
    API_HASH = "115e8242ea0423893160bb61a9e05eab"
    BOT_TOKEN = "5836700205:AAFN4MqEVqfmbuhVeCECXZ1K_lNRfwKCsJU"
    DATABASE_URL = "postgresql://postgres:KtLaCeKSr0FZup72XUwn@containers-us-west-168.railway.app:7020/railway"
