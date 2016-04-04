class ValidationError(ValueError):
    pass

import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)

    sys.setdefaultencoding(default_encoding)