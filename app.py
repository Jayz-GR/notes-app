from flask import Flask, render_template, request, redirect
import json, os

app = Flask(__name__)
DATA_FILE = 'notes.json'

def load_notes():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE) as f:
            return json.load(f)
    return []

def save_notes(notes):
    with open(DATA_FILE, 'w') as f:
        json.dump(notes, f)

@app.route('/', methods=['GET', 'POST'])
def index():
    notes = load_notes()
    if request.method == 'POST':
        note = request.form('note')
        notes.append(note)
        save_notes(notes)
        return redirect('/')
    return render_template('index.html', notes=notes)

@app.route('/delete/<int:index>')
def delete(index):
    notes = load_notes()
    notes.pop(index)
    save_notes(notes)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)