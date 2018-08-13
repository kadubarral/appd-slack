import os

from flask import abort, Flask, jsonify, request
from appd_data import get_app


app = Flask(__name__)


def is_request_valid(request):
    is_token_valid = request.form['token'] == os.environ['SLACK_VERIFICATION_TOKEN']
    is_team_id_valid = request.form['team_id'] == os.environ['SLACK_TEAM_ID']

    return is_token_valid and is_team_id_valid


@app.route('/appd', methods=['POST'])
def appd():
    if not is_request_valid(request):
        abort(400)
    if request.form['text'] == 'app_list':
        return jsonify(
            response_type = 'in_channel',
            text ='```' + ', '.join(get_app()) + '```'
        )
    else:
        return jsonify(
            response_type = 'in_channel',
            text = 'try /appd help for a list of commands'
        )