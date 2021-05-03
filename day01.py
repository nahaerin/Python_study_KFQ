#!/usr/bin/env python
# coding: utf-8

# # DAY01. 자료형 / 자료구조
# - 숫자, 문자열
# - 리스트, 딕셔너리, 튜플, 집합

# In[359]:


120 #숫자


# In[360]:


True #논리값


# In[361]:


'a' #문자열


# ## 1. 숫자형 자료형 (연산자)

# In[362]:


a = 120
b = 40

print("나누기 :", a/b)
print("몫 :", a//b)
print("나머지 :", a%b)
print("제곱 :", a**2)


# In[363]:


int(3.5)    #정수형
float(3.5)  #실수형


# In[364]:


a = 5
type(a)


# In[365]:


b = 3.7
type(b)


# ## 2. 문자열

# In[366]:


string = "I am Sam"
type(string)


# #### 문자열 안에 ' 표시하는 방법

# In[367]:


"""Life is too short, You need python"""


# In[368]:


'''Life is too short, You need python'''


# In[369]:


"She is Paul's friend"


# In[370]:


'She is Paul\'s friend'


# In[371]:


'"Python is very easy." he says.'


# In[372]:


"\"Python is very easy.\" he says."


# #### 개행 (줄 바꾸기) -> \n

# In[373]:


multiline = "I am Sam \n\ho is this"
print(multiline)


# In[374]:


multiline1 = '''I am Sam 
 Who is this'''
print(multiline1)


# #### 문자열 더하기

# In[375]:


h = "I "
t = 'am Sam '
h + t


# In[376]:


(h + t)*2


# In[377]:


print('='*20)
print('awesome')
print('='*20)


# In[378]:


len(h+t)  # 문자열 길이


# #### 문자열 인덱싱

# In[379]:


d = h+t
print(d)
print(len(d))


# In[380]:


d[0]+d[1]+d[2]+d[3]


# In[381]:


d[-1] # 뒤에서 1미만 자리


# In[382]:


d[-9]+d[-8]+d[-7]+d[-6]


# #### 문자열 슬라이싱

# In[383]:


print(d[:2]) # 2미만 자리
print(d[2:]) # 2초과 자리
print(d[0:4])
print(d[-9:-5])
print(d[2:])
print(d[:4])


# In[384]:


test = '20190727cool'

year = test[:4]
date = test[4:8]
condition = test[8:]

print(year)
print(date)
print(condition)


# In[385]:


test[:-4]+'k'+test[9:]  #문자열 중간 인덱스를 바꾸는 기능은 없음.


# test = [year, date] 위 문자열을 수치형으로 바꾸고 싶다면?
# - 방법 1 : for loop
# - 방법 2 : map()

# In[386]:


test = [year, date]
test


# In[387]:


test[1][1]


# In[388]:


test[0]  # 문자형


# In[389]:


int(test[0]) # 수치형


# In[390]:


int(test[0])+1 # 수치형 연산 가능


# In[391]:


[int(a) for a in test]


# #### 문자열 포매팅

# In[392]:


"I eat %d apples." % 3


# In[393]:


"I eat %s apples." % 5


# In[394]:


"현재 온도는 %d도 입니다" % 20


# In[395]:


"현재 온도는 %s도 입니다" % '이십'


# In[396]:


num = 7
"I eat %d appples." % num


# In[397]:


number = 10
day = 'three'
"I ate %d apples. I was sick for %s days" %(number, day)


# In[398]:


"I ate %d apples. I was sick for %s days" %(number, number)


# In[399]:


# 포매팅에서 %기호를 쓰고 싶을 때
print('probability is 99%')


# In[400]:


f"probability is {99}%"


# In[401]:


"probability is %d" % 99 + "%"


# In[402]:


"probability is %d%%" %99  # %%이라고 입력하면 %로 나온다.


# #### 문자열 정렬 및 공백

# In[403]:


"%10s" % 'hi'  #10자리 공백 뒤 hi 입력


# In[404]:


"%0.4f" % 3.425897   # 뒤에 소수점 4자리


# In[405]:


"%.4f" % 3.425897     # 뒤에 소수점 4자리


# In[406]:


"%10.4f" % 3.425897  # 정수 10자리, 소수점 4자리


# #### format 형식을 이용한 포매팅

# In[407]:


"{}".format(5.22)


# In[408]:


"{:.1f}".format(5.22) # 소수점 1자리


# In[409]:


"{:10.4f}".format(3.425897) # 정수 10자리, 소수점 4자리


# In[410]:


a = "I am {}"


# In[411]:


a.format(20)


# In[412]:


"I ate {} apples. I was sick for {} days.".format(number, day)


# In[413]:


"I ate {number} apples. I was sick for {day} days.".format(number, day)


# In[414]:


"I ate {number} apples. I was sick for {day} days.".format(number=10, day='one')


# #### 인덱스 / 이름 혼용

# In[415]:


day = 3
"I ate {0} apples. so I was sick for {day} days.".format(10, day)


# In[416]:


"I ate {} apples. so I was sick for {} days.".format(10, day)


# In[417]:


"I ate {0} apples. so I was sick for {day} days.".format(10, day=3)


# In[418]:


# 왼쪽 정렬
"{}".format("hi")


# In[419]:


"{:10}".format("hi")


# In[420]:


"{0:>10}".format("hi") #오른쪽 정렬할 때는 > 기호. 왼쪽 정렬할 때는 < 기호.


# In[421]:


"{0:-^10}".format("hi")


# ## 3. 리스트 자료형

# In[422]:


odd = [1,3,5,7,9]
type(odd)


# In[423]:


a = [1,2,'a']
type(a)


# In[424]:


a = []                    # 빈 리스트에
a.extend([1,2,3])         # 값 추가
a


# In[425]:


a.extend([4,5])           # 리스트에 값 추가
a


# In[426]:


a.pop()                   # pop: 꺼내는 함수. (디폴트: 마지막꺼)
a


# In[427]:


a[0]


# In[428]:


a[0]+a[2]


# In[429]:


a[-1]


# In[430]:


a = [1,2,3,['a','b','c']]


# In[431]:


print(a[-1])
print(a[3])


# In[432]:


a[3][0]


# In[433]:


a = [1,2,['a','b',['Life','is']]]


# In[434]:


a[-1][-1][0]


# #### 리스트 슬라이싱

# In[435]:


a = [1,2,3,4,5]


# In[436]:


a[0:2]


# In[437]:


b = a[:2]
b


# In[438]:


c = a[2:]
c


# In[439]:


c.insert(1,2)  # 1번 위치에 2를 넣음
c


# In[440]:


c.insert(0,[1,2])
c


# In[441]:


c.extend([-2,-1])
c


# #### 리스트 연산

# In[442]:


a = [1,2,3]
b = [4,5,6]
a+b


# In[443]:


a = [1,2,3]
a * 3


# In[444]:


str(a[2]) + 'hi'    # str: 문자열 변환


# #### 리스트 수정과 삭제

# In[445]:


a = [1,2,3]
a[2] = 4
a


# In[446]:


a = [1,2,3]
del a[1]
a


# #### 리스트에 요소 추가

# In[447]:


a = [1,2,3]
a.append(4)
a


# In[448]:


a.append([5,6])
a


# In[449]:


a.append(7,8,9)
a


# In[450]:


get_ipython().run_line_magic('pinfo', 'list.append')


# In[451]:


b = [1,4,3,2]
b


# In[452]:


b.sort()    # 오름차순
b


# In[453]:


a = ['a','c','b','d']
a.sort()
a


# In[454]:


a.reverse()   # 내림차순
a


# expend는 리스트 안에 요소를 넣어줌.
# 
# append는 하나의 요소를 넣어줌.
# 
# 상황에 맞게 사용하기.

# ## 4. 튜플
# - 리스트 vs 튜플  
# 리스트 각각의 속성이 동일 할 때 사용하는 경우가 많고 튜플은 각각의 속성이 다를 때 사용하는 경우가 많다.

# In[455]:


t1 = (1,)  # 1개의 자료값 입력시 반드시 , 붙어야 한다
t2 = (2)


# In[456]:


t1


# In[457]:


t2


# In[458]:


type(t1)


# In[459]:


type(t2)


# In[460]:


t2 = (1,2,3)
t2[2] = 4       #자료 요소 변경 불가


# #### tuple unpacking
# - unpacking은 tuple에서만 사용하는 것은 아니다.

# In[461]:


record_tup = ('Seoul', 2021, 10, 9)
record_tup


# In[462]:


city, year, pop, metros = record_tup


# In[463]:


print(city)
print(year)
print(pop)
print(metros)


# 리스트 각각의 속성이 동일 할 때 사용하는 경우가 많고 튜플은 각각의 속성이 다를 때 사용하는 경우가 많다.

# ## 5. 딕셔너리 자료형
# - 키-밸류 구조
# - 순서가 있는 자료구조가 아니므로 key로 자료 접근을 해야한다는 특징이 있다.

# In[464]:


dic = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}


