import fileinput
import fnmatch
import os

#replaces characters with new ones
replace_texts ={'.': '', 'Oh,': 'oh', 'Oh': 'oh', 'God': 'god', 'blazer': 'blaza', 'plaza': 'blaza', 'kind of': 'kinda',
                'Kind of': 'kinda', "All right": "alright", "all right": "alright", "want to": "wanna",
                "Want to": "Wanna", "let me": "lemme", "Some gamers": "sup gamers", "Let me": "Lemme", ',': ''}

# searches for srt file within same directory
for file in os.listdir('.'):
    if fnmatch.fnmatch(file, '*.srt'):
      captions = file

for line in fileinput.input(captions, inplace=True):
    # skip the timecode lines
    if '-->' in line:
        print(line, end='')
    else:
        for search_text in replace_texts:
            replace_text = replace_texts[search_text]
            line = line.replace(search_text, replace_text)
        print(line, end='')