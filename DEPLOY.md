Deploying to Streamlit Cloud

Overview
- This repo contains a Streamlit app (`app.py`) and the trained model (`final_credit_risk_model.pkl`) plus label encoders. Streamlit Cloud can deploy straight from a GitHub repository.

Prerequisites
- A GitHub account.
- (Optional) `gh` CLI for faster repo creation and push.
- If your model files are large (>100 MB), use Git LFS or host the model externally (S3, GCS) and update `app.py` to download at startup.

Steps
1. Initialize Git (if not already):

```powershell
cd "C:\Users\Work\Desktop\Credit Risk Modeling using German Dataset by target"
git init
git add .
git commit -m "Initial commit: Streamlit app + model"
```

2. Create a GitHub repo and push (two options):

- Web UI: Create a new repo on GitHub, then follow the commands provided by GitHub to push.

- Using `gh` CLI (recommended):

```powershell
gh repo create YOUR_GITHUB_USERNAME/your-repo-name --public --source=. --remote=origin --push
```

3. Open Streamlit Cloud and connect your GitHub account:
- Visit https://share.streamlit.io/
- Click "New app" → choose the repo and branch → select the `app.py` file → click "Deploy".

4. Environment & secrets:
- If your app needs environment variables (e.g., API keys), use Streamlit Cloud's "Secrets" UI to add them.

Notes & Troubleshooting
- `requirements.txt` must be present at repo root (already included).
- If the app fails on Streamlit Cloud due to missing model files, ensure `final_credit_risk_model.pkl` and the encoder `*_label_encoder.pkl` files are pushed to the repo, or modify `app.py` to download them at runtime.
- For large files (>100 MB), use Git LFS or external hosting; Streamlit Cloud won't accept repositories with files larger than GitHub's size limits.

Optional: Automate using GitHub Actions
- You can add CI to check the app starts, or to build model artifacts; leave a note if you want that.

If you'd like, I can:
- Create the Git commit for you and help push (you'll need to authenticate), or
- Generate a small `download_model.py` that fetches the model from an external URL at startup (if you prefer to host the model outside GitHub).
