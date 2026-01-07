# AI-Based Audio Moment Extraction – Week 1

## Description
This project aims to build an AI/ML pipeline to analyze YouTube videos (podcasts/interviews) and extract key conversational moments such as question–answer, agreement, and disagreement.

This repository contains **Week 1 implementation**, which focuses on video input handling and audio preprocessing.

## Week 1 Scope
- Accept a public YouTube video URL
- Download the video
- Extract audio from the video
- Preprocess audio (mono, 16kHz) for ML readiness

No machine learning models are used in this stage.

## Technologies Used
- Python
- yt-dlp
- FFmpeg

## How to Run
```bash
python main.py
