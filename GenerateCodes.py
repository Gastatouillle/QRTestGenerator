import qrcode
import random
import os
import shutil

headers = [
    "teamnumber", 
    "matchnumber", 
    "Autoprocess", 
    "Autonet", 
    "Autol1", 
    "Autol2", 
    "Autol3", 
    "Autol4", 
    "brokenDownTimerDuration(auton)", 
    "brokenDownTimerDuration(tele+endgame)", 
    "process", 
    "net", 
    "l1", 
    "l2", 
    "l3", 
    "l4", 
    "missed",
    "park", 
    "shallow", 
    "deep"
]

boolStart = 17
intStart = 2

def GenerateCode(GenNum):
    boolData = headers[boolStart:]
    intData = headers[intStart:boolStart]
    infoData = []
    infostr = ""

    with open("TeamsList.txt") as TeamsList:
        TeamsListLines = TeamsList.readlines()
        TeamsListNoNewLine = []
        for sub in TeamsListLines:
            TeamsListNoNewLine.append(sub.replace("\n", ""))
        for gen in range(0,GenNum):
            infoData = []
            infostr = ""
            MatchNum = random.randint(0,150)
            TeamNum = TeamsListNoNewLine[random.randint(0, len(TeamsListNoNewLine)-1)]
            print(f"TeamNum: {TeamNum}")
            infoData.append(int(TeamNum))
            infoData.append(MatchNum)
            for i in range(len(intData)):
                infoData.append(random.randint(0,8))


            for i in range(len(boolData)):
                if boolData[i] == 1:
                    infoData.append(True)
                else:
                    infoData.append(False)
            for i in infoData:
                infostr = infostr + ',' + str(i)
            infostr = infostr.removeprefix(',')
            print(infostr)
            qr = qrcode.make(infostr)
            type(qr)
            qr.save(f"GenCodes/QR{gen}.png")

shutil.rmtree("GenCodes")
os.makedirs("GenCodes")
GenerateCode(50)
print("-----------------------------------")

