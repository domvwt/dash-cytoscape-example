PROJECT_ID=$(gcloud config get-value project)
docker tag dash-cytoscape-example gcr.io/${PROJECT_ID}/dash-cytoscape-example
docker push gcr.io/${PROJECT_ID}/dash-cytoscape-example