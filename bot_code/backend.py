import json
import os

def load_mod_data():
    json_path = os.path.join("resources", "skyblock", "mods.json")
    with open(json_path, "r") as f:
        return json.load(f)

def get_mod_info(modname):
    mods = load_mod_data()
    
    mod = mods.get(modname.lower())
    if not mod:
        return f"Mod '{modname}' not found."
    
    # Format the mod information
    name = mod.get("name", "Unknown Mod")
    description = mod.get("description", {}).get("summary", "No description available.")
    features = mod.get("description", {}).get("features", [])
    
    # Format description and features
    description_text = f"{description}\nFeatures: " + ", ".join(features) if features else description
    
    # Format links
    links = mod.get("links", [])
    links_text = "\n".join([f"[{link['name']}]({link['url']})" for link in links])
    
    # Combine everything into the response
    return f"**{name}**\n\n{description_text}\n\n**Links:**\n{links_text}"

def handle_ping_command(latency):
    latency_ms = round(latency * 1000)  # Convert latency to milliseconds
    return f"Pong! 🏓 Latency: {latency_ms}ms"
