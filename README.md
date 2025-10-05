# 🏫 UDISE+ Student Auto-Filler (Python + Selenium)

Automates filling **General Profile**, **Enrolment Profile**, **Facility Profile**, and **Profile Preview** on the **UDISE+** portal using **Python + Selenium**.  
Use this tool only with authorized/test accounts — automating official portals may have legal/operational consequences.

---

## 🚀 Features
- 🔐 Automated login step (script enters username & password — **update to secure storage recommended**)  
- 🧭 Prompts for student **class** at start (1–10). Falls back to **10** on invalid input.  
- 📊 Auto-generates **height & weight** based on class (randomized around realistic base values).  
- ✅ Fills form controls (selects, radio buttons, checkboxes) across:
  - General Profile (blood group)
  - Enrolment Profile (RTE question)
  - Facility Profile (textbook, SLD/ASD/ADHD, gifted, olympiads, digital-device capability, parent education, distance)
  - Profile Preview (Complete Data → Next Student)
- 🔁 Loops through students (`while True`) — press `Ctrl+C` to stop.
- ⚙️ Uses `webdriver_manager` to auto-install matching ChromeDriver.

---

## 📂 Suggested Project Structure
udise-autofill/
│
├── src/
│   └── autofill.py        # main script (your provided code)
│
├── config/
│   └── README.md          # docs on where to put credentials (or env var usage)
│
├── uv.lock # pinned dependencies (created by uv)
├── requirements.txt
└── README.md


---


---

## ⚙️ Dependencies (`uv.lock` contains all dependencies)
This project uses **uv** for dependency management and the exact dependency snapshot is stored in `uv.lock`.  
See *Notes* below for commands to install `uv` and to install the pinned dependencies from `uv.lock`.

---

## ⚙️ Requirements
- Python 3.8+  
- Google Chrome installed  
- Install Python deps:
```bash
pip install -r requirements.txt


# 🔐 Important Safety & Usage Notes

Do NOT commit real credentials. Use env vars or a .gitignore-ed config file.

Test first on a sandbox/test account. Do NOT run on production accounts without authorization.

Many selectors are hard-coded XPaths; they may break if the portal UI changes. Expect to update selectors regularly.

Replace time.sleep() pauses with smarter WebDriverWait conditions where possible for reliability.

The script currently runs an infinite loop — consider replacing with a CSV-driven loop (students.csv) or a fixed number of iterations.

# License

MIT License © 2025 CodeBySumant

**Notes on `uv.lock` and installing dependencies:** `uv.lock` is the lockfile produced by the `uv` tool (it pins exact dependency versions for reproducible installs). Use `uv sync` / `uv`'s pip-compatible commands to install the environment from that lockfile. You can also generate a `requirements.txt` from `pyproject.toml` if you need one via `uv pip compile pyproject.toml -o requirements.txt`. :contentReference[oaicite:0]{index=0}

---

Would you like me to:
- paste this as a real `README.md` file into the repo (give me permission to create files), or  
- also generate a small `setup.sh` that installs `uv` and runs `uv sync` for convenience?
::contentReference[oaicite:1]{index=1}
