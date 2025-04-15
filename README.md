# Map Dashboard

[![GitHub issues](https://img.shields.io/github/issues/munzz11/map-dashboard)](https://github.com/munzz11/map-dashboard/issues)
[![Docker Pulls](https://img.shields.io/docker/pulls/munzz11/reef-map-dashboard)](https://hub.docker.com/r/munzz11/reef-map-dashboard)
[![Docker Image Size (latest by date)](https://img.shields.io/docker/image-size/munzz11/reef-map-dashboard)](https://hub.docker.com/r/munzz11/reef-map-dashboard)
[![Docker Image Version (latest semver)](https://img.shields.io/docker/v/munzz11/reef-map-dashboard)](https://hub.docker.com/r/munzz11/reef-map-dashboard)

A web-based dashboard for visualizing and analyzing robotic platform location data. Built with Flask and Leaflet.js, this application provides real-time and historical tracking of robotic platforms on an interactive map.

## Features

- Interactive map visualization using Leaflet.js
- Historical data playback
- Deployment and platform filtering
- KML export for Google Earth

## API Attachments

### GET /api/deployments
Returns list of available deployments.

### GET /api/platforms/<deployment>
Returns list of platforms for a specific deployment.

### GET /api/locations
Returns location history with optional filters:
- `deployment`: Filter by deployment
- `platform`: Filter by platform

### GET /api/download_kml/<deployment>
Downloads KML file for a specific deployment.

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| API_URL | Data Gateway API URL | http://data-gateway:8080 |
| FLASK_RUN_HOST | Flask server host | 0.0.0.0 |
| FLASK_RUN_PORT | Flask server port | 5001 |

## Development

### Prerequisites
- Python 3.11 or later
- Docker and Docker Compose

### Local Development
1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

### Docker
Build and run using Docker:
```bash
docker build -t map-dashboard .
docker run -p 5001:5001 map-dashboard
```

## Project Structure
```
map-dashboard/
├── app.py              # Flask application
├── requirements.txt    # Python dependencies
├── Dockerfile         # Docker configuration
└── templates/         # HTML templates
    └── index.html     # Main dashboard template
```
