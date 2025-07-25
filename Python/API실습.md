# 날씨 정보 받아오기
## 목표
파이썬으로 인터넷에 있는 날씨 정보를 가져와 내가 원하는 정보만 출력
## 전문용어 이해하기
* 서버: 부탁을 받으면 처리해주거나, 부탁대로 원하는 값을 돌려주는 역할
* 클라이언트: 부탁하는 역할

> 클라이언트가 서버에 요청하는 두 가지 방법
> 1) 웹 브라우저(크롬)을 켜서 주소창에 주소(URL)을 입력
> 2) 서버에 정보를 요청하는 파이썬 코드 작성

* 예시 URL =  https://fakestoreapi.com/carts

```python
import requests

url = 'https://fakestoreapi.com/carts'
data = requests.get(url).json() # requests.get(url): 해당 서버(url)에 데이터를 달라고 요청을 보내는 함수
# .json(): 내부의 데이터를 JSON(파이썬 딕셔너리와 비슷) 형태로 변환해주는 함수
print(data)
"""
[{'id': 1, 'userId': 1, 'date': '2020-03-02T00:00:00.000Z', 'products': [{'productId': 1, 'quantity': 4}, {'productId': 2, 'quantity': 1}, {'productId': 3, 'quantity': 6}], '__v': 0}, {'id': 2, 'userId': 1, 'date': '2020-01-02T00:00:00.000Z', 'products': [{'productId': 2, 'quantity': 4}, {'productId': 1, 'quantity': 10}, {'productId': 5, 'quantity': 2}], '__v': 0}, {'id': 3, 'userId': 2, 'date': '2020-03-01T00:00:00.000Z', 'products': [{'productId': 1, 'quantity': 2}, {'productId': 9, 'quantity': 1}], '__v': 0}, {'id': 4, 'userId': 3, 'date': '2020-01-01T00:00:00.000Z', 'products': [{'productId': 1, 'quantity': 4}], '__v': 0}, {'id': 5, 'userId': 3, 'date': '2020-03-01T00:00:00.000Z', 'products': [{'productId': 7, 'quantity': 1}, {'productId': 8, 'quantity': 1}], '__v': 0}, {'id': 6, 'userId': 4, 'date': '2020-03-01T00:00:00.000Z', 'products': [{'productId': 10, 'quantity': 2}, {'productId': 12, 'quantity': 3}], '__v': 0}, {'id': 7, 'userId': 8, 'date': '2020-03-01T00:00:00.000Z', 'products': [{'productId': 18, 'quantity': 1}], '__v': 0}]
"""
```
## API
* 클라이언트가 원하는 기능을 수행하기 위해서 서버 측에 만들어 놓은 프로그램
  * 기능 예시: 데이터 저장, 조회, 수정, 삭제 등등
* 서버 측에 특정 주소로 요청이 오면 정해진 기능을 수행하는 API를 미리 만들어 둠
  * 클라이언트는 서버가 만들어 놓은 주소로 요청을 보냄

## 날씨 정보를 제공해주는 API
> 찾아야 할 것
> 1) 날씨 정보를 가지고 있는 서버
> 2) 해당 서버가 제공하는 API

### 오픈 API
* 외부에서 사용할 수 있도록 무료로 개방된 API
* 사용법은 공식 문서에 ..
* 프로젝트에서 사용되는 API
  * OpenWeatherMap API: 기상 데이터 및 날씨 정보를 제공하는 오픈 API
  * 금융상품통합비교공시 API: 금융감독원에서 제공하는 금융 상품 정보를 제공하는 오픈 API

> #### 특징 및 주의사항
> * API KEY를 활용하여 사용자를 확인함
>   * 사용자 인증 혹은 회원가입을 하면 서버에서 API KEY를 발급해줌
>   * 서버에 요청할 때 마다 해당 API KEY를 함께 보내 정상적인 사용자인 것을 확인 받음
> * 일부 오픈 API는 사용량이 제한되어 있음

## JSON
* JavaScript Object Notation 의 약자. 직역하면 '자바스크립트 객체 표기법'
* 데이터를 저장하거나 전송할 때 많이 사용되는 경량의 텍스트 기반의 데이터 형식
* 통신 방법이나 프로그래밍 문법이 아니라 단순히 데이터를 표현하는 표현 방법 중 하나
* 특징
  * 데이터는 중괄호({}) 로 둘러싸인 키-값 쌍의 집합으로 표현됨
  * 키 = 문자열 / 값 = 다양한 데이터 유형을 가질 수 있음
  * 값은 쉼표(,)로 구분됨
* Python은 JSON을 활용하는 기능을 가지고 있음
  * 참고
    * 파싱(Parsing): 데이터를 의미 있는 구조로 분석하고 해석하는 과정
    * json.loads(): JSON 형식의 문자열을 파싱하여 python Dictionary로 변환

## OpenWeatherMap API
* 기상 데이터 및 날씨 정보를 제공하는 오픈 API
* 전세계 날씨 데이터를 가져와 날씨, 일일 및 시간 별 예보 등 다양한 정보를 얻을 수 있음
* API 사용량 제한
  * 60 calls/minute
  * 1,000,000 calls/month