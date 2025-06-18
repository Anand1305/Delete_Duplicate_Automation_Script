import time
import SendEmailModule

def LogFile(duplicateList,sender,reciver):
    try:
        timestamp = time.ctime()

        fileName = "LogFile%s" %(timestamp)

        fileName = fileName.replace(" ","_")
        fileName = fileName.replace(":","_")

        fobj = open(fileName,'w')

        Border = "-"*80

        fobj.write(Border+'\n')
        fobj.write("This is a log file which consists the name of the duplicate files from the directory "+'\n')
        fobj.write(Border+'\n')

        fobj.write('\n\n\n\n\n\n\n')

        for i in range(0,len(duplicateList)):
            for j in range(0,len(duplicateList[i])):
                fobj.write(str(duplicateList[i][j]))
                fobj.write('\n')

        fobj.write('\n\n\n\n\n\n\n')

        fobj.write(Border+'\n')

        fobj.write("\t\t\t Automation Script \t\t\t\n")

        fobj.write("\t\t\t Execution time is : "+str(timestamp)+'\n')

        fobj.write(Border+'\n')

        fobj.close()

        print("Log File Created successfully")

        SendEmailModule.SendEmail(fileName,sender,reciver)
    except Exception:
        print("Exception while creating log file")