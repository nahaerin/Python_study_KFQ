#!/usr/bin/env python
# coding: utf-8

# # Class

# 단순 덧셈 연산만 하는 계산기 함수를 작성해보자

# In[1]:


def adding(a):
    result = 0
    result += a
    return result


# 위와 같이 함수를 작성하면 추가적인 숫자를 더하는 기능을 만들 수 없다.  
# result가 앞의 수를 기억하도록 전역변수로 설정

# In[2]:


result = 0
def adding(a):
    global result
    result += a
    return result


# In[3]:


a = adding(4)


# In[4]:


b = adding(4)


# In[5]:


c = adding(5)


# In[6]:


a,b,c


# 이제 다른 작업을 하기 위해 adding 함수에 첫 값 2를 넣고 e에 저장

# In[7]:


e = adding(2) 
e


# 위와 같이 이전의 다른 작업에서의 결과가 들어가는 오류 발생  
# **이와 같이 함수는 독립적 사용이 어려움**
# 
# 참고) 2의 배수만 입력으로 받아 더하는 계산기가 필요하다면?

# In[8]:


result1 = 0
def adding1(a):
    assert a%2 == 0, 'error: input is odd number'  #assert 조건문, 조건에 맞지 않을 때 에러문  -> 조건문에 맞으면 밑에 실행
    global result1
    result1 += a
    return result1


# In[9]:


adding1(4)


# In[11]:


adding1(8)


# In[12]:


# error
adding1(3)


# **2의 배수만 입력으로 받아 더하는 계산기가 여러개 필요하다면?**  
# -> Class 사용
# 
# 계산기 클래스의 2의 배수만 입력으로 받는 메서드의 형태로 프로그램을 작성하면 해당 클래스의 인스턴스로 객체를 생성(필요한 만큼)하여 객체 간의 간섭 없이 필요 메서드를 반복하여 수행할 수 있다.

# #### Case 1: 객체 생성 후 초기값을 입력받는 메서드를 통해 초기값 생성

# In[19]:


class FourCal:
    def setdata(self, num):  # 메소드
        """
        simple caculator for adding
        ----------
        Parameter:
            num: int or float
        """
        self.init = num     # 속성
    
    def adding(self, num):  # 메소드
        self.num = num
        assert self.num%2 == 0, 'error: input is odd number'
        self.init += self.num
        return self.init


# 객체 생성

# In[20]:


b = FourCal()  # 인스턴스 생성. b라는 객체


# In[21]:


b.setdata(3)   # 


# In[22]:


b.init


# In[23]:


b.adding(4) 


# In[24]:


b.adding(8) 


# In[26]:


b.setdata(2) 


# In[27]:


b.adding(2) 


# In[28]:


b.adding(4) 


# #### Case2: 생성자 활용

# In[29]:


class FourCal1:
    def __init__(self):
        self.init = 0
    def adding(self, num):
        assert num%2 == 0, 'error: input is odd number'
        self.init += num
        return self.init


# In[30]:


c = FourCal1()   # 클래스 FourCal1의 인스턴스 생성


# In[34]:


c.init           # 객체 c를 확인해보면, 인스턴스 생성시 생성자 init()이 자동실행되므로 이미 init 속성이 0으로 생성되어 있는 것을 볼 수 있다.


# -> __init__을 하게 되면 객체를 생성함과 동시에 init이 자동으로 들어감. (파이썬 내장 함수)

# 이어서 adding 메서드에 구체적인 값을 할당하여 계산 기능을 수행한다.

# In[35]:


c.adding(2)


# ### 모듈의 사용
# 위 FourCal1 클래스를 fourcal.py로 저장하고 modules 폴더에 위치시킨 후 import하여 사용한다.

# In[40]:


# 경로 설정
import sys
sys.path.append("C:\\study_bigdata\\study\\modules")


# In[39]:


import fourcal


# In[42]:


fourcal.FourCal1


# ### 클래스 상속(FourCal1 -> MoreFourCal)
# 
# 왜 상속을 해야할까?
# 
# 보통 상속은 기존 클래스를 변경하지 않고 기능을 추가하거나 기존 기능을 변경하려고 할 때 사용한다.  
# "클래스에 기능을 추가하고 싶으면 기존 클래스를 수정하면 되는데 왜 굳이 상속을 받아서 처리해야 하지?" 라는 의문이 들 수도 있다. 하지만 기존 클래스가 라이브러리 형태로 제공되거나 수정이 허용되지 않는 상황이라면 상속을 사용해야한다.

