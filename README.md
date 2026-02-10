# Insurance Premium Category Predictor 🚑💰

This project predicts the **insurance premium category** based on user details using a **Machine Learning model**.

## ✨ Features
- ✅ FastAPI backend (ML prediction API)
- ✅ Streamlit frontend (UI app)
- ✅ Fully Dockerized setup (API + Frontend)
- ✅ Ready for cloud deployment

---

## 🐳 Docker Setup (Run Locally)

### Step 1: Pull Docker Images from Docker Hub

**API**
```bash
docker pull ankanbasak0/insurance-api:latest
```

**Frontend**
```
docker pull ankanbasak0/insurance-frontend:latest
```

### Step 2: Run the Containers
**Terminal 1 (Run API)**
```
docker run -p 8000:8000 ankanbasak0/insurance-api:latest
```

**Terminal 2 (Run Frontend)**
```
docker run -p 8501:8501 ankanbasak0/insurance-frontend:latest
```

### Step 3: Open in Browser

**👉 Open this link:**
```
http://localhost:8501
```
