# ncbi_query
A tool for querying the NCBI databases and parsing the JSON/XML responses.

## How to run
```bash
pip install requests
```

## Usage
```bash
python3 ncbi_query.py [database] [query]
```
`database` = NCBI database name (pubmed, gene, mesh, etc.)
`query` = Term to search for (organism, gene, etc.)