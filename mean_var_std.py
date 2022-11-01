import numpy as np

def calculate(list):
  if len(list)!= 9:
    raise ValueError("List must contain nine numbers.")

  list=np.array(list).reshape(3,3)
  
  calculations={
  'mean':[list.mean(0).tolist(),list.mean(1).tolist(),np.mean(list)],
  'variance':[list.var(0).tolist(),list.var(1).tolist(),np.var(list)],
  'standard deviation':[list.std(0).tolist(),list.std(1).tolist(),np.std(list)],
  'max':[list.max(0).tolist(),list.max(1).tolist(),np.max(list)],
  'min':[list.min(0).tolist(),list.min(1).tolist(),np.min(list)], 
  'sum':[list.sum(0).tolist(),list.sum(1).tolist(),np.sum(list)]
  }
  return calculations