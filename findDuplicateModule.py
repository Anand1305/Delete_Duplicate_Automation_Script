import os
import CalculateCheckSumModule
import DeleteDuplicateModule

def FindDuplicate(directorName):
    try:
        flag = os.path.exists(directorName)

        if(flag == False):
            print("Directory does not exists")
            exit()
        
        flag = os.path.isabs(directorName)

        if(flag == False):
            directorName = os.path.abspath(directorName)

        flag = os.path.isdir(directorName)

        if(flag == False):
            print("the directory name exists but it's not a directory")
            exit()

        fdict = {}

        for FolderName,subFolderNames,FileNames in os.walk(directorName):
            for fname in FileNames:
                fname = os.path.join(FolderName,fname)
                checksum = CalculateCheckSumModule.CalculateCheckSum(fname)

                if checksum in fdict:
                    fdict[checksum].append(fname)
                
                else:
                    fdict[checksum] = [fname]

            return fdict
        
    except Exception:
        print("Exception occured while directory traversal")