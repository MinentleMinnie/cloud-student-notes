from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

notes = []


@app.route("/")
def home():
    return render_template("index.html", notes=notes)


@app.route("/add", methods=["POST"])
def add_note():
    note = request.form.get("note", "").strip()

    if note:
        notes.append(note)

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)