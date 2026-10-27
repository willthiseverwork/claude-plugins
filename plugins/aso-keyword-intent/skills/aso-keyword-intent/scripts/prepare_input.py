import csv,sys
rows=list(csv.DictReader(sys.stdin)); w=csv.DictWriter(sys.stdout,fieldnames=["Keyword"]);w.writeheader();[w.writerow({"Keyword":r.get("Keyword") or r.get("keyword","")}) for r in rows]
