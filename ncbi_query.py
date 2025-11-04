import sys
import requests
import xml.etree.ElementTree as ET

BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"

# ESearch returns UIDs that match query which can be passed to ESummary
def ESearch(db: str, query: str) -> list:
    r = requests.get(BASE_URL + 'esearch.fcgi', params={'db': db,
                                                        'term': query,
                                                        'retmode': 'json'})
    json = r.json()
    print(f"ESearch results count: {json['esearchresult']['count']} (retmax = {json['esearchresult']['retmax']})")
    ids = json['esearchresult']['idlist']
    return ids if ids else []

# ESummary returns XML DocSums for each UID which can be parsed
def ESummary(db: str, UIDs: list[int]):
    r = requests.get(BASE_URL + 'esummary.fcgi', params={'db': db,
                                                         'id': ','.join(UIDs)})
    if r.ok:
        root = ET.fromstring(r.text)
        # parse XML for desired data
        print(f"ROOT TAG: {root.tag}")
        # for child in root:
        #     print(f"> CHILD TAG: {child.tag}")
    else:
        print(f"Response not OK. Status code: {r.status_code}\n")
    
def main():
    if len(sys.argv) < 3:
        print("Usage: python3 ncbi_query.py [database] [query/term/organism]")
        sys.exit(1)
        
    db = sys.argv[1]
    query = sys.argv[2]
    print(f"Searching for {query} in {db}...")

    uids = ESearch(db, query)
    if not uids:
        print("No results found")
        sys.exit(1)

    ESummary(db, uids)
        
        
main()