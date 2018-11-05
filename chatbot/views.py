from django.shortcuts import render
from chatbot.json_parser import *
from chatbot.preprocessing import *


def index(request):
    if request.method == 'POST':
        query_string = request.POST['query_string']
        file_path = 'chatbot/CTBC.json'
        question_list, answer_list, full_list = load_json(file_path)
        model = training_bm25_model(full_list)
        idf = get_average_idf_by_model(model)
        scores = query_by_model(model, idf, query_string)
        print(scores)
        idx = scores.index(max(scores))
        print(idx)
        print(question_list[idx])
        print(answer_list[idx])
        return render(request, 'chatbot/index.html',
                      {'question': question_list[idx], 'answer': answer_list[idx], 'query_str': query_string})
    else:
        return render(request, 'chatbot/index.html')
