#Script from http://veekaybee.github.io/how-big-of-a-sample-size-do-you-need/ on how to calculate sample size, adjusted for my own population size
#and confidence intervals
#Original here: http://bc-forensics.com/?p=15

import math
 
# SUPPORTED CONFIDENCE LEVELS: 50%, 68%, 90%, 95%, and 99%
confidence_level_constant = [50,.67], [68,.99], [90,1.64], [95,1.96], [99,2.57]
 
# CALCUALTE THE SAMPLE SIZE
def sample_size(population_size, confidence_level, confidence_interval):
  Z = 0.0
  p = 0.5
  e = confidence_interval/100.0
  N = population_size
  n_0 = 0.0
  n = 0.0
 
  # LOOP THROUGH SUPPORTED CONFIDENCE LEVELS AND FIND THE NUM STD
  # DEVIATIONS FOR THAT CONFIDENCE LEVEL
  for i in confidence_level_constant:
    if i[0] == confidence_level:
      Z = i[1]
 
  if Z == 0.0:
    return -1
 
  # CALC SAMPLE SIZE
  n_0 = ((Z**2) * p * (1-p)) / (e**2)
 
  # ADJUST SAMPLE SIZE FOR FINITE POPULATION
  n = n_0 / (1 + ((n_0 - 1) / float(N)) )
 
  return int(math.ceil(n)) # THE SAMPLE SIZE
 
def main():
  sample_sz = 0
  population_sz = 100000
  confidence_level = 95.0
  confidence_interval = 2.0
 
  sample_sz = sample_size(population_sz, confidence_level, confidence_interval)
 
  print "SAMPLE SIZE: %d" % sample_sz
 
if __name__ == "__main__":
  main()
