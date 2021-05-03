#!/usr/bin/env python
# coding: utf-8

# # 정규표현식
# - official document : https://docs.python.org/3/library/re.html (영어) / https://docs.python.org/ko/3/howto/regex.html (한글)

# In[1]:


import re


# ## 문자열의 분리: re.split()
# 'name : ykhong, age = 20; major/engineering'  
# 위와 같이 구분자가 일정하지 않은 경우 문자열을 분리하기 쉽지 않다.  
# -> 정규표현식의 split() 사용

# In[2]:


line = 'name : ykhong, age = 20; major/engineering'


# In[7]:


line.split(":,")  # 처리가 잘 안됨.


# #### 1) 분리
# 문자열 첫 문장부호인 콜론으로 분리해보면 아래와 같이 name과 나머지로 분리된다.

# In[8]:


re.split(':', line)


# #### 2) 콜론과 쉼표 (:,) 분리

# In[10]:


re.split(':,',line)  # -> ';,'를 찾아 분리하므로 잘 안됨.


# 방법 1: [] 사용  -> []안에 있는 각각의 요소들로 분리  
# 방법 2: | 사용

# In[15]:


# 방법1
re.split('[:,;=/]', line)  


# In[16]:


# 방법2
re.split(':|,|;|=|/',line)


# **※ 생각해보기**  
# 
# name 다음에 콜론이 2개 연속 붙어 있는 경우 어떤 패턴을 적용하는 것이 좋을까?  
# 
# line2 = 'name :: ykhong, age = 20; major/engineering'

# In[18]:


line2 = 'name :: ykhong, age = 20; major/engineering'


# In[23]:


re.split('[::,=;/]',line2)


# 콜론 2개를 붙여 [::.=;/]를 적용한다고 해도 대괄호 안은 or이기 때문에 결과는 같다.

# In[24]:


re.split('[:+,=;/]',line2) 


# +를 이용해 :+를 적용해도 마찬가지의 결과가 발생한다.  
# 대괄호 안에서 ::으로 인식되는 것이 아니라 + 기호 역시 찾아야 하는 구분자일 뿐이다.

# In[33]:


re.split(':+',line2)


# In[38]:


# 방법1
re.split('::|,|=|;|/',line2)


# In[44]:


# 방법2
print(re.sub('::',':',line2)) # replace
print(re.split('[:,=;/]',re.sub('::',':',line2)))


# #### 4) \s 사용
# - whitespace 문자 1개와 매치
# - 1칸의 whitespace를 구분자로 하여 분리시킨다. 따라서 whitespace를 없애는 효과가 있다.

# In[49]:


re.split('\s', 'name : ykhong, age = 20; major/engineering') 


# In[50]:


re.split('\s','name :  ykhong, age = 20; major/engineering')   # whitespace가 2개 들어가 있는 경우


# In[52]:


re.split('\s+','name :  ykhong, age = 20; major/engineering')  # whitespace가 2개 들어가 있어도 잘 분리


# - \s 역시 활용 가능할 것으로 판단되니 패턴에 추가해서 적용해보자

# In[53]:


re.split('[:,=;/\s]','name : ykhong, age = 20; major/engineering')


# 오히려 빈문자열이 대량 발생하며 오히려 처리하기 더 불편  
# 
# why?  
# - whitespace마다 끊어줘서 

# **※ 생각해보기**
# 
# 아래와 같은 output에서 empty string은 어떻게 제거할까?

# In[56]:


re.split('[:,=;/\s]', 'name : ykhong, age = 20; major/engineering') 


# - 방법1

# In[60]:


bool("")


# In[61]:


temp = re.split('[:,=;/\s]', 'name : ykhong, age = 20; major/engineering') 
result = [word for word in temp if bool(word) is True]
result


# - 방법2

# In[65]:


list(filter(None, temp)) 


# ### 동일한 패턴을 반복해서 수행하는 경우 패턴을 계속적으로 만들어 적용하면 매우 불편

# #### [패턴 컴파일]: re.compile

# In[66]:


pattern = re.compile("[:,=;/\s]")


# In[67]:


re.split(pattern, line) 


# In[68]:


pattern.split(line) 


# ### Quiz
# 
# ex = 'name : ykhong, age = 20; major/engineering hobby none'
# 
# 위 데이터를 처리하고 name, age, major, hobby를 key로 가지는 dict로 변환해보세요.

