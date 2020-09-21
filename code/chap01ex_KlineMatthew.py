"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import sys

import nsfg
import thinkstats2

def ReadFile(dct_file='2002FemResp.dct',
                dat_file='2002FemResp.dat.gz',
                nrows=None):
    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file, compression='gzip', nrows=nrows)
    return df

def ValPregnum(resp):
    # read the pregnancy frame
    preg = nsfg.ReadFemPreg()
    # make the map from caseid to list of pregnancy indices
    preg_map = nsfg.MakePregMap(preg)
    # iterate through the respondent pregnum series
    for index, pregnum in resp.pregnum.items():
        caseid = resp.caseid[index]
        indices = preg_map[caseid]
        # check that pregnum from the respondent file equals
        # the number of records in the pregnancy file
        if len(indices) != pregnum:
            print(caseid, len(indices), pregnum)
            return False
    return True

def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    
    file = ReadFile()
    assert(len(file) == 7643)
    assert(file.pregnum.value_counts()[1] == 1267)
    assert(ValPregnum(file))
    
    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
    

#console out put: 
#runfile('C:/Users/Matt Kline/Documents/GitHub/ThinkStats2/code/chap01ex_KlineMatthew.py', wdir='C:/Users/Matt Kline/Documents/GitHub/ThinkStats2/code')
#C:\Users\Matt Kline\Documents\GitHub\ThinkStats2\code\chap01ex_KlineMatthew.py: All tests passed.
