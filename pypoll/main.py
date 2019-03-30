import csv
with open("election_data.csv","r") as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    header=next(csvreader)
    rows = []
    countpercandidate = []
    candidatelist = []
    votercount = 0
    
    for x in csvreader:
        votercount = votercount + 1
        candidatelist.append(x[2])
        if x[2] not in rows:
            rows.append(x[2])

    print(f"Election Results")
    print(f'----------------------')
    print(f"Total Votes: {votercount}")
    print(f'----------------------')
    maxposition = 0
    mypoll=open("outputfile.txt", 'w+')
    mypoll.write(f"Total Votes: {votercount}\n")
    for j in range(len(rows)):
        countpercandidate.append(candidatelist.count(rows[j]))
        print(f"{(rows[j])} {format(((candidatelist.count(rows[j]))/(votercount)*100),'.3f')}% ({candidatelist.count(rows[j])})")
        mypoll.write(f"{(rows[j])} {format(((candidatelist.count(rows[j]))/(votercount)*100),'.3f')}% ({candidatelist.count(rows[j])})\n")
    maxposition = countpercandidate.index(max(countpercandidate))
    print(f'----------------------')
    print(f"Winner: {rows[maxposition]}")
    print(f'----------------------')
    mypoll.write(f"Winner: {rows[maxposition]}\n")
    mypoll.close()