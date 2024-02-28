from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.static_folder = 'static'

notes = []

@app.route('/', methods=["GET", "POST"])
def index():
        if request.method == "POST":
            note = request.form.get("note")
            if note: 
                notes.append(note)
            return redirect(url_for('index'))
        indexed_notes = list(enumerate(notes))
        return render_template("home.html", notes= indexed_notes)


if __name__ == '__main__':
    app.run(debug=True)