# In[43]:


class MoreFourCal(FourCal1):
    def subtracting(self, num):
        self.init -= num
        return self.init


# In[44]:


e = MoreFourCal()
e.init


# In[45]:


e.subtracting(2)


# In[47]:


e.subtracting(-5)


# ### 매개변수 개수가 몇 개든 상관없는 함수의 생성 -> `*`의 사용
# 
# ex) (몇개든) 숫자를 받아서 평균을 구하는 함수를 만든다면?

# In[48]:


def my_avg(*args):
    result = sum(args)/(len(args))
    return result


# In[49]:


my_avg(1,2,3,4,5) 


# In[50]:


sum([1,2,3,4,5])/4


# 튜플 언패킹(unpacking)시 한 변수가 여러 값을 받고 싶다면?

# In[51]:


a, b, c = (1,2,3)
a, b, c


# In[52]:


a, *b, c = (1,2,3,4,5)
a, b, c


# In[53]:


a, b, *c = (1,2,3,4,5)
a, b, c


# # try - except (예외처리)
# 
# try 구문 내의 코드를 실행 중 예외가 발생하지 않으면 실행을 완료하고, 예외가 발생하면 except 구문을 실행한다.

# ex) ZeroDivisionError

# In[54]:


10/0  # error


# 위와 같은 예외가 나타났을때 표현하는 방법을 try-except 구문을 사용해보자.

# In[55]:


a = 0
try:
    10/a
except ZeroDivisionError:
    print("0이 입력되었습니다. 다른 값을 넣어주세요.")


# 실행하고자 하는 코드는 10을 입력변수 a로 나누는 연산인데 변수에 0이 입력되어 에러가 발생한다.  
# except에 발생가능한(예상되는) 에러의 이름을 지정해놓고, 실제 try 구문에서 발생한 에러와 일치하면 except가 실행된다.

# 참고) 아래와 같이 지정한 에러명과 실제 발생한 에러명이 다를 경우 except 구문은 실행되지 않는다.

# In[56]:


a = 0
try:
    10/a
except ValueError:
    print("0이 입력되었습니다. 다른 값을 넣어주세요.")


# ### 여러개의 예외 처리

# In[57]:


try:
    a = [1,2]
    print(a[3])
    4/0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except IndexError:
    print("인덱싱 할 수 없습니다.")


# try 구문의 실행 중 인덱스에러가 먼저 발생하므로 코드를 더 실행하지 않고 except를 실행한다.

# ### try-except는 왜 필요한 것인가?
# - 프로그램이 바로 예외로 인해 종료되지 않고, 예외 발생시 적절한 처리를 해둠으로써 프로그램이 계속 진행되도록 할 수 있다.
# - 사용자에게 알려주어 프로그램의 정상 진행을 유도할 수 있다.

# In[58]:


b = 10
a = 5
res = []
for i in range(a, -1, -1):
    try:
        res.append(b/i)
        print("현재 가치 {}".format(b/i))
    except ZeroDivisionError:
        a = 5
        print("최대치에 도달하여 값을 초기화 했습니다.")


# ### raise의 사용 (ValueError)

# In[59]:


def test(a,b):
    pocket = ['money', 'card', 'cash']
    if a not in pocket:
        raise ValueError
    if b not in pocket:
        raise ValueError
    print("성공")
    
try:
    test('money', 'book')
except ValueError:
    print("잘못된 값을 넣었습니다!")


# -> 첫번째 if에서는 True, 두번째 if에서는 False. => ValueError 발생시킴 (raise).

# # 소수점 처리
# - `np.round()` : 반올림
# - `np.ceil()` : 올림
# - `np.floor()` : 내림
# - `np.trunc()` : 버림
# - 문자열 포매팅

# In[63]:


import numpy as np
import math # math에도 round, ceil, floor, trunc 기능 있다.


# In[68]:


a = 1234.56778
print("소수점 2번째 자리까지 반올림:", np.round(a,2))
print("소수점 0번째 자리까지 반올림:", np.round(a,0))


# **올림**
# 
# The ceil of the scalar x is the smallest integer i, such that i >= x. -> 정수로 반환되므로 소수점 자리 지정 X

