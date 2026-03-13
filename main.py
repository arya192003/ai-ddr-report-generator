from src.extract_pdf import extract_text
from src.extract_images import extract_images
from src.ddr_generator import generate_ddr

inspection_file = "data/inspection.pdf"
thermal_file = "data/thermal.pdf"

print("Extracting text...")

inspection_text = extract_text(inspection_file)
thermal_text = extract_text(thermal_file)

print("Extracting images...")

inspection_images = extract_images(inspection_file)
thermal_images = extract_images(thermal_file)

print("Generating DDR Report...")

ddr = generate_ddr(inspection_text, thermal_text)

import os

os.makedirs("output", exist_ok=True)

with open("output/final_ddr.md", "w", encoding="utf-8") as f:
    f.write(ddr)

print("DDR report generated successfully!")