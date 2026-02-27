from fastapi import FastAPI
from .database import engine, Base, SessionLocal
from .models import Player, Enemy
 
app = FastAPI()
 
Base.metadata.create_all(bind=engine)
 
types = ["Agua", "Fuego", "Planta", "Electrico", "Tierra", "Volador"]

type_advantages = {
    "Agua": ["Fuego", "Tierra"],
    "Fuego": ["Planta"],
    "Planta": ["Agua", "Tierra"],
    "Electrico": ["Agua", "Volador"],
    "Tierra": ["Electrico", "Fuego"],
    "Volador": ["Planta"]
}
 
@app.get("/")
def root():
    return {"message": "RPG API Running"}
 
@app.get("/types")
def get_types():
    return {"available_types": types}
 
@app.post("/players")
def create_player(name: str, type: str):
    db = SessionLocal()
    player = Player(name=name, type=type)
    db.add(player)
    db.commit()
    db.refresh(player)
    db.close()
    return player

@app.post("/enemies")
def create_enemy(name: str, type: str, level: int = 1):
    db = SessionLocal()
    enemy = Enemy(name=name, type=type, level=level)
    db.add(enemy)
    db.commit()
    db.refresh(enemy)
    db.close()
    return enemy

@app.get("/players")
def list_players():
    db = SessionLocal()
    players = db.query(Player).all()
    db.close()
    return players

@app.post("/fight")
def fight(player_id: int, enemy_id: int):
    db = SessionLocal()
 
    player = db.query(Player).filter(Player.id == player_id).first()
    enemy = db.query(Enemy).filter(Enemy.id == enemy_id).first()
 
    if not player or not enemy:
        db.close()
        return {"error": "Jugador o enemigo no encontrado"}
 
    multiplier = 1
 
    if enemy.type in type_advantages.get(player.type, []):
        multiplier = 2
    elif player.type in type_advantages.get(enemy.type, []):
        multiplier = 0.5
 
    player_power = player.level * multiplier
    enemy_power = enemy.level
 
    if player_power >= enemy_power:
        if player.level < 5:
            player.level += 1
        result = "Jugador gana"
    else:
        result = "Enemigo gana"
 
    db.commit()
    db.close()
 
    return {
        "resultado": result,
        "nivel_jugador": player.level
    }
