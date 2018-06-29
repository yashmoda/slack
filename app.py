import json
from pprint import pprint

from flask import Flask, request
from slackclient import SlackClient

app = Flask(__name__)

SLACK_CLIENT_SECRET = "c3133a561a7aca3e51e00cb661561fd4"
SLACK_CLIENT_ID = "388791347440.390608538199"
SLACK_VERIFICATION_TOKEN = "KNNVoswKBSKDx46XH0WMP3TV"
SLACK_OAUTH_ACCESS_TOKEN = "xoxp-388791347440-389332355988-391269601047-d947e9c26e529797cdf4f9cfcb3917f0"
SLACK_BOT_ACCESS_TOKEN = "xoxb-388791347440-390560025398-ZuCjCEdyUERbRy3fMBSP12lm"

sc = SlackClient("xoxb-388791347440-390560025398-ZuCjCEdyUERbRy3fMBSP12lm")

# pprint(sc.api_call("channels.list"))

sc.api_call(
  "chat.postMessage",
  channel="general",
  text="Hello from Python! :tada:"
)


@app.route("/open/", methods=["POST"])
def action():
    message_action = json.loads(request.form["payload"])
    trigger_id = message_action['trigger_id']
    open_dialog = sc.api_call(
        "dialog.open",
        trigger_id=message_action["trigger_id"],
        dialog={
            "title": "Request a coffee",
            "submit_label": "Submit",
            "callback_id": "yash_ticket",
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
    app.run(host='35.182.190.74', port=8000, debug=True)
