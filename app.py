from flask import Flask, render_template, request

app = Flask(__name__)

MORSE_CODE_DICT = {
'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-', ',': '--..--', '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'
}

def to_morse(text):
morse = ''
for char in text.upper():
if char == ' ':
orse += ' '
else:
morse += MORSE_CODE_DICT[char] + ' '
return morse

def to_english(morse):
english = ''
morse_dict = {v: k for k, v in MORSE_CODE_DICT.items()}
for code in morse.split():
if code == '':
english += ' '
else:
english += morse_dict[code]
return english

@app.route('/', methods=['GET', 'POST'])
def translate():
if request.method == 'POST':
text = request.form['text']
mode = request.form['mode']
if mode == 'to_morse':
result = to_morse(text)
else:
result = to_english(text)
return render_template('index.html', result=result)
return render_template('index.html')

if __name__ == '__main__':
app.run(debug=True)
