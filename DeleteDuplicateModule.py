import findDuplicateModule
import os
from CreateFileLogModule import LogFile

def DeleteDuplicate(directoryName,sender,reciver):
    try:
        fdict = findDuplicateModule.FindDuplicate(directoryName)
        
        count = 0

        duplicateList = []
   
        for fname in fdict.values():
            if(len(fname) > 1):
                duplicateList.append(fname)
                
        for i in range(0,len(duplicateList)):
            for j in range(1,len(duplicateList[i])):
                os.remove(duplicateList[i][j])
        
        LogFile(duplicateList,sender,reciver)
    
    except Exception:
        print("Exception occured while deleting the duplicate files")
            

    
    
    
                

    