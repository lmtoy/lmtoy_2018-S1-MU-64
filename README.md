# 2018-S1-MU-64

This project observed Sextans A searching for CO.   The known VLSR is 315 km/s, with HI emission
between 280 and 380 km/s. See e.g. https://arxiv.org/pdf/1804.07730.pdf

## OBSNUM

A total of 49 science obsnum's were taken in the CO line (115.3 GHz).
The good data were taken in a 4 night end sprint (March 12, 13, 18, 19) before Covid shut down the observatory.
Each dataset integrated a 120 arcsec region in OTF style for about 600 seconds. Beams 0,5,12,13,14,15 were
often suspect. Individual inspection was needed. The final RMS in the combined map (92431..92787)
was about 21 mK, with no clear CO detection. 

Earlier obsnum's  (85929..92188) were using the wrong OFF position (0,0) - and thus are "useless", except
it could be used as a bootstrap comparison with the 49 correct OFF positions.

More detailed descriptions are in the file **mk_runs.py**.


## related papers

First Detection of Molecular Gas in the Giant Low Surface Brightness Galaxy Malin 1 -
https://iopscience.iop.org/article/10.3847/2041-8213/ad8656

They found 143 (+/-41) mJy km/s
