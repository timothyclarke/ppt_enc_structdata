#!/bin/env python

import sys
import re


print "---"
print "classes:"
if re.match( r'enc_test', sys.argv[1], re.I ):
  print "  enc_example:"
  print "    data:"
  print "      software:"
  print "        - \"bash\""
  print "        - \"openssl\""
  print "        - \"puppet\""
  print "      versions:"
  print "        bash:     \"installed\""
  print "        openssl:  \"latest\""
  print "        puppet:   \"3.7.1-1.el6\""

