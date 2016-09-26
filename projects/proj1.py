import sys
import os
import base64
import textwrap

try:
    import json
except:
    print "Fail"
    sys.exit(1)


def encode(DATA):
    print "Paste the following into the submission box for this assignment",
    print "on blackboard"
    print 79*'='
    blob = base64.b64encode(json.dumps(DATA))
    print "\n".join(textwrap.wrap(blob,79))
    print "\n"

try:
    DATA = {'user': os.environ.get('USER', '')}
    DATA['path'] = os.environ.get('PATH', 'NONE')
    DATA['uname'] = os.uname()
    DATA['version'] = sys.version
    DATA['exec'] = sys.executable
    DATA['modpath'] = sys.path
    encode(DATA)
except:
    print "FAIL!!"
    sys.exit(1)
