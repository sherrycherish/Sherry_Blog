from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors

import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)

    sys.setdefaultencoding(default_encoding)