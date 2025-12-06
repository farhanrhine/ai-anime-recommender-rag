uv sync
uv pip install -e .  

# step1: activate the virtual environment
PS C:\Al_Anime_Recommender_System> . .venv/Scripts/activate

# step 2: inside virtual environments build first vector database
(Al_Anime_Recommender_System) PS C:\Al_Anime_Recommender_System> uv run src/recommender_system/pipeline/build_embedding_pipeline.py

# step 3: test fastapi its working locally or not? 

uvicorn recommender_system.api.fastapi_app:app --reload

and also for stremlit ui run in another terminal
 
uv run streamlit run app/streamlit_app.py  


# step 4: everything okay then ,  build docker file and .dockerignore at root and build image
docker build -t farhanrhine/anime-recommender-api -f docker/Dockerfile .


# step 5: run docker image using docker command 

docker run -p 8000:8000 --env-file .env -v ${PWD}/chroma_db:/app/chroma_db farhanrhine/anime-recommender-api 


# step 6: push docker image at dockerhub 

docker login
docker images
docker push farhanrhine/anime-recommender-api-latest 


                      
