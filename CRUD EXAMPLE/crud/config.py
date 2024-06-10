import os
basedir=os.path.abspath(os.path.dirname(__file__))
class congig(object):
    Secreat_key="qwerty"
    Secreat_key=os.environ.get("Secreat_key")
    SQLALCHEMY_DATABASE_url=os.environ.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATION=False