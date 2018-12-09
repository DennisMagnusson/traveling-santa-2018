import pandas as pd
import numpy as np











if __name__ == "__main__":
  df = pd.read_csv("cities.csv")
  df['dist'] = df['X']**2+df['Y']**2
  df = df.sort_values(by=["dist"])
  #x = []
  #for i in df['X'].values:
    #x.append(i)
  #y = []
  #for i in df['Y'].values:
    #y.append(i)
  x = df['X'].values
  y = df['Y'].values
  cols = df['CityId'].values
  xc = 316.837639061509
  yc = 2202.34070733524
  
  i=0
  path = []
  s = set()
  while len(path) != len(x):
    if i in s:
      i += 1
      continue
    mini = 9999999999999
    j = 0
    best = i+1
    j = i-200
    if j < 0:
      j = 0
    while j < i+200:
      if j >= len(x)-1:
        break
      if j in s or i == j:
        j += 1
        continue
      dist = (x[i]-x[j])**2+(y[i]-y[j])**2 

      if dist < mini:
        mini = dist
        best = j
      
      j += 1
    
    path.append(best)
    s.add(best)
    i = best

  """
  for i in range(len(df)):
    l.append([df['X'], df['Y']])
  """

  print("Path")
  print("0")
  for i in path: 
    print(cols[i-2])
  
  print("0")
  #print(int(df.values[0][0]))

