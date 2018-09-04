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


def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    print('%s: All tests passed.' % script)
    df_resp = nsfg.ReadFemResp()
    df_preg = nsfg.ReadFemPreg()
    print(df_resp.pregnum.value_counts().sort_index())
    #indices = nsfg.MakePregMap(df_preg)    
    #print(df_resp[pregnum])
    #for i in indices:
     #   print(df_preg[indices].pregnum)
    

if __name__ == '__main__':
    main(*sys.argv)

    
