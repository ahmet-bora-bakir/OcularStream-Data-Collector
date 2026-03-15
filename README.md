# OcularStream-Data-Collector
unfinished

A high-fidelity data logger and time-synchronization utility specifically designed for eye-tracking research, with native support for **The Eye Tribe** hardware.

## 🎯 Project Objective

The tool serves two main purposes:

1. **Complete Raw Data Capture**  
   Records the full, unaltered JSON output from the eye tracker to ensure no information is lost for subsequent offline analysis.

2. **Multi-Device Temporal Synchronization**  
   Provides a reliable temporal reference point, enabling accurate alignment of eye-tracking data with timestamps from computer's time data.

## 📊 Data Structure & Captured Metrics

Every tracking frame is stored exactly as received — a nested JSON object containing binocular gaze points, individual eye data, pupil metrics, fixation status, and hardware-reported timestamps.

### Example Recorded Frame (simplified real API structure):

```json
{
  "category": "tracker",
  "request": "get",
  "statuscode": 200,
  "values": {
    "frame": {
      "timestamp": "2026-02-09 15:47:31.523",
      "time": 1455020851523,
      "fix": true,
      "state": 7,
      "raw": {
        "x": 768.86,
        "y": 730.59
      },
      "avg": {
        "x": 768.86,
        "y": 730.59
      },
      "lefteye": {
        "avg": {
          "x": 698.94,
          "y": 580.62
        },
        "raw": {
          "x": 699.12,
          "y": 581.05
        },
        "pcenter": {
          "x": 0.3812,
          "y": 0.4927
        },
        "psize": 32.35,
        "pcf": 0.98
      },
      "righteye": {
        "avg": {
          "x": 837.74,
          "y": 866.46
        },
        "raw": {
          "x": 838.01,
          "y": 865.92
        },
        "pcenter": {
          "x": 0.6241,
          "y": 0.5034
        },
        "psize": 27.10,
        "pcf": 0.97
      }
    }
  }
}
```

> **Note:** The actual fields may vary slightly depending on tracker firmware version and API mode (push/pull). Refer to the official documentation for the complete and up-to-date object specification.

🔗 **Official Technical Documentation**  
For detailed API specifications, status codes, frame states, calibration routines, and protocol details:  
👉 [The Eye Tribe API Reference](https://github.com/EyeTribe/documentation)  
(or archived version at theeyetribe.com/dev if still available)

## 🚀 Key Features

- **Full-spectrum logging** — captures all available metrics: binocular averages, per-eye raw/averaged coordinates, pupil center & size, fixation flag, gaze state, confidence values, etc.
- **High-resolution timestamps** — preserves both string and millisecond UNIX-like time for precise synchronization
- **Research-oriented output** — plain JSON lines or structured files, easy to parse in Python (pandas/json), MATLAB, R, Julia, etc.
- **Minimal processing overhead** — near real-time logging with very low CPU usage
- **Synchronization-friendly** — consistent timestamp format to facilitate cross-modal alignment

## ⚠️ Important Notes & Disclaimer

- **Time Synchronization**  
  Although the tool logs high-precision timestamps provided by the Eye Tribe server, **absolute clock synchronization** across multiple devices remains the responsibility of the end-user (e.g. NTP, PTP, or shared hardware trigger).

- **Hardware Requirement**  
  An active Eye Tribe tracker and running Eye Tribe Server (or compatible driver) are required.

- **Liability**  
  This software is provided for research purposes only. The author assumes no responsibility for data loss, hardware damage, experimental errors, or any other consequences arising from its use. Users employ it at their own risk.

## ⚖️ License

GNU General Public License v3.0 (GPL-3.0)
