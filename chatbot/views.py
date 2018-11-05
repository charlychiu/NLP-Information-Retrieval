from django.shortcuts import render
from chatbot.json_parser import *
from chatbot.preprocessing import *


def index(request):
    file_path = 'chatbot/CTBC.json'
    question_list, answer_list = load_json(file_path)
    print(question_list)
    model = training_bm25_model(answer_list)
    idf = get_average_idf_by_model(model)
    scores = query_by_model(model, idf, '訂單 資料')
    print(scores)
    idx = scores.index(max(scores))
    print(idx)
    print(question_list[idx])
