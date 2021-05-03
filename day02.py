#!/usr/bin/env python
# coding: utf-8

# # if
# ```
# if 조건문:  
#     수행할 문장1  
#     수행할 문장2  
#     수행할 문장3  
# ```

# In[1]:


a = 10
if a >= 10:
    print("yes")


# In[ ]:


money = True
if money:
    print("택시를")


# ### if-else

# In[2]:


money = 2000
if money >= 3000 :
    print("택시를 타고 가라")
else:
    print("걸어가라")


# In[3]:


money >= 3000


# ex) 돈이 3000원 이상 있거나 카드가 있다면 택시를 타고 그렇지 않으면 걸어가라.

# In[11]:


money = 2000
card = True

if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어가라")


# In[12]:


(money >= 3000 or card) is True


# → 조건문이 헷갈린다면 이렇게 확인해보고 사용할 수 있다.

# ex) 만약 주머니에 돈이 있으면 택시를 타고, 없으면 걸어가라.

# In[16]:


pocket = ['paper', 'cellphone', 'money']

if 'money' in pocket:
    print("택시를 타고 가라")
else :
    print("걸어가라")


# In[17]:


pocket = ['paper', 'cellphone', 'money']

if 'money' in pocket:
    pass
else :
    print("걸어가라")


# ### elif

# ex) 주머니에 돈이 있으면 택시를 타고, 주머니에 돈은 없지만 카드가 있으면 택시를 타고, 돈도 없고 카드도 없으면 걸어가라

# In[21]:


pocket = ['paper', 'cellphone']
card = False

if 'money' in pocket:
    print("택시를 타고 가라")
elif card:
    print("택시를 타고 가라")
else :
    print("걸어가라")


# ### 한줄로 작성하는 if문

# In[22]:


score = 50

if score >= 60:
    message = "success"
else:
    message = "failure"
    
message


# In[23]:


message = "success" if score >= 60 else "failure"
message


# # while
# ```
# while 조건문:
#     수행할 문장1
#     수행할 문장2
#     수행할 문장3
# ```

# ex) hello world 10번 입력

# In[24]:


i = 1
while i < 11:
    print("hello world")
    i += 1


# In[26]:


i = 1
while i < 11:
    print("{}회 hello world".format(i))
    i += 1


# ### break

# In[27]:


i = 1
while True:
    print("{}회 hello world".format(i))
    i += 1
    if i == 11: 
        break


# In[29]:


i = 1
while True:
    print("{}회 hello world".format(i))
    i += 1
    if i == 11: 
        print("종료")
        break


# In[30]:


i = 1
while i < 11:
    print("{}회 hello world".format(i))
    i += 1
    if i == 11:
        print("종료")


# ex) 나무 10번 찍어 넘어가게 하기

# In[7]:


i = 1
while i < 11:
    print("나무를 {}번 찍었습니다.".format(i))
    i += 1
    if i == 11:
        print("나무 넘어갑니다.")


# In[8]:


treeHit = 0
while treeHit < 10:
    treeHit = treeHit + 1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        break
        print("나무 넘어갑니다.")


# - 주사위 놀이  
# 주사위 눈이 6이 나오면 종료, 총 던진 횟수 출력

# In[9]:


import numpy as np


# In[11]:


get_ipython().run_line_magic('pinfo', 'np.random.randint')


# In[10]:


np.random.randint(1, 7, size = 100)


# ### QUIZ
# 
# 1) hello world 매 10회마다 출력, 100번까지 총 10회 출력

# In[34]:


i = 1
while i < 101:
    if i%10 == 0:
        print(f"{i}회 hello world")
    i += 1


# 2) 주사위 눈이 6이 나오면 종료  
# 해당 시행에서 나온 눈을 출력하고, 총 던진 횟수를 출력하세요

# In[26]:


i = 0
while True:
    dice = np.random.randint(1,7)
    print(f"나온 눈은 {dice}")
    i += 1
    if dice == 6:
        print(f"던진 횟수 : {i}")
        break


# In[35]:


i = 0
s = 0
while i != 6:
    i = np.random.randint(1,7)
    s += 1
    print("나온 눈은 {}".format(i))
    if i == 6:
        print("던진 횟수 : {}".format(s))


# In[36]:


i = 0
s = 0
res = []
while i != 6:
    i = np.random.randint(1,7)
    res.append(i)
    s += 1
    print("나온 눈은 {}".format(i))
    if i == 6:
        print("던진 횟수 : {}".format(s))
        print(res)


# 3) 커피머신: 다음과 같은 메시지를 출력하는 커피머신 루프  
# 돈을 받았으니 커피를 줍니다.  
# 남은 커피의 양은 10개 입니다.  
# 돈을 받았으니 커피를 줍니다.  
# 남은 커피의 양은 9개 입니다.

# In[27]:


coffee = 10
while True:
    print("돈을 받았으니 커피를 줍니다.")
    print(f"남은 커피의 양은 {coffee}개 입니다.")
    coffee -= 1
    if coffee == 0:
        break


# # for
# ```
# for 변수 in 리스트(또는 튜플, 문자열):
#     수행할 문장1
#     수행할 문장2
# ```

# In[40]:


for i in range(0,10):
    print(i)


# In[37]:


sum = 0
for i in range(10):
    sum += i
    
sum


# In[41]:


a = []
for i in range(1,5):
    a.append(i)
print(a)


# In[42]:


b = []
for i in range(1,6,2):
    b.append(i)
print(b)


# In[44]:


