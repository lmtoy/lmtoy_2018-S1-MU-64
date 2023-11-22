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

on['SKY'] = [-85929,-86054,-86145,-86147,-86149,-86151,-86153,-86155,-86159,-86161,
             -86163,-86165,-86167,-86169,-86173,-86175,-86177,-86179,-86181,-86183,
             -86187,-86189,-86191,-86193,-86195,-86197,-86201,-86203,-86205,-86298,
             -86300,-86302,-86304,-86306,-86308,-86312,-86314,-86316,-86318,-86320,
             -86322,-86326,-86328,-86330,-86332,-86334,-86336,-86340,-86342,-86344,
             -86346,-86348,-86350,-86354,-86356,-86358,-86360,-86362,-86364,-87501,
             -87503,-87505,-87509,-87511,-87513,-87515,-87519,-87521,-87523,-87525,
             -87527,-87531,-87533,-87535,-87537,-87539,-87541,-87545,-87547,-87549,
             -87551,-88194,-88202,-88204,-88206,-88208,-88210,-88212,-88214,-88216,
             -88218,-88220,-88222,-88228,-88230,-88232,-88234,-88236,-88238,-88240,
             -88242,-88244,-88246,-88252,-88254,-88256,-88258,-88260,-88262,-88264,
             -88266,-88268,-88270,-88272,-88274,-88343,-88345,-88347,-88349,-88351,
             -88353,-88355,-88357,-88359,-88361,-88363,-88365,-88367,-88369,-88371,
             -88375,-88377,-88379,-88381,-88383,-88385,-88387,-88389,-88391,-88393,
             -88395,-88397,-88399,-88401,-88403,-88405,-88409,-88411,-88413,-88415,
             -88417,-88419,-88421,-88423,-88425,-88427,-88429,-88431,-88433,-88435,
              92165, 92168, 92172, 92173, 92177, 92178, 92182, 92183, 92187, 92188,
            ]

#        common parameters per source on the first dryrun (run1, run2)
pars1 = {}
pars1['SEXTANS-A'] = "dv=100 dw=300 extent=150"
pars1['SKY']       = "dv=100 dw=300 extent=150"

#        common parameters per source on subsequent runs (run1a, run2a)
pars2 = {}
pars2['SEXTANS-A'] = ""
pars2['SKY']       = ""

runs.mk_runs(project, on, pars1, pars2)

