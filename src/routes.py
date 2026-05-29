@app.route("/planets", methods=["GET"])
def get_planets():

    planets = Planet.query.all()

    results = list(map(lambda planet: planet.serialize(), planets))

    return jsonify(results), 200


@app.route("/planets/<int:planet_id>", methods=["GET"])
def get_one_planet(planet_id):

    planet = Planet.query.get(planet_id)

    if not planet:
        return jsonify({"msg": "Planet not found"}), 404

    return jsonify(planet.serialize()), 200


@app.route("/planets", methods=["POST"])
def create_planet():

    body = request.get_json()

    new_planet = Planet(
        name=body["name"],
        climate=body["climate"],
        population=body["population"]
    )

    db.session.add(new_planet)
    db.session.commit()

    return jsonify(new_planet.serialize()), 201


@app.route("/planets/<int:planet_id>", methods=["PATCH"])
def update_planet(planet_id):

    planet = Planet.query.get(planet_id)

    if not planet:
        return jsonify({"msg": "Planet not found"}), 404

    body = request.get_json()

    if "name" in body:
        planet.name = body["name"]

    if "climate" in body:
        planet.climate = body["climate"]

    db.session.commit()

    return jsonify(planet.serialize()), 200


@app.route("/planets/<int:planet_id>", methods=["DELETE"])
def delete_planet(planet_id):

    planet = Planet.query.get(planet_id)

    if not planet:
        return jsonify({"msg": "Planet not found"}), 404

    db.session.delete(planet)
    db.session.commit()

    return jsonify({"msg": "Deleted"}), 200



@app.route("/caracters", methods=["GET"])
def get_canarters():

    caracters = caracter.query.all()

    results = list(map(lambda caracter: caracter.serialize(), caracters))

    return jsonify(results), 200


@app.route("/caracters/<int:caracter_id>", methods=["GET"])
def get_one_caracter(caracter_id):

    caracter = caracter.query.get(caracter_id)

    if not caracter:
        return jsonify({"msg": "caracter not found"}), 404

    return jsonify(caracter.serialize()), 200


@app.route("/caracters", methods=["POST"])
def create_caracter():

    body = request.get_json()

    new_caracter = caracter(
        name=body["name"],
        climate=body["climate"],
        population=body["population"]
    )

    db.session.add(new_caracter)
    db.session.commit()

    return jsonify(new_caracter.serialize()), 201


@app.route("/caracters/<int:caracter_id>", methods=["PATCH"])
def update_caracter(caracter_id):

    caracter = caracter.query.get(caracter_id)

    if not caracter:
        return jsonify({"msg": "caracter not found"}), 404

    body = request.get_json()

    if "name" in body:
        caracter.name = body["name"]

    if "climate" in body:
        caracter.climate = body["climate"]

    db.session.commit()

    return jsonify(caracter.serialize()), 200


@app.route("/caracters/<int:caracter_id>", methods=["DELETE"])
def delete_caracter(caracter_id):

    caracter = caracter.query.get(caracter_id)

    if not caracter:
        return jsonify({"msg": "caracter not found"}), 404

    db.session.delete(caracter)
    db.session.commit()

    return jsonify({"msg": "Deleted"}), 200



@app.route("/users", methods=["POST"])
def create_user():

    body = request.get_json()

    user = User(
        username=body["username"]
    )

    db.session.add(user)
    db.session.commit()

    return jsonify(user.serialize()), 201


@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):

    user = User.query.get(user_id)

    if not user:
        return jsonify({"msg": "User not found"}), 404

    return jsonify(user.serialize()), 200



@app.route("/favorites", methods=["POST"])
def create_favorite():

    body = request.get_json()

    favorite = Favorite(
        user_id=body["user_id"],
        planet_id=body.get("planet_id"),
        character_id=body.get("character_id")
    )

    db.session.add(favorite)
    db.session.commit()

    return jsonify(favorite.serialize()), 201



@app.route("/favorites/<int:favorite_id>", methods=["PATCH"])
def update_favorite(favorite_id):

    favorite = Favorite.query.get(favorite_id)

    if not favorite:
        return jsonify({"msg": "Favorite not found"}), 404

    body = request.get_json()

    if "planet_id" in body:
        favorite.planet_id = body["planet_id"]

    if "character_id" in body:
        favorite.character_id = body["character_id"]

    db.session.commit()

    return jsonify(favorite.serialize()), 200



@app.route("/users/<int:user_id>/favorites", methods=["GET"])
def get_user_favorites(user_id):

    user = User.query.get(user_id)

    if not user:
        return jsonify({"msg": "User not found"}), 404

    favorites = []

    for fav in user.favorites:

        if fav.planet:
            favorites.append({
                "type": "planet",
                "data": fav.planet.serialize()
            })

        if fav.character:
            favorites.append({
                "type": "character",
                "data": fav.character.serialize()
            })

    return jsonify(favorites), 200



