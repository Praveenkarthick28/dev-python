import re
text = "work hard , party hard , live hard"
pattern = r"hard"
replacement = "smart"
new_text = re.sub(pattern, replacement, text)
print(new_text)
