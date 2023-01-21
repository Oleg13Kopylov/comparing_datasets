# ELECTRA

Описание вида "название файла – его содержание"

Первая серия экспериментов:

1) **electra_on_hotels_24_december.ipynb**
– модель electra обучается на отзывах об отелях и
обученная модель сохраняется в google drive
2) **electra_on_movies_24_december.ipynb**
– модель electra обучается на отзывах о фильмах и 
обученная модель сохраняется в google drive
3) **electra_loading_model_and_testing_25_december.ipynb**
– результаты тестирования модели electra
(в том числе перекрестная проверка). Обучающая и тестовая
выборки фиксированные.
Модели загружаются из google drive, они уже обучены
(в файлах 1-2).
В конце ноутбука приведен dataframe
с результатами тестирования каждой из моделей electra на 
каждом из датасетов (один датасет с отзывами на отели, 
другой датасет – с отзывами на фильмы).

Вторая серия экспериментов:

4) **electra_on_spam_emails_19_january.ipynb** –
модель electra
обучается определять, является ли электронное письмо спамом
5) **electra_on_spam_sms_19_january.ipynb** –
модель electra
обучается определять, является ли sms спамом
6) **electra_loading_model_and_testing_on_spam_19_january.ipynb** –
– результаты тестирования модели electra
(в том числе перекрестная проверка).

Ссылки на яндекс диск с моделями, которые я обучил:
1) electra, обученная на отзывах на фильмы:
https://disk.yandex.com/d/gdexjz-0XJwqIg
2) electra, обученная на отзывах на отели:
https://disk.yandex.com/d/kPiTG9jUpYwjpg
3) electra, обученная определять спам в электронных письмах:
https://disk.yandex.com/d/W0xYhtxNkWzJsA
4) electra, обученная определять спам в sms:
https://disk.yandex.com/d/dDdK_0lO02eu-g