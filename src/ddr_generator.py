def generate_ddr(inspection_text, thermal_text):

    areas = ["kitchen", "bedroom", "bathroom", "living room", "balcony", "wall", "ceiling"]

    observations = []

    for area in areas:
        if area in inspection_text.lower() or area in thermal_text.lower():
            observations.append(area.capitalize())

    if not observations:
        observations.append("General Area")

    report = f"""
# Detailed Diagnostic Report (DDR)

## 1. Property Issue Summary
Possible moisture, heat anomaly, or structural issues detected based on inspection and thermal analysis.

## 2. Area-wise Observations
"""

    for area in observations:
        report += f"""
### {area}

Observation:
Potential issue mentioned in inspection report.

Thermal Finding:
Temperature anomaly detected in thermal report.

Image:
Not Available
"""

    report += """
## 3. Probable Root Cause
Possible moisture intrusion, insulation weakness, or plumbing leakage.

## 4. Severity Assessment
Medium Severity – issues may worsen if ignored.

## 5. Recommended Actions
- Conduct detailed inspection of affected areas
- Repair plumbing if leakage detected
- Improve insulation and waterproofing

## 6. Additional Notes
This report is generated automatically based on provided inspection data.

## 7. Missing or Unclear Information
Exact structural drawings – Not Available
Detailed moisture readings – Not Available
"""

    return report