# In[465]:


dic['name']


# In[466]:


dic.keys()


# In[467]:


dic.values()


# In[468]:


list(dic.values())


# In[469]:


a = {1:'hi'}
a[1]


# In[470]:


a = {'a' : [1,2,3]}
a['a']


# In[471]:


c = {1:('a','b')}
c[1]


# In[472]:


a[2] = 'b' # 딕셔너리에 key를 만들면서 value를 넣을 수 있다.
a


# In[473]:


dic = {'name' : 'pey', 'phone':'0119993323', 'birth':'1118'}
del dic['name']        # key 삭제
dic


# In[474]:


for k in dic.keys():
    print(k)


# In[475]:


dic.items()  # key-value 튜플 형식으로 반환


# ## 6. 집합 자료형

# In[476]:


s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])


# #### 교집합

# In[477]:


s1 & s2


# In[478]:


s1.intersection(s2)


# #### 합집합

# In[479]:


s1 | s2


# In[480]:


s1.union(s2)


# #### 차집합

# In[481]:


s1 - s2


# In[482]:


s2 - s1


# In[483]:


s1.difference(s2)


# #### 1개의 값 추가

# In[484]:


s1 = set([1,2,3])
s1.add(4)


# In[485]:


s1


# #### 여러 값 추가

# In[486]:


