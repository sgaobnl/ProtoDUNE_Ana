# -*- coding: utf-8 -*-
"""
File Name: init_femb.py
Author: GSS
Mail: gao.hillhill@gmail.com
Description: 
Created Time: 7/15/2016 11:47:39 AM
Last modified: Sun Apr 15 21:07:12 2018
"""

#defaut setting for scientific caculation
#import numpy
#import scipy
#from numpy import *
#import numpy as np
#import scipy as sp
#import pylab as pl

class APA_MAP:
    def apa_femb_mapping(self ):
        if (self.APA == "ProtoDUNE"):
            apa_femb_loc = [ 
                            #wire   #FEMBchn  #FEMBasic # ASICchn
                            ["X01", "031", 2, "15"], ["X03", "030", 2, "14"], ["X05", "029", 2, "13"], ["X07", "028", 2, "12"],
                            ["X09", "027", 2, "11"], ["X11", "026", 2, "10"], ["V01", "025", 2, "09"], ["V03", "024", 2, "08"],
                            ["V05", "023", 2, "07"], ["V07", "022", 2, "06"], ["V09", "021", 2, "05"], ["U01", "020", 2, "04"],
                            ["U03", "019", 2, "03"], ["U05", "018", 2, "02"], ["U07", "017", 2, "01"], ["U09", "016", 2, "00"],

                            ["X13", "015", 1, "15"], ["X15", "014", 1, "14"], ["X17", "013", 1, "13"], ["X19", "012", 1, "12"],
                            ["X21", "011", 1, "11"], ["X23", "010", 1, "10"], ["V11", "009", 1, "09"], ["V13", "008", 1, "08"],
                            ["V15", "007", 1, "07"], ["V17", "006", 1, "06"], ["V19", "005", 1, "05"], ["U11", "004", 1, "04"],
                            ["U13", "003", 1, "03"], ["U15", "002", 1, "02"], ["U17", "001", 1, "01"], ["U19", "000", 1, "00"],
    
                            ["X02", "048", 4, "00"], ["X04", "049", 4, "01"], ["X06", "050", 4, "02"], ["X08", "051", 4, "03"],
                            ["X10", "052", 4, "04"], ["X12", "053", 4, "05"], ["V02", "054", 4, "06"], ["V04", "055", 4, "07"],
                            ["V06", "056", 4, "08"], ["V08", "057", 4, "09"], ["V10", "058", 4, "10"], ["U02", "059", 4, "11"],
                            ["U04", "060", 4, "12"], ["U06", "061", 4, "13"], ["U08", "062", 4, "14"], ["U10", "063", 4, "15"],

                            ["X14", "032", 3, "00"], ["X16", "033", 3, "01"], ["X18", "034", 3, "02"], ["X20", "035", 3, "03"],
                            ["X22", "036", 3, "04"], ["X24", "037", 3, "05"], ["V12", "038", 3, "06"], ["V14", "039", 3, "07"],
                            ["V16", "040", 3, "08"], ["V18", "041", 3, "09"], ["V20", "042", 3, "10"], ["U12", "043", 3, "11"],
                            ["U14", "044", 3, "12"], ["U16", "045", 3, "13"], ["U18", "046", 3, "14"], ["U20", "047", 3, "15"],
                            
                            ["X26", "096", 7, "00"], ["X28", "097", 7, "01"], ["X30", "098", 7, "02"], ["X32", "099", 7, "03"], 
                            ["X34", "100", 7, "04"], ["X36", "101", 7, "05"], ["V22", "102", 7, "06"], ["V24", "103", 7, "07"], 
                            ["V26", "104", 7, "08"], ["V28", "105", 7, "09"], ["V30", "106", 7, "10"], ["U22", "107", 7, "11"], 
                            ["U24", "108", 7, "12"], ["U26", "109", 7, "13"], ["U28", "110", 7, "14"], ["U30", "111", 7, "15"], 

                            ["X38", "112", 8, "00"], ["X40", "113", 8, "01"], ["X42", "114", 8, "02"], ["X44", "115", 8, "03"], 
                            ["X46", "116", 8, "04"], ["X48", "117", 8, "05"], ["V32", "118", 8, "06"], ["V34", "119", 8, "07"], 
                            ["V36", "120", 8, "08"], ["V38", "121", 8, "09"], ["V40", "122", 8, "10"], ["U32", "123", 8, "11"], 
                            ["U34", "124", 8, "12"], ["U36", "125", 8, "13"], ["U38", "126", 8, "14"], ["U40", "127", 8, "15"], 
                            
                            ["X25", "079", 5, "15"], ["X27", "078", 5, "14"], ["X29", "077", 5, "13"], ["X31", "076", 5, "12"],
                            ["X33", "075", 5, "11"], ["X35", "074", 5, "10"], ["V21", "073", 5, "09"], ["V23", "072", 5, "08"],
                            ["V25", "071", 5, "07"], ["V27", "070", 5, "06"], ["V29", "069", 5, "05"], ["U21", "068", 5, "04"],
                            ["U23", "067", 5, "03"], ["U25", "066", 5, "02"], ["U27", "065", 5, "01"], ["U29", "064", 5, "00"],

                            ["X37", "095", 6, "15"], ["X39", "094", 6, "14"], ["X41", "093", 6, "13"], ["X43", "092", 6, "12"],
                            ["X45", "091", 6, "11"], ["X47", "090", 6, "10"], ["V31", "089", 6, "09"], ["V33", "088", 6, "08"],
                            ["V35", "087", 6, "07"], ["V37", "086", 6, "06"], ["V39", "085", 6, "05"], ["U31", "084", 6, "04"],
                            ["U33", "083", 6, "03"], ["U35", "082", 6, "02"], ["U37", "081", 6, "01"], ["U39", "080", 6, "00"]
                        ]
        elif (self.APA == "LArIAT" ):
            apa_femb_loc = [ 
                            #wire   #FEMBchn  #FEMBasic # ASICchn
                            ["U01", "031", 2, "15"], ["U02", "030", 2, "14"], ["U03", "029", 2, "13"], ["U04", "028", 2, "12"],
                            ["U05", "027", 2, "11"], ["U06", "026", 2, "10"], ["U07", "025", 2, "09"], ["U08", "024", 2, "08"],
                            ["U09", "023", 2, "07"], ["U10", "022", 2, "06"], ["U11", "021", 2, "05"], ["U12", "020", 2, "04"],
                            ["U13", "019", 2, "03"], ["U14", "018", 2, "02"], ["U15", "017", 2, "01"], ["U16", "016", 2, "00"],
                            ["U17", "015", 1, "15"], ["U18", "014", 1, "14"], ["U19", "013", 1, "13"], ["U20", "012", 1, "12"],
                            ["U21", "011", 1, "11"], ["U22", "010", 1, "10"], ["U23", "009", 1, "09"], ["U24", "008", 1, "08"],
                            ["U25", "007", 1, "07"], ["U26", "006", 1, "06"], ["U27", "005", 1, "05"], ["U28", "004", 1, "04"],
                            ["U29", "003", 1, "03"], ["U20", "002", 1, "02"], ["U31", "001", 1, "01"], ["U32", "000", 1, "00"],
    
                            ["X33", "048", 4, "00"], ["X34", "049", 4, "01"], ["X35", "050", 4, "02"], ["X36", "051", 4, "03"],
                            ["X37", "052", 4, "04"], ["X38", "053", 4, "05"], ["X39", "054", 4, "06"], ["X40", "055", 4, "07"],
                            ["X41", "056", 4, "08"], ["X42", "057", 4, "09"], ["X43", "058", 4, "10"], ["X44", "059", 4, "11"],
                            ["X45", "060", 4, "12"], ["X46", "061", 4, "13"], ["X47", "062", 4, "14"], ["X48", "063", 4, "15"],
                            ["X49", "032", 3, "00"], ["X50", "033", 3, "01"], ["X51", "034", 3, "02"], ["X52", "035", 3, "03"],
                            ["X53", "036", 3, "04"], ["X54", "037", 3, "05"], ["X55", "038", 3, "06"], ["X56", "039", 3, "07"],
                            ["X57", "040", 3, "08"], ["X58", "041", 3, "09"], ["X59", "042", 3, "10"], ["X50", "043", 3, "11"],
                            ["X61", "044", 3, "12"], ["X62", "045", 3, "13"], ["X63", "046", 3, "14"], ["X64", "047", 3, "15"],
                            
                            ["V01", "079", 5, "15"], ["V02", "078", 5, "14"], ["V03", "077", 5, "13"], ["V04", "076", 5, "12"],
                            ["V05", "075", 5, "11"], ["V06", "074", 5, "10"], ["V07", "073", 5, "09"], ["V08", "072", 5, "08"],
                            ["V09", "071", 5, "07"], ["V10", "070", 5, "06"], ["V11", "069", 5, "05"], ["V12", "068", 5, "04"],
                            ["V13", "067", 5, "03"], ["V14", "066", 5, "02"], ["V15", "065", 5, "01"], ["V16", "064", 5, "00"],
                            ["V17", "095", 6, "15"], ["V18", "094", 6, "14"], ["V19", "093", 6, "13"], ["V20", "092", 6, "12"],
                            ["V21", "091", 6, "11"], ["V22", "090", 6, "10"], ["V23", "089", 6, "09"], ["V24", "088", 6, "08"],
                            ["V25", "087", 6, "07"], ["V26", "086", 6, "06"], ["V27", "085", 6, "05"], ["V28", "084", 6, "04"],
                            ["V29", "083", 6, "03"], ["V20", "082", 6, "02"], ["V31", "081", 6, "01"], ["V32", "080", 6, "00"],

                            ["X01", "096", 7, "00"], ["X02", "097", 7, "01"], ["X03", "098", 7, "02"], ["X04", "099", 7, "03"], 
                            ["X05", "100", 7, "04"], ["X06", "101", 7, "05"], ["X07", "102", 7, "06"], ["X08", "103", 7, "07"], 
                            ["X09", "104", 7, "08"], ["X10", "105", 7, "09"], ["X11", "106", 7, "10"], ["X12", "107", 7, "11"], 
                            ["X13", "108", 7, "12"], ["X14", "109", 7, "13"], ["X15", "110", 7, "14"], ["X16", "111", 7, "15"], 
                            ["X17", "112", 8, "00"], ["X18", "113", 8, "01"], ["X19", "114", 8, "02"], ["X20", "115", 8, "03"], 
                            ["X21", "116", 8, "04"], ["X22", "117", 8, "05"], ["X23", "118", 8, "06"], ["X24", "119", 8, "07"], 
                            ["X25", "120", 8, "08"], ["X26", "121", 8, "09"], ["X27", "122", 8, "10"], ["X28", "123", 8, "11"], 
                            ["X29", "124", 8, "12"], ["X20", "125", 8, "13"], ["X31", "126", 8, "14"], ["X32", "127", 8, "15"] 
                           ]
        elif (self.APA == "APA40" ):
            apa_femb_loc = [ 
                            ["X28", "031", 2, "15"], ["X27", "030", 2, "14"], ["X26", "029", 2, "13"], ["X25", "028", 2, "12"],
                            ["X24", "027", 2, "11"], ["X23", "026", 2, "10"], ["X22", "025", 2, "09"], ["X21", "024", 2, "08"],
                            ["X20", "023", 2, "07"], ["X19", "022", 2, "06"], ["X18", "021", 2, "05"], ["X17", "020", 2, "04"],
                            ["X16", "019", 2, "03"], ["X15", "018", 2, "02"], ["U04", "017", 2, "01"], ["U03", "016", 2, "00"],
                            ["U02", "015", 1, "15"], ["U01", "014", 1, "14"], ["X14", "013", 1, "13"], ["X13", "012", 1, "12"],
                            ["X12", "011", 1, "11"], ["X11", "010", 1, "10"], ["X10", "009", 1, "09"], ["X09", "008", 1, "08"],
                            ["X08", "007", 1, "07"], ["X07", "006", 1, "06"], ["X06", "005", 1, "05"], ["X05", "004", 1, "04"],
                            ["X04", "003", 1, "03"], ["X03", "002", 1, "02"], ["X02", "001", 1, "01"], ["X01", "000", 1, "00"],

                            ["V10", "048", 4, "00"], ["U12", "049", 4, "01"], ["V11", "050", 4, "02"], ["U13", "051", 4, "03"],
                            ["V12", "052", 4, "04"], ["U14", "053", 4, "05"], ["V13", "054", 4, "06"], ["U15", "055", 4, "07"],
                            ["V14", "056", 4, "08"], ["U16", "057", 4, "09"], ["V15", "058", 4, "10"], ["U17", "059", 4, "11"],
                            ["V16", "060", 4, "12"], ["U18", "061", 4, "13"], ["V17", "062", 4, "14"], ["V18", "063", 4, "15"],
                            ["V01", "032", 3, "00"], ["V02", "033", 3, "01"], ["V03", "034", 3, "02"], ["U05", "035", 3, "03"],
                            ["V04", "036", 3, "04"], ["U06", "037", 3, "05"], ["V05", "038", 3, "06"], ["U07", "039", 3, "07"],
                            ["V06", "040", 3, "08"], ["U08", "041", 3, "09"], ["V07", "042", 3, "10"], ["U09", "043", 3, "11"],
                            ["V08", "044", 3, "12"], ["U10", "045", 3, "13"], ["V09", "046", 3, "14"], ["U11", "047", 3, "15"],

                            ["U20", "079", 5, "15"], ["U19", "078", 5, "14"], ["X42", "077", 5, "13"], ["X41", "076", 5, "12"],
                            ["X40", "075", 5, "11"], ["X39", "074", 5, "10"], ["X38", "073", 5, "09"], ["X37", "072", 5, "08"],
                            ["X36", "071", 5, "07"], ["X35", "070", 5, "06"], ["X34", "069", 5, "05"], ["X33", "068", 5, "04"],
                            ["X32", "067", 5, "03"], ["X31", "066", 5, "02"], ["X30", "065", 5, "01"], ["X29", "064", 5, "00"],
                            ["X56", "095", 6, "15"], ["X55", "094", 6, "14"], ["X54", "093", 6, "13"], ["X53", "092", 6, "12"],
                            ["X52", "091", 6, "11"], ["X51", "090", 6, "10"], ["X50", "089", 6, "09"], ["X49", "088", 6, "08"],
                            ["X48", "087", 6, "07"], ["X47", "086", 6, "06"], ["X46", "085", 6, "05"], ["X45", "084", 6, "04"],
                            ["X44", "083", 6, "03"], ["X43", "082", 6, "02"], ["U22", "081", 6, "01"], ["U21", "080", 6, "00"],

                            ["V19", "096", 7, "00"], ["U23", "097", 7, "01"], ["V20", "098", 7, "02"], ["U24", "099", 7, "03"], 
                            ["V21", "100", 7, "04"], ["U25", "101", 7, "05"], ["V22", "102", 7, "06"], ["U26", "103", 7, "07"], 
                            ["V23", "104", 7, "08"], ["U27", "105", 7, "09"], ["V24", "106", 7, "10"], ["U28", "107", 7, "11"], 
                            ["V25", "108", 7, "12"], ["U29", "109", 7, "13"], ["V26", "110", 7, "14"], ["V27", "111", 7, "15"], 
                            ["V28", "112", 8, "00"], ["V29", "113", 8, "01"], ["V30", "114", 8, "02"], ["U30", "115", 8, "03"], 
                            ["V31", "116", 8, "04"], ["U31", "117", 8, "05"], ["V32", "118", 8, "06"], ["U32", "119", 8, "07"], 
                            ["V33", "120", 8, "08"], ["U33", "121", 8, "09"], ["V34", "122", 8, "10"], ["U34", "123", 8, "11"], 
                            ["V35", "124", 8, "12"], ["U35", "125", 8, "13"], ["V36", "126", 8, "14"], ["U36", "127", 8, "15"] 
                        ]


        All_sort = []
        for i in range(0,128,1):
            for chn in apa_femb_loc:
                if int(chn[1][0:3]) == i :
                    All_sort.append(chn)
    
        X_sort = []
        for i in range(1,49,1):
            for chn in apa_femb_loc:
                if chn[0][0] == "X" and int(chn[0][1:3]) == i :
                    X_sort.append(chn)
        V_sort = []
        for i in range(1,41,1):
            for chn in apa_femb_loc:
                if chn[0][0] == "V" and int(chn[0][1:3]) == i :
                    V_sort.append(chn)
    
        U_sort = []
        for i in range(1,41,1):
            for chn in apa_femb_loc:
                if chn[0][0] == "U" and int(chn[0][1:3]) == i :
                    U_sort.append(chn)

        print "APA is " self.APA
        return All_sort, X_sort, V_sort, U_sort
    
    def apa_mapping(self):
        apa_yuv = []
        apa_y = []
        apa_u = []
        apa_v = []
        All_sort, X_sort, V_sort, U_sort = self.apa_femb_mapping()
        for onewire in All_sort:
            apa_yuv.append(int(onewire[1]))
    
        for onewire in X_sort:
            if onewire[0][0] == "X":
                apa_y.append(int(onewire[1]))
        for onewire in V_sort:
            if onewire[0][0] == "V":
                apa_v.append(int(onewire[1]))
        for onewire in U_sort:
            if onewire[0][0] == "U":
                apa_u.append(int(onewire[1]))
        return apa_yuv, apa_y, apa_u, apa_v

    def __init__(self):
#        self.APA = 'LArIAT'
#        self.APA = 'APA40'
        self.APA = 'ProtoDUNE'

