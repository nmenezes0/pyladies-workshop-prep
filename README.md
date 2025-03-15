# Workshop prep for PyCon LT 2025

Repo with prep code for trialling out workshop materials.

To run:
* Clone the repo
* `uv install` to install packages
* (Optionally) `pre-commit install` to install pre-commit
* `make run-streamlit-app` to run the streamlit app


To run data scraping to get PyConLT talks data:
```
uv run python scripts/pycon_lt_data.py
```

This outputs to the `data` folder within `app`.