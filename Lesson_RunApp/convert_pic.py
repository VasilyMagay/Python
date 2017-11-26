import subprocess
import os

source_name = 'Source'
result_name = 'Result'

current_dir = os.path.dirname(os.path.abspath(__file__))

source_dir = os.path.join(current_dir, source_name)
result_dir = os.path.join(current_dir, result_name)

if not os.path.exists(result_dir):
    os.makedirs(result_dir)

file_list = os.listdir(source_dir)

for file in file_list:
    file_parts = file.split('.')
    if file_parts[len(file_parts) - 1] == 'jpg':
        s_file = os.path.join(source_dir, file)
        r_file = os.path.join(result_dir, 'new' + file)
        # convert input.jpg -resize 200 output.jpg
        subprocess.run(['convert.exe', s_file, '-resize', '200', r_file])