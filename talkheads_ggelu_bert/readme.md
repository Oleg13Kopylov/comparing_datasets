# talkheads_ggelu_bert

Описание вида "название файла – его содержание" для 
BERT with Talking-Heads Attention and Gated GELU
(talkheads_ggelu_bert).

Первая серия экспериментов:

1) **talkheads_ggelu_bert_on_hotels_28_december.ipynb**
– модель talkheads_ggelu_bert обучается на отзывах об отелях и
обученная модель сохраняется в google drive
2) **talkheads_ggelu_bert_on_movies_28_december.ipynb**
– модель talkheads_ggelu_bert обучается на отзывах о фильмах и 
обученная модель сохраняется в google drive
3) **talkheads_ggelu_bert_loading_model_and_testing_29_december.ipynb**
– результаты тестирования модели talkheads_ggelu_bert
(в том числе перекрестная проверка). Обучающая и тестовая
выборки фиксированные. Модели загружаются из google drive, они уже обучены
(в файлах 1-2). В конце ноутбука приведен dataframe
с результатами тестирования каждой из моделей talkheads_ggelu_bert
на каждом из датасетов (один датасет с отзывами на отели, 
другой датасет – с отзывами на фильмы).


Вторая серия экспериментов:

4) **talkheads_ggelu_bert_on_spam_emails_20_january.ipynb** –
модель talkheads_ggelu_bert
обучается определять, является ли электронное письмо спамом
5) **talkheads_ggelu_bert_on_spam_sms_20_january.ipynb** –
модель talkheads_ggelu_bert
обучается определять, является ли sms спамом
7) **talkheads_ggelu_bert_loading_model_and_testing_on_spam_20_january.ipynb**
– результаты тестирования модели talkheads_ggelu_bert
(в том числе перекрестная проверка).

Ссылки на яндекс диск с моделями, которые я обучил:
1) talkheads_ggelu_bert, обученная на отзывах на фильмы:
https://disk.yandex.ru/d/c84wHyXRGUWgiA
2) talkheads_ggelu_bert, обученная на отзывах на отели:
https://disk.yandex.ru/d/GEWUrhLR43asxQ
3) talkheads_ggelu_bert, обученная определять спам в электронных письмах:
https://disk.yandex.com/d/qdOJrUcH1hDacg
4) talkheads_ggelu_bert, обученная определять спам в sms:
https://disk.yandex.com/d/gGWVzk9a6txruQ