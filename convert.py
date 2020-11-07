import os
import xarray as xa
import pandas as pd

# 读取当前路径下的文件
path = os.listdir()
if ".DS_Store" in path:
    path.remove(".DS_Store")
path.remove("convert.py")

# 进度路径循环

def intoPath(path):
    for subPath in path:
        os.chdir(subPath)
        fileSet = os.listdir(os.getcwd())
        if ".DS_Store" in fileSet:
            fileSet.remove(".DS_Store")
        for files in fileSet:
            nc2csv(files)
        os.chdir("..")

# 获取文件以及文件内容并保存为csv

def nc2csv(nc):
    base = ["latitude","longitude","hice","fice"]
    ncDoc = xa.open_dataset(nc)
    ncPd = ncDoc[base].to_dataframe()
    ncPd.to_csv(nc+".csv")

intoPath(path)