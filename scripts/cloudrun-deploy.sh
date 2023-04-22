PROJECT_ID=$(gcloud config get-value project)
gcloud run deploy --image gcr.io/${PROJECT_ID}/dash-cytoscape-example --platform managed --region europe-west2 --allow-unauthenticated