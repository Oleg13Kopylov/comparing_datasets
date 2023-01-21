# DistilBERT

Описание вида "название файла – его содержание"

Первая серия экспериментов:

1) **distilbert_on_hotels_25_december.ipynb**
– модель distilbert обучается на отзывах об отелях и
обученная модель сохраняется в google drive
2) **distilbert_on_movies_25_december.ipynb**
– модель distilbert обучается на отзывах о фильмах и 
обученная модель сохраняется в google drive
3) **distilbert_loading_model_and_testing_26_december.ipynb**
– результаты тестирования модели distilbert
(в том числе перекрестная проверка). Обучающая и тестовая
выборки фиксированные.
Модели загружаются из google drive, они уже обучены
(в файлах 1-2).
В конце ноутбука приведен dataframe
с результатами тестирования каждой из моделей distilbert на 
каждом из датасетов (один датасет с отзывами на отели, 
другой датасет – с отзывами на фильмы).


Вторая серия экспериментов:

4) **distilbert_on_spam_emails_19_january.ipynb** –
модель distilbert
обучается определять, является ли электронное письмо спамом
5) **distilbert_on_spam_sms_19_january.ipynb** –
модель distilbert
обучается определять, является ли sms спамом
6) **distilbert_loading_model_and_testing_on_spam_19_january.ipynb** – 
– результаты тестирования модели distilbert
(в том числе перекрестная проверка).

Ссылки на яндекс диск с моделями, которые я обучил:
1) distilbert, обученный на отзывах на фильмы:
https://disk.yandex.com/d/TXvGCu0_5INEXQ
2) distilbert, обученный на отзывах на отели:
https://disk.yandex.com/d/GiqDYF06V8w8Bg
3) distilbert, обученный определять спам в электронных письмах:
https://disk.yandex.com/d/FFUYjZZQsT_hQQ
4) distilbert, обученный определять спам в sms:
https://disk.yandex.com/d/ebWt8Bhf8PRkbA

