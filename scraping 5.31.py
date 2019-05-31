# -*- coding: utf-8 -*-
import os
import json
from xlwt import Workbook
import time
'''In a directory of Chinese food safety court case txt,
scrape all phrases that include the fine number, save as data.json,
and output as an xlsx organized by case names chronologically.'''
def getFine(root):
    start_time=time.time()
    data={}
    if os.path.exists(root):
        for fileorDir in os.listdir(root):
            path=os.path.join(root,fileorDir)
            if os.path.isfile(path) and str(path)[-3:]=='txt':
                keyName=str(fileorDir).split('_')[0]
                data[keyName]=[]
                with open(path,'rb') as f:
                    txt=f.read()
                txt1=txt.decode().split('。')
                txt2=[]
                txt3=[]
                for sent in txt1:
                    txt2+=sent.split('，')
                for phrase in txt2:
                    txt3+=phrase.split('；')
                for phrase in txt3:
                    if '处罚' in phrase and '元' in phrase:
                        data[keyName].append(phrase)
    #save as json
    with open('data.json','w') as fw:
        json.dump(str(data),fw)        
    #save as xlsx 
    f=Workbook()  
    table=f.add_sheet('data')       
    keys=[key for key in data]
    output=[]
    for key in keys:
        line=[key]+data[key]
        output.append(line)
    output=sorted(output, key=lambda line: line[0])
    for x,line in enumerate(output):
        for y,phrase in enumerate(line):
            table.write(x,y,phrase)
    f.save('data1.xlsx')
    #time
    print (u"用时：")
    print (float(time.time()-start_time))     
                
                    
                    
                    

        
                
                
                        
                    
                    
                