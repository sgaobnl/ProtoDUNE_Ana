# -*- coding: utf-8 -*-
"""
File Name: init_femb.py
Author: GSS
Mail: gao.hillhill@gmail.com
Description: 
Created Time: 7/15/2016 11:47:39 AM
Last modified: Fri Sep 21 15:52:20 2018
"""
import matplotlib
matplotlib.use('Agg')
#defaut setting for scientific caculation
#import numpy
#import scipy
#from numpy import *
#import numpy as np
#import scipy as sp
#import pylab as pl
#from openpyxl import Workbook
import numpy as np
import struct
import os
from sys import exit
import sys
import os.path
import math

import multiprocessing as mp
from chn_plot_out import plot_a_chn


if __name__ == '__main__':
    APAno = int(sys.argv[1])
    rmsdate = sys.argv[2]
    fpgdate = sys.argv[3]
    asidate = sys.argv[4]
    rmsrunno = sys.argv[5]
    fpgarunno = sys.argv[6]
    asicrunno = sys.argv[7]
    apafolder = sys.argv[8] 
    jumbo_flag = (sys.argv[9] == "True")
    tpcno  = (sys.argv[10])
    wibno  = int(sys.argv[11])
    fembno  = int(sys.argv[12])
    chnno  = int(sys.argv[13])

    if (apafolder == "APA40"):
        rms_rootpath =  "D:/APA40/Rawdata/Rawdata_" + rmsdate + "/"
        fpga_rootpath = "D:/APA40/Rawdata/Rawdata_" + fpgdate + "/"
        asic_rootpath = "D:/APA40/Rawdata/Rawdata_" + asidate + "/"
        apa = "APA40"
    elif (apafolder != "APA"):
        rms_rootpath =  "/nfs/rscratch/bnl_ce/shanshan/Rawdata/Coldbox/Rawdata_" + rmsdate + "/"
        fpga_rootpath = "/nfs/rscratch/bnl_ce/shanshan/Rawdata/Coldbox/Rawdata_" + fpgdate + "/"
        asic_rootpath = "/nfs/rscratch/bnl_ce/shanshan/Rawdata/Coldbox/Rawdata_" + asidate + "/"
        apa = "ProtoDUNE"
    else:
        rms_rootpath =  "/nfs/rscratch/bnl_ce/shanshan/Rawdata/APA%d/Rawdata_"%APAno + rmsdate + "/"
        fpga_rootpath = "/nfs/rscratch/bnl_ce/shanshan/Rawdata/APA%d/Rawdata_"%APAno + fpgdate + "/"
        asic_rootpath = "/nfs/rscratch/bnl_ce/shanshan/Rawdata/APA%d/Rawdata_"%APAno + asidate + "/"
        rms_rootpath =  "/nfs/sw/shanshan/Rawdata/APA%d/Rawdata_"%APAno + rmsdate + "/"
        fpga_rootpath = "/nfs/sw/shanshan/Rawdata/APA%d/Rawdata_"%APAno + fpgdate + "/"
        asic_rootpath = "/nfs/sw/shanshan/Rawdata/APA%d/Rawdata_"%APAno + asidate + "/"
 
        apa = "ProtoDUNE"
 
    from timeit import default_timer as timer
    s0= timer()
    print "Start...please wait..."
    
    fft_s = 5000
    gains = ["250"] 
    gains = ["140"] 
    tps = ["05", "10", "20", "30"]
    tps = [  "20"]
    wib_femb_chns = [  
                        #wib(0-4), femb(0-3), chn(0~127)
                        #[0, 2, 120   ],
                        [wibno, fembno, chnno]
                    ]    
    
    for wfc in wib_femb_chns:
        wibno = wfc[0]
        fembno = wfc[1]
        chnno = wfc[2]
        out_path = rms_rootpath + "/" + "results/" + "Chns_" + rmsrunno + "_" + fpgarunno + "_" + asicrunno+"/"
        if (os.path.exists(out_path)):
            pass
        else:
            try: 
                os.makedirs(out_path)
            except OSError:
                print "Can't create a folder, exit"
                exit()
        mps = []
        for gain in gains: 
            for tp in tps:
                 ana_a_chn_args = (out_path, rms_rootpath, fpga_rootpath, asic_rootpath, APAno, rmsrunno, fpgarunno, asicrunno, wibno, fembno, chnno, gain, tp, jumbo_flag, fft_s, apa, tpcno)
                 p = mp.Process(target=plot_a_chn, args=ana_a_chn_args)
                 mps.append(p)
        for p in mps:
            p.start()
        for p in mps:
            p.join()
        #        ana_a_chn(rms_rootpath, asic_rootpath, asic_rootpath, APAno, rmsrunno, fpgarunno, asicrunno, wibno, fembno, chnno, gain, tp, jumbo_flag)
        print "time passed %d seconds"%(timer() - s0)
    print "DONE"