s1.update([4,5,6])
s1


# #### 값 삭제

# In[487]:


s1.remove(2)
s1


# ## 7. 불(bool) 자료형 : 논리값

# In[488]:


a = True
b = False


# In[489]:


type(a)


# ### 비교연산자 / 논리연산자
# - `==`, `!=`, `>`, `<`, `>=`, `<=`, `&`, `|`, `and`, `or`, `in`

# In[490]:


10 == 10 and 1 != 2


# In[491]:


10 == 10 & 1 != 2


# In[492]:


(10 == 10) & (1 != 2)


# - 비교 연산자 &, and, |, or 사용시 주의가 필요하다.
# - search : python operators precedence (연산자 우선 순위)

# In[493]:


True & False


# In[494]:


True or False


# In[495]:


10 in [1,2,10]


# In[496]:


3 in [1,2,10]


# In[497]:


3 not in [2,4,6]


# In[498]:


a = [1,2,3,4]
while a:
    print(a.pop())
    
a


# ## 8. 기타 문자열 적용 유용 메서드 (strip, split, replace)

# In[499]:


test_str = '     hp010-0000-1111ph     '
print(test_str)


# In[500]:


test_str1 = test_str.strip()
print(test_str1)


# - str.strip() 확장  
# test_str1에서 ph와 hp를 제거하고 싶다면?

# In[501]:


test_str1.rstrip('ph')


# In[502]:


test_str1.lstrip('hp')


# In[503]:


test_str1.rstrip('ph').lstrip('hp')


# In[504]:


test_str2 = test_str1.replace('hp',"")
print(test_str2)


# In[505]:


test_str3 = test_str1.split('-')
print(test_str3)


# ## 9. 연습

# -  a = "a:b:c:d"에서 객체 a의 메서드를 이용하여 a#b#c#d으로 바꿔서 출력해보세요.

# In[506]:


a = "a:b:c:d"
a.replace(':','#')


# - [1,3,5,4,2]를 [5,4,3,2,1]로 만들어 보세요.

# In[507]:


a = [1,3,5,4,2]
a.sort(reverse = True)
a


# -  ['This', 'is', 'awesome'] 리스트를 This is awesome 문자열로 만들어 출력해보세요.

# In[508]:


a = ['This', 'is', 'awesome']
a[0] + ' ' + a[1] + ' ' + a[2]


# In[513]:


a = ['This', 'is', 'awesome']
b = ""
for i in a:
    b += i + " "
b


# -  a = {'A':90, 'B':80, 'C':70}에서 B에 해당하는 값 출력함과 동시에 a 딕트에서 삭제

# In[509]:


a = {'A':90, 'B':80, 'C':70}
a.pop('B')


# In[510]:


a


# - a = [1,1,1,2,2,3,3,3,4,4,5]를 중복 숫자 없이 다음과 같이 만들어 보세요. -> [1,2,3,4,5]

# In[511]:


a = [1,1,1,2,2,3,3,3,4,4,5]
list(set(a))

