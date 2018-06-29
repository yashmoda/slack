import json

from flask import Flask, request
from slackclient import SlackClient

app = Flask(__name__)

SLACK_CLIENT_SECRET = "c3133a561a7aca3e51e00cb661561fd4"
SLACK_CLIENT_ID = "388791347440.390608538199"
SLACK_VERIFICATION_TOKEN = "KNNVoswKBSKDx46XH0WMP3TV"
SLACK_OAUTH_ACCESS_TOKEN = "xoxp-388791347440-389332355988-389037564449-df49c361e409031a153c642556e29fa8"

slack_client = SlackClient(SLACK_OAUTH_ACCESS_TOKEN)


@app.route("/open/", methods=["POST"])
def action():
    message_action = json.loads(request.form["payload"])
    trigger_id = message_action['trigger_id']
    open_dialog = slack_client.api_call(
        "dialog.open",
        trigger_id=message_action["trigger_id"],
        dialog={
            "title": "Request a coffee",
            "submit_label": "Submit",
            "elements": [
                {
                    "label": "Coffee Type",
                    "type": "select",
                    "name": "meal_preferences",
                    "placeholder": "Select a drink",
                    "options": [
                        {
                            "label": "Cappuccino",
                            "value": "cappuccino"
                        },
                        {
                            "label": "Latte",
                            "value": "latte"
                        },
                        {
                            "label": "Pour Over",
                            "value": "pour_over"
                        },
                        {
                            "label": "Cold Brew",
                            "value": "cold_brew"
                        }
                    ]
                }
            ]
        }
    )

    print(open_dialog)
    print("\n\n\n\n" + trigger_id)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
