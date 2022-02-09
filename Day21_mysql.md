# TIL(Today I Learned)

___

> Fab/1st/2022_Multi campus_유선종 Day21

## mySQL
오늘은 mySQL의 이론적인 부분에 대해서 알아보고자 한다.

### 1. mySQL? 오라클? 엑세스?
나는 SQL을 접하게 된 계기가 컴퓨터활용능력 1급을 딸때 처음 알게 됐다. 컴활 2급은 엑셀, 컴활 1급은 엑셀과 엑세스였기 때문에 당시 엑세스를 공부하느라 정말 힘들었던 기억이 있다.
> 그런데 MS의 엑세스가 다른 mysql이나 오라클같은 데이터베이스와 비슷한 프로그램이기 때문에 컴활 1급을 공부했던 사람이라면 mySQL도 쉽게 배울 수 있다.
- 그렇다면 mySQL이나 오라클같은 데이터베이스 프로그램은 무슨 역할을 하기에 컴퓨터활용능력에서도 다루는 것일까? 이 프로그램들은 데이터를 저장하는 프로그램이다. 한마디로 저장 공간이다.
- 그런데 왜 우리는 데이터분석을 하는데 데이터베이스에 대해서 배울까? 그 이유는 모든 회사에서 이 데이터베이스 프로그램을 다루기 때문이다.
> 최근에는 클라우드 기반의 AWS를 사용하는 기업들이 늘어나고 있지만, 아직까지도 대부분의 기업들은 데이터베이스 프로그램을 이용해서 데이터를 저장한다.
- 특히 mySQL과 오라클은 기업에서 가장 많이 사용하는 프로그램이다. 오라클이 가장 뛰어나다고 알려져있고, 점유율도 가장 높다. 그러나 비싼 비용을 지불해야하기 때문에 학생의 입장에서는 오라클을 배우기가 힘들다.
- 다행히도 SQL은 표준을 정하여 발표하기 때문에 어떤 프로그램을 사용하더라도 SQL문은 그 표준을 따르고 데이터를 저장하는 구조 또한 비슷하기 때문에 학생이라면 mySQL을 공부해서 현업에 가서는 오라클을 배우면 된다.
___
### 2. DBMS를 이해하려면?
- DBMS(DataBase Management System) 혹은 스키마에 대해 공부하기 위해서는 우리는 그 구조에 대해 알아야 한다.
- DBMS에서는 수많은 데이터를 테이블이라는 형태로 저장하는데, 각각의 데이터는 열 인덱스를 기준으로 데이터를 저장한다. 
  - 예를 들어, 박보영이라는 회원 데이터가 있는데 박보영의 나이는 33살이고 사는 곳은 서울이라는 데이터가 있다고 하자. 그러면 우리는 다음과 같은 표로 저장할 것이다.

| 이름   | 나이 | 지역 |
| ------ | ---- | ---- |
| 박보영 | 33   | 서울 |

> 이러한 테이블은 우리에게 매우 익숙한 형태이다.
- DBMS에서는 열을 컬럼(column), 행을 로우(row)하고 한다. 그리고 이러한 행과 로우로 이루어진 하나의 저장소를 테이블이라고 한다.
- 이러한 테이블이 무수히 모여있을 경우 하나의 DBMS를 이룬다. 각 테이블이 어떤 구조로 연결되어 있느냐에 따라 관계형 DBMS, 객체지향 DBMS, 네트워크 DBMS, 게층형 DMBS로 나뉜다.
> 그러나 가장 많이 사용하는 구조가 관계형 DBMS이므로 관계형만 있다고 봐도 무방한다.
___
### 3. SQL
- SQL(Structured Query Language)은 말 그대로 데이터베이스에서 사용하는 언어이다.
- 테이블 단위로 연산을 수행하고 영어와 비슷한 대화식의 구문으로 되어있다. 표준을 정하기 때문에 한번 익히면 쉽게 이용할 수 있다.
___
### 4. DBMS의 특징
데이터베이스에서는 중요한 특징들이 있다.

#### 1. 데이터의 무결성
- 데이터베이스 안의 데이터는 어떠한 오류가 있어서는 안된다. 이를 데이터 무결성(integrity)이라고 하는데, 이를 위해서 제약조건이 존재한다.
- 데이터베이스에서 데이터무결성을 위해 기본키(key)를 설정한다. 이 기본키가 데이터 무결성을 지켜주는 데이터라고 보면 된다.
- 예를 들어보자.
  - 마트에서 회원등록을 할 때, 보통 그 사람의 나이, 위치, 성별, 카드번호 등 다양한 정보들을 입력하게 되어있다. 그러나 우리가 필수적으로 입력할 필요는 없다.
  -  반면에, 이름을 입력하지 않으면 우리는 입력한 정보가 누구의 정보인지 알기 힘들 것이다. 즉, 여기서 기본키는 이름이 되고 이름을 입력하지 않으면 데이터베이스에 입력할 수 없다.
  - 이름은 무조건 필요한 정보이기 때문에 정보가 없다면 오류가 존재하는 것이다.
- 하지만 여기서 중복된 이름이 존재한다면? 이라는 물음이 떠오른다. 그렇다면 박보영1, 박보영2로 저장할 것인가? 물론 그렇게 구분해도 되지만, 더 좋은 방법은 각자의 회원번호를 부여해서 회원번호를 기본키로 입력하면 된다. 그렇게 하면 중복되는 데이터도 없고 무조건 입력되는 정보이기 때문에 데이터 무결성을 지킬 수 있는 기본키로서의 역할을 한다.
> 데이터 무결성은 DBMS에서 가장 중요한 특징이다. 기본키의 존재유무에 따라 DBMS 구조가 결정되기 때문에 확실하게 이해하자.
___
#### 2. 데이터의 독립성
데이터베이스의 크기를 변경하거나 데이터 파일의 저장소를 변경하더라도 기존에 작성된 응용 프로그램은 아무런 변경이 없이 계속 사용되어야 한다. 즉, 응용 프로그램은 전혀 영향을 받지 않아야 한다.

#### 3. 보안
데이터베이스는 회사의 중요한 데이터이기 때문에 보안에 더더욱 신경써야 한다. 과거에 고객들의 데이터가 유출당한 사례가 종종 있듯이 고객들의 데이터라면 특히 더더욱 신경써야 한다.

#### 4. 데이터 중복의 최소화
DBMS는 중복을 최소화하려 노력하고 실제로 최소화하여 저장하기 때문에 다른 사람들과 공유하기 좋다. 예를 들어, 다른 사원이 작성한 엑셀 데이터라도 DBMS에서 저장하면 중복된 데이터는 통합하여 저장되기 때문에 유용하다.

#### 5. 응용 프로그램 제작 및 수정이 쉬워짐
DBMS는 통일된 방식으로 응용 프로그램 작성이 가능해지고 유지보수가 쉽기 때문에 유용하다.