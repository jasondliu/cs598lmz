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

