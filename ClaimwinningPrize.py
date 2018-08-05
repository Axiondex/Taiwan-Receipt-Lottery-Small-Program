from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import re, sys, urllib
import htmlparse
import os
#FileSave() call GrabWebSrc()
#RunNumber() call SplitNumb() call RegexFiliter()
class Prize:
    #def __init__(self):
    def WriteDataInToText(self):
        with open("recipthtml.txt","wb+") as reciptHtml: #Save html information from GrabWebSrc()
            #call GrabWebSrc function
            reciptHtml.write(self.grabWebSrc())
            if reciptHtml.closed == False:
                reciptHtml.close()
    def grabWebSrc(self):
        req = Request('http://invoice.etax.nat.gov.tw/')
        #grab website information
        try:
            response = urlopen(req)
        except(URLError, e):
            print(e.code())
        #page = response.read().decode('UTF-8','replace')
        page = response.read()
        #print (page)
        #print response.info()
        return page
    
    def openfile(self):
        with open("recipthtml.txt","r+", encoding="utf-8") as recipttext:
            content = recipttext.read()
        recipttext.close()
        return content
    def numberCheck(self,numbers,winningnumbers):
        length = len(numbers)
        level = 0
        for index, winningnumlevel in enumerate(winningnumbers[:4]):
            level = index
            for winningnum in winningnumlevel:
                #print(winningnum)
                '''if len(winningnum) < len(numbers):
                    length = len(winningnum)
                else:
                    print("fail")'''
                matchednumber = sum(a == b for a, b in zip(reversed(winningnum),reversed(numbers)))
                self.reward(level, matchednumber)
                
    def reward(self, level,matchednumber):
        prize = ""
        if matchednumber == 8 and level == 0:
            print(" win the first prize 100 million")
        elif matchednumber == 8 and level == 1:
            prize = ("win 2 million")
        elif level >= 2:
            if matchednumber == 3:
                print ("win 200")
                prize = "win 200"
            elif matchednumber == 4:
                print ("win 1000")
                prize = "win 200"
            elif matchednumber == 5:
                print ("win 4000")
                prize = "win 4000"
            elif matchednumber == 6:
                print ("win 10000")
                prize = "win 10000"
            elif matchednumber == 7:
                print ("win 40000")
                prize = "win 40000"
            elif matchednumber == 8:
                print ("win twenty thousand")
                prize = "win twenty thousand"
        return prize
    def EnterNumber(self,winningnumbers):
        while True:
            typein = input("Enter the Number")
            if not typein.isdigit() and typein != "":
                typein = input("Please type again")
            else:
                break
            self.numberCheck(typein,winningnumbers)
    def RefreshData(self):
        if(not os.path.isfile("recipthtml.txt")):
            WriteDataInToText()
        else:
             typein = input("Do you want to reload the Data from website? (Y/N)")
             if(typein in "Yy" ):
                 WriteDataInToText()
recipt = Prize()
recipt.RefreshData()
parser = htmlparse.MyHTMLParser(recipt.openfile())
parser.generateItem()
parser.close()
rewardTitle = ['特別獎', '特獎', '頭獎', '增開六獎']
print(parser.titles[0])
for index, num in enumerate(parser.numbers[:4]):
    print(rewardTitle[index])
    print(num)
recipt.EnterNumber(parser.numbers)
#recipt.numberCheck("1340",parser.numbers)
