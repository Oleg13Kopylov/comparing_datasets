# MobileBERT

Описание вида "название файла – его содержание"

Первая серия экспериментов:

1) **mobilebert_on_hotels_26_december.ipynb**
– модель mobilebert обучается на отзывах об отелях и
обученная модель сохраняется в google drive
2) **mobilebert_on_movies_26_december.ipynb**
– модель mobilebert обучается на отзывах о фильмах и 
обученная модель сохраняется в google drive
3) **mobilebert_loading_model_and_testing_26_december.ipynb**
– результаты тестирования модели mobilebert
(в том числе перекрестная проверка). Обучающая и тестовая
выборки фиксированные.
Модели загружаются из google drive, они уже обучены
(в файлах 1-2).
В конце ноутбука приведен dataframe
с результатами тестирования каждой из моделей mobilebert
на каждом из датасетов (один датасет с отзывами на отели, 
другой датасет – с отзывами на фильмы).

Вторая серия экспериментов:

4) **mobilebert_on_spam_emails_20_january.ipynb** –
модель mobilebert
обучается определять, является ли электронное письмо спамом
5) **mobilebert_on_spam_sms_20_january.ipynb** –
модель mobilebert
обучается определять, является ли sms спамом
6) **mobilebert_loading_model_and_testing_on_spam_20_january.ipynb**
– результаты тестирования модели mobilebert
(в том числе перекрестная проверка).


Ссылки на яндекс диск с моделями, которые я обучил:
1) mobilebert, обученный на отзывах на фильмы:
https://disk.yandex.com/d/fZ8uWdT-e1WI5g
2) mobilebert, обученный на отзывах на отели:
https://disk.yandex.com/d/c_H7t53QFnePCg
3) mobilebert, обученный определять спам в электронных письмах:
https://disk.yandex.com/d/lh-B5OzgAWprrg
4) mobilebert, обученный определять спам в sms:
https://disk.yandex.com/d/gql-98pRgWO4QA


