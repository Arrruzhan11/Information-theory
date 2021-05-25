#1 - PROBABILITY
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

print("Frequency of all characters:\n " + str(all_freq))
print(all_char)
print("Probability of all characters:\n " + str(probability))

#2 ENCODING

list1=[]
list2=[]
for key, val in sorted(probability.items(), key=lambda probability: probability[1], reverse=True):
    list1.append(val)
    list2.append(key)
    print(key, val)


def divideList(list1):
    left = 0
    right = 0
    m = 0
    arr1 = []
    arr2 = []
    for i in range(0, len(list1)):
        if len(list1) - m <= i:
            break
        left += list1[i]
        arr1.append(list1[i])
        for j in range(m+1, len(list1)):
            if len(list1) - i == j:
                m = j
                break
            right += list1[-j]
            arr2.insert(0, list1[-j])
            if left <= right:
                m = j
                break
            m = j
    return arr1, arr2

code = []
def labeling(list1, t1):
    arr1, arr2 = divideList(list1)
    #print(arr1)
    #print(arr2)
    if len(arr1) != 1:
        labeling(arr1, t1+'0')
    else:
        code.append(t1 + '0')
    if len(arr2) != 1:
        labeling(arr2, t1+'1')
    else:
        code.append(t1 + '1')

labeling(list1, '')
print(list2)
print(code)

encoded = []
for i in input_str:
    for j in range(len(list2)):
        if i == list2[j]:
            #print(code[j], end=' ')
            encoded.append(code[j])

# TO CHECK EACH CHAR>>>>
print('CHECKING A CHAR...')
for j in range(len(list2)):
    if list2[j] == 'A':
        print(code[j], end=' ')

#3 - DECODING
print('\n', encoded)
print('\n')
code_index = 0
decoded_txt = ''
for i in encoded:
    for j in code:
        if i == j:
            code_index = code.index(j)
            decoded_txt += list2[code_index]
print(decoded_txt)

