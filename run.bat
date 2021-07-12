call python -m venv venvironment
call venvironment\Scripts\activate
call pip install -r requirements.txt
call tar_zstd_extractor.py
call deactivate
cmd/k