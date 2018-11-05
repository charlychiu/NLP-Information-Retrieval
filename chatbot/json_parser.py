import json
from pprint import pprint
from operator import add


def load_json(file_path):
    with open(file_path, encoding='utf8') as f:
        json_data = json.load(f)
        question_list = list()
        answer_list = list()
        for record in json_data:
            question_list.append(record['question'])
            answer_list.append(record['answer'])
        full_sentence_list = list(map(add, question_list, answer_list))
    return question_list, answer_list, full_sentence_list


if __name__ == '__main__':
    q_data, a_data, full_data = load_json('CTBC.json')
    # pprint(data[0]['question'])
    # pprint(data[0]['answer'])
    print(full_data)