# In[69]:


np.ceil(a)


# **내림**
# 
# Return the floor of x as an integral. This is the largest integer <= x. -> 정수로 반환되므로 소수점 자리 지정 X

# In[70]:


np.floor(a)


# **버림**
# 
# The truncated value of the scalar x is the nearest integer i which is closer to zero than x is.

# In[71]:


np.trunc(a)


# **[생각해보기]**
# 
# floor와 trunc의 차이점: trunc는 0과 가까운. floor는 scalar보다 작은 정수 중 큰 것

# In[72]:


np.trunc(-1.42)


# In[73]:


np.floor(-1.42)


# # 연습문제

# 1.여러 값을 매개변수로 받아 그 중 3이상의 값의 합계를 (n-1)로 나눈 값을 구하는 UDF 작성  
# 전달할 여러 값:  
# 1-1) 1,4,5,2,8,4,6,2,9  
# 1-2) 1$\sim$9까지의 정수 3묶음 리스트 ([1~9]*3)

# In[85]:


def temp_avg(*args):
    tmp = [a for a in args if a >= 3]
    return sum(tmp)/(len(tmp)-1)

temp_avg(1,4,5,2,8,4,6,2,9)


# In[5]:


def temp_avg1(args):
    tmp = [a for a in args if a >= 3]
    return sum(tmp)/(len(tmp)-1) 

temp_data = list(range(1,10))*3
temp_avg1(temp_data)


# In[8]:


# 1-1
def temp_avg(*num):
    temp_list = [n for n in list(num) if n>=3]
    avg = sum(temp_list) / (len(temp_list)-1)
    return avg

print(temp_avg(1,4,5,2,8,4,6,2,9))

# 1-2
def temp_avg1(x):
    temp_list = [num for num in x if num >= 3]
    avg = sum(temp_list) / (len(temp_list)-1)
    return avg

print(temp_avg1(temp_data))


# 2.값을 초기화하기 위한 initiation() 메서드를 FourCal1 클래스에 구현하세요. (단, initiation 메서드 실행시 초기화된 결과값(0)은 반환할 필요가 없고, '초기화 완료'라는 메시지를 출력하세요.)

# In[98]:


class FourCal1:
    def initiation(self):
        self.initiation = 0
        print('초기화완료')


# In[99]:


cc = FourCal1()


# In[100]:


cc.initiation()


# In[9]:


# 
class FourCal1:
    def __init__(self):
        self.init = 0
        
    def adding(self, num):
        """
        simple calculator for adding
        ----------
        Parameter:
            num: int or float
        """
        assert num % 2 == 0, 'error: input is odd number'
        self.init += num
        return self.init
    
    def initiation(self):
        self.init = 0
        print('초기화 완료')


# 3.세개의 숫자를 인수로 받아서 첫번째 수를 밑으로 두번째, 세번째 숫자를 지수로 하여 그 숫자들의 범위만큼 지수 연산을 수행한 결과를 리스트로 반환하는 UDF를 구현하고 모듈화한 후 import하여 사용해보세요.  
# <조건>  
# func(2,1,5) -> [2,4,8,16,32]  
# func(3,3,1) -> [3,9,27]

# In[121]:


def func(*a):
    try:
        if a[2] > a[1] :
            c = [a[0] ** b for b in list(range(a[1],a[2]+1))]
        else:
            c = [a[0] ** b for b in list(range(a[2],a[1]+1))]
        return c
    except TypeError:
        print("잘못 입력하였습니다. 정수를 입력하세요.")


# In[122]:


func(2,1,5) 


# In[123]:


func(3,3,1) 


# In[124]:


func(3,3,1.5)


# In[10]:


#
def exponen(x, a, b):
    assert (type(x)==int) & (type(a)==int) & (type(b)==int), 'input not integer'
    if b>a:
        result = [x**i for i in range(a, b+1)]
    else:
        result = [x**i for i in range(b, a+1)]
    return result

exponen(3, 3, 1)


# 4.아래와 같은 records 데이터가 있을 때, 'a'이면 각 요소의 개수를 리스트로 저장하고, 'b'이면 최소값을 리스트로 저장해보세요. 

# In[11]:


records = [('a',2,4),
           ('b',4,5,7,1),
           ('a',4,7,9),
           ('b',6,8,3)] 


# In[148]:


a_length = []
b_min = []

