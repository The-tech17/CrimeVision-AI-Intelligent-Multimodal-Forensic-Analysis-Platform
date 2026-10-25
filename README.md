# CrimeVision AI — Intelligent Multimodal Forensic Analysis Platform
**Skill Wallet Capstone Project 2**  
*Senior Forensic Systems Architecture | Federal Rules of Evidence (FRE 901/902) Compliant*

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 🏛️ Executive Architecture Overview
**CrimeVision AI** is a court-admissible multimodal forensic intelligence platform engineered to bridge visual crime scene photography, witness emergency 911 audio recordings, and CCTV surveillance video streams into a unified, cryptographically verified evidentiary ledger.

The system addresses the critical problem of forensic data fragmentation and legal evidentiary chain-of-custody tracking under **FRE 901 (Requirement of Authentication or Identification)** and **FRE 902 (Evidence That Is Self-Authenticating)**.

```
                           CRIMEVISION AI ARCHITECTURE
                                        
   [ Crime Scene Photos ]       [ 911 Audio / Radio ]       [ CCTV Surveillance ]
             │                            │                            │
             ▼                            ▼                            ▼
   ┌──────────────────┐         ┌──────────────────┐         ┌──────────────────┐
   │ RT-DETR Detection│         │ Whisper Acoustic │         │ Trajectory &     │
   │ & Spatial BBox   │         │ & Stress Diarize │         │ Penal Classifier │
   └─────────┬────────┘         └─────────┬────────┘         └─────────┬────────┘
             │                            │                            │
             └────────────────────┬───────────────────────────────────┘
                                  ▼
                   ┌───────────────────────────────┐
                   │  Master Cryptographic Ledger  │
                   │  (SHA-256 Manifest / FRE 902) │
                   └──────────────┬────────────────┘
                                  │
                  ┌───────────────┴───────────────┐
                  ▼                               ▼
     ┌────────────────────────┐      ┌────────────────────────┐
     │ Grounded Zero-Halluc.  │      │ ReportLab 1-Click      │
     │ Evidence RAG Chat      │      │ Forensic PDF Dossier   │
     └────────────────────────┘      └────────────────────────┘
```

---

## 📦 Core Modules & Functional Capabilities

### 1. Configuration & Forensic Security (Chain of Custody)
- **API Key Security**: Input field for **Google Gemini** or **Groq API** keys with automatic fallback to high-fidelity standalone forensic simulation mode.
- **FRE 901/902 Chain-of-Custody**:
  - SHA-256 cryptographic hashing for every ingested artifact.
  - Investigator sign-off ledger (Badge ID, Agency jurisdiction, Timestamp).
  - Master Case Manifest Digest calculation.

### 2. Tab 1 — Crime Scene Visual Evidence Tagger (Epic 2)
- **Multimodal Object Detection**: Simulates **RT-DETR** (Real-Time DEtection TRansformer) and integrates live Vision APIs to tag:
  - Firearms & Edged Weapons
  - Masked Persons of Interest
  - Blood Spatter Patterns (Arterial vs. Pool)
  - Structural Forced Entry Breaches (Jimmy marks, sheared deadbolts)
  - Spent Ballistic Shell Casings
- **Forensic HUD Overlay**: Renders millimeter reticles, evidence tent badges (`EV-MK-1`), confidence scores, and normalized spatial bounding boxes.
- **Actionable Tactical Leads**: Immediate prioritized next steps (NIBIN ballistics matching, DNA swabbing, Mikrosil toolmark casting).

### 3. Tab 2 — Witness Audio Transcription & Timeline (Epic 3)
- **Whisper & Multimodal Acoustic Analysis**: Processes 911/112 emergency calls and field witness recordings.
- **Voice Stress Analysis (VSA)**: Quantifies vocal microtremor and pitch perturbation (e.g. 84% - Acute Panic).
- **Speaker Diarization**: Chronological segmentation separating CALLER, DISPATCHER, and WITNESS statements.
- **Entity Extraction**: Automatically isolates weapons mentioned, acoustic gunshots, vehicle descriptions, and flight vectors.

### 4. Tab 3 — CCTV Video Analysis & Event Progression (Epic 4)
- **Surveillance Frame Sampling**: Chronological keyframe inspection across incident seconds (`T+00` to `T+44`).
- **Suspect & Vehicle Trajectory Tracking**: Calculates movement velocity (m/s) and spatial vectors.
- **Statutory Legal Penal Codification**: Maps each event to penal code statutes (e.g. Criminal Trespass, Possession of Burglary Tools, Aggravated Assault with Deadly Weapon, Grand Larceny 1st Degree, Vehicular Elusion).

### 5. Tab 4 — Multimodal Fusion & Grounded Evidence Chat (Epic 5)
- **Unified Master Event Ledger**: Blends image, audio, and CCTV timestamps into a consolidated timeline.
- **Grounded RAG Interrogation**: Natural language investigator Q&A with **zero hallucination** and mandatory citation of Evidence IDs (e.g., `[EV-IMG-001]`, `[EV-AUD-001]`, `[EV-VID-001]`, `[LED-003]`).

### 6. Tab 5 — Automated Forensic PDF Export (Epic 6)
- **1-Click Court-Admissible Dossier**: Generates publication-grade forensic summary reports via **ReportLab**.
- **Self-Authenticating Legal Stamp**: Embeds SHA-256 manifests, custody register tables, verbatim transcripts, and investigator certification blocks.

---

## 🚀 Rapid Local Deployment

### Prerequisites
- Python 3.10, 3.11, 3.12, 3.13, or 3.14
- Git

### Installation
```bash
# Clone the repository
git clone https://github.com/your-username/CrimeVision-AI.git
cd CrimeVision-AI

# Install dependencies (zero external DB required)
pip install -r requirements.txt

# Launch the Streamlit application
streamlit run app.py
```

---

## 🌐 Streamlit Community Cloud Deployment
This project is configured with zero external database dependencies (uses in-memory session state and deterministic serialization) for 1-click deployment on Streamlit Community Cloud:
1. Push code to GitHub.
2. Go to [share.streamlit.io](https://share.streamlit.io).
3. Select your repository and point main file path to `app.py`.
4. Deploy!

---

## ⚖️ Legal & Evidentiary Compliance
- **FRE 901**: Digital evidence authentication via cryptographically unique SHA-256 hashing.
- **FRE 902**: Self-authenticating commercial records and forensic manifest seals.
- **FRE 803(2)**: Excited utterance preservation in emergency 911 audio transcriptions.
