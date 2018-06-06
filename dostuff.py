import sys
file1 = open("saved_det.txt","r+",1)
fileWr = open("def_list.txt","a+",0)
flag=0
for line in file1:
  if flag==1:
     break
  for c in line.split():
    if c=='-':
      flag=1
      continue
    if c=='confidence:':
      break
    else:
      if flag==1:
		fileWr.write(c+"\n")


file1.close()
fileWr.close()
