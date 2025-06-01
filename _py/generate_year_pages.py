import yaml
from pathlib import Path
import glob

# Find all .yml files in the current directory (sorted for sanity)
yml_files = sorted(glob.glob("*.yml"))

all_entries = []

# Load and merge all YAML entries
for file in yml_files:
    with open(file, 'r') as f:
        entries = yaml.safe_load(f)
        all_entries.extend(entries)

# Ensure _years/ exists
output_dir = Path('_years')
output_dir.mkdir(exist_ok=True)

# Template for each year page
template = """---
layout: year
title: "{title}"
year: {year}
intro: "{intro}"
involved: "{involved}"
---
"""

# Create markdown files
for entry in all_entries:
    filename = output_dir / f"{entry['year']}.md"
    with open(filename, 'w') as f:
        f.write(template.format(
            title=entry['title'].replace('"', '\\"'),
            year=entry['year'],
            intro=entry['intro'].replace('"', '\\"'),
            involved=entry['involved'].replace('"', '\\"')
        ))

print(f"✅ Generated {len(all_entries)} year pages in _years/")
