from pathlib import Path

#project folder
folders = [
    "app",
    "app/templates",
    "app/static/js",
    "app/static/css",
    "worker",
    "infra",
    "scripts",
    "docs"
]

#project files
files = [
    #Root files
    "requirements.txt",
    ".env",

    #Backend
    "app/__init__.py",
    "app/main.py",
    "app/config.py",
    "app/db.py",
    "app/aws.py",
    "app/vector.py",
    "app/rag.py",
    "app/memory.py",
    "app/guardrails.py",
    "app/graph.py",
    "app/observability.py",

    #frontend
    "app/templates/index.html",
    "app/static/css/style.css",
    "app/static/js/app.js",

    #Document ingetion
    "worker/__init__.py",
    "worker/ingest.py",

    #Database
    "infra/schema.sql",
    "scripts/init_db.py",

    #Documentation
    "docs/SETUP.md",
]

def create_structure():
    for folder in folders:
        Path(folder).mkdir(parents=True, exist_ok=True)

    for file in files:
        path = Path(file)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.touch(exist_ok=True)

    print("Project folder and files are created")
    print(f"Total folder: {len(folder)}")
    print(f"Total files: {len(files)}")

if __name__ == "__main__":
    create_structure()