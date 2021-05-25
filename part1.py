input_str = open('hah.txt', 'r').read()
all_freq = {}
probability = {}
for i in input_str:                            # finding frequencies
   if i in all_freq:
      all_freq[i] = all_freq[i]+1
   else:
      all_freq[i] = 1

all_char = sum(all_freq.values())             # finding total characters

for i in input_str:
   probability[i] = all_freq[i]/all_char     # finding probabilities

#print("Frequency of all characters:\n " + str(all_freq))
#print(all_char)
print("Probability of all characters:\n " + str(probability))

