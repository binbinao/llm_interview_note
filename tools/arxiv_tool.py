#!/usr/bin/env python3
"""
arXiv Tool - Search and download papers from arXiv
"""

import argparse
import requests
import os
from datetime import datetime

BASE_URL = "http://export.arxiv.org/api/query?"


def search_arxiv(query, max_results=5):
    """Search arXiv for papers matching the query"""
    params = {
        "search_query": query,
        "start": 0,
        "max_results": max_results,
        "sortBy": "relevance",
        "sortOrder": "descending"
    }
    
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    return response.text


def download_paper(arxiv_id, output_dir="pdf_note"):
    """Download a paper PDF given its arXiv ID"""
    pdf_url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
    os.makedirs(output_dir, exist_ok=True)
    filename = os.path.join(output_dir, f"{arxiv_id}.pdf")
    
    with requests.get(pdf_url, stream=True) as r:
        r.raise_for_status()
        with open(filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return filename


def main():
    parser = argparse.ArgumentParser(description='arXiv Paper Search and Download Tool')
    parser.add_argument('command', choices=['search', 'download'], 
                        help='Command to execute: search or download')
    parser.add_argument('--query', help='Search query for arXiv papers')
    parser.add_argument('--max-results', type=int, default=5, 
                        help='Maximum number of search results (default: 5)')
    parser.add_argument('--id', help='arXiv ID for downloading a paper')
    parser.add_argument('--output', default="pdf_note", 
                        help='Output directory for downloaded PDFs (default: pdf_note)')
    
    args = parser.parse_args()
    
    if args.command == 'search':
        if not args.query:
            parser.error("Search requires --query argument")
        results = search_arxiv(args.query, args.max_results)
        print(results)
    elif args.command == 'download':
        if not args.id:
            parser.error("Download requires --id argument")
        filename = download_paper(args.id, args.output)
        print(f"Downloaded paper to: {filename}")


if __name__ == "__main__":
    main()