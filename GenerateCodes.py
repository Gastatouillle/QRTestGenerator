import qrcode
import random
import os
import shutil

PitAttributes = ['canShoot', 'canClimb', 'canTrap', 'canIntake', 'canDrive', 'canPass', 'canAmp']
MatchNumAttributes = ['scoredSpeakerAuto', 'scoredAmpAuto', 'failedToScoreAuto', 'scoredSpeakerTele', 'scoredAmpTele', 'trappedTele', 'passedTele', 'intakedTele', 'failedToScoreTele']
MatchBoolAttributes = ['failedEnd','climbedEnd', 'trappedEnd']


def GenerateCode(GenNum):
    for gen in range(0,GenNum):
        MatchType = random.randint(0,1)
        TeamNum = 5584
        MatchNum = random.randint(0,150)

        if MatchType == 1:
            QRdata = ['P']
            QRdata.append(f"Teamnum={TeamNum}")
            for x in PitAttributes:
                DictData = {x: random.randint(0,1)}
                if DictData[x] == 1:
                    QRdata.append(x)
        else: 
            QRdata = ['M']
            QRdata.append(f"Teamnum={TeamNum}")
            QRdata.append(f"Matchnumber={MatchNum}")
            for x in MatchNumAttributes:
                QRdata.append(f"{x}={random.randint(0,45)}")
            
            for x in PitAttributes:
                QRdata.append(f"{x}={random.randint(0,1)}")
        
        print(QRdata)
        qr = qrcode.make(QRdata)
        type(qr)
        qr.save(f"GenCodes/QR{gen}.png")

shutil.rmtree("GenCodes")
os.makedirs("GenCodes")
GenerateCode(50)
