# запросы на добовление
import sys
sys.path.append('../')

from core import *
from instance.models import *

# добаыить товар
@api.route('/addStuff', methods=['PUT'])
@jwt_required()
def AddStuf():
    user = get_jwt()["sub"]
    if GetRole(user) == 'user':
        resp = {
            "errCode": 2,
            "errString": "вы пользователь, вы не можете продовать"
        }
        return resp, 403

    try:
        name = request.form["name"]
        price = request.form["price"]
        size = request.form["size"]
        mass = request.form["mass"]
        description = request.form["description"]
        photoFile = request.files['photo']
        photoName = request.form["photoName"]
    except:
        resp = {
            "errCode": 1,
            "errString": "нехватает данных"
        }
        return resp, 401

    path = '../front/public/img/stuff/' + photoFile.filename
    photoFile.save(path)
    os.rename(path, '../front/public/img/stuff/'+photoName)

    photoName = '/img/stuff/'+photoName
    producer = Producer.query.filter_by(name=user).first().id
    item = Stuff(name=name, photo=photoName, price=price, size=size, mass=mass, description=description, producer=producer)
    db.session.add(item)
    db.session.commit()

    return 'создал'

# добавить склад
@api.route('/addStorehouse', methods=["PUT"])
@jwt_required()
def AddStorehouse():
    user = get_jwt()["sub"]
    if GetRole(user) == 'user':
        resp = {
            "errCode": 2,
            "errString": "вы пользователь, вы не можете продовать"
        }
        return resp, 403

    try:
        city = request.json["city"]
    except:
        resp = {
            "errCode": 1,
            "errString": "нехватает данных"
        }
        return resp, 401

    userID = Producer.query.filter_by(name=user).first().id
    storehouse = Storehouse.query.filter_by(producer=userID).all()
    for el in storehouse:
        if el.city==city:
            resp = {
                "errCode": 4,
                "errString": "по этому адрессу уже есть склад"
            }
            return resp, 401
    
    storehouse = Storehouse(city=city, producer=userID)
    db.session.add(storehouse)
    db.session.commit()

    return 'создал'

# добавить пвз
@api.route('/addPVZ', methods=["PUT"])
@jwt_required()
def AddPVZ():
    user = get_jwt()["sub"]
    if GetRole(user) == 'user':
        resp = {
            "errCode": 2,
            "errString": "вы пользователь, вы не можете продовать"
        }
        return resp, 403
    
    try:
        address = request.json["address"]
        city = request.json["city"]
        time_from = request.json["time_from"]
        price_from = request.json["price_from"]
        distance_from = request.json["distance_from"]
    except:
        resp = {
            "errCode": 1,
            "errString": "нехватает данных"
        }
        return resp, 401

    pvz = PVZ.query.filter_by(address=address).all()
    if pvz:
        resp = {
            "errCode": 4,
            "errString": "по этому адрессу уже есть пвз"
        }
        return resp, 401

    userID = Producer.query.filter_by(name=user).first().id
    pvz = PVZ(producer=userID, city=city, address=address, time_from=time_from, price_from=price_from, distance_from=distance_from)
    db.session.add(pvz)
    db.session.commit()

    return 'создал'
