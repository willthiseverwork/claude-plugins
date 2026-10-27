import csv,sys
expected=["Keyword","Label","Confidence","Segment","Metadata_action","Strip_words","Content_cluster","Reason"]
r=csv.reader(open(sys.argv[1],encoding="utf-8")); header=next(r); assert header==expected,header
for row in r: assert len(row)==8,row
print("valid eight-column contract")
