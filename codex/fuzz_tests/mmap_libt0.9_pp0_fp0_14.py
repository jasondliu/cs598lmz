import mmap
import os

NCCO_TEMPLATE = """
[
    {{
        "action": "talk",
        "text": "You have joined the conversation",
        "profile": "joey"
    }},
    {{
        "action": "talk",
        "text": "Please wait while we connect you",
        "profile": "joey"
    }},
    {{
        "action": "connect",
        "from": "tel:+1-555-555-1212",
        "streamUrl": [
            "https://[redacted]/wav?uuid={uuid}"
        ]
    }},
    {{
        "action": "talk",
        "text": "The call has ended"
    }}
]
"""

@app.route("/", methods=["GET"])
def welcome():

    if request.query_string == b"":
        return file_to_string("templates/index.html")

    # Need to do this because lambda does not have : in it's PATH_INFO
    path_info = request
