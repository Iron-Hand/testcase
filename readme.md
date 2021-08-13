Запуск осуществляется с помощью скрипта start.sh

Методы:
/api/ping - работает без параметров

/api/status - в качестве параметра передаем uuid счета в ссылке (например: /api/status/5597cc3d-c948-48a0-b711-393edf20d9c0) возвращает состояние счета в формате json

/api/substract и /api/add  - на вход передаем post запросом uuid счета и amount (сумма зачисления или списания соответственно) в формате json (
например: {
    "uuid": "5597cc3d-c948-48a0-b711-393edf20d9c0",
    "amount": "1.00"
}