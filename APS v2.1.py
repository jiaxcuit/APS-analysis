"""
Created on Tue Sep 29 2020

A script that reads in APS.DAT and automatic analyse all spectrums.
The script include multiple parts:
    1. import packages and apsmodule
    2. tk choosing file section
    3. loading APS data into list of data for each element is an APS object
    4. analyzation (linear fit)
    5. overlay all the result
    6. writing back the result of substract APS and fit line in CSV
Please run the session you are looking for or following the flow.
This script is open for modification but the "apsmodule" is not.
Before modifying the module please consult with Yi-Chun

Note:
    1.
    For the filename I use my personal style of material_APS.DAT. And this affects how the program truncate the name.
    To change the truncation length just use APS.save_aps_(fit_)csv(data,location,trunc=-n) for n word truncation.
    Again for my personall usage, the default folder direction is to my onedrive APS folder.

@author: Yi-Chun Chin    joe6302413@gmail.com
"""
#%% packages and libraries
import matplotlib.pyplot as plt, tkinter as tk, tkinter.filedialog
from os.path import normpath,split
from os import getenv
from apsmodule import APS
import os
# APSdir=normpath(getenv('OneDrive')+'\\Data\\APS') if getenv('OneDrive')!=None \
#     else ''

# %%
APSdir='/Users/liujiaxin/Library/CloudStorage/OneDrive-ImperialCollegeLondon/AYear 4/MSci Project/MSci Project - Shared/Jiaxin and Emma/Data/241112 APS'

#%% clean apsfiles
apsfiles=[]

#%% choose files
# root=tk.Tk()
# # root.withdraw()
# # root.iconify()
# # root.call('wm', 'attributes', '.', '-topmost', True)
# apsfiles+=tk.filedialog.askopenfilenames(parent=root,initialdir=APSdir, 
#                                           title='Please select APS files',
#                                           filetypes=[('DAT','*.DAT'),('','*.*')])
# root.destroy()

# %%

#apsfiles = [
    #'/Users/liujiaxin/Library/CloudStorage/OneDrive-ImperialCollegeLondon/AYear 4/MSci Project/MSci Project - Shared/Jiaxin and Emma/Data/241112 APS/Ag_ref_APS_12_m4_pro.dat',
            #'/Users/liujiaxin/Library/CloudStorage/OneDrive-ImperialCollegeLondon/AYear 4/MSci Project/MSci Project - Shared/Jiaxin and Emma/Data/241112 APS/Ag_ref_APS_13_m1_pro.dat',
            #'/Users/liujiaxin/Library/CloudStorage/OneDrive-ImperialCollegeLondon/AYear 4/MSci Project/MSci Project - Shared/Jiaxin and Emma/Data/241112 APS/Ag_ref_APS_20_m1_pro.dat']

folder_path="C:\\Users\\horga\\OneDrive - Imperial College London\\MSci Project - Shared\\241112 APS\\P3HT_APS\\"
apsfiles = []
    
# Loop through all files in the folder
for filename in os.listdir(folder_path):
    # Check if the file ends with the given suffix
    if filename.endswith('pro.dat'):
        apsfiles.append(folder_path+filename)

print(apsfiles)
#%% load files into apsdata
plt.close('all')
apsdata=[]
apsdata+=APS.import_from_files(apsfiles,sqrt=False,trunc=-4)

#%% analyze apsdata
plt.close('all')
for i in apsdata:
    i.analyze(0,20)
    
#%% overlay all the apsdata
fig=plt.figure('APS overlay')
for i in apsdata: i.plot()
    
#%% Saving APS and APS fit and HOMO with error
#location='/Users/liujiaxin/Library/CloudStorage/OneDrive-ImperialCollegeLondon/AYear 4/MSci Project/MSci Project - Shared/APS results'
location="C:\\Users\\horga\\OneDrive - Imperial College London\\MSci Project - Shared\\APS results"
# location=split(apsfiles[0])[0]
# APS.save_aps_csv(apsdata,location,filename='Mo2TiC2 sqrt APS')
# APS.save_aps_fit_csv(apsdata,location,filename='Mo2TiC2 sqrt APS_fit')
# APS.save_homo_error_csv(apsdata,location,filename='Mo2TiC2 sqrt APS_HOMO')
APS.save_aps_csv(apsdata,location)
APS.save_aps_fit_csv(apsdata,location)
APS.save_homo_error_csv(apsdata,location)

#%% smoothing DOS
_=[i.DOSsmooth(7,3,plot=True) for i in apsdata]

#%% overlay all the DOS
plt.figure('DOS')
for i in apsdata: i.DOSplot()

#%% Saving DOS into csv
location=split(apsfiles[0])[0]
# APS.save_DOS_csv(apsdata,location,filename='Mo2TiC2 sqrt DOS')
APS.save_DOS_csv(apsdata,location,filename='DOS')
