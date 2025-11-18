# Remote Audio & Acoustic Harassment Research Data

[](https://opensource.org/licenses/MIT)
[](https://en.wikipedia.org/wiki/Comma-separated_values)
[](https://github.com/)

## 📖 Project Description

This repository contains comprehensive structured datasets and research materials dedicated to the investigation of **Remote Audio Harassment**, **Acoustic Intrusion**, and **Environmental Noise Pollution**.

The goal of this project is to provide a standardized glossary and technical reference for researchers, victims, legal professionals, and acousticians. The data bridges the gap between complex physics/engineering concepts (acoustics, signal processing, EMF) and the subjective or health-related experiences of those suffering from noise harassment in the home environment.

### Key Research Areas Covered:

  * **Noise Color Spectrum:** Detailed definitions of White, Pink, Brown, Blue, Violet, and Grey noise.
  * **Psychoacoustics:** Concepts explaining how the brain processes intrusive sound (e.g., The Haas Effect, Binaural Beats, Misophonia).
  * **Signal Physics:** Explanations of wave propagation, standing waves, resonance, and interference.
  * **Hardware:** Technical specifications of emitters (subwoofers, parametric speakers, tactile transducers) and detectors (spectrograms, accelerometers).
  * **Bio-Effects:** Documented physiological effects of infrasound and low-frequency noise.
  * **Legal & Investigative:** Terminology relevant to noise ordinances, nuisance laws, and evidence collection.

## 📂 File Structure

The core data is stored in CSV format for easy import into spreadsheet software (Excel, Google Sheets) or data analysis tools (Python/Pandas, R).

| File Name | Description | Rows |
| :--- | :--- | :--- |
| `Comprehensive_Audio_Harassment_Terms.csv` | **Master Dataset.** The most complete list covering all 11 categories, including bio-effects, advanced signal physics, and legal contexts. | 111+ |
| `Enriched_Audio_Sound_Terms_v2.csv` | A condensed version focusing primarily on definitions and frequency ranges of standard noise types and basic waveforms. | \~30 |
| `Audio_Sound_Master_Spreadsheet.csv` | The original raw data structure used to initialize the research. | N/A |

### Data Schema

Each CSV file typically follows this schema:

  * **Group:** The high-level domain (e.g., Physics, Hardware, Perception).
  * **Category:** Specific classification (e.g., Noise Types, Emitters, Bio-Effects).
  * **Term:** The specific subject matter.
  * **Definition:** Standard dictionary or technical definition.
  * **Characteristics/Range:** Technical specs (Frequency in Hz, Decibel behavior, etc.).
  * **Relevance:** Contextual explanation of how this term applies to home harassment scenarios.

## 🚀 Installation & Setup

To use this data, you can simply download the CSV files directly or clone the repository.

### 1\. Clone the Repository

```bash
git clone https://github.com/your-username/audio-harassment-research-data.git
cd audio-harassment-research-data
```

### 2\. (Optional) Python Environment

If you intend to analyze the data programmatically, we recommend setting up a Python environment.

```bash
pip install pandas
```

## 💻 Usage Examples

### Method 1: Spreadsheet Analysis

Simply open `Comprehensive_Audio_Harassment_Terms.csv` in Microsoft Excel, Apple Numbers, or Google Sheets. You can filter by **Category** to isolate specific research areas (e.g., filter for "Emitters" to see a list of devices capable of producing harassment).

### Method 2: Python/Pandas Analysis

You can use Python to query the dataset for specific frequency ranges or categories.

```python
import pandas as pd

# Load the master dataset
df = pd.read_csv('Comprehensive_Audio_Harassment_Terms.csv')

# Example 1: Find all terms related to "Infrasound" or Low Frequencies
low_freq = df[df['Characteristics/Range'].str.contains('Hz', na=False)]
print(low_freq[['Term', 'Characteristics/Range']].head())

# Example 2: Filter by specific category
hardware = df[df['Category'] == 'Emitters']
print(hardware[['Term', 'Relevance to Home/Harassment']])
```

## 🤝 Contribution Guidelines

Contributions are highly encouraged\! If you are an acoustician, legal expert, or researcher, please help us improve this database.

1.  **Fork** the repository.
2.  **Create a Branch** for your feature (`git checkout -b feature/add-new-terms`).
3.  **Add your changes.** (Please ensure new terms include a Definition and Relevance context).
4.  **Commit** your changes (`git commit -m 'Add definitions for Ultrasonic Heterodyning'`).
5.  **Push** to the branch (`git push origin feature/add-new-terms`).
6.  **Open a Pull Request**.

## ⚖️ Disclaimer

**For Informational Purposes Only:**
The information provided in this repository is for educational and research purposes. It does not constitute legal or medical advice.

**Health Warning:**
Some terms describe phenomena (e.g., Infrasound, Binaural Beats) that can have physiological effects. Users should exercise caution when generating or testing these signals.

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](https://www.google.com/search?q=LICENSE) file for details.

-----

*Generated by AI Data Assistant - November 2025*
