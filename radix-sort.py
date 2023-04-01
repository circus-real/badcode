def placeSort(arr, place):
  #create 10 lists for digits 0-9
  temp = []
  for i in range(10):
    temp.append([])
  #loop through `arr` and append items to corresponding sub-lists
  for i in arr:
    lastDigit = str(i)[-(place+1)]
    temp[lastDigit].append(i)
  #append all sub-lists to return-list
  finalArr = []
  for i in range(10):
    finalArr.append(temp[i])
  
  return finalArr

pass