for i in range(0,len(records)):
    t1, *t2 = records[i]
    if t1 == 'a':
        a_length.append(len(t2)) 
    else:
        b_min.append(min(t2))


# In[149]:


a_length


# In[150]:


b_min


# In[12]:


#
a_length = []
b_min = []
for tag, *args in records:
    if tag == 'a':
        a_length.append(len(args))
    elif tag == 'b':
        b_min.append(min(args))
        
print(a_length, b_min)


# 5.  
# 1) stock.txt 파일을 불러와서 순서대로 'company', 'share', 'price'의 키 이름을 가지는 딕셔너리를 생성해보세요. (단, share와 value는 각각 정수, 실수로 생성)  
# 2) 1)의 딕셔너리에 'AMZ' 200, 420.8을 추가해보세요.

# In[83]:


f = open("../examples/stock.txt", 'r')
stock = f.readlines()
f.close()
stock


# In[86]:


a = stock[0].strip().split(',')
b = list(map(int, stock[1].strip().split(',')))
c = [float(i) for i in stock[2].strip().split(',')]


# In[87]:


stock1 = {'company': a, 'share': b, 'price': c}
stock1


# In[252]:


stock1['company'].append('AMZ')
stock1['share'].append(200)
stock1['price'].append(420.8)

stock1


# In[16]:


#
with open('../examples/stock.txt', 'r') as f:
    stock = f.readlines()

import re
pattern = re.compile(r'\n')

stock1 = []
for i in range(0, len(stock)):
    stock1.append(re.sub(r'\n', "", stock[i]))
    
stock2 = {'company' : stock1[0].split(','),
          'share' : list(map(int, (stock1[1].split(',')))),
          'price' : list(map(float, (stock1[2].split(','))))
         }

stock2['company'].append('AMZ')
stock2['share'].append(200)
stock2['price'].append(420.8)

stock2


# 6.input()을 이용하여 임의의 단어를 입력받아 리스트로 반환하는 UDF를 작성해보세요.

# In[80]:


def words():
    return input().split(',')


# In[81]:


a = words()


# In[82]:


print(a)


# In[18]:


#
def words():
    x = input()
    words = []
    words.append(x)
    return words

a = words()
b = a[0].split(',')
b = a[0].replace(" ","").split(",")
b


# 7.교재 p.195

# In[63]:


score = list(map(int, input().split()))

if False in [s >= 0 and s <= 100 for s in score]:
    print("잘못된 점수")
else:
    if sum(score)/4 >= 80:
        print("합격")
    else:
        print("불합격")
    


# In[ ]:


if 0<=score[0]<=100 and 0<=score[1]<=100 and 0<=score[2]<=100 and 0<=score[3]<=100:
    if sum(score)/4 >= 80:
        print('합격')
    else:
        print('불합격')
else:
    print('잘못된 점수')


# In[26]:


a = [82, 72, 93, 82]
if sum(a)/4 >= 80:
    print("합격")
else:
    print("불합격")


# In[17]:


a


# In[19]:


# 조건을 만족하는 코드
def judge1():
    x = input()
    xx = list(map(int, x.split(",")))
    a = xx[0]
    b = xx[1]
    c = xx[2]
    d = xx[3]
    
    if a>100 or b>100 or c>100 or d>100:
        print("잘못된 점수")
    elif ((a+b+c+d)/4) >= 80:
        print('합격')
    else:
        print('불합격')


# In[20]:


# assertion error 삽입
def judge2():
    x = input()
    xx = list(map(int, x.split(',')))
    assert len(xx) == 4, '4개의 값을 입력하세요'
    a = xx[0]
    b = xx[1]
    c = xx[2]
    d = xx[3]
    
    if a>100 or b>100 or c>100 or d>100:
        print('잘못된 점수')
    elif ((a+b+c+d)/4) >= 80:
        print('합격')
    else:
        print('불합격')


# In[ ]:


# 예외처리 적용
try:
    x = input()
    xx = list(map(int, x.split(',')))
    
    a = xx[0]
    b = xx[1]
    c = xx[2]
    d = xx[3]
    
    if a>100 or b>100 or c>100 or d>100:
        print('잘못된 점수')
    elif ((a+b+c+d)/4) >= 80:
        print('합격')
    else:
        print('불합격')
except IndexError: print('오류: 4개의 값을 입력해주세요')

