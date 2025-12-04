import os

structure = [
    "data",
    "src/al_anime_recommender_system",
    "src/al_anime_recommender_system/utils",
    "src/al_anime_recommender_system/config",
    "src/al_anime_recommender_system/pipeline",
    "app",
    "docker",
    "kubernetes",
]

for path in structure:
    os.makedirs(path, exist_ok=True)

files = [
    "src/al_anime_recommender_system/__init__.py",
    "src/al_anime_recommender_system/data_loader.py",
    "src/al_anime_recommender_system/vector_store.py",
    "src/al_anime_recommender_system/recommender.py",
    "src/al_anime_recommender_system/prompt_template.py",
    "src/al_anime_recommender_system/utils/__init__.py",
    "src/al_anime_recommender_system/utils/logger.py",
    "src/al_anime_recommender_system/utils/custom_exception.py",
    "src/al_anime_recommender_system/config/__init__.py",
    "src/al_anime_recommender_system/config/settings.py",
    "src/al_anime_recommender_system/pipeline/__init__.py",
    "src/al_anime_recommender_system/pipeline/build_embedding_pipeline.py",
    "src/al_anime_recommender_system/pipeline/recommend_pipeline.py",
    "app/streamlit_app.py",
    "docker/Dockerfile",
    "docker/requirements.txt",
    "kubernetes/deployment.yaml",
    "kubernetes/service.yaml",
    "kubernetes/monitoring.yaml",
]

for f in files:
    with open(f, "w") as file:
        file.write("")
