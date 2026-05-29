from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Planet(db.Model):
    __tablename__ = "planet"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    climate = db.Column(db.String(120))
    population = db.Column(db.String(120))


class Character(db.Model):
    __tablename__ = "character"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    gender = db.Column(db.String(50))
    eye_color = db.Column(db.String(50))


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)

    favorites = db.relationship(
        "Favorite",
        back_populates="user"
    )



class Favorite(db.Model):
    __tablename__ = "favorite"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    planet_id = db.Column(db.Integer, db.ForeignKey("planet.id"), nullable=True)
    character_id = db.Column(db.Integer, db.ForeignKey("character.id"), nullable=True)

    user = db.relationship(
        "User",
        back_populates="favorites"
    )

    planet = db.relationship(
        "Planet",
        back_populates="favorites"
    )

    character = db.relationship(
        "Character",
        back_populates="favorites"
    )

favorites = db.relationship(
    "Favorite",
    back_populates="planet"
)

favorites = db.relationship(
    "Favorite",
    back_populates="character"
)

def serialize(self):
    return {
        "id": self.id,
        "name": self.name,
        "climate": self.climate,
        "population": self.population
    }