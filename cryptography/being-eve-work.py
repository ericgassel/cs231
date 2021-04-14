#Diffie-Hellman 
g = 17
p = 61
A = 46
B = 5
test = 1
count = 0
a = b = 0
while(count<2):
    if g**test%p == A:
        a = test
        count+=1
    if g**test%p == B:
        b = test
        count+=1
    test+=1
print('a = ',a,'b = ',b)

K1 = B**a%p
K2 = A**b%p
if K1 == K2:
    print('K = ',K1)

#RCA
e = 31
n = 4661
p = q = d = 0
for test_p in range(50,90):
    for test_q in range(50,90):
        if test_p*test_q == n:
            p = test_p
            q = test_q
        if p != 0:
            break
    if p != 0:
        break  
print('p = ',p,'q = ',q) 

test_d = n
while (test_d>0):
    if (e*test_d)%((p-1)*(q-1)) == 1:
        d = test_d
        break
    test_d-=1
print('d = ',d)

encrypted_data = [2677, 4254, 1152, 4645, 4227, 1583, 2252, 426, 3492, 4227, 3889, 1789, 4254, 
                    1704, 1301, 4227, 1420, 1789, 1821, 1466, 4227, 2252, 3303, 1420, 2234, 4227,
                    4227, 1789, 1420, 1420, 4402, 1466, 4070, 3278, 3278, 414, 414, 414, 2234, 1466, 1704, 
                    1789, 2955, 4254, 1821, 4254, 4645, 2234, 1704, 2252, 3282, 3278, 426, 2991, 2252, 1604, 
                    3278, 1152, 4645, 1704, 1789, 1821, 4484, 4254, 1466, 3278, 1512, 3602, 1221, 1872, 3278, 
                    1221, 1512, 3278, 4254, 1435, 3282, 1152, 1821, 2991, 1945, 1420, 4645, 1152, 1704, 1301, 
                    1821, 2955, 1604, 1945, 1221, 2234, 1789, 1420, 3282, 2991, 4227, 4410, 1821, 1301, 4254, 
                    1466, 3454, 4227, 4410, 2252, 3303, 4645, 4227, 3815, 4645, 1821, 4254, 2955, 2566, 3492, 
                    4227, 3563, 2991, 1821, 1704, 4254]
message = []
for cipher in encrypted_data:
    decrypted_data = cipher**d%n
    message.append(decrypted_data)

decrypted_message = ''
for number in message:
    decrypted_message+=chr(number)
print(decrypted_message)


