# Требования к программному продукту

#### Неавторизованный пользователь
*Данную часть системы может видеть пользователь с ролью Гость. Гость может просматривать новости и статистику, аутентифицироваться и регистрироваться.*

| Номер | Описание требования | Статус |
| ------ | ----- | --- |
| R 1.1 | При открытии сайта отображается главная страница приложения `home` | Сделано |
| R 1.2 | В шапке сайта на каждой странице отображаются контакты, виджет авторизации | Сделано |
| R 1.3 | На главной странице отображаются последние новости, статистика | |
| R 1.4 | При нажатии на пункт `Войти` главного меню пользователь направляется на страницу `login` | Сделано |
| R 1.5 | При нажатии на пункт `Регистрация` главного меню пользователь направляется на страницу `register` | Сделано |
| R 1.6 | При нажатии на одну из новостей в списке, происходит переход на страницу полной новости | |

#### Регистрация
*Данная часть системы доступна всем пользователям и предоставляет возможность добавить новую учётную запись со своими данными* 

| Номер | Описание требования | Статус |
| ------ | ----- | --- |
| R 2.1 | Для создания новой учётной записи используется форма на странице `register` | Сделано |
| R 2.2 | Форма для регистрации содержит следующие элементы: <ul><li>Текстовое поле для ввода номера телефона</li><li>Текстовое поле для ввода имени</li><li>Текстовое поле для ввода фамилии</li><li>Текстовое поле для ввода пароля</li><li>Радиокнопки ддя выбора типа пользователя</li><li>Кнопка `Зарегистрироваться` для подтверждения данных</li></ul> | Сделано |
| R 2.3 | Поля телефон и пароль являются обязательными для заполнения | Сделано |
| R 2.4 | Если в поле для ввода телефона введены некорректные данные, появляется сообщение `Неверный формат телефона!` | Сделано |
| R 2.5 | Если пользователь с таким телефоном уже существует, появляется сообщение `Пользователь с таким телефоном уже существует!` | Сделано |
| R 2.6 | Если пароль пользователя слишком простой (в соответствии со стандартными валидаторами), появляется сообщение с деталями ошибки | Сделано |
| R 2.7 | Тип профиля по умолчанию - `Благотворитель` | Сделано |
| R 2.8 | Если данные введены верно, то после нажатия на кнопку `Зарегистрироваться` происходит создание нового пользователя. | Сделано |
| R 2.9 | После успешной регистрации пользователь аутентифицируется автоматически | Сделано |
| R 2.10 | После успешной регистрации пользователь перенаправляется на страницу редактирования профиля | Сделано |

#### Аутентификация
*Данная часть системы доступна всем пользователям и предоставляет возможность выполнить вход в систему* 

| Номер | Описание требования | Статус |
| ------ | --- | --- |
| R 3.1 | Для входа в систему используется форма на странице `login` | Сделано |
| R 3.2 | Если ранее авторизованный пользователь заходит на страницу `login`, то он перенаправляется на главную страницу приложения `home` | |
| R 3.3 | Форма для аутентификации содержит следующие элементы: <ul><li>Текстовое поле для ввода телефона</li><li>Текстовое поле для ввода пароля</li><li>Кнопка `Войти` для подтверждения данных</li></ul> | Сделано |
| R 3.4 | Текстовые поля телефон и пароль являются обязательными для заполнения | Сделано |
| R 3.5 | Если хотя бы одно из полей не заполнено, появляется сообщение `Обязательное поле.` | Сделано |
| R 3.6 | Если пользователь неверно ввёл логин и (или) пароль, появляется сообщение `Пожалуйста, введите правильные телефон и пароль. Оба поля могут быть чувствительны к регистру.`| Сделано |
| R 3.7 | Если пользователь верно ввёл логин и пароль, то происходит вход в систему и он перенаправляется на страницу `home` | Сделано |

### Сторона пользователя
*Здесь описаны общие требования ко всем авторизованным пользователям независимо от типа их учётной записи*

