gi = (i for i in ())
# Test gi.gi_code and gi.gi_frame
gi.gi_code  # Noncompliant {{Remove this reference to the "gi_code" member.}}
#   ^^^^^^
gi.gi_frame  # Noncompliant
#   ^^^^^^^

# Test gi.gi_running
gi.gi_running  # Noncompliant
#   ^^^^^^^^^^

# Test gi.gi_frame.f_code
gi.gi_frame.f_code  # Noncompliant
#   ^^^^^^^

# Test gi.gi_frame.f_code.co_name
gi.gi_frame.f_code.co_name  # Noncompliant
#   ^^^^^^^

# Test gi.gi_frame.f_back
gi.gi_frame.f_back  # Noncompliant
#   ^^^^^^^

# Test gi.gi_frame.f_back.f_code
gi.gi_frame.f_back.f_code  # Noncompliant
#   ^^^^^^^

# Test gi.gi_frame.f_back.f
