# using gzip compression
for f in *.csv; do
    gzip "$f"
done

