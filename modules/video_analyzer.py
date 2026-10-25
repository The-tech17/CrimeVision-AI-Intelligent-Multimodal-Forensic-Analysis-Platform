"""
CCTV Video Analysis & Event Progression Module (Epic 4)
Processes surveillance video streams, samples chronological keyframes,
tracks suspect/vehicle movement trajectories, and classifies legal penal categories.
"""

from typing import Dict, Any, List, Optional
from PIL import Image, ImageDraw, ImageFont


def generate_cctv_frame_graphic(
    frame_info: Dict[str, Any],
    camera_id: str = "CAM-04 VAULT FOYER"
) -> Image.Image:
    """
    Renders high-authenticity CCTV surveillance frame with tactical timestamp burn-ins,
    scanlines, camera crosshairs, suspect coordinate bounding reticles, and velocity vectors.
    """
    width, height = 720, 420
    img = Image.new("RGB", (width, height), (10, 14, 20))
    draw = ImageDraw.Draw(img)

    # Grayscale hallway floor and walls
    horizon = 180
    draw.rectangle([0, 0, width, horizon], fill=(22, 26, 34))
    
    # Floor perspective tiles
    for x in range(0, width, 70):
        draw.line([(x, horizon), (int(width/2 + (x - width/2) * 2.0), height)], fill=(32, 38, 50), width=1)
    for y in range(horizon, height, 35):
        draw.line([(0, y), (width, y)], fill=(30, 36, 46), width=1)

    # Simulated CRT Scanlines
    for y in range(0, height, 4):
        draw.line([(0, y), (width, y)], fill=(0, 0, 0), width=1)

    # Vault Door on Left
    draw.rectangle([30, 50, 200, 300], fill=(40, 48, 62), outline=(75, 88, 110), width=2)
    draw.ellipse([90, 130, 140, 180], outline=(120, 140, 170), width=2)

    # Suspect Tracking Position & Reticle
    coords = frame_info.get("tracking_coordinates", {"x": 0.5, "y": 0.5})
    sx = int(coords["x"] * width)
    sy = int(coords["y"] * height)
    target_type = frame_info.get("target_type", "Suspect #1")
    velocity = frame_info.get("velocity_mps", 1.5)

    # Draw suspect silhouette / vehicle based on target type
    if "Vehicle" in target_type or "Transit" in target_type:
        # Van outline
        draw.rectangle([sx - 100, sy - 50, sx + 100, sy + 30], fill=(35, 40, 52), outline=(0, 229, 255), width=2)
        draw.rectangle([sx - 90, sy - 40, sx - 20, sy - 15], fill=(70, 90, 120))  # Window
        draw.ellipse([sx - 70, sy + 20, sx - 40, sy + 50], fill=(15, 15, 20))   # Wheel
        draw.ellipse([sx + 40, sy + 20, sx + 70, sy + 50], fill=(15, 15, 20))    # Wheel
    else:
        # Human suspect figure
        draw.ellipse([sx - 18, sy - 55, sx + 18, sy - 20], fill=(18, 22, 30), outline=(0, 229, 255), width=2)
        draw.polygon([(sx - 25, sy - 20), (sx + 25, sy - 20), (sx + 20, sy + 45), (sx - 20, sy + 45)], fill=(25, 30, 40), outline=(0, 229, 255), width=1)
        draw.line([(sx - 10, sy + 45), (sx - 15, sy + 90)], fill=(20, 25, 35), width=8)
        draw.line([(sx + 10, sy + 45), (sx + 15, sy + 90)], fill=(20, 25, 35), width=8)

    # Tactical Tracking Box around target
    box_w, box_h = 70, 110
    draw.rectangle([sx - box_w//2, sy - 65, sx + box_w//2, sy + 55], outline=(0, 229, 255), width=2)
    # Velocity Vector Arrow
    vector_len = int(velocity * 8)
    draw.line([(sx, sy), (sx + vector_len, sy - int(vector_len * 0.4))], fill=(255, 234, 0), width=2)

    # Label on Target
    try:
        font = ImageFont.load_default()
    except Exception:
        font = None
    target_tag = f"TRACK: {target_type} [{velocity:.1f} m/s]"
    draw.rectangle([sx - box_w//2, sy - 85, sx - box_w//2 + len(target_tag)*7, sy - 67], fill=(0, 229, 255))
    draw.text((sx - box_w//2 + 3, sy - 83), target_tag, fill=(0, 0, 0), font=font)

    # CCTV Burn-In Header (Green/Cyan Monochrome Tactical OSD)
    sec_offset = frame_info.get("sec_offset", "T+00:00")
    frame_idx = frame_info.get("frame_index", 0)
    actual_time = frame_info.get("timestamp", "02:41:10 EST")
    penal_code = frame_info.get("penal_code", "N/A")

    # Dark banner bar at top
    draw.rectangle([0, 0, width, 32], fill=(8, 12, 16))
    draw.text((12, 8), f"● REC [LIVE FEED]  |  {camera_id}  |  FRAME #{frame_idx:04d}", fill=(0, 255, 128), font=font)
    draw.text((width - 180, 8), f"{actual_time} ({sec_offset})", fill=(0, 229, 255), font=font)

    # Bottom Penal Code Banner
    draw.rectangle([0, height - 30, width, height], fill=(12, 16, 22))
    draw.text((12, height - 22), f"LEGAL PENAL CODIFICATION: {penal_code}", fill=(255, 170, 0), font=font)
    draw.text((width - 160, height - 22), "FPS: 30.00  |  4K UHD", fill=(140, 160, 180), font=font)

    return img


def compile_trajectory_data(event_progression: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Transforms sequential frame events into structured trajectory path vectors for visualization.
    """
    trajectory_points = []
    for item in event_progression:
        coords = item.get("tracking_coordinates", {"x": 0.5, "y": 0.5})
        trajectory_points.append({
            "Time Offset": item.get("sec_offset", "T+00"),
            "Frame": item.get("frame_index", 0),
            "Target": item.get("target_type", "Target"),
            "Coord X": coords["x"],
            "Coord Y": coords["y"],
            "Velocity (m/s)": item.get("velocity_mps", 0.0),
            "Penal Charge": item.get("penal_code", "N/A"),
            "Event Summary": item.get("event_summary", "")
        })
    return trajectory_points
