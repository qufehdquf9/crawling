# crawling

## Selenium이란?
---
Selenium은 주로 웹앱을 테스트하는데 이용하는 프레임워크다. webdriver라는 API를 통해 운영체제에 설치된 Chrome등의 브라우저를 제어하게 된다.

브라우저를 직접 동작시킨다는 것은 JavaScript를 이용해 비동기적으로 혹은 뒤늦게 불러와지는 컨텐츠들을 가져올 수 있다는 것이다. 즉, ‘눈에 보이는’ 컨텐츠라면 모두 가져올 수 있다는 뜻이다. 우리가 requests에서 사용했던 .text의 경우 브라우저에서 ‘소스보기’를 한 것과 같이 동작하여, JS등을 통해 동적으로 DOM이 변화한 이후의 HTML을 보여주지 않는다. 반면 Selenium은 실제 웹 브라우저가 동작하기 때문에 JS로 렌더링이 완료된 후의 DOM결과물에 접근이 가능하다.

##### 출처
[나만의 웹 크롤러] https://beomi.github.io/2017/02/27/HowToMakeWebCrawler-With-Selenium/