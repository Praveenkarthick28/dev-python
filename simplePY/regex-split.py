import re
text = "we, i, you, he, she, it, they"
matter = ","
alter = re.split(matter, text)
print(alter)