# In[69]:


ex = 'name : ykhong, age = 20; major/engineering hobby none'


# In[88]:


temp = list(filter(None,re.split('[:,=;/\s]',ex)))
temp


# In[97]:


temp_key = temp[::2] 
temp_value = temp[1::2]


# In[102]:


print(temp_key) 
print(temp_value)


# In[109]:


result = {key:value for key, value in zip(temp_key, temp_value)}
result


# ## 문자열 처음, 끝 간단 매칭

# In[111]:


ex.startswith('name')


# In[113]:


ex.endswith('.txt')


# ### 매칭의 활용: 특정 폴더 내 파일 검색 등
# 

# In[122]:


import os
filenames = os.listdir('../examples')
filenames 


# In[125]:


files = [file for file in filenames if file.endswith('.txt')]
files


# In[136]:


def read_files(loc, x):
    loc = loc+'/'+x
    with open(loc, 'r') as f:
        content = f.readlines()
    return content


# In[138]:


content = []
loc = '../examples'
for file in files:
    content.append(read_files(loc, file))


# In[139]:


a, b = content


# In[140]:


a


# In[141]:


b


# ## 텍스트 패턴 매칭
# - re.match(pattern, string)
# 
# 간단한 매칭을 하려면 위와 같이 문자열 메소드로 충분하지만 패턴이 복잡해지면 마찬가지로 정규표현식을 활용한다.

# In[143]:


date = '4/27/2021'


# 숫자를 의미하는 [0-9]를 적용하면 첫번째 숫자 4를 매칭한다.  
# 매칭한 value에 0번 인덱스로 접근

# In[150]:


re.match('[0-9]',date) 


# In[151]:


re.match('[0-9]',date)[0] 


# 마찬가지로 \d의 패턴을 사용할 수 있다.

# In[161]:


re.match('\d', '19')  # 처음 매칭되는 숫자 하나만 나온다.


# In[162]:


re.match('\d+', '19') 


# 이어서 월/일까지 매칭하고 밸류를 추출해보자.

# In[165]:


re.match('\d/\d',date) # 0/0 의 형식과 일치한거 찾기


# In[166]:


re.match('\d/\d',date)[0] 


# **※ +의 사용**
# 
# '\d/\d'의 패턴을 사용했을 때 원하는 결과가 아닌 4/2만 추출된다. 매칭되는 숫자가 한 개만 나오기 때문.

# In[168]:


re.match('\d+/\d+/\d+',date)[0] 


# In[171]:


re.match('\d+/\d+/\d+','4월/27/2021')  # 결과가 안나옴. '숫자/숫자/숫자' 형식과 일치 하지 않기 때문


# **※ 활용**  
# text = '오늘은 4/27/2021. 어제는 4/26/2021'

# In[172]:


text = '오늘은 4/27/2021. 어제는 4/26/2021'


# In[174]:


print(re.match('\d+/\d+/\d+', text)) 


# re.match를 이용할 경우 아무런 결과를 볼 수가 없다.  
# re.match는 문자열 처음에서 매칭을 찾기 때문이다.  
# 프린트 문을 이용해보면 아무런 결과 없음을 알 수 있다.  
# 
# 문자열 전체에서 해당 패턴을 찾고자 하면 `re.findall()`을 사용한다.

# In[176]:


p = re.compile('\d+/\d+/\d+')  # 숫자/숫자/숫자 형태를 compile 저장


# In[178]:


p.findall(text)                # 문자열 전체에서 숫자/숫자/숫자 형태를 가진 것을 찾아준다.


# In[181]:


re.findall('[가-힣]', text) 


# In[180]:


re.findall('[가-힣]+', text) 


# In[183]:


re.findall('[가-힣ㅋ]+', (text+'ㅋㄷ')) 


# In[184]:


re.findall('[가-힣ㅋㄷ]+', (text+'ㅋㄷ')) 


# In[186]:


re.findall('[가-힣ㄱ-ㅎ]+', (text+'ㅋㄷ')) 


# ### Quiz
# 
# 위의 결과를 바탕으로 월, 일, 년을 모두 분리하고 2차원 리스트로 구성해보세요.
# 
# 목표: [['4','27','2021'],['4','26','2021']]

