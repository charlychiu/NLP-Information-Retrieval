import jieba
from gensim.summarization import bm25


def training_bm25_model(data_set):
    sentence_tmp_list = list()
    for data in data_set:
        seg_list = jieba.cut(data)
        tmp_list = list()
        for seg in seg_list:
            tmp_list.append(seg)
        sentence_tmp_list.append(tmp_list)
    bm25Model = bm25.BM25(sentence_tmp_list)
    return bm25Model


def get_average_idf_by_model(bm25_model):
    average_idf = sum(map(lambda k: float(bm25_model.idf[k]), bm25_model.idf.keys())) / len(bm25_model.idf.keys())
    return average_idf


def query_by_model(bm25_model, average_idf, query_string):
    query = []
    for word in query_string.strip().split():
        query.append(word)
    scores = bm25_model.get_scores(query, average_idf)
    return scores


if __name__ == '__main__':
    seg_list = jieba.cut("在非洲，每六十秒，就有一分鐘過去")
    print("|".join(seg_list))
    corpus = [
        ["black", "cat", "white", "cat"],
        ["cat", "outer", "space"],
        ["wag", "dog"]
    ]
