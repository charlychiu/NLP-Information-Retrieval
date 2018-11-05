import json
from pprint import pprint


def load_json(file_path):
    with open(file_path, encoding='utf8') as f:
        data = json.load(f)
        question_list = list()
        answer_list = list()
        for record in data:
            question_list.append(record['question'])
            answer_list.append(record['answer'])
        return question_list, answer_list


if __name__ == '__main__':
    data = load_json('CTBC.json')
    pprint(data[0]['question'])
    pprint(data[0]['answer'])