sum = 0
for i in range(1,11):
    sum = sum + i
sum


# In[46]:


for i in range(1,11):
    print(f"나무 {i}번 찍었습니다.")
print("넘어갑니다.")


# In[47]:


for i in range(1,12):
    if i < 11:
        print("나무 {}번 찍었습니다.".format(i))
    else: print("넘어갑니다")


# ## enumerate

# In[49]:


p = ['money', 'card']
enumerate(p)


# In[50]:


for idx, value in enumerate(p):
    print(idx, value)


# ## zip

# In[53]:


p = ['money', 'card']
q = [10,20,30]

for num, word in zip(q, p):
    print(num, word)


# ex) 구구단

# In[65]:


for i in range(2,10):
    print("== {} 단 ==".format(i))
    for j in range(1,10):
        print(f"{i} * {j} = {i*j}")
    print(" ")


# In[64]:


for i in range(2,10):
    print("="*2, "%d단" % i, "="*2)
    for j in range(1,10):
        print("{} * {} = {}".format(i, j, i*j), "")
    print(" ")


# ## 리스트 컴프리핸션 (내포)

# In[66]:


a = [1,2,3,4]
result = []
for num in a:
    result.append(num*3)
    
result


# In[67]:


a = [1,2,3,4]
result = [num * 3 for num in a]   #컴프리핸션
result


# In[68]:


a = [1,2,3,4]
result = [b * 3 for b in a if b % 2 == 0]
result


# → 동일한 코드
# ```
# for b in a:
#     if b % 2 ==0:
#         result.append(b * 3)
# ```

# # UDF (사용자 정의 함수)

# In[70]:


def add(a, b):
    result = a+b
    return result

add(3,4)


# **결과값이 없는 함수**

# In[73]:


def adding(a, b):
    print("%d, %d의 합은 %d입니다." % (a, b, a+b))

adding(7,8)


# In[75]:


a = adding(7,8)
print(a)    # None


# In[76]:


def adding1(a,b):
    res = a+b     

print(adding1(1,2))   # None


# In[77]:


def adding2(a,b):
    res = a+b
    return res

print(adding2(1,2))


# In[80]:


def cal(a,b):
    res = a+b
    res2 = a-b
    return res, res2  #하나의 튜플 값으로 나옴

cal(2,1)  


# ### 사용자 정의 함수에 초기값을 지정하는 경우
# - 초기값이 지정된 인수가 입력되지 않으면 초기값이 실행
# - 새로운 파라미터가 입력되면 입력값으로 실행

# In[86]:


def say_myself(name, old, man=True):
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살 입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself("홍길동", 27)


# In[87]:


say_myself("홍길동", 31, False)


# In[88]:


say_myself(man = False, name = "홍길동", old = 28)


# In[89]:


def say_myself(name, old, man=True):
    """ 
    old : 나이 (integer only)
    """
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살 입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")


# In[94]:


say_myself('abc',5)


# ## 함수 안 변수의 효력

# In[99]:


a = 1
def vartest(a):
    a = a+1
    
vartest(a)
print(a)


# In[101]:


a = 1
def vartest(a):
    a = a+1
    return(a)
    
vartest(a)


# In[102]:


print(a)


# ### 전역변수
# 
# - 전역변수의 사용은 주의가 필요하다.

# In[104]:


c = 1
def vartest1(a):
    global c
    c = c+1

vartest1(c)
c


# ### Lambda 표현식

# In[109]:


a = 3
b = 4
add = lambda a, b : a+b


# In[112]:


(lambda a, b : a+b)(3,4)


# In[111]:


result = add(3,4)
print(result)


# ### input 함수

# In[117]:


a = input()


# In[118]:


a


# In[119]:


number = int(input("정수를 입력하세요: "))


# In[120]:


number


# # 파일 읽고 쓰기

# ## 파일 생성

# In[121]:


f = open("examples/test.txt", "w")     # examples 폴더에 test.txt 파일 생성 & 열기 / w : white (아무것도 없는 도화지 생성)  
for i in range(1,11):       
    data = "%d번째 줄입니다.\n" % i    # __번째 줄입니다. 라는 말을
    f.write(data)                      # 파일에 입력
f.close()                              # 파일 닫기


# In[122]:


f = open("examples/test.txt", "a")     # examples 폴더에 test.txt 파일 생성 & 열기 / a : add (추가하겠다) 
for i in range(1,11):       
    data = "%d번째 줄입니다.\n" % i    # __번째 줄입니다. 라는 말을
    f.write(data)                      # 파일에 입력
f.close()                              # 파일 닫기


# In[123]:


f = open("examples/test1.csv", "w")     # examples 폴더에 test.txt 파일 생성 & 열기
for i in range(1,11):       
    data = "%d번째 줄입니다.\n" % i    # __번째 줄입니다. 라는 말을
    f.write(data)                      # 파일에 입력
f.close()                              # 파일 닫기


# ## 파일 읽어오기

# ### readline()

# In[129]:


f = open("examples/test.txt", 'r')
line = f.readline
print(line)
f.close()


# In[131]:


with open("examples/test.txt", 'r') as f:
    while True:
        line = f.readline()
        if not line: break
        print(line)


# In[132]:


text = []
with open('examples/test.txt', 'r') as f:
    while True:
        line = f.readline()
        text.append(line)
        if not line: break


# In[134]:


f = open("examples/test.txt", 'r')
data1 = f.readlines()
data2 = f.read()
f.close()


# In[135]:


data1


# In[136]:


data2


# In[ ]:




