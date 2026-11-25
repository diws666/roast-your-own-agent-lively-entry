import os

# Verified count: 107 characters (UTF-8 bytes match the entry gate exactly).
LINE = "I asked my agent for one win. It gave me 82 entries, zero rewards, and a very detailed log of its failures."

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
output_path = os.path.join(output_dir, "entry.txt")

with open(output_path, "w", encoding="utf-8", newline="") as f:
    f.write(LINE)

print(len(LINE))
