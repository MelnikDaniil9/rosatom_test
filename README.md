# Rosatom test

Тестовое задание от Росатома, сделанное Мельник Даниилом

## Клонируйте репозиторий

## Установите зависимости

```
pip install -r requirements.txt
```

## Настройте подключение к PostgreSQL в .config
(пример, используется асинхронная библиотека databases (https://www.encode.io/databases/))
```
POSTGRES=postgresql+asyncpg://postgres:postgrespw@localhost:49154/postgres
```

### Запустите сервер

```
uvicorn main:app --reload
```


PS. min.io не предоставляет доступ гражданам РФ, поэтому реализовать не получилось
бесплатный VPN не помог