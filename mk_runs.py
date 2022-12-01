#! /usr/bin/env python
#
#   script generator for project="2018-S1-MU-64"
#   Sextans-A
#
#   85929 (2019-11-05) through 92188 (2020-03-06) have the wrong OFF (on0: 170 obsnums)
#   92431 (2020-03-12) through 92787 (2020-03-19) should be ok (on1:  49 obsnums)


import os
import sys

# in prep of the new lmtoy module
try:
    lmtoy = os.environ['LMTOY']
    sys.path.append(lmtoy + '/lmtoy')
    import runs
except:
    print("No LMTOY with runs.py")
    sys.exit(0)

project="2018-S1-MU-64"

#        obsnums per source (make it negative if not added to the final combination)
on = {}

on['SEXTANS-A'] = [ 92431, 92435, 92439, 92445, 92449, 92455, 92459,
                    92463, 92469, 92473, 92542, 92548, 92554, 92556,
                    92560, 92562, 92566, 92568, 92572, 92574, 92578,
                    92580, 92584, 92586, 92590, 92668,-92670, 92672,
                    92674, 92676, 92684, 92686, 92692, 92694, 92698,
                    92700, 92702, 92755, 92761, 92763,-92765, 92769,
                    92771, 92773, 92777, 92779, 92781, 92785, 92787,
                   ]

#        common parameters per source on the first dryrun (run1, run2)
pars1 = {}
pars1['SEXTANS-A'] = "dv=100 dw=300 extent=150"

#        common parameters per source on subsequent runs (run1a, run2a)
pars2 = {}
pars2['SEXTANS-A'] = ""

runs.mk_runs(project, on, pars1, pars2)

