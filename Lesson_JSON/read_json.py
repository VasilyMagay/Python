import chardet
import json

def codepage(filename):
    cp = 'utf8'
    with open(filename, 'rb') as f:
        data = f.read()
        result = chardet.detect(data)
        cp = result['encoding']
    return cp

def get_dict_from_json_news_file(filename, cp='', min_word_len = 6):
    
    dict = {}
    
    if len(cp) == 0:
        cp = codepage(filename)

    with open(filename, 'r', encoding=cp) as f:
        json_data = json.load(f)
    
        for item in json_data['rss']['channel']['items']:
            descr = item['description']
            line = descr.strip()
            line_list = line.split(' ')
            for word in line_list:
                if len(word) >= min_word_len:
                    word = word.lower()
                    dict[word] = dict.get(word, 0) + 1
        
    return dict
    
def print_top(dict, top_num=10):
    sorted_list = sorted(dict.items(), key=lambda x: x[1], reverse=True)
    for i in range(top_num):
        print(sorted_list[i])
    
def process_file(filename):
    print('News file: {}'.format(filename))
    dict = get_dict_from_json_news_file(filename)    
    print_top(dict)    
    
files = ['newsafr.json', 'newscy.json', 'newsfr.json', 'newsit.json']

for fname in files:
    process_file(fname)

