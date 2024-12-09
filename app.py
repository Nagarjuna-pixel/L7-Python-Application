from flask import Flask, render_template, request, redirect, url_for
from models import add_flavor, search_flavors

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add_flavor", methods=["GET", "POST"])
def add_flavor_route():
    if request.method == "POST":
        name = request.form["name"]
        is_seasonal = "is_seasonal" in request.form
        allergens = request.form["allergens"]
        add_flavor(name, is_seasonal, allergens)
        return redirect(url_for("display_flavors"))
    return render_template("add_flavor.html")

@app.route("/display_flavors", methods=["GET"])
def display_flavors_route():
    query = request.args.get("query", "")
    flavors = search_flavors(query)
    return render_template("display_flavors.html", flavors=flavors, query=query)

if __name__ == "__main__":
    app.run(debug=True)
