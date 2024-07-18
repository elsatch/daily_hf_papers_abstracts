# HF Daily Papers Processor

This project automates the process of downloading, summarizing, and converting daily papers from Hugging Face into easily readable formats.

## Features

- Download daily papers from Hugging Face API
- Extract abstracts and generate markdown summaries
- Handle empty files and weekends/holidays
- Avoid reprocessing existing files

## Project Structure

```
hf_daily_papers/
│
├── data/
│   ├── input/  # Downloaded JSON files
│   ├── output/ # Generated markdown files
│
├── src/
│   ├── download_daily_papers.py
│   ├── daily_papers_abstract_extractor.py
│
└── README.md
```

## Installation

1. Clone this repository:

   ```
   git clone https://github.com/elsatch/daily_hf_papers_abstracts.git
   cd hf_daily_papers
   ```

2. Install the required dependencies:

   ```
   pip install requests
   ```

## Usage

1. Download daily papers:
   ```
   python src/download_daily_papers.py [YYYYMMDD]
   ```
   If no date is provided, it will download papers for the current date.

2. Process JSON files and generate markdown summaries:
   ```
   python src/daily_papers_abstract_extractor.py
   ```


## Notes

- The scripts handle empty files that may occur during weekends or holidays.
- Existing processed files are not overwritten to avoid unnecessary reprocessing.
- You can run these scripts daily to keep up with the latest papers.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](https://choosealicense.com/licenses/mit/).
