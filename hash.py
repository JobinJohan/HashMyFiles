# Johan Jobin, University of Neuchatel
# Security
# Assignment 2
# Program to monitor the integrity of files and folders using a strong crypto-graphic hash function (SHA-256)
#
# command: python hash.py <directory> <fileContainingExceptions>
#
# -*- coding: utf-8 -*-


import sys
import os
import hashlib
import json
import csv

try:
   boolean= (sys.argv)==2
   listOfExceptions= open(sys.argv[2], "r")
   
except:
   print("Wrong arguments, command is: python hash.py <directory> <fileContainingExceptions>")
   sys.exit(1)
   
input_data = []
for row in csv.reader(listOfExceptions, delimiter=',', quoting=csv.QUOTE_NONE):
   input_data += row
print(input_data)

   
print("----------------------HASH MY FILES----------------------\n")
print("Choose your mode:")
choice = input('1\) Scan all directories, subdirectories and compute the SHA-256 hash of each file \n2\) Check the modification\n3\) Exit\n')

if(choice== '1'):
   dictionary = {}
   for root, dirs, files in os.walk(sys.argv[1], topdown=False): 
      matching= [s for s in input_data if s in root]
      if(len(matching)==0):
         for folder in dirs:
            if(folder not in input_data):
               if(folder != []):
                  dictionary[folder]="folder" 
               
         for name in files:
               if(name not in input_data):
                  with open(os.path.join(root, name), 'rb') as afile:
                     buf = afile.read()      
                     dictionary[name]= hashlib.sha256(buf).hexdigest()
      else:
         continue
           
   try:
      output = open('./output.json','w')
   except:
      print("Impossible to write the file")
      sys.exit(1)
   json_string = json.dumps(dictionary)
   output.write(json_string)
   output.close()
  
elif(choice=='2'):
   path = input("Enter the path of the files containing hashes\n")
   try:
      refFile = open(path, "r")
   except:
      print("Incorrect path, file not found")
      sys.exit(1)
   try:
      dictionaryFromFile = json.load(refFile)
   except:
      print("Corrupted file or invalid json format, create the file with the mode 1\) of this program")
      sys.exit(1)
      
   currentDictionary = {}
   for root2, dirs2, files2 in os.walk(sys.argv[1], topdown=False):
      matching2= [s for s in input_data if s in root2]
      if(len(matching2)==0):      
         for name2 in files2:
            if(name2 not in input_data):
               with open(os.path.join(root2, name2), 'rb') as afile2:
                  buf2 = afile2.read()
                  currentDictionary[name2]= hashlib.sha256(buf2).hexdigest()
         for folder2 in dirs2:
            if(folder2 not in input_data):
               if(folder2 != []):
                  currentDictionary[folder2]="folder"   
      else:
         continue

   finalDocument={}
   for key in dictionaryFromFile.keys():
      if(dictionaryFromFile[key]=="folder"):
         finalDocument[key]="folder"
      else:
         finalDocument[key]="No information yet"
   for key in currentDictionary.keys():
      if(currentDictionary[key]=="folder"):
         finalDocument[key]="folder"
      else:
         finalDocument[key]="No information yet" 
      
   for key in finalDocument.keys():
      """key present in both files """
      if((dictionaryFromFile.get(key,"none")!= "none") and (currentDictionary.get(key,"none") !="none")):
         """hash is the same in both files"""
         if(dictionaryFromFile[key]==currentDictionary[key]):
            if(dictionaryFromFile[key]=="folder"):
               finalDocument[key]="Folder not modified"
            else:
               finalDocument[key]="File not modified: "+dictionaryFromFile[key]+"" 
         else:
            if(dictionaryFromFile[key]=="folder"):
               finalDocument[key]="Folder modified" 
            else:
               finalDocument[key]="File modified: previous hash:"+dictionaryFromFile[key]+" current hash: "+currentDictionary[key]
 
      elif((dictionaryFromFile.get(key,"none")!= "none") and (currentDictionary.get(key,"none") == "none")):
         """key only present in the backup file"""
         if(dictionaryFromFile[key]=="folder"):
            finalDocument[key]="Folder deleted"
         else:
            finalDocument[key]="File deleted"
         
      elif((dictionaryFromFile.get(key,"none")== "none") and (currentDictionary.get(key,"none") != "none")):
         """key ony present in the file currentDictionary"""
         if(currentDictionary[key]=="folder"):
            finalDocument[key]="Folder created"
         else:
            finalDocument[key]="File created with hash: "+currentDictionary[key]+""
   print(finalDocument)
elif(choice=='3'):
   print("Thank you for using HASH MY FILES, see you soon !")
else:
   print("Enter a valid option please")
   
   