# In[204]:


d = re.findall('\d+/\d+/\d+',text)


# In[210]:


[i.split('/') for i in d] 


# # numpy
# 넘파이는 빠르고 효율적인 계산을 위해 만들어진 라이브러리이다. 고성능의 다차원 배열 객체를 계산할 효율적인 도구를 제공한다. 넘파이의 핵심은 ndarray 객체이다. 동일한 자료형을 가지는 n차원의 배열을 기본으로 한다.

# In[212]:


import numpy as np


# In[213]:


a = np.array([[1,2,3],[4,5,6]])


# In[214]:


a


# In[215]:


a.ndim    # axis(축)의 수 변환


# In[217]:


a.shape   # 행 x 열  


# In[218]:


a.dtype


# In[219]:


b = np.array([
    [[1,2,3],[4,5,6]],
    [[7,8,9],[10,11,12]]
])


# In[220]:


b.ndim


# In[221]:


b.shape     # 깊이, 행, 렬


# In[223]:


bb = np.array([[[1,2,3],[4,5,6]],
              [[7,8,9],[10,11,12]],
              [[13,14,15],[16,17,18]]])


# In[224]:


bb.shape


# In[226]:


# 넘파이 기본 계산
a = np.array([1,2,3])
b = np.array([10,20,30])


# In[227]:


a+b  # 요소별 합


# In[228]:


np.add(a,b)  # 요소별 합


# In[229]:


b-a  # 요소별 차


# In[230]:


a ** 2 # 제곱 연산


# In[231]:


a*b   # 요소별 곱


# In[232]:


a/b  # 요소별 나누기


# In[233]:


b < 15


# ## 축을 기준으로 한 연산

# 2차원인 경우  axis = 0 (행) / axis = 1 (열)

# In[234]:


c = np.array([[1,2,3], [4,5,6]])


# In[235]:


# 행방향 (0) 
c.sum(axis = 0)    # 각 열의 행끼리 계산


# In[236]:


# 열방향 (1)
c.sum(axis = 1)    # 각 행의 열끼리 계산


# 3차원인 경우 axis = 0 (깊이) / axis = 1 (행) / axis = 2 (열)

# In[237]:


d = np.array([[[1,2,3],[4,5,6]],
              [[7,8,9],[10,11,12]]])


# In[239]:


d.shape


# In[240]:


d.sum(axis = 0) 


# In[241]:


d.sum(axis = 1) 


# In[242]:


d.sum(axis = 2) 


# ## 넘파이 _______
# - 넘파이의 일차운 배열의 경우 파이썬 리스트 자료형의 방법과 매우 유사
# - 다차원 배열은 축을 기준으로 함

# In[247]:


# 1차원
e = np.array([1,2,3,4,5,6,7])


# In[244]:


e[0] 


# In[245]:


e[-1] 


# In[246]:


e[:3] 


# In[248]:


# 2차원
f = np.array([[1,2,3],[4,5,6],[7,8,9]])


# In[249]:


f[0,2]


# In[250]:


f[1:,0]


# In[251]:


f[:,1]


# In[252]:


f[0][2] 


# In[253]:


d[0,0,1] 


# In[256]:


d[0][0][1] 


# In[257]:


# 2차원 형태 그대로 추출
f[:, np.newaxis, 1] 


# ### ravel(), reshape(), T

# In[258]:


# 배열 형태 변환
g = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) 


# In[259]:


# 1차원으로 쭉 폄 -> np.ravel()
g.ravel() 


# In[260]:


# shape을 바꿔줌
g.reshape(2,6) 


# In[261]:


# 전치행렬  (Transpose) 
g.T


# # 연습문제
# 
# 데이터는 1000개의 날짜를 포함하고 있습니다. 데이터를 조사하고 날짜 데이터가 정상적이지 않다면, 정상적이지 않은 데이터의 인덱스를 확인하고, 해당 데이터를 추출해보세요.

# In[315]:


f = open('C:/study_bigdata/study/examples/date2.csv', 'r')
lines = f.readlines()
f.close()

date = lines[0].split(',')

tmp = [bool(re.match('\d+/\d+/\d+', da)) for da in date]

idx = [a for a,b in enumerate(tmp) if b==False]
np.array(date)[idx]


# In[ ]:




