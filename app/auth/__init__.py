from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views

import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)

    sys.setdefaultencoding(default_encoding)