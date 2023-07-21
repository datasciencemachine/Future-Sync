from flask import Flask, request
from redis_functions import get_redis_client, set_state, get_state

app = Flask(__name__)

@app.route("/post", methods=["POST"])
def post():
    house_id = request.json["houseId"]
    macid = request.json["macid"]
    state = request.json["state"]

    print(f"Received POST request with house_id={house_id}, macid={macid}, state={state}")

    set_state(macid, state)

    return "Success"


@app.route("/get", methods=["GET"])
def get():
    house_id = request.args.get("houseId")
    macid = request.args.get("macid")

    print(f"Received GET request with house_id={house_id}, macid={macid}")

    state = get_state(macid)

    return {
        "houseId": house_id,
        "macid": macid,
        "state": state
    }


if __name__ == "__main__":
    app.run(debug=True)
