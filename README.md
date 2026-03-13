# ai-ddr-report-generator
AI system that converts inspection and thermal reports into a DDR report
# AI DDR Report Generator

This project automatically generates a DDR (Daily/Defect/Diagnostic Report) by analyzing inspection and thermal reports.

## Features

- Extracts text from inspection PDFs
- Extracts thermal images from reports
- Parses observations
- Automatically generates a structured DDR report

## Project Structure

ai-ddr-generator
│
├── data
│   ├── inspection.pdf
│   ├── thermal.pdf
│
├── images
│
├── src
│   ├── extract_pdf.py
│   ├── extract_images.py
│   ├── observation_parser.py
│   ├── ddr_generator.py
│
├── output
│   └── final_ddr.md
│
├── requirements.txt
└── main.py

## How to Run

Install dependencies:

pip install -r requirements.txt

Run the project:

python main.py

## Output

The system generates a DDR report in:

output/final_ddr.md

## Author

Arya
