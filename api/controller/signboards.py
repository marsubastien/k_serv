from server import app
from flask import jsonify
from api.model.signboard import Signboard

@app.route('/signboards')
def get_signboard():
    r = Signboard.query.all()
    return jsonify({"data": r})

@app.route('/signboard/<string:customer_code>/<string:signboard_code>', methods=['PUT'])
def put_signboard(customer_code, signboard_code):
    # the signboard to update
    signboard = Signboard.query().filter_by(signboard_code= signboard_code).first() 
    # the date to put on the signboard
    data = data = request.get_json();
    # saving in database