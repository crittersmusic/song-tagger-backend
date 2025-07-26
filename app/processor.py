import subprocess
import json

def extract_tags(audio_path: str):
    try:
        result = subprocess.run(
            ["./streaming_extractor_music", audio_path, "output.json"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
    except subprocess.CalledProcessError as e:
        return {"error": e.stderr.decode()}

    with open("output.json", "r") as f:
        data = json.load(f)

    tags = {
        "bpm": data.get("rhythm", {}).get("bpm"),
        "key": data.get("tonal", {}).get("key_key"),
        "scale": data.get("tonal", {}).get("key_scale"),
        "mood": data.get("mood", {}).get("sadness", None)
    }
    return tags
