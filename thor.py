from thor_devkit.cry import mnemonic
from thor_devkit import cry
from thor_devkit.cry import hdnode

words = 'biscuit cracker staff random comic enjoy bag install white'
address = '0xabcda323e9c2caf3851403e6cfafe7aa81996b04'
word10 = ''
word11 = ''
word12 = ''
words2 = ''

counter = 0
totalCount = 4194304
done = False;

WordlistOne = open('firstword.txt').readlines()
WordlistTwo = open('english.txt').readlines()
WordlistThree = open('english.txt').readlines()
file1 = open("output.txt","w")

for line in WordlistOne:
    if(done == True):
        break;
    for line2 in WordlistTwo:
        if(done == True):
            break;
        counter=counter+1
        print('Percent Complete: ' + str(counter * 100/totalCount))
        #print('Trying Word#:' + str(counter) + ' ' + line)
        for line3 in WordlistThree:
            i = line.strip()
            j = line2.strip()
            k = line3.strip()
            words2 = words + ' ' + i + ' ' + j + ' ' + k
            words2 = words2.split(' ')
            flag = mnemonic.validate(words2)
            
            if(flag == True):
                #print('Trying Word#:' + ' ' + i + ' ' + j + ' ' + k)
                
                hd_node = cry.HDNode.from_mnemonic(
                        words2,
                        init_path=hdnode.VET_EXTERNAL_PATH
                        )
                addr = '0x'+hd_node.derive(0).address().hex()
                if(addr == address):
                    word10 = i
                    word11 = j
                    word12 = k
                    print('Found!!!: ' + i + ' + ' + j + ' + ' + k)
                    file1.write(i + 'is the 9th word' + '\n')
                    file1.write(j + 'is the 10th word' +  '\n')
                    file1.write(k + 'is the 11th word' +  '\n')
                    file1.close()
                    done = True;
                    break;
    file1.write(line + 'is not the first word')
    print(line + 'is not the first word')
