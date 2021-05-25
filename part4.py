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
encoded_str = ''
for i in input_str:
    for j in range(len(list2)):
        if i == list2[j]:
            print(code[j], end='')
            encoded.append(code[j])
            encoded_str += code[j]

# TO CHECK EACH CHAR>>>>
# print('CHECKING A CHAR...')
# for j in range(len(list2)):
#     if list2[j] == 'A':
#         print(code[j], end=' ')

#3 - DECODING
print('\n')
code_index = 0
decoded_txt = ''
for i in encoded:
    for j in code:
        if i == j:
            code_index = code.index(j)
            decoded_txt += list2[code_index]
print(decoded_txt)

#4 - HAMMING(7,4) ENCODING
def hamming(bits):
    r1 = parity(bits, [0, 1, 2])
    r2 = parity(bits, [1, 2, 3])
    r3 = parity(bits, [0, 1, 3])
    return bits + r1 + r2 + r3

def parity(s, indicies):
    sub = ""
    for i in indicies:
        sub += s[i]
    return str(str.count(sub, "1") % 2)

# def decoding_hamming(hamming):
#     s1 = parity(hamming, [4, 0, 1, 2])
#     s2 = parity(hamming, [5, 1, 2, 3])
#     s3 = parity(hamming, [6, 0, 1, 3])
#     return s1 + s2 + s3

split_four = []
for i in range(0, len(encoded_str), 4):
    split_four.append(encoded_str[i: i + 4])

result=''
# check =[]
print("Encoded with Hamming (7,4):")
for i in split_four:
    if len(i) >= 4:
        output = hamming(i)
        result += output
        # result += ' '
        # input = decoding_hamming(output)
        # check.append(input)

print(result)
# print(check)

