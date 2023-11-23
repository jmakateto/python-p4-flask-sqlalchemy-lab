from flask import render_template
from .models import Animal, Zookeeper, Enclosure


@app.route("/animal/<int:id>")
def animal_by_id(id):
    animal = Animal.query.get(id)
    return render_template("animal.html", animal=animal)


@app.route("/zookeeper/<int:id>")
def zookeeper_by_id(id):
    zookeeper = Zookeeper.query.get(id)
    return render_template("zookeeper.html", zookeeper=zookeeper)


@app.route("/enclosure/<int:id>")
def enclosure_by_id(id):
    enclosure = Enclosure.query.get(id)
    return render_template("enclosure.html", enclosure=enclosure)
