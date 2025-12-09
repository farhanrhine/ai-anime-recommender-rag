"""
🎌 AI Anime Recommender System - Project Structure Generator

Run this script to create the project folder structure for a 
RAG-based recommendation system with FastAPI, Docker, and Kubernetes.

Usage:
    python create_structure.py
"""

import os

# Directories to create
structure = [
    # Data
    "data",
    
    # Source code
    "src/recommender_system",
    "src/recommender_system/api",
    "src/recommender_system/utils",
    "src/recommender_system/config",
    "src/recommender_system/pipeline",
    
    # Frontend
    "app",
    
    # Docker
    "docker",
    
    # Kubernetes manifests
    "kubernetes",
    
    # Logs
    "logs",
]

# Files to create (empty)
files = [
    # Root files
    ".env",
    ".gitignore",
    ".dockerignore",
    
    # Main source package
    "src/recommender_system/__init__.py",
    "src/recommender_system/data_loader.py",
    "src/recommender_system/vector_store.py",
    "src/recommender_system/recommender.py",
    "src/recommender_system/prompt_template.py",
    
    # API
    "src/recommender_system/api/__init__.py",
    "src/recommender_system/api/fastapi_app.py",
    "src/recommender_system/api/models.py",
    
    # Utils
    "src/recommender_system/utils/__init__.py",
    "src/recommender_system/utils/logger.py",
    "src/recommender_system/utils/custom_exception.py",
    
    # Config
    "src/recommender_system/config/__init__.py",
    "src/recommender_system/config/settings.py",
    
    # Pipelines
    "src/recommender_system/pipeline/__init__.py",
    "src/recommender_system/pipeline/build_embedding_pipeline.py",
    "src/recommender_system/pipeline/recommend_pipeline.py",
    
    # Streamlit frontend
    "app/streamlit_app.py",
    
    # Docker
    "docker/Dockerfile",
    
    # Kubernetes manifests
    "kubernetes/storageclass.yaml",
    "kubernetes/pv.yaml",
    "kubernetes/pvc.yaml",
    "kubernetes/secret.yaml",
    "kubernetes/deployment.yaml",
    "kubernetes/service.yaml",
]

def create_structure():
    """Create project directories and files."""
    
    print("🎌 Creating AI Anime Recommender project structure...\n")
    
    # Create directories
    for path in structure:
        os.makedirs(path, exist_ok=True)
        print(f"📁 Created: {path}/")
    
    print()
    
    # Create files
    for f in files:
        # Ensure parent directory exists
        parent = os.path.dirname(f)
        if parent:
            os.makedirs(parent, exist_ok=True)
        
        # Create empty file if it doesn't exist
        if not os.path.exists(f):
            with open(f, "w") as file:
                file.write("")
            print(f"📄 Created: {f}")
        else:
            print(f"⏭️  Skipped (exists): {f}")
    
    print("\n✅ Project structure created successfully!")
    print("\nNext steps:")
    print("  1. Run: uv sync")
    print("  2. Create .env with API keys")
    print("  3. Add your code to the files")

if __name__ == "__main__":
    create_structure()
