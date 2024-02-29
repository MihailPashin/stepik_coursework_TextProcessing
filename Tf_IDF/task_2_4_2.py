'''Дана следующая коллекция текстов. Постройте словарь (отображение из строкового представления токенов в их номера) и вектор весов (DF).

DF(w)=DocCount(w,c)Size(c)DF(w)=Size(c)DocCount(w,c)​ -- частота слова ww в коллекции cc (отношение количества документов, в которых слово используется, к общему количеству документов).
'''
import re
import collections
import numpy as np

sentences = ['Казнить нельзя, помиловать. Нельзя наказывать.',
'Казнить, нельзя помиловать. Нельзя освободить.',
'Нельзя не помиловать.',
'Обязательно освободить.']

TOKENIZE_RE = re.compile(r'[\w\d]+', re.I)

corpus = [x.lower() for x in sentences]

def tokenize(txt):

    return TOKENIZE_RE.findall(txt)

# Библиотека по созданию словаря из видео    
def build_vocabulary(tokenized_texts, max_size=1000000, max_doc_freq=0.8, min_count=5, pad_word=None): 
    word_counts = collections.defaultdict(int)
    doc_n = 0
# посчитать количество документов, в которых употребляется каждое слово
# а также общее количество документов
    for txt in tokenized_texts:
        doc_n += 1
        unique_text_tokens = set(txt)
        for token in unique_text_tokens:
            word_counts[token] += 1
# убрать слишком редкие и слишком частые слова
    word_counts = {word: cnt for word, cnt in word_counts.items() if cnt >= min_count and cnt / doc_n <= max_doc_freq}
# отсортировать слова по убыванию частоты
    sorted_word_counts = sorted(word_counts.items(),
    reverse=True,
    key=lambda pair: pair[1])
# добавим несуществующее слово с индексом 0 для удобства пакетной обработки 
    if pad_word is not None: 
        sorted_word_counts = [(pad_word, 0)] + sorted_word_counts
# если у нас по прежнему слишком много слов, оставить только max_size самых частотных 
    if len(word_counts) > max_size:
        sorted_word_counts = sorted_word_counts[:max_size]
    # нумеруем слова
    word2id = {word: i for i, (word, _) in enumerate(sorted_word_counts)}
    # нормируем частоты слов
    word2freq = np.array([cnt / doc_n for _, cnt in sorted_word_counts], dtype='float32')
    return word2id, word2freq

corpus_tokens = [tokenize(x) for x in corpus]

MAX_DF = 1

MIN_COUNT = 1

vocabulary, word_doc_freq = build_vocabulary(corpus_tokens, max_doc_freq=MAX_DF, min_count=MIN_COUNT)

UNIQUE_WORDS_N = len(vocabulary)

word_df = [(word, word_doc_freq[i]) for i, (word, _) in enumerate(vocabulary.items())]

# Сортировка по алфавиту
word_df = sorted(word_df)

# Сортировка по убыванию весов
answer = sorted(word_df, key = lambda x: x[1])

answer_1 = [];

answer_2 = [];

for k, v in list(answer):

    answer_1.append(k)

    answer_2.append(str(v))

print(" ".join(answer_1))

print(" ".join(answer_2))
