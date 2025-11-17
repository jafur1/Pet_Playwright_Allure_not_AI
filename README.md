
# Pet Project

Ниже описан полный цикл запуска тестов Playwright и формирования Allure-отчёта.

## Подготовка окружения

1. Активируйте виртуальное окружение:
   ```
   .\venv\Scripts\Activate.ps1
   ```
2. Убедитесь, что Playwright-браузеры установлены (если пропущено):
   ```
   playwright install
   ```

## Запуск тестов

Тесты запускаются в headed-режиме, чтобы можно было записывать видео браузера:
```
pytest --headed
```

Результаты Allure появляются в каталоге `allure-results`.

## Установка Allure Commandline

Если Allure CLI ещё не установлен, скачайте ZIP с релизом и распакуйте, например, в `C:\Tools\allure`.
Для версии `2.29.0`:
```
New-Item -ItemType Directory -Path C:\Tools\allure -Force
Invoke-WebRequest -Uri https://github.com/allure-framework/allure2/releases/download/2.29.0/allure-2.29.0.zip -OutFile C:\Tools\allure\allure.zip
Expand-Archive -Path C:\Tools\allure\allure.zip -DestinationPath C:\Tools\allure -Force
```

Добавьте `C:\Tools\allure\allure-2.29.0\bin` в `PATH` (опционально), либо обращайтесь к `allure.bat` по абсолютному пути.

## Генерация и просмотр отчёта

#### РЕКОМЕНДУЮ УКАЗЫВАТЬ ПОЛНЫЙ ПУТЬ Allure

1. Сгенерируйте HTML-отчёт (удаляет старые данные в `allure-report`):
   ```
   allure.bat generate allure-results --clean -o allure-report
   ```
2. Откройте отчёт в браузере:
   ```
   allure.bat open allure-report
   ```

Команда `open` запустит локальный сервер (Jetty) и выведет URL в консоль.


