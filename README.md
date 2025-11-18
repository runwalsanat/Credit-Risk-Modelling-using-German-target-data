Quick run instructions (Windows PowerShell)

1. Activate the project virtual environment:

```powershell
& "C:\Users\Work\Desktop\Credit Risk Modeling using German Dataset by target\.venv\Scripts\Activate.ps1"
```

2. Install dependencies (only if not already installed):

```powershell
C:\Users\Work\Desktop\Credit Risk Modeling using German Dataset by target\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

3. Run the Streamlit app:

```powershell
streamlit run app.py
```

4. Open the displayed local URL (usually `http://localhost:8501`).

Optional: To deploy to Streamlit Cloud, push this repository to GitHub and use the web UI to connect the repo; ensure `requirements.txt` is present.
