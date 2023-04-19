import csv

def process_row(row):
    kota = row['kota']
    filename = kota.lower().replace(" ", "_")
    kontak1 = row['kontak1'][:-5].replace(".", ":")
    kontak2 = row['kontak2'][:-5].replace(".", ":")
    puncak = row['puncak'][:-5].replace(".", ":")
    kontak3 = row['kontak3'][:-5].replace(".", ":")
    kontak4 = row['kontak4'][:-5].replace(".", ":")
    jam = row['jam']
    menit = row['menit']
    detik = str(round(float(row['detik'])))
    magnitude = round(float(row['magnitude']) * 100)
    zone = row['zone']
    
    if kontak2 == '' or kontak3 == '':
        total_eclipse = False
    else:
        total_eclipse = True

    if kontak1 == '':
        observer = False
    else:
        observer = True
    
    if observer:
        if total_eclipse:
            gerhana = 'Gerhana Matahari Total'
        else:
            gerhana = f'Gerhana Matahari Sebagian {magnitude}%'
    else:
        gerhana = f'Tidak mengalami gerhana'
    
    if jam == '0':
        durasi = f'{menit} menit {detik} detik'
    else:
        durasi = f'{jam} jam {menit} menit {detik} detik'

    if observer:
        content = f"{kota}: {gerhana}. Mulai {kontak1} {zone}, puncak {puncak} {zone}, selesai {kontak4} {zone}. Durasi {durasi}."
    else:
        content = f"{kota}: {gerhana}."

    with open(f"api/{filename}.txt", "w") as f:
        f.write(content)

with open('data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        process_row(row)
