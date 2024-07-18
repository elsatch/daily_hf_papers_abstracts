import json
import os
import sys
from datetime import datetime
import re


def clean_text(text):
    # Replace newlines with spaces
    text = text.replace('\n', ' ')
    # Remove any resulting multiple spaces
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def json_to_markdown(json_data):
    if not json_data:
        return None  # Return None for empty data
    
    # Extract the date from the first paper's publishedAt field
    first_paper_date = datetime.fromisoformat(json_data[0]['paper']['publishedAt'].replace('Z', '+00:00'))
    date_str = first_paper_date.strftime('%Y-%m-%d')
    
    markdown_content = f"# Daily Papers Summary for {date_str}\n\n"
    
    for article in json_data:
        paper = article['paper']
        title = clean_text(paper['title'])
        summary = clean_text(paper['summary'])
        paper_id = paper['id']
        
        hf_link = f"https://huggingface.co/papers/{paper_id}"
        arxiv_link = f"https://arxiv.org/pdf/{paper_id}"
        
        markdown_content += f"## {title}\n\n"
        markdown_content += f"[Open in Hugging Face]({hf_link}) | [Open PDF]({arxiv_link})\n\n"
        markdown_content += f"{summary}\n\n"
    
    return markdown_content

def get_output_filename(input_filename):
    # Extract date from input filename (assuming format daily_papers_YYYYMMDD.json)
    date_str = input_filename.split('_')[-1].split('.')[0]
    return f"daily_papers_summary_{date_str}.md"

def process_daily_papers(input_file):
    # Load the JSON data
    with open(input_file, 'r') as file:
        data = json.load(file)

    # Convert JSON to markdown
    markdown_output = json_to_markdown(data)
    
    if markdown_output is None:
        print(f"Warning: {input_file} is empty. No markdown file will be created.")
        delete = input("Do you want to delete this empty file? (Y/N): ").strip().lower()
        if delete == 'y':
            os.remove(input_file)
            print(f"Deleted {input_file}")
        return

    # Get the output filename based on the input filename
    output_filename = get_output_filename(os.path.basename(input_file))

    # Create the data/output directory if it doesn't exist
    output_dir = os.path.join('data', 'output')
    os.makedirs(output_dir, exist_ok=True)

    # Check if output file already exists
    output_path = os.path.join(output_dir, output_filename)
    if os.path.exists(output_path):
        print(f"Output file {output_filename} already exists. Skipping conversion.")
        return

    # Write the markdown content to the file in the output directory
    with open(output_path, 'w') as file:
        file.write(markdown_output)

    print(f"Markdown file '{output_path}' has been created successfully.")

def process_all_files():
    input_dir = os.path.join('data', 'input')
    input_files = [f for f in os.listdir(input_dir) if f.endswith('.json')]
    
    if not input_files:
        print("No input files found in data/input directory.")
        return

    for input_file in sorted(input_files):
        input_path = os.path.join(input_dir, input_file)
        print(f"Processing {input_path}...")
        process_daily_papers(input_path)

if __name__ == "__main__":
    process_all_files()