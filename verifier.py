#!/usr/bin/env python
import cPickle
import sys
f=open(sys.argv[1]).read()
r=cPickle.loads(f)
sys.stdout.write(r)
