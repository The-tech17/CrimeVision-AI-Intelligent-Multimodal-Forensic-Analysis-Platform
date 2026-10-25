"""
Forensic Demo Cases & Synthetic Crime Scene Evidence Repository
Provides realistic, multi-layered forensic cases for immediate demonstration and validation.
"""

from typing import Dict, Any, List

CASES: Dict[str, Dict[str, Any]] = {
    "CASE-2026-CR-0894": {
        "case_id": "CASE-2026-CR-0894",
        "title": "Sovereign Diamond Vault Armed Breach & Homicide Investigation",
        "incident_type": "Armed Robbery / Aggravated Assault with Deadly Weapon / Homicide",
        "primary_penal_code": "18 U.S.C. § 2113(d) / N.Y. Penal Law § 160.15 (Robbery 1st)",
        "lead_investigator": "Det. Marcus Vance",
        "badge_id": "BADGE-7491-NYPD-CSU",
        "jurisdiction": "Major Case Squad / Forensic Investigation Division",
        "incident_datetime": "2026-10-24 02:41:10 EST",
        "incident_location": "580 5th Avenue, Suite 300, Diamond District, NY",
        
        # Visual Evidence (Tab 1 - Epic 2)
        "visual_evidence": {
            "evidence_id": "EV-IMG-001",
            "description": "High-resolution forensic photographic capture of vault room foyer & breached security threshold.",
            "scene_classification": "Armed Burglary & Homicide Crime Scene",
            "threat_level": "CRITICAL",
            "camera_metadata": "Nikon D850 Forensic Macro-Kit | ISO 800 | f/5.6 | 1/125s | Crime Scene Unit Tag #449",
            "detected_objects": [
                {
                    "label": "firearm_handgun",
                    "category": "Deadly Weapon",
                    "confidence": 0.964,
                    "bbox": [0.38, 0.52, 0.54, 0.69],  # [ymin, xmin, ymax, xmax] normalized
                    "threat": "CRITICAL",
                    "notes": "Semi-automatic polymer frame handgun (9x19mm Glock-style profile). Slide in locked forward battery.",
                    "marker_id": "EV-MK-1"
                },
                {
                    "label": "masked_suspect",
                    "category": "Person of Interest",
                    "confidence": 0.941,
                    "bbox": [0.12, 0.44, 0.88, 0.74],
                    "threat": "HIGH",
                    "notes": "Adult male, est. height 5ft 11in, tactical balaclava mask, dark Carhartt-style jacket, black nitrile gloves.",
                    "marker_id": "EV-MK-2"
                },
                {
                    "label": "blood_spatter_pool",
                    "category": "Biological Fluid",
                    "confidence": 0.918,
                    "bbox": [0.71, 0.22, 0.89, 0.46],
                    "threat": "CRITICAL",
                    "notes": "Arterial cast-off trajectory radiating from west wall terminating in 18cm pooling. Immediate DNA extraction priority.",
                    "marker_id": "EV-MK-3"
                },
                {
                    "label": "forced_entry_breach",
                    "category": "Structural Breach",
                    "confidence": 0.895,
                    "bbox": [0.08, 0.06, 0.62, 0.28],
                    "threat": "MEDIUM",
                    "notes": "Heavy door jamb deformation. Sheared magnetic lock armature plate; secondary hydraulic tool impression striations.",
                    "marker_id": "EV-MK-4"
                },
                {
                    "label": "spent_shell_casing",
                    "category": "Ballistic Artifact",
                    "confidence": 0.882,
                    "bbox": [0.79, 0.61, 0.84, 0.67],
                    "threat": "HIGH",
                    "notes": "Single brass casing, headstamp 'WIN 9mm LUGER'. Firing pin strike indentation visible on primer cup.",
                    "marker_id": "EV-MK-5"
                }
            ],
            "investigative_leads": [
                "1. Immediate NIBIN Submission: Expedite spent 9mm casing [EV-MK-5] for automated ballistic comparison against regional active gang/robbery databases.",
                "2. Urgent DNA PCR Profiling: Swab arterial spatter pattern [EV-MK-3] at the door threshold to confirm victim vs. suspect blood profile.",
                "3. Toolmark Striation Casting: Apply Mikrosil silicone elastomer to sheared lock armature [EV-MK-4] to identify specific hydraulic wedge tool model.",
                "4. Suspect Gait & Attire Triangulation: Cross-index black tactical apparel [EV-MK-2] against perimeter transit station surveillance."
            ]
        },

        # Witness Audio / 911 Recording (Tab 2 - Epic 3)
        "audio_evidence": {
            "evidence_id": "EV-AUD-001",
            "source_type": "Emergency 911 Call Recording - Dispatch Trunk #4",
            "caller_id": "Arthur Pendelton (Senior Building Night Security Officer)",
            "call_timestamp": "2026-10-24 02:42:25 EST",
            "duration_seconds": 48.5,
            "overall_stress_level": 84,  # Percentile
            "voice_stress_classification": "ACUTE PANIC / ELEVATED VOCAL MICROTREMOR",
            "transcripts": [
                {
                    "timestamp": "00:00 - 00:04",
                    "speaker": "DISPATCHER",
                    "text": "911 Emergency. What is your location and emergency?",
                    "stress_score": 12,
                    "event_tag": "CALL_INITIATED"
                },
                {
                    "timestamp": "00:05 - 00:11",
                    "speaker": "CALLER (Arthur)",
                    "text": "This is Central Security at the Diamond Exchange on 5th! Silent seismic trip alarm triggered in vault room 3B!",
                    "stress_score": 78,
                    "event_tag": "ALARM_REPORTED"
                },
                {
                    "timestamp": "00:12 - 00:17",
                    "speaker": "CALLER (Arthur)",
                    "text": "[Audible Tremor] Oh God... I just heard glass shattering and two loud bangs! Gunshots down corridor B!",
                    "stress_score": 93,
                    "event_tag": "GUNSHOTS_AUDIBLE"
                },
                {
                    "timestamp": "00:18 - 00:23",
                    "speaker": "DISPATCHER",
                    "text": "Units are rolling code 3. Are you sheltered in place? Can you see weapons or perpetrators?",
                    "stress_score": 18,
                    "event_tag": "TACTICAL_RESPONSE_DISPATCHED"
                },
                {
                    "timestamp": "00:24 - 00:33",
                    "speaker": "CALLER (Arthur)",
                    "text": "I see him on monitor 4! Male in full black tactical gear, carrying a black semi-automatic pistol and a red crowbar! He just kicked through the fire door!",
                    "stress_score": 88,
                    "event_tag": "PERPETRATOR_SIGHTED"
                },
                {
                    "timestamp": "00:34 - 00:39",
                    "speaker": "DISPATCHER",
                    "text": "Copy: male, black tactical gear, armed with handgun. Do you have eyes on a getaway vehicle?",
                    "stress_score": 20,
                    "event_tag": "BOLO_BROADCAST"
                },
                {
                    "timestamp": "00:40 - 00:48",
                    "speaker": "CALLER (Arthur)",
                    "text": "Yes! Dark gray Ford Transit van, tinted windows, partial plate 'K-7-9'... tires just screeched away northbound on 5th!",
                    "stress_score": 85,
                    "event_tag": "GETAWAY_VEHICLE_LOGGED"
                }
            ],
            "extracted_entities": {
                "Weapons Mentioned": ["Black semi-automatic handgun", "Red steel crowbar / pry bar"],
                "Acoustic Events": ["Seismic alarm trigger", "Glass shatter", "2x Gunshot discharges (9mm acoustics)"],
                "Perpetrator Physicals": ["Male", "Full black tactical gear", "Balaclava face covering"],
                "Getaway Vehicle": ["Dark gray Ford Transit cargo van", "Tinted privacy glass", "Partial plate 'K79'"],
                "Flight Vector": "Northbound on 5th Avenue toward 48th St."
            }
        },

        # CCTV Video & Event Progression (Tab 3 - Epic 4)
        "video_evidence": {
            "evidence_id": "EV-VID-001",
            "camera_id": "CAM-04 (Vault Corridor Internal Dome - 4K 30fps)",
            "time_window": "02:41:10 - 02:44:30 EST",
            "frame_rate": 30,
            "total_sampled_frames": 6,
            "event_progression": [
                {
                    "sec_offset": "T+00:02",
                    "frame_index": 48,
                    "timestamp": "02:41:12 EST",
                    "event_summary": "Suspect in black tactical hoodie enters corridor via West stairwell fire exit.",
                    "legal_classification": "Criminal Trespass / Burglary in Progress",
                    "penal_code": "N.Y. Penal Law § 140.15",
                    "tracking_coordinates": {"x": 0.15, "y": 0.35},
                    "target_type": "Suspect #1",
                    "velocity_mps": 1.4
                },
                {
                    "sec_offset": "T+00:08",
                    "frame_index": 192,
                    "timestamp": "02:41:18 EST",
                    "event_summary": "Mechanical breach of vault foyer perimeter door utilizing high-tensile pry tool.",
                    "legal_classification": "Possession of Burglary Tools & Criminal Mischief 2nd",
                    "penal_code": "N.Y. Penal Law § 140.35 & § 145.10",
                    "tracking_coordinates": {"x": 0.32, "y": 0.42},
                    "target_type": "Suspect #1 + Burglary Tool",
                    "velocity_mps": 0.2
                },
                {
                    "sec_offset": "T+00:15",
                    "frame_index": 360,
                    "timestamp": "02:41:25 EST",
                    "event_summary": "Suspect encounters guard station; draws handgun from right waistband. Single muzzle flash captured.",
                    "legal_classification": "Aggravated Assault with Deadly Weapon / Brandishing Firearm",
                    "penal_code": "N.Y. Penal Law § 120.10 & § 265.03",
                    "tracking_coordinates": {"x": 0.58, "y": 0.50},
                    "target_type": "Firearm Discharge",
                    "velocity_mps": 0.0
                },
                {
                    "sec_offset": "T+00:23",
                    "frame_index": 552,
                    "timestamp": "02:41:33 EST",
                    "event_summary": "Suspect breaches internal safe shelf #4; sweeps certified loose diamond packets into canvas duffle.",
                    "legal_classification": "Grand Larceny 1st Degree (Theft > $1,000,000)",
                    "penal_code": "N.Y. Penal Law § 155.42",
                    "tracking_coordinates": {"x": 0.72, "y": 0.65},
                    "target_type": "High-Value Asset Seizure",
                    "velocity_mps": 0.6
                },
                {
                    "sec_offset": "T+00:32",
                    "frame_index": 768,
                    "timestamp": "02:41:42 EST",
                    "event_summary": "Suspect sprints past camera towards North loading dock door; blood trail visibly left on floor.",
                    "legal_classification": "Flight from Felony Crime Scene",
                    "penal_code": "N.Y. Penal Law § 195.05",
                    "tracking_coordinates": {"x": 0.88, "y": 0.30},
                    "target_type": "Suspect #1 Flight",
                    "velocity_mps": 3.8
                },
                {
                    "sec_offset": "T+00:44",
                    "frame_index": 1056,
                    "timestamp": "02:41:54 EST",
                    "event_summary": "CAM-08 (Loading Dock): Dark gray Ford Transit van accelerates rapidly out of alleyway into traffic.",
                    "legal_classification": "Facilitating Felony Escape / Vehicular Elusion",
                    "penal_code": "N.Y. Penal Law § 115.05",
                    "tracking_coordinates": {"x": 0.95, "y": 0.15},
                    "target_type": "Getaway Vehicle (Ford Transit)",
                    "velocity_mps": 9.2
                }
            ]
        },

        # Master Fused Event Ledger (Tab 4 - Epic 5)
        "master_ledger": [
            {
                "ledger_id": "LED-001",
                "timestamp": "2026-10-24 02:41:12 EST",
                "evidence_id": "EV-VID-001",
                "modality": "CCTV VIDEO",
                "source": "CAM-04 (Frame #48)",
                "event_type": "PERIMETER_BREACH",
                "threat": "HIGH",
                "description": "Suspect in black tactical hoodie enters corridor via West stairwell fire exit.",
                "legal_tag": "N.Y. Penal Law § 140.15 (Criminal Trespass)",
                "corroborated_by": ["CAM-02 Stairwell Sensor"]
            },
            {
                "ledger_id": "LED-002",
                "timestamp": "2026-10-24 02:41:18 EST",
                "evidence_id": "EV-VID-001",
                "modality": "CCTV VIDEO",
                "source": "CAM-04 (Frame #192)",
                "event_type": "STRUCTURAL_FORCED_ENTRY",
                "threat": "HIGH",
                "description": "Mechanical breach of vault door using red pry bar.",
                "legal_tag": "N.Y. Penal Law § 140.35 (Burglary Tools)",
                "corroborated_by": ["EV-IMG-001 (Toolmark Striations at [0.08, 0.06])"]
            },
            {
                "ledger_id": "LED-003",
                "timestamp": "2026-10-24 02:41:25 EST",
                "evidence_id": "EV-VID-001",
                "modality": "CCTV VIDEO",
                "source": "CAM-04 (Frame #360)",
                "event_type": "WEAPON_DISCHARGE",
                "threat": "CRITICAL",
                "description": "Suspect brandishes handgun and fires single shot down corridor.",
                "legal_tag": "N.Y. Penal Law § 120.10 (Aggravated Assault / Weapon Discharge)",
                "corroborated_by": [
                    "EV-IMG-001 (Firearm & 9mm Casing at [0.79, 0.61])",
                    "EV-AUD-001 (911 Call Witness Reports Gunshots at 00:14)"
                ]
            },
            {
                "ledger_id": "LED-004",
                "timestamp": "2026-10-24 02:41:33 EST",
                "evidence_id": "EV-VID-001",
                "modality": "CCTV VIDEO",
                "source": "CAM-04 (Frame #552)",
                "event_type": "ASSET_THEFT",
                "threat": "HIGH",
                "description": "Theft of certified loose diamond parcel valued at $1.4M.",
                "legal_tag": "N.Y. Penal Law § 155.42 (Grand Larceny 1st)",
                "corroborated_by": ["Vault Inventory Ledger #D-89"]
            },
            {
                "ledger_id": "LED-005",
                "timestamp": "2026-10-24 02:41:42 EST",
                "evidence_id": "EV-IMG-001",
                "modality": "CRIME SCENE PHOTO",
                "source": "Forensic Macro Unit (Tag #449)",
                "event_type": "BIOLOGICAL_DEPOSITION",
                "threat": "CRITICAL",
                "description": "Arterial blood spray and drip pool deposited at vault threshold during suspect flight.",
                "legal_tag": "Physical Biological Evidence (CODIS Eligible)",
                "corroborated_by": ["EV-VID-001 (Suspect Sprints Towards Exit at T+00:32)"]
            },
            {
                "ledger_id": "LED-006",
                "timestamp": "2026-10-24 02:42:25 EST",
                "evidence_id": "EV-AUD-001",
                "modality": "911 WITNESS AUDIO",
                "source": "Dispatch Trunk Line #4",
                "event_type": "WITNESS_STATEMENT",
                "threat": "MEDIUM",
                "description": "Night guard Arthur Pendelton reports suspect description, gunfire, and gray Transit getaway van.",
                "legal_tag": "Excited Utterance / Present Sense Impression (FRE 803(2))",
                "corroborated_by": [
                    "EV-VID-001 (Van Acceleration at T+00:44)",
                    "EV-IMG-001 (Masked Suspect Attire Profile)"
                ]
            },
            {
                "ledger_id": "LED-007",
                "timestamp": "2026-10-24 02:44:00 EST",
                "evidence_id": "EV-VID-002",
                "modality": "STREET CCTV",
                "source": "NYPD Argus Camera 5th & 48th",
                "event_type": "GETAWAY_CORROBORATION",
                "threat": "HIGH",
                "description": "Dark gray Ford Transit van observed speeding through red light at 5th and 48th.",
                "legal_tag": "Vehicle Flight Tracking",
                "corroborated_by": ["EV-AUD-001 (Caller Partial Plate 'K79')"]
            }
        ]
    },
    
    "CASE-2026-CR-1142": {
        "case_id": "CASE-2026-CR-1142",
        "title": "Pacific Trust Financial Perimeter Penetration & Safe Breach",
        "incident_type": "Commercial Nighttime Burglary / Thermal Lance Safe Breach",
        "primary_penal_code": "Cal. Pen. Code § 459 / § 464 (Burglary with Explosives or Torch)",
        "lead_investigator": "Insp. Elena Rostova",
        "badge_id": "BADGE-3312-SFPD-CSI",
        "jurisdiction": "Robbery & Burglary Division - San Francisco",
        "incident_datetime": "2026-10-22 03:15:00 PST",
        "incident_location": "400 California Street, Financial District, SF",
        
        "visual_evidence": {
            "evidence_id": "EV-IMG-002",
            "description": "Nighttime macro photo of breached rear reinforced alloy steel wall.",
            "scene_classification": "Commercial Safe Burglary Crime Scene",
            "threat_level": "HIGH",
            "camera_metadata": "Canon EOS R5C | ISO 1600 | f/4.0 | 1/60s",
            "detected_objects": [
                {
                    "label": "thermal_cutting_torch",
                    "category": "Burglary Tool / Weapon",
                    "confidence": 0.952,
                    "bbox": [0.45, 0.35, 0.68, 0.58],
                    "threat": "HIGH",
                    "notes": "Portable oxy-acetylene mini torch kit with blue nozzle tip.",
                    "marker_id": "EV-MK-1"
                },
                {
                    "label": "reinforced_wall_breach",
                    "category": "Structural Breach",
                    "confidence": 0.938,
                    "bbox": [0.20, 0.15, 0.75, 0.50],
                    "threat": "MEDIUM",
                    "notes": "Precision circular cutout in 8mm rolled steel safe wall.",
                    "marker_id": "EV-MK-2"
                },
                {
                    "label": "heavy_prybar",
                    "category": "Toolmark Source",
                    "confidence": 0.915,
                    "bbox": [0.72, 0.55, 0.88, 0.78],
                    "threat": "MEDIUM",
                    "notes": "36-inch yellow crowbar with paint transfer at point of fulcrum.",
                    "marker_id": "EV-MK-3"
                }
            ],
            "investigative_leads": [
                "1. Trace Chemical Analysis: Swab slag remnants on thermal cutout [EV-MK-2] for flux signature.",
                "2. Paint Transfer Spectrometry: Analyze yellow paint on crowbar [EV-MK-3] against hardware distributors."
            ]
        },
        
        "audio_evidence": {
            "evidence_id": "EV-AUD-002",
            "source_type": "Alarm Company Monitoring Dispatch Recording",
            "caller_id": "ADT Commercial Central Monitoring Station",
            "call_timestamp": "2026-10-22 03:18:10 PST",
            "duration_seconds": 32.0,
            "overall_stress_level": 45,
            "voice_stress_classification": "MODERATE PROFESSIONAL URGENCY",
            "transcripts": [
                {
                    "timestamp": "00:00 - 00:06",
                    "speaker": "DISPATCHER",
                    "text": "SFPD Emergency, Operator 42.",
                    "stress_score": 10,
                    "event_tag": "CALL_INITIATED"
                },
                {
                    "timestamp": "00:07 - 00:15",
                    "speaker": "ALARM AGENT",
                    "text": "This is ADT Commercial. We have multiple thermal sensor and motion trips at Pacific Trust on California.",
                    "stress_score": 42,
                    "event_tag": "SENSOR_ALARM"
                },
                {
                    "timestamp": "00:16 - 00:25",
                    "speaker": "ALARM AGENT",
                    "text": "Video verification shows two subjects in dark jumpsuits exiting through rear alley with large black duffle bags.",
                    "stress_score": 50,
                    "event_tag": "SUSPECTS_CONFIRMED"
                }
            ],
            "extracted_entities": {
                "Weapons/Tools": ["Thermal cutting equipment", "Prybars"],
                "Perpetrators": ["Two individuals, dark jumpsuits"],
                "Flight Vector": "Rear alley toward Montgomery Street"
            }
        },

        "video_evidence": {
            "evidence_id": "EV-VID-002",
            "camera_id": "CAM-01 (Rear Commercial Alleyway High-Def)",
            "time_window": "03:14:00 - 03:19:00 PST",
            "frame_rate": 30,
            "total_sampled_frames": 4,
            "event_progression": [
                {
                    "sec_offset": "T+00:00",
                    "frame_index": 0,
                    "timestamp": "03:14:15 PST",
                    "event_summary": "Two figures carrying heavy gear bags enter alleyway on foot.",
                    "legal_classification": "Criminal Trespass",
                    "penal_code": "Cal. Pen. Code § 602",
                    "tracking_coordinates": {"x": 0.22, "y": 0.70},
                    "target_type": "2x Suspects",
                    "velocity_mps": 1.2
                },
                {
                    "sec_offset": "T+00:20",
                    "frame_index": 600,
                    "timestamp": "03:18:35 PST",
                    "event_summary": "Both suspects emerge running with bulging duffle bags; mount a matte-black sport motorcycle.",
                    "legal_classification": "Burglary & Evading Arrest",
                    "penal_code": "Cal. Pen. Code § 459 / Veh. Code § 2800.1",
                    "tracking_coordinates": {"x": 0.85, "y": 0.40},
                    "target_type": "Motorcycle Flight",
                    "velocity_mps": 12.5
                }
            ]
        },

        "master_ledger": [
            {
                "ledger_id": "LED-101",
                "timestamp": "2026-10-22 03:14:15 PST",
                "evidence_id": "EV-VID-002",
                "modality": "CCTV VIDEO",
                "source": "CAM-01 Rear Alley",
                "event_type": "ALLEY_ENTRY",
                "threat": "MEDIUM",
                "description": "Two suspects enter alley carrying heavy equipment bags.",
                "legal_tag": "Cal. Pen. Code § 602 (Trespass)",
                "corroborated_by": ["CAM-02 Street Angle"]
            },
            {
                "ledger_id": "LED-102",
                "timestamp": "2026-10-22 03:15:30 PST",
                "evidence_id": "EV-IMG-002",
                "modality": "CRIME SCENE PHOTO",
                "source": "Forensic Macro Cam",
                "event_type": "THERMAL_BREACH",
                "threat": "HIGH",
                "description": "Thermal cutting torch breach into steel wall safe.",
                "legal_tag": "Cal. Pen. Code § 464 (Burglary with Torch)",
                "corroborated_by": ["EV-AUD-002 (Thermal Sensor Trip)"]
            },
            {
                "ledger_id": "LED-103",
                "timestamp": "2026-10-22 03:18:35 PST",
                "evidence_id": "EV-VID-002",
                "modality": "CCTV VIDEO",
                "source": "CAM-01 Rear Alley",
                "event_type": "MOTORCYCLE_ESCAPE",
                "threat": "HIGH",
                "description": "Suspects mount matte-black sport motorcycle and flee northbound.",
                "legal_tag": "Cal. Pen. Code § 459 (Burglary Flight)",
                "corroborated_by": ["EV-AUD-002 (ADT Operator Eye-Witness Account)"]
            }
        ]
    }
}
