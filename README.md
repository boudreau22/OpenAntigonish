# OpenAntigonish Vaccine Timeline

This project provides a timeline of COVID-19 vaccine developments, including key milestones for Pfizer/BioNTech, Moderna, Johnson & Johnson, and Novavax.

## Data

The data is stored in `vaccine_timeline.json` and includes:
- **pfizerFacts**: Specific milestones for the Pfizer vaccine.
- **pfizerTimeline**: Phases and periods for the Pfizer vaccine.
- **otherVaccines**: Milestones for Moderna, J&J, and Novavax.

## Visualization

To view the interactive timeline, you need to run a local web server because modern browsers block `fetch` requests for local files (`file://`).

1. Ensure you have Python installed.
2. Run the following command in the project directory:
   ```bash
   python3 -m http.server
   ```
3. Open your browser and navigate to `http://localhost:8000/index.html`.

## Validation

To validate the integrity of the data file, run:
```bash
python3 validate_data.py
```
