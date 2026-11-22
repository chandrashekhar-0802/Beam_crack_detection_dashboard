# StructGuard AI

StructGuard AI is a local Streamlit dashboard for image-based crack records and calculated
Strength of Materials calculations.

## Run

```bat
cd "C:\Users\sujal\Downloads\SOM PROJECT\structguard_dashboard"
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Or run `run_dashboard.bat`.

## Data

- The dashboard works offline with preloaded/captured inspection records and no camera or hardware connection.
- Use **Crack Analytics** to upload an existing `inspections.csv`.
- `widths.csv` may be uploaded separately.
- Local project mode accepts a folder and searches for `inspections.csv`.
- Pixel measurements are not combined with millimetre measurements.

## Scientific scope

YOLO dimensions are surface image estimates. They do not determine stress, crack depth,
removed cross-sectional area, or structural safety. All material values and load inputs
must be treated as assumptions unless supplied and verified by the project team.
