
rm -rf results 


mkdir results

echo > results/a.txt
echo > results/b.txt
echo > results/c.txt
echo > results/d.txt
echo > results/e.txt
echo > results/f.txt
echo > results/g.txt
echo > results/h.txt
echo > results/i.txt

sqlite3 reuters.db < ./queries/a.txt > ./results/a.txt
sqlite3 reuters.db < ./queries/b.txt > ./results/b.txt
sqlite3 reuters.db < ./queries/c.txt > ./results/c.txt
sqlite3 reuters.db < ./queries/d.txt > ./results/d.txt
sqlite3 reuters.db < ./queries/e.txt > ./results/e.txt
sqlite3 reuters.db < ./queries/f.txt > ./results/f.txt

sqlite3 matrix.db < ./queries/g.txt > ./results/g.txt

sqlite3 reuters.db < ./queries/h.txt > ./results/h.txt
sqlite3 reuters.db < ./queries/i.txt > ./results/i.txt