| Номер | Описание требования | Статус |
| ------ | --- | --- |
| R 4.1 | В шапке сайта отображается виджет авторизации, содержащий аватар и полное имя пользователя | Сделано |
| R 4.1.1 | Если у пользователя отсутствует аватар, то на его месте отображается стандартное изображение `no-avatar.jpg` | Сделано |
| R 4.1.2 | Если у пользователя не заполнено одно из полей имя или фамилия, то вместо имени пользователя отображается значение заполненного поля | Сделано |
| R 4.1.3 | Если у пользователя не заполнены поля имя и фамилия, то вместо имени пользователя отображается номер телефона | Сделано |
| R 4.2 | При наведении на виджет, появляется выпадающее меню, содержащее следующие общие пункты: <ul><li>`Профиль`: ссылка на профиль пользователя</li><li>`Настройки`: ссылка на страницу настроек аккаунта</li><li>`Выйти`: кнопка для выхода из учётной записи</li></ul> | Сделано |
| R 4.2.1 | При нажатии на пункт меню, происходит переход на соответствующую страницу | |
| R 4.2.2 | При нажатии на пункт `Выйти` происходит выход из учётной записи и перенаправление на страницу `logout` | Сделано |
| R 4.3 | Профиль пользователя содержит базовую общедоступную информацию о пользователе и кнопку `Редактировать` | |
| R 4.3.1 | При нажатии на кнопку `Редактировать`, появляется форма для редактирования профиля пользователя | |
| R 4.3.2 | Форма для редактирования профиля содержит следующие поля: <ul><li>Текстовое поле для изменения имени</li><li>Текстовое поле для изменения фамилии</li><li>Текстовое поле для изменения телефона</li><li>Поле для загрузки изображения-аватара</li><li>Кнопка `Сохранить` для подтверждения данных</li></ul> | |
| R 4.3.3 | Поле для ввода телефона является обязательным для заполнения | |
| R 4.3.4 | Если одно или несколько обязательных полей не заполнены, появляется сообщение `Все поля обязательны для заполнения`| | 
| R 4.3.5 | При загрузки формы, все поля инициализируются текущими значениями | |
| R 4.3.6 | Если в поле для ввода телефона введены некорректные данные, появляется сообщение `Неверный формат телефона!` | |
| R 4.3.7 | Если в поле для загрузки аватара помещён файл некорректного формата (не изображение), появляется сообщение `Неверный формат изображения!` | |
| R 4.3.8 | Если в поле для загрузки аватара помещён файл размером больше 2МБ, появляется сообщение `Недопустимый размер изображения!` | |
| R 4.4 | Страница настроек содержит форму для редактирования данных учётной записи пользователя | |
| R 4.4.1 | Форма редактирования учётной записи содержит следующие поля: <ul><li>Текстовое поле для ввода старого пароля</li><li>Текстовое поле для ввода нового пароля</li><li>Текстовое поле для подтверждения нового пароля</li><li>Кнопка `Сохранить` для подтверждения данных</li></ul> | |
| R 4.4.2 | Все поля формы обязательны для заполнения | |
| R 4.4.3 | Если хотя бы одно из полей не заполнено, появляется сообщение `Все поля обязательны для заполнения!` | |  
| R 4.4.4 | Если старый пароль не совпадает с текущим паролем учётной записи, появляется сообщение `Текущий пароль введён неверно!`| |
| R 4.4.5 | Если поля для ввода и подтверждения нового пароля содержат разные значения, появляется сообщение `Пароли не совпадают!` | |
| R 4.4.6 | Если все поля заполнены верно, происходит смена пароля для учётной записи пользователя | |

### Сторона пользователя "Семья"
*Данная часть системы доступна пользователям с ролью "Семья"*

| Номер | Описание требования | Статус |
| ------ | --- | --- |
| R 5.1 | В меню пользователя, помимо стандартных, добавлены следующие пункты: <ul><li>`Новая поездка`: ссылка на страницу добавления новой поездки</li><li>`История`: ссылка на страницу со списком поездок</li></ul> | |
| R 5.2 | Страница добавления поездки содержит форму добавления новой поездки | |
| R 5.2.1 | Форма добавления новой поезки содержит следующие поля: <ul><li>Текстовое поле для ввода адреса отправления</li><li>Текстовое поле для ввода адреса назначения</li><li>Поля для ввода даты и времени отправления</li><li>Текстовое поле для ввода дополнительной информации</li><li>Кнопку `Создать` для подтверждения данных</li></ul>| | 
| R 5.2.2 | Все поля формы обязательны для заполнения | |
| R 5.2.3 | Если хотя бы одно из полей не заполнено, появляется сообщение `Все поля обязательны для заполнения!` | | 
| R 5.2.4 | При создании новой поездки, ей присваевается статус `Создана` | |
| R 5.2.5 | После создания новой поездки, отправляется запрос к API службы такси, а поездка получает рассчитанный километраж и статус `На модерации` | |
| R 5.3 | Страница с историей содержит список всех поездок пользователя | |
| R 5.3.1 | Список всех поездок пользователя отображается в виде таблицы с полями: <ul><li>Пункт отправления</li><li>Пункт назначения</li><li>Километраж</li><li>Статус</li></ul>| | 

### Сторона пользователя "Администратор"
*Данная часть системы доступна пользователям с ролью "Администратор"*

| Номер | Описание требования | Статус |
| ------ | --- | --- |
| R 6.1 | В меню пользователя, помимо стандартных, добавлены следующие пункты: <ul><li>`Поездки`: ссылка на страницу со списком поездок</li><li>`Пользователи`: ссылка на страницу со списком пользователей</li></ul> | |
| R 6.2 | Страница с поездками содержит список всех поездок всез пользователей в виде таблицы | |
| R 6.2.1 | Таблица с поездками содержит следующие поля: <ul><li>Пользователь</li><li>Пункт отправления</li><li>Пункт назначения</li><li>Километраж</li><li>Статус</li></ul> | |
| R 6.2.1 | При нажатии на строку с поездкой, открывается страница с деталями поездки | |
| R 6.3 | Страница с пользователями содержит список всех зарегистрированных пользователей в виде таблицы | |
| R 6.3.1 | Таблица с пользователями содержит следующие поля: <ul><li>Телефон</li><li>Полное имя</li><li>Тип</li></ul> | |
| R 6.3.1 | При нажатии на строку с пользователем, открывается страница профиля этого пользователя | |
| R 6.4 | Страница с деталями поездки содерит полную информацию о поездке | |
| R 6.4.1 | Если поездка имеет статус `На модерации`, то дополнительно отображается панель, содержащая кнопки `Подтвердить` и `Отклонить` | |
| R 6.4.2 | При нажатии на кнопку `Подтвердить` статус поездки изменяется на `Подтверждена` | |
| R 6.4.3 | При нажатии на кнопку `Отклонить` статус поездки изменяется на `Отклонена` | |
