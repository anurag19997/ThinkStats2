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

def validate(resp, preg):
    preg_map = nsfg.MakePregMap(preg) 
    for index, pregnum in resp.pregnum.items():
        caseidresp = resp.caseid[index]
        indices = preg_map[caseidresp]
        if len(indices) != pregnum:
            print(resp[index])
            return False
    
    return True
    
def main(script):
    """Tests the functions in this module.


    
    script: string script name
    """
    df_resp = nsfg.ReadFemResp()
    df_preg = nsfg.ReadFemPreg()
    assert(df_resp.pregnum.value_counts().sum() == 7643)
    assert(validate(df_resp, df_preg))
    print('%s: All tests passed.' % script)
    

if __name__ == '__main__':
    main(*sys.argv)

    
