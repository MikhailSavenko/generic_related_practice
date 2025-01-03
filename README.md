# Управление контентом с использованием Generic Related

## Описание проекта

Данный проект создан в рамках изучения темы Generic Relations и ContentType framework.

Проект включает три модели, связанные с использованием GenericForeignKey и Generic Related. Добавлены вьюсеты и конечные точки для обеспечения функциональности. Пользователь может добавлять два различных типа сущностей в избранное.

Проект имеет настройки БД PostgreSQL. В settings есть возможность раскомментрировать настройки Database и оставит стандартный SQLite.
## Возможности

-Реализация трёх моделей со связью через GenericForeignKey и Generic Related.

-Добавление вьюсетов и конечных точек для доступа и манипуляции данными.

-Функционал для добавления пользователем двух типов сущностей в избранное.

## Установка

1. Клонируйте репозиторий:
    ```sh
    git clone https://github.com/MikhailSavenko/generic_related_practice.git
    cd generic_related_practice
    ```
2. Установите необходимые зависимости:
    ```sh
    pip install -r requirements.txt
    ```
3. Выполните миграции:
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```
4. Запустите сервер разработки:
    ```sh
    python manage.py runserver
    ```

## Использование

Для доступа к конечным точкам API перейдите по адресу:

http://localhost:8000/

Вы можете использовать инструменты, такие как Postman или cURL, чтобы взаимодействовать с API.