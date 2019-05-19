
import os

path = r'C:\Users\wangggod\Desktop\car_test\deeplearning_data\test_program'

#usefulNum统计识别结果为可用，uselessNum统计识别结果为不可用,errorNum统计报错图片
totleNum = 0
usefulNum = 0
uselessNum = 0
errorNum=0

#useful统计区间数量 _0.6部分表示置信度大于该值的数量
num_05 = 0
num_06 = 0
num_07 = 0
num_08 = 0
num_09 = 0
num_1 = 0

#统计结果 
effectiveNum = 0
correctNum = 0

f = open("result_1.txt",'r',True)
while True:

    #按行读取每一行，并存储在ch变量中，如果没有读取到就退出循环
    ch = f.readline() 
    if not ch:
        break
    #判断第一个出现的useful的位置是前还是后，并且进行统计，因为每张图片的logid长度不一定，故取最大的位置    
    if ch[2]=='e':
        errorNum = errorNum+1
    elif ch.find('useful')<60:
        a = ch.find(''''useful', 'score': ''')

        #根据score出现的位置后推两位进行数据读取，判断落在哪个置信区间
        if ch[a+19] == '1':
            num_1 = num_1+1
            
        if ch[a+21] == '9':
            num_09 = num_09+1

        if ch[a+21] == '8':
            num_08 = num_08+1

        if ch[a+21] == '7':
            num_07 = num_07+1

        if ch[a+21] == '6':
            num_06 = num_06+1

        if ch[a+21] == '5':
            num_05 = num_05+1

        usefulNum = usefulNum+1
        totleNum = totleNum+1
        #print(a)
        print(ch[a+19:a+22])
    else :
        uselessNum = uselessNum+1
        totleNum = totleNum+1

    #print(ch.find('score'))
    print(ch,end = '')
f.close()
print("useful number:",usefulNum)
print("useless number:",uselessNum)
print("errorNum number:",errorNum)
print("num_05 number:",num_05,"rate:",num_05/usefulNum)
print("num_06 number:",num_06,"rate:",num_06/usefulNum)
print("num_07 number:",num_07,"rate:",num_07/usefulNum)
print("num_08 number:",num_08,"rate:",num_08/usefulNum)
print("num_09 number:",num_09,"rate:",num_09/usefulNum)
print("num_1 number:",num_1,"rate:",num_1/usefulNum)

print("Effective recognition rate:",(totleNum-errorNum)/totleNum)
print("Corrective recognition rate:",(totleNum-abs((usefulNum-25)+(uselessNum-75)))/totleNum)