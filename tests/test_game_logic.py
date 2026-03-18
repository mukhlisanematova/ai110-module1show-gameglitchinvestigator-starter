from logic_utils import check_guess

def test_winning_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"

# --- Tests targeting the high/low hint direction bug ---
# Bug: hints were inverted — guessing too high said "Go HIGHER"
# and guessing too low said "Go LOWER". Fixed so the message
# matches the direction the player actually needs to move.

def test_too_high_hint_says_go_lower():
    # Guess is above the secret, so player must go lower
    outcome, message = check_guess(75, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_too_low_hint_says_go_higher():
    # Guess is below the secret, so player must go higher
    outcome, message = check_guess(25, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_high_hint_does_not_say_go_higher():
    # Regression: hint must NOT tell the player to go higher when already too high
    _, message = check_guess(99, 1)
    assert "HIGHER" not in message

def test_low_hint_does_not_say_go_lower():
    # Regression: hint must NOT tell the player to go lower when already too low
    _, message = check_guess(1, 99)
    assert "LOWER" not in message
