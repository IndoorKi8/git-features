$initialized=Test-Path -Path ".venv"
if (!$initialized) {
    python -m venv .venv
}
. .venv/scripts/activate
pip install -r requirements.txt