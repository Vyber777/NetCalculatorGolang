# NetCalculatorGolang
Проект для Спринта 1 от [Яндекса](https://lms.yandex.ru/) :smile:

Он предстваляет собой модифицированную с учетом новых знаний версию проекта калькулятора арифметических выражений, сделанную мной ранее для предыдущего спринта  
Как и старый проект калькулятора, он умеет:
- Считать выражения переданные пользователем
- Понимать и учитывать приоритет с помощью скобок
- Работать с основными арифметическими действиями

Но в отличии от старого, он работает как сервер в сети, который может вычислять выражения через запрос, что конечно же намного лучше

## Как пользоваться?

Для запуска сервера в своей локальной сети нужно скачать файл *main.go* и запустить его.  
Например вот так:  
**go run ПУТЬ\ДО\СКАЧАННОГО\ФАЙЛА\main.go**  

После запуска сервера, вы можете снова открыть консоль и воспользоваться cURL для теста:  

**curl -X POST -H "Content-Type: application/json" -d "{\"expression\": \"*ВМЕСТО ЭТОГО ТЕКСТА ВЫРАЖЕНИЕ*\"}" "http://localhost:8000/api/v1/calculate"**

Если вдруг у вас не имееется *curl*, то вы всегда можете его скачать)))

## Что-то непонятно и нужна помощь или уточнения?

Вы всегда можете мне написать на почту (скорость ответа не гарантирована):  
    **vyber777@gmail.com**
Либо найти меня в Телеграм (тут будет быстрее):
    **@Velan0_0**