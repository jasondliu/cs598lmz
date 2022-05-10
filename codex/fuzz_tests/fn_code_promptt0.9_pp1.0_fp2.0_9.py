fn = lambda: None
# Test fn.__code__ not raises AttributeError.
fn.__code__

responder = Responder(show_beta_message=False)
responder.parse(["auth", "logout"])
responder.run()

try:
    responder.parse(["auth", "test", "token_auth_with_code_exchange_exception"])
    responder.run()
except Exception as e:
    assert "AADSTS70002: Error validating credentials" in str(e)

try:
    responder.parse(["auth", "test", "generic_exception"])
    responder.run()
except Exception as e:
    assert "An unknown error occurred while authenticating" in str(e)

import builtins
ptvsd = builtins.__dict__.get("ptvsd")
if ptvsd:
    ptvsd.wait_for_attach()

from tests.helpers import clear_everything
from jam.auth import RefreshTokenAuth
from tests.dummy_jasmine import Jasmine

clear_everything()
jasmine = Jasmine(
