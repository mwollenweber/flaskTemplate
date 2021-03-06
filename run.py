'''

Copyright Matthew Wollenweber 2015
mjw@insomniac.technology
All Rights Reserved.

'''

__description__ = ''
__author__ = 'Matthew Wollenweber'
__email__ = 'mjw@insomniac.technology'
__version__ = '0.0.1'
__date__ = '2015/02/12'

import sys
import errno
import traceback
from app import create_app

if __name__ == '__main__':
    try:
        app = create_app("development")
        app.run(debug=True, host='0.0.0.0', port=8000)

    except KeyboardInterrupt:
        print "KeyboardInterrupt! Exiting."
        sys.exit(0)

    except:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        traceback.print_exception(exc_type, exc_value, exc_traceback, limit=5, file=sys.stderr)
        sys.exit(-1)

