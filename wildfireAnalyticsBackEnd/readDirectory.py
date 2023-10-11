'''
Code to obtain certain files from a directory.
'''


import glob


'''
Parameters:
    - string: Name of directory
Returns:
    - string: name of a shapefile in the directory
        or an empty string

Notes:
For pure functionality: should shapefileName be an array?
Should it return value error instead of any empty string?
'''
def getShapeFile(directoryName):
    shp_files_list = glob.glob(f"{directoryName}/*.shp")
    if shp_files_list:
        shapefileName = shp_files_list[0]  # directoryName/shapefileName.shp
        return shapefileName
    return ""
