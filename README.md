# ncbi_query
A tool for querying the NCBI databases through its API and parsing the JSON/XML responses.

"The Entrez Programming Utilities (E-utilities) are a set of nine server-side programs that provide a stable interface into the Entrez query and database system at the National Center for Biotechnology Information (NCBI)." - https://www.ncbi.nlm.nih.gov/books/NBK25497/

ESearch and ESummary are two of such E-utility programs. ESearch returns a list of UIDs that match the search query which can be passed to ESummary, which returns DocumentSummaries in XML corresponding to a list of UIDs.

The XML response structure depends heavily on which database is queried, so the XML parsing needs to be tailored to the specific search interests. For now, only basic tags from the XML are printed, but the XML could be parsed for publication titles, 

## Dependencies
```bash
pip install requests
```

## Usage
```bash
python3 ncbi_query.py [database] [query]
```
- `database` = NCBI database name (pubmed, gene, mesh, etc.)
- `query` = Term to search for (organism, gene, etc.)

