# NetCalculatorGolang
Проект для Спринта 1 от Яндекса :smile:

Он предстваляет собой модифицированную с учетом новых знаний версию проекта для предыдущего спринта  
Как и старый проект калькулятора, он умеет:
- Считать выражения переданные пользователем
- Понимать и учитывать приоритет с помощью скобок
- Работать с основными арифметическими действиями

Но в отличии от старого, он работает как сервер в сети, который может вычислять выражения через запрос, что конечно же намного лучше

## Как пользоваться?

go run D:\IDZ\Го\calc\NetCalculatorGolang\main.go

После запуска сервера, вы можете снова открыть консоль и воспользоваться cURL для теста:  
'''curl -X POST -H "Content-Type: application/json" -d "{\"expression\": ВМЕСТО ЭТОГО ТЕКСТА ВЫРАЖЕНИЕ\"\"}" "http://localhost:8000/api/v1/calculate"'''