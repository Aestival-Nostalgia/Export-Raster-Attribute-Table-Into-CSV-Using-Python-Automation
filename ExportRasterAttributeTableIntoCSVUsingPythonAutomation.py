# -*- coding: utf-8 -*-
import arcpy, os
import csv
import sys
reload(sys) 
sys.setdefaultencoding('utf-8')

ws = r"D:\G\DATA_Clip\实验区"
outPath = r"D:\G\PRO"
outExt = ".csv"

arcpy.env.workspace = ws
rasters = arcpy.ListRasters("*")
for raster in rasters:
    rasloc = ws + os.sep + raster
    fields = "*"
    try:
        lstFlds = arcpy.ListFields(rasloc)
        header = ''
        for fld in lstFlds:
            header += ",{0}".format(fld.name)
            if len(lstFlds) != 0:
                outCSV = outPath + os.sep + raster + outExt
                f = open(outCSV,'w')
                header = header[1:] + ',RasterName\n'
                f.write(header)
                with arcpy.da.SearchCursor(rasloc, fields) as cursor:
                    for row in cursor:
                        f.write(str(row).replace("(","").replace(")","") + "," + raster + '\n')
                f.close()
                print(raster + " Finished!")
    except Exception as e:
        print(raster + " " + str(e))

# 本代码请注意缩进，很多注意事项
# 基于Python2.7
# 有很多奇奇怪怪的小问